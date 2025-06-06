#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : BusBusiness.py
# @Time    : 2023/12/7 1:24
# @Dsc     : 总线业务线程类，需要在执行过程中输出信息，能够接受中断的业务

from PySide6.QtCore import QThread, QThreadPool, QRunnable, Signal, QDateTime

from AppImplement.RWConfigFile.RWPlayerDeck import PlayerDeckProcessor
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor
from AppImplement.Business.Foundation import *
from AppImplement.Business.OrdinaryBusiness import *
from AppImplement.Business.NonGameBusiness import *
from AppImplement.Business.UseStuffBusiness import *

# [日常领取]子功能名称与函数名映射关系dict
DAILY_AWARD_FUNC_DICT = {
    "VIP签到": executeVipSignin,
    "每日签到": executeDailySignin,
    "免费许愿": executeFreeWish,
    "法老宝藏": executePharaohTreasure,
    "塔罗寻宝": executeTarotTreasure,
    "底部任务": executeReceiveBottomQuest,
    "公会花园": executeUnionGarden,
    "营地钥匙": executeReceiveCampsiteKey,
    "月卡福利": executeMonthlyCardWelfare,
    "公会任务": executeReceiveUnionQuest,
    "打开美食大赛": executeOpenFoodContest,
    "打开背包": executeOpenBackpack,
    "领取双人魔塔奖励": executeReceiveTeamMagicTower,
    "赠送鲜花": executeGiveFlowers,
    "领取缘分树奖励": executeReceiveDestinyTree
}

# [日常收尾]子功能名称与函数名映射关系dict
DAILY_END_FUNC_DICT = {
    "底部任务": executeReceiveBottomQuest,
    "公会任务": executeReceiveUnionQuest,
    "情侣任务": executeReceiveLoversQuest,
    "悬赏活动": executeReceiveWanted,
    "大富翁": executeReceiveMonopoly,
    "背包兑换": executeOpenFoodContest
}

# [刷序列关]任务面板与函数名映射关系dict
SERIAL_LEVEL_QUEST_PANEL_FUNC_DICT = {
    "美食大赛": executeReceiveFoodContest,
    "探险营地": executeReceiveTXYDQuest
}


class BusinessBus(QThread):
    # 向主窗口发送待打印日志
    signal_send_business_message = Signal(str, str)
    # 向主窗口报告异常
    signal_send_business_error = Signal(str)
    # 向主窗口发送功能执行情况（功能在流程中的序号，功能的状态）
    # 状态：['hanging'(挂起)、'waiting'(等待)、'executing'(执行)、'completed'(完成)、'banned'(禁用)、'wrong'(错误)]
    signal_send_func_status = Signal(int, str)
    # 告诉主窗口完成整个流程(True表示正常结束, False表示异常结束)
    signal_flow_finished = Signal(bool)
    # 关闭所有子放卡线程
    signal_terminate_sub_thread = Signal()

    def __init__(self):
        super().__init__()

        # 文件处理器
        self.player_deck_procs = PlayerDeckProcessor(None)
        self.place_plan_procs = PlacingPlanProcessor(None)

        # 整个流程全局信息
        self.global_flow_info = {}
        # 通关时 所需的 基本信息
        self.player1_info = {}
        self.player2_info = {}
        self.level_info = {}

        # 是否运行中，避免重复启用线程
        self.flag_running = False

        # 放卡线程池
        self.card_place_thread_pool = QThreadPool(self)
        # 最大线程数 = 最大卡槽数(21) * 2
        self.card_place_thread_pool.setMaxThreadCount(42)
        self.place_card_thread_list = []

        # 业务流程字典
        self.func_flow = []

    # 业务总线的参数相关 ----------------------------------------------------------------
    def setGlobalFlowInfo(self, global_flow_info: dict):
        """设置整个流程的全局信息

        Args:
            global_flow_info: dict
                {
                    "1p_2nd_psw": player1_2nd_psw,                          // 1P二级密码
                    "2p_2nd_psw": player2_2nd_psw,                          // 2P二级密码
                    "current_2p_name_pic": player2_name_pic_path,           // 2P昵称路径
                    "current_1p_cross_room_pic": player1_cross_room_pic,    // 1P跨服房间列表昵称截图路径
                    "deck_path": deck_path,                                 // 卡片组ini文件
                    "plan_path": plan_path                                  // 放卡方案ini文件
                }
        """
        self.global_flow_info = global_flow_info

    def setPlayerInfo(self, player1_info: dict, player2_info: dict = None):
        """设置账号信息属性。2P信息为 None 时表示单人模式

        Args:
            player1_info: dict
                账号1通关信息
                {
                    "hwnd": int,                // 句柄
                    "zoom" float,               // 窗口缩放比例
                    "player_pos": str,          // 角色位置，格式：1,2
                    "cards_plan": list[dict],   // 卡片放置策略
                    "deck_no": int              // 选卡界面卡片组编号
                    "flop_pos": str             // 翻牌位置，格式：1;2;3;4
                }
                其中，cards_plan中每个dict的格式
                {
                    "card_pos_series": str,     // 卡片放置位置，格式：1,3,500;2,3;3,3;4,3,2000
                    "card_slot": int,           // 卡槽位置
                    "card_cd": int              // 卡片默认CD，单位毫秒(ms)
                }
            player2_info: dict
                账号2通关信息，格式同账号1。为 None 时表示单人模式
        """
        self.player1_info = player1_info
        # if player2_info is not None:
        self.player2_info = player2_info

    def setLevelInfo(self, level_info: dict):
        """设置关卡信息属性

        Args:
            level_info: dict
                关卡信息
                {
                    "has_stage2": bool[True, False],
                    "shall_continue": bool[True, False],
                    "max_check_time": int,                  //对局多少分钟后判定为通关异常
                    "skip_choose_level": bool,              //跳过选择关卡，不存在该字段表示不跳过
                    "loop_count": int,                      //关卡循环次数
                    "exit_delay": int                       //定时退出关卡，单位毫秒，-1表示不主动退出
                }
        """
        self.level_info = level_info

    def setFuncFlow(self, func_flow: list):
        self.func_flow = func_flow
        # print("设置了内部参数：\n", self.func_flow)

    # 最基本的 从 准备/开始 到结束翻牌 方法 ----------------------------------------------------
    def teamFromStartToFlop(self):
        """组队, 从点击 (准备/开始) 到 (结算完成翻牌)
        """
        hwnd_1p = self.player1_info["hwnd"]
        hwnd_2p = self.player2_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        zoom2 = self.player2_info["zoom"]
        # 2P准备
        delay(500)
        mouseClick(hwnd_2p, 872 * zoom2, 480 * zoom2)
        # 1P开始
        delay(500)
        mouseClick(hwnd_1p, 872 * zoom1, 480 * zoom1)
        # 检测进入关卡
        if not loopCheckStartGame(hwnd_1p, hwnd_2p, zoom1, zoom2):
            raise BusinessError("超过2min未检测到进入关卡！")
        self.formatBusinessMessage("检测到进入关卡")
        if self.level_info["loop_count"] > 0:
            self.level_info["loop_count"] -= 1
        # 放置1P
        delay(100)
        placeCard(hwnd_1p, self.player1_info["player_pos"], zoom1)
        # 放置2P
        placeCard(hwnd_2p, self.player2_info["player_pos"], zoom2)
        # 启动放卡线程
        self.startPlacingCard(self.player1_info["cards_plan"], 1)
        self.startPlacingCard(self.player2_info["cards_plan"], 2)

        exit_delay = self.level_info["exit_delay"]
        if self.level_info["loop_count"] <= 0 and exit_delay >= 0:
            # 一定时间后关闭放卡线程并退出关卡
            delay(exit_delay)
            self.endAllPlacingWorker()
            delay(300)
            exitGame(hwnd_1p, zoom1)
            exitGame(hwnd_2p, zoom2)
            return False

        delay(45000)
        # 检测进度
        if self.level_info["has_stage2"]:
            self.formatBusinessMessage("开始检测进度")
            # 等待检测到"继续挑战"
            continue_result = loopCheckContinue(hwnd_1p, self.level_info["max_check_time"])
            if not continue_result:
                # 超过容忍时间 还未检测到“继续挑战”
                raise BusinessError(f"超过{self.level_info['max_check_time']}分钟还未检测到“继续挑战”！！！")
            elif continue_result == 2:
                fail_tip_close_pos = find_pic(
                    hwnd_1p, FAIL_GAME_TIP_CLOSE_PATH, [250, 430, 750, 550],
                    record_fail=True, record_name="通关失败但未找到小贴士关闭按钮"
                )
                if fail_tip_close_pos:
                    mouseClick(hwnd_1p, fail_tip_close_pos[0] * zoom1, fail_tip_close_pos[1] * zoom1)
                    mouseClick(hwnd_2p, fail_tip_close_pos[0] * zoom2, fail_tip_close_pos[1] * zoom2)
                self.formatBusinessMessage("通关失败", "WARN")
                self.endAllPlacingWorker()
                loopCheckFlipChest(hwnd_1p)
                executeFlop(hwnd_1p, self.player1_info["flop_pos"], zoom1)
                executeFlop(hwnd_2p, self.player1_info["flop_pos"], zoom2)
                return
            # 成功检测到“继续挑战”
            if self.level_info["shall_continue"]:
                # 1P、2P先后点击“继续挑战”
                mouseClick(hwnd_1p, 424 * zoom1, 344 * zoom1)
                delay(100)
                mouseClick(hwnd_2p, 424 * zoom2, 344 * zoom2)
                self.formatBusinessMessage("选择继续挑战")

                delay(1000)

                # 如果没能点击成功，则再点击一次
                if find_color(hwnd_1p, [60, 20, 80, 40], 0x3D4A4C):
                    self.formatBusinessMessage("继续挑战点击失效，正在重新尝试", "WARN")
                    mouseClick(hwnd_1p, 424 * zoom1, 344 * zoom1)
                    delay(100)
                    mouseClick(hwnd_2p, 424 * zoom2, 344 * zoom2)
                    delay(2000)
            else:
                # 1P、2P先后点击“领取奖励”
                mouseClick(hwnd_1p, 512 * zoom1, 344 * zoom1)
                delay(500)
                mouseClick(hwnd_2p, 512 * zoom2, 344 * zoom2)
                self.formatBusinessMessage("选择领取奖励")

        self.formatBusinessMessage("开始检测结算")
        if not loopCheckEndGame(hwnd_1p, self.level_info["max_check_time"]):
            raise BusinessError(f"超过{self.level_info['max_check_time']}分钟还未检测到“结算翻牌”！！！")
        # 关闭所有放卡线程
        self.endAllPlacingWorker()
        loopCheckFlipChest(hwnd_1p)

        # 成功检测到结算翻牌
        executeFlop(hwnd_1p, self.player1_info["flop_pos"], zoom1)
        executeFlop(hwnd_2p, self.player1_info["flop_pos"], zoom2)
        self.formatBusinessMessage(f"翻取了第{self.player1_info['flop_pos']}张牌")
        return True

    def singleFromStartToFlop(self):
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        # 1P开始
        delay(500)
        mouseClick(hwnd_1p, 872 * zoom1, 480 * zoom1)
        # 检测进入关卡
        if not loopCheckStartGame(hwnd_1p, zoom1=zoom1):
            raise BusinessError("超过2min未检测到进入关卡！")
        self.formatBusinessMessage("检测到进入关卡")
        if self.level_info["loop_count"] is not None:
            self.level_info["loop_count"] -= 1
        # 放置1P
        delay(100)
        placeCard(hwnd_1p, self.player1_info["player_pos"], zoom1)
        # 启动放卡线程
        self.startPlacingCard(self.player1_info["cards_plan"], 1)

        exit_delay = self.level_info["exit_delay"]
        if self.level_info["loop_count"] <= 0 and exit_delay >= 0:
            # 一定时间后关闭放卡线程并退出关卡
            delay(exit_delay)
            self.endAllPlacingWorker()
            delay(300)
            exitGame(hwnd_1p, zoom1)
            return False

        delay(45000)
        # 检测进度
        if self.level_info["has_stage2"]:
            self.formatBusinessMessage("开始检测进度")
            # 等待检测到"继续挑战"
            continue_result = loopCheckContinue(hwnd_1p, self.level_info["max_check_time"])
            if not continue_result:
                # 超过容忍时间 还未检测到“继续挑战”
                raise BusinessError(f"超过{self.level_info['max_check_time']}分钟还未检测到“继续挑战”！！！")
            elif continue_result == 2:
                fail_tip_close_pos = find_pic(
                    hwnd_1p, FAIL_GAME_TIP_CLOSE_PATH, [250, 430, 750, 550],
                    record_fail=True, record_name="通关失败但未找到小贴士关闭按钮"
                )
                if fail_tip_close_pos:
                    mouseClick(hwnd_1p, fail_tip_close_pos[0] * zoom1, fail_tip_close_pos[1] * zoom1)
                self.formatBusinessMessage("通关失败", "WARN")
                self.endAllPlacingWorker()
                loopCheckFlipChest(hwnd_1p)
                executeFlop(hwnd_1p, self.player1_info["flop_pos"], zoom1)
                return
            # 成功检测到“继续挑战”
            if self.level_info["shall_continue"]:
                # 1P点击“继续挑战”
                mouseClick(hwnd_1p, 424 * zoom1, 344 * zoom1)
                self.formatBusinessMessage("选择继续挑战")

                delay(1000)

                # 如果没能点击成功，则再点击一次
                if find_color(hwnd_1p, [60, 20, 80, 40], 0x3D4A4C):
                    self.formatBusinessMessage("继续挑战点击失效，正在重新尝试", "WARN")
                    mouseClick(hwnd_1p, 424 * zoom1, 344 * zoom1)
                    delay(2000)
            else:
                # 1P点击“领取奖励”
                mouseClick(hwnd_1p, 512 * zoom1, 344 * zoom1)
                self.formatBusinessMessage("选择领取奖励")

        self.formatBusinessMessage("开始检测结算")
        if not loopCheckEndGame(hwnd_1p, self.level_info["max_check_time"]):
            raise BusinessError(f"超过{self.level_info['max_check_time']}分钟还未检测到“结算翻牌”！！！")
        # 关闭所有放卡线程
        self.endAllPlacingWorker()
        loopCheckFlipChest(hwnd_1p)

        # 成功检测到结算翻牌
        executeFlop(hwnd_1p, self.player1_info["flop_pos"], zoom1)
        self.formatBusinessMessage(f"翻取了第{self.player1_info['flop_pos']}张牌")
        return True

    # 最关键的 启用放卡 或 结束放卡 ---------------------------------------------------------
    def startPlacingCard(self, cards_plan, player=1):
        """...

        Args:
            cards_plan: list[dict]
                存放玩家放卡方案的列表，每个放卡信息都是dict的形式
            player: int[1 | 2]
                表示 玩家1(房主) 或 家2(房客) 的数字
        """
        hwnd = self.player1_info["hwnd"] if player == 1 else self.player2_info["hwnd"]
        zoom = self.player1_info["zoom"] if player == 1 else self.player2_info["zoom"]

        for card_info in cards_plan:
            place_thread = CardPlaceThread(hwnd, zoom, card_info)
            place_worker = CardPlaceWorker(place_thread)
            self.place_card_thread_list.append(place_thread)
            self.card_place_thread_pool.start(place_worker)

    def endAllPlacingWorker(self, wait_time=5):
        # print("尝试结束")
        # start_time = time()
        self.card_place_thread_pool.clear()
        for place_thread in self.place_card_thread_list:
            print("关闭放卡线程：", place_thread)
            place_thread.stop()
        self.place_card_thread_list.clear()
        self.card_place_thread_pool.waitForDone(wait_time)
        # print("花费时间：", time() - start_time)

    # 功能：循环刷指定关卡 ---------------------------------------------------------------
    def loopSpecificLevel(self, zone, level, loop_count):
        # 针对有次数限制的关卡，执行对应的方法【引发问题：选择此类关卡时不能跳过选关，负面影响可忽略】
        if zone == "魔塔蛋糕":
            self.startMagicTower(int(level), loop_count)
            return
        elif zone == "火山遗迹":
            self.startVolcanicRelic(level, loop_count)
            return
        elif zone in CROSS_SERVER_LEVEL_TYPE_NO:
            self.startCrossService(self.global_flow_info["current_1p_cross_room_pic"], zone, level, loop_count)
            return
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        if self.player2_info is not None:
            hwnd_2p = self.player2_info["hwnd"]
            zoom2 = self.player2_info["zoom"]
        if "skip_choose_level" not in self.level_info or not self.level_info["skip_choose_level"]:
            # 切换地图，同时1P创建房间
            self.formatBusinessMessage("正在切换到关卡")
            createAnyRoom(hwnd_1p, zone, level, zoom=zoom1)
            # 应用卡片组
            # self.formatBusinessMessage("应用1P卡片组")
            roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
            if self.player2_info is not None:
                createAnyRoom(hwnd_2p, zone, level, False, zoom=zoom2)
                # 邀请队友
                self.formatBusinessMessage("邀请2P")
                if not teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["current_2p_name_pic"], zoom1, zoom2):
                    # 若没找到2P
                    exitRoom(hwnd_1p, zoom1)
                    raise BusinessError("未找到2P或2P进入房间失败！")
                # self.formatBusinessMessage("应用2P卡片组")
                roomChooseDeck(hwnd_2p, self.player2_info["deck_no"], zoom2)
        if self.player2_info is not None:
            # 从点击 准备/开始 到完成翻牌
            for i in range(loop_count):
                self.formatBusinessMessage(f"开始第{i + 1}局")
                self.teamFromStartToFlop()
                # self.formatBusinessMessage(f"结束第{i + 1}局")
            # 退出房间
            exitRoom(hwnd_1p, zoom1)
            exitRoom(hwnd_2p, zoom2)
        else:
            for i in range(loop_count):
                self.formatBusinessMessage(f"开始第{i + 1}局")
                self.singleFromStartToFlop()
                # self.formatBusinessMessage(f"结束第{i + 1}局")
            # 退出房间
            exitRoom(hwnd_1p, zoom1)

    # 功能：刷序列关卡 -----------------------------------------------------------------
    def startSerialLevel(self, series_path, plan_path_team, plan_path_1p, plan_path_2p, quest_panel):
        """执行关卡序列文件中每行的通关策略，每通关一次打开任务面板领取奖励

        Args:
            series_path: str
                关卡序列文件绝对路径。
                关卡序列文件每行格式：<通关账号>*<地图区域>*<关卡名称>*<通关策略>*<放卡方案>
                <通关账号>: 组队/单人1P/单人2P
            plan_path_team: str
                组队模式时，组队放卡方案ini文件绝对路径
            plan_path_1p: str
                单人1P模式时，该账号放卡方案ini文件绝对路径
            plan_path_2p: str
                单人2P模式时，该账号放卡方案ini文件绝对路径
            quest_panel: str["无", "美食大赛", "探险营地"]
                每次通关后，领取任务奖励的任务面板
        """
        sep = "*"
        if series_path == "":
            SERIAL_LEVEL_QUEST_PANEL_FUNC_DICT[quest_panel](
                self.player1_info["hwnd"],
                self.player1_info["zoom"]
            )
            if self.player2_info is not None:
                SERIAL_LEVEL_QUEST_PANEL_FUNC_DICT[quest_panel](
                    self.player2_info["hwnd"],
                    self.player2_info["zoom"]
                )
            return
        series_file = open(series_path, 'r', encoding='utf8')
        series_level_list = []
        for file_line in series_file.read().splitlines():
            player_num, level_strategy = file_line.split(sep, 1)
            if player_num not in ["组队", "单人1P", "单人1p", "单人2P", "单人2p"]:
                raise BusinessError(f"关卡序列文件中存在无法识别的<通关账号>: {player_num}\n请确保该元素的值填写为“组队/单人1P/单人2P”")
            series_level_list.append((player_num, level_strategy))
        series_file.close()

        temp_player1_info = self.player1_info
        temp_player2_info = self.player2_info

        for series_tuple in series_level_list:
            if series_tuple[0] == "组队":
                plan_path = plan_path_team
                self.setPlayerInfo(temp_player1_info, temp_player2_info)
            elif series_tuple[0] in ["单人1P", "单人1p"]:
                plan_path = plan_path_1p
                self.setPlayerInfo(temp_player1_info, None)
            elif series_tuple[0] in ["单人2P", "单人2p"]:
                plan_path = plan_path_2p
                self.setPlayerInfo(temp_player2_info, None)
            # 执行通关策略
            self.formatBusinessMessage(series_tuple[1])
            self.executeUnionQuest(series_tuple[1], plan_path, sep=sep)
            # 每次通关后打开面板领取奖励
            if quest_panel != "无":
                SERIAL_LEVEL_QUEST_PANEL_FUNC_DICT[quest_panel](
                    self.player1_info["hwnd"],
                    self.player1_info["zoom"]
                )
                if self.player2_info is not None:
                    SERIAL_LEVEL_QUEST_PANEL_FUNC_DICT[quest_panel](
                        self.player2_info["hwnd"],
                        self.player2_info["zoom"]
                    )

    # 功能：一键签到 ------------------------------------------------------------------
    def signinAndActivity(self, activity_list: list):
        pass

    # 功能：公会任务 ------------------------------------------------------------------
    def startUnionQuest(self, quest_no_list, plan_path, roam_plan_path, roam_type):
        """先打开公会任务面板，再遍历所选公会任务，获取任务截图名称列表，再关闭公会任务界面。最后根据任务截图名称列表通关。

        Args:
            quest_no_list: str
                ...
            plan_path: str
                ...
            roam_plan_path: str
                ...
            roam_type: str
                三岛漫游的主题名称。
                文本应为: 平民鼠的逆袭/神殿集会/施工现场/Exciting/罐头炸弹/拆迁大队/百鬼夜行/车来了/峡道空袭/鼠以群聚

        Returns:
            ...
            example:
            ...
        """
        hwnd1 = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        openBottomMenu(hwnd1, "跳转", "公会任务", zoom1)
        # 获取会长任务结果列表
        quest_result_list = findUnionPresidentQuest(hwnd1, quest_no_list, zoom=zoom1)
        # 关闭公会任务界面
        mouseClick(hwnd1, 855 * zoom1, 55 * zoom1)
        delay(500)

        quest_no = 0
        for quest_result in quest_result_list:
            quest_no += 1
            self.formatBusinessMessage(f"开始公会任务{quest_no}...")
            if self.player2_info is None and quest_no in [3]:
                self.formatBusinessMessage("该任务属于组队任务，单人模式自动跳过")
            if quest_result in ["已完成", "没找到"]:
                self.formatBusinessMessage(f"{quest_result}公会任务{quest_no}")
                continue
            if quest_result.rsplit('-', 1)[1] == "跳过":
                self.formatBusinessMessage(f"跳过公会任务{quest_no}")
                continue
            if quest_result.find("漫游") != -1:
                # 特殊处理三岛漫游任务，将<放卡方案>元素设置为: [(美味)(火山)(浮空)]漫游_漫游类型
                parse_result = quest_result.split('-')
                if len(parse_result) > 3:
                    quest_result = '-'.join(parse_result[:3]) + parse_result[3] + '_' + roam_type
                else:
                    quest_result = quest_result + '-' + parse_result[1] + '_' + roam_type
                curr_plan_path = roam_plan_path
            else:
                curr_plan_path = plan_path
            self.formatBusinessMessage(f"公会任务{quest_no}: {quest_result}")
            # 执行
            self.executeUnionQuest(quest_result, curr_plan_path)

    def executeUnionQuest(self, quest_result, plan_path, sep='-'):
        parse_result = quest_result.split(sep)
        if len(parse_result) > 3:
            zone, level, strategy, plan_name = parse_result
        else:
            zone, level, strategy = parse_result
            plan_name = level

        # 设置关卡信息
        if strategy == "无二阶段":
            self.level_info["has_stage2"] = False
        elif strategy == "继续挑战":
            self.level_info["has_stage2"] = True
            self.level_info["shall_continue"] = True
        elif strategy == "领取奖励":
            self.level_info["has_stage2"] = True
            self.level_info["shall_continue"] = False
        else:
            # 默认作为”无二阶段“处理
            self.level_info["has_stage2"] = False

        # 获取放卡方案信息
        union_placing_plan_procs = PlacingPlanProcessor(plan_path)
        plan_info = union_placing_plan_procs.readPlan(plan_name)
        if isinstance(plan_info, tuple):
            self.formatBusinessMessage("未找到目标放卡方案，将使用”默认方案“作为通关配置", "WARN")
            plan_info = union_placing_plan_procs.readPlan("默认方案")
            if isinstance(plan_info, tuple):
                raise BusinessError("未找到目标放卡方案，且不存在”默认方案“，无法正常通关！")
        # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
        player1_info_dict = self.convertToExecute(
            {"1p_hwnd": self.player1_info["hwnd"], "1p_zoom": self.player1_info["zoom"]},
            plan_info, self.player1_info["flop_pos"], 1)
        player2_info_dict = None
        if self.player2_info is not None and plan_info["player_num"] == 2:
            player2_info_dict = self.convertToExecute(
                {"2p_hwnd": self.player2_info["hwnd"], "2p_zoom": self.player2_info["zoom"]},
                plan_info, self.player2_info["flop_pos"], 2)
        self.setPlayerInfo(player1_info_dict, player2_info_dict)

        self.loopSpecificLevel(zone, level, 1)

    # 功能：情侣任务 ------------------------------------------------------------------
    def startLoversQuest(self, plan_path):
        hwnd1 = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        openBottomMenu(hwnd1, "跳转", "情侣任务", zoom1)
        # 获取情侣任务结果列表
        quest_result_list = findLoversQuest(hwnd1, zoom1)
        # 关闭情侣任务界面
        mouseClick(hwnd1, 850 * zoom1, 55 * zoom1)
        delay(500)

        quest_no = 0
        for quest_result in quest_result_list:
            quest_no += 1
            self.formatBusinessMessage(f"开始情侣任务{quest_no}...")
            if quest_result in ["已完成", "没找到"]:
                self.formatBusinessMessage(f"{quest_result}情侣任务{quest_no}")
                continue
            if quest_result.rsplit('-', 1)[1] == "跳过":
                self.formatBusinessMessage(f"跳过情侣任务{quest_no}")
                continue
            self.formatBusinessMessage(f"情侣任务{quest_no}: {quest_result}")
            # 执行
            self.executeUnionQuest(quest_result, plan_path)

    # 功能：火山遗迹 ------------------------------------------------------------------
    def startVolcanicRelic(self, level, loop_count):
        zone = "火山遗迹"
        # 切换地图
        self.formatBusinessMessage("正在切换到关卡")
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        createAnyRoom(hwnd_1p, zone, level, zoom=zoom1)
        if self.player2_info is not None:
            hwnd_2p = self.player2_info["hwnd"]
            zoom2 = self.player2_info["zoom"]
            createAnyRoom(hwnd_2p, zone, level, False, zoom=zoom2)
        # 应用卡片组
        # self.formatBusinessMessage("应用1P卡片组")
        roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
        if self.player2_info is not None:
            # 邀请队友
            self.formatBusinessMessage("邀请2P")
            if not teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["current_2p_name_pic"], zoom1, zoom2):
                # 若没找到2P
                exitRoom(hwnd_1p, zoom1)
                raise BusinessError("未找到2P或2P进入房间失败！")
            # self.formatBusinessMessage("应用2P卡片组")
            roomChooseDeck(hwnd_2p, self.player2_info["deck_no"], zoom2)
            # 从点击 准备/开始 到完成翻牌
            try:
                for i in range(loop_count):
                    self.formatBusinessMessage(f"开始第{i + 1}局")
                    self.teamFromStartToFlop()
                    # self.formatBusinessMessage(f"结束第{i + 1}局")
            except BusinessError as business_error:
                business_error_str = business_error.error_info
                # print(business_error_str)
                # print("查找结果", business_error_str.find("超过"))
                if business_error_str.find("超过") != -1:
                    business_error_str = business_error_str + "\n可能是剩余次数不足！"
                    self.formatBusinessMessage(business_error_str, "WARN")
                else:
                    raise business_error
            # 退出房间
            exitRoom(hwnd_1p, zoom1)
            exitRoom(hwnd_2p, zoom2)
        else:
            try:
                for i in range(loop_count):
                    self.formatBusinessMessage(f"开始第{i + 1}局")
                    self.singleFromStartToFlop()
                    # self.formatBusinessMessage(f"结束第{i + 1}局")
            except BusinessError as business_error:
                business_error_str = business_error.error_info
                if business_error_str.find("超过") != -1:
                    business_error_str = business_error_str + "\n可能是剩余次数不足！"
                    self.formatBusinessMessage(business_error_str, "WARN")
                else:
                    raise business_error
            # 退出房间
            exitRoom(hwnd_1p, zoom1)

    # 功能：魔塔蛋糕 ------------------------------------------------------------------
    def startMagicTower(self, level_num: int, loop_count):
        """从主界面开始，先跳转至“美味岛”，再进入魔塔
           并根据当前启用账号数选择单人或双人魔塔，再根据level_num选择关卡
           最后完成关卡退出魔塔界面

        Args:
            level_num: int
                ...
            loop_count: int
                ...
        """
        # 切换地图
        self.formatBusinessMessage("正在切换到关卡")
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]

        tab_num = 0
        if self.player2_info is not None:
            hwnd_2p = self.player2_info["hwnd"]
            zoom2 = self.player2_info["zoom"]
            openMagicTowerDialog(hwnd_2p, tab_num, open_dialog=False, zoom=zoom2)
            tab_num = 1
        if level_num < 0:
            tab_num = 2
            # 魔塔第三页是单人模式
            self.player2_info = None
        openMagicTowerDialog(hwnd_1p, tab_num, zoom=zoom1)

        for loop_time in range(loop_count):
            self.formatBusinessMessage(f"开始第{loop_time + 1}局")
            # 选择魔塔关卡，并进入房间
            chooseMagicTowerLevel(hwnd_1p, level_num, zoom1)
            # 若提示次数不足
            if find_pic(hwnd_1p, MAGIC_TOWER_TAB1_NO_RESIDUAL_PATH, [330, 180, 580, 310]):
                mouseClick(hwnd_1p, 520 * zoom1, 380 * zoom1)
                delay(500)
                self.formatBusinessMessage("检测到魔塔第一页次数不足！", "WARN")
                break
            elif find_pic(hwnd_1p, MAGIC_TOWER_TAB3_NO_RESIDUAL_PATH, [300, 210, 650, 400]):
                mouseClick(hwnd_1p, 585 * zoom1, 250 * zoom1)
                delay(500)
                self.formatBusinessMessage("检测到魔塔第三页次数不足！", "WARN")
                break

            # 应用卡片组
            # self.formatBusinessMessage("应用1P卡片组")
            roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
            if self.player2_info is not None:
                # 邀请队友
                self.formatBusinessMessage("邀请2P")
                if not teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["current_2p_name_pic"], zoom1, zoom2):
                    # 若没找到2P
                    exitRoom(hwnd_1p, zoom1)
                    raise BusinessError("未找到2P或2P进入房间失败！")
                # self.formatBusinessMessage("应用2P卡片组")
                roomChooseDeck(hwnd_2p, self.player2_info["deck_no"], zoom2)
                # 从点击 准备/开始 到完成翻牌
                try:
                    self.teamFromStartToFlop()
                except BusinessError as business_error:
                    business_error_str = business_error.error_info
                    if business_error_str.find("超过") != -1:
                        business_error_str = business_error_str + "\n可能是剩余次数不足！"
                        self.formatBusinessMessage(business_error_str, "WARN")
                    else:
                        raise business_error
                # 2P退出房间
                exitRoom(hwnd_2p, zoom2)
            else:
                try:
                    self.singleFromStartToFlop()
                except BusinessError as business_error:
                    business_error_str = business_error.error_info
                    if business_error_str.find("超过") != -1:
                        business_error_str = business_error_str + "\n可能是剩余次数不足！"
                        self.formatBusinessMessage(business_error_str, "WARN")
                    else:
                        raise business_error
            # self.formatBusinessMessage(f"结束第{loop_time + 1}局")
        # 1P关闭魔塔界面
        mouseClick(hwnd_1p, 925 * zoom1, 32 * zoom1)
        delay(500)

    # 功能：跨服远征 ------------------------------------------------------------------
    def startCrossService(self, player1_room_name_path, level_type, level_num, loop_count):
        # 切换地图
        self.formatBusinessMessage("正在切换到关卡")
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        switchWorldZone(hwnd_1p, "跨服远征", zoom1)
        if self.player2_info is not None:
            hwnd_2p = self.player2_info["hwnd"]
            zoom2 = self.player2_info["zoom"]
            switchWorldZone(hwnd_2p, "跨服远征", zoom2)

        self.formatBusinessMessage(f"正在创建 {level_type} 房间")
        chooseCrossServiceLevel(hwnd_1p, level_type, level_num, zoom1)
        # 应用卡片组
        # self.formatBusinessMessage("应用1P卡片组")
        roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)

        if self.player2_info is not None:
            # 2P进入房间
            self.formatBusinessMessage(f"2P正在进入房间")
            searchAndEnter1pRoom(hwnd_2p, player1_room_name_path, level_type, zoom2)
            # self.formatBusinessMessage("应用2P卡片组")
            roomChooseDeck(hwnd_2p, self.player2_info["deck_no"], zoom2)
            # 从点击 准备/开始 到完成翻牌
            for i in range(loop_count):
                self.formatBusinessMessage(f"开始第{i + 1}局")
                self.teamFromStartToFlop()
                # self.formatBusinessMessage(f"结束第{i + 1}局")
            # 退出房间
            exitRoom(hwnd_1p, zoom1)
            exitRoom(hwnd_2p, zoom2)
            # 退出跨服
            mouseClick(hwnd_1p, 915 * zoom1, 30 * zoom1)
            mouseClick(hwnd_2p, 915 * zoom1, 30 * zoom2)
        else:
            for i in range(loop_count):
                self.formatBusinessMessage(f"开始第{i + 1}局")
                self.singleFromStartToFlop()
                # self.formatBusinessMessage(f"结束第{i + 1}局")
            # 退出房间
            exitRoom(hwnd_1p, zoom1)
            # 退出跨服
            mouseClick(hwnd_1p, 915 * zoom1, 30 * zoom1)
        # 退出跨服界面后，延时1s再操作
        delay(1000)

    # 功能：悬赏三连 ------------------------------------------------------------------
    def startWanted(self, active_level_dict):
        """...

        Args:
            active_level_dict: dict[str, tuple[bool, str]]
                三岛悬赏关卡信息。tuple包含两个元素，第一个bool类型元素表示是否执行对应关卡；第二个str类型元素表示通关放卡方案名称
                2025/01/16: 官方更新星际穿越悬赏任务，"悬赏四连"更符合该功能名称，改名还要做适配，代码不好看，算了
                格式：{
                    "美味岛": (True, "悬赏美味方案名称"),
                    "火山岛": (True, "悬赏火山方案名称"),
                    "浮空岛": (False, "悬赏浮空方案名称"),
                    "星际穿越": (False, "悬赏星际方案名称")
                }
        """
        flag_2p_opened = False      # 2P是否打开过悬赏界面
        for three_island in ["美味岛", "火山岛", "浮空岛", "星际穿越"]:
            if not active_level_dict[three_island][0]:
                continue
            self.formatBusinessMessage(f"开始{three_island}悬赏")
            # 获取放卡方案
            plan_info = self.place_plan_procs.readPlan(active_level_dict[three_island][1])
            if isinstance(plan_info, tuple):
                self.formatBusinessMessage("未找到目标放卡方案，将使用”默认方案“作为通关配置", "WARN")
                plan_info = self.place_plan_procs.readPlan("默认方案")
                if isinstance(plan_info, tuple):
                    raise BusinessError("未找到目标放卡方案，且不存在”默认方案“，无法正常通关！")
            # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
            player1_info_dict = self.convertToExecute(
                {"1p_hwnd": self.player1_info["hwnd"], "1p_zoom": self.player1_info["zoom"]},
                plan_info, "1;2", 1)
            player2_info_dict = None
            if self.player2_info is not None and plan_info["player_num"] == 2:
                player2_info_dict = self.convertToExecute(
                    {"2p_hwnd": self.player2_info["hwnd"], "2p_zoom": self.player2_info["zoom"]},
                    plan_info, "1;2", 2)
            self.setPlayerInfo(player1_info_dict, player2_info_dict)
            # 切换地图
            self.formatBusinessMessage("正在切换到关卡")
            hwnd_1p = self.player1_info["hwnd"]
            zoom1 = self.player1_info["zoom"]
            switchWorldZone(hwnd_1p, three_island, zoom1)
            if self.player2_info is not None:
                hwnd_2p = self.player2_info["hwnd"]
                zoom2 = self.player2_info["zoom"]
                switchWorldZone(hwnd_2p, three_island, zoom2)

            self.formatBusinessMessage(f"正在创建房间")
            # 打开悬赏活动界面
            createWantedRoom(hwnd_1p, three_island, zoom1)
            # 应用卡片组
            # self.formatBusinessMessage("应用1P卡片组")
            roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)

            if self.player2_info is not None:
                if not flag_2p_opened:
                    openWantedDialog(hwnd_2p, zoom2)
                    flag_2p_opened = True
                # 邀请队友
                self.formatBusinessMessage("邀请2P")
                if not teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["current_2p_name_pic"], zoom1, zoom2):
                    # 若没找到2P
                    exitRoom(hwnd_1p, zoom1)
                    raise BusinessError("未找到2P或2P进入房间失败！")
                # self.formatBusinessMessage("应用2P卡片组")
                roomChooseDeck(hwnd_2p, self.player2_info["deck_no"], zoom2)
                # 从点击 准备/开始 到完成翻牌
                self.teamFromStartToFlop()
                # 退出房间
                exitRoom(hwnd_1p, zoom1)
                exitRoom(hwnd_2p, zoom2)
            else:
                self.singleFromStartToFlop()
                # 退出房间
                exitRoom(hwnd_1p, zoom1)

    # 功能：勇士挑战 ------------------------------------------------------------------
    def startWarriorChallenge(self, level_pic, loop_count):
        # 切换地图
        self.formatBusinessMessage("正在切换到关卡")
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        singleLayerChooseLevel(hwnd_1p, "火山岛", "勇士挑战", zoom1)
        if self.player2_info is not None:
            hwnd_2p = self.player2_info["hwnd"]
            zoom2 = self.player2_info["zoom"]
            switchWorldZone(hwnd_2p, "火山岛", zoom2)

        # 跳转至已解锁关卡中难度最高的一关
        while find_pic(hwnd_1p, WARRIOR_CHALLENGE_TURN_RIGHT_PATH, [450, 150, 540, 200]):
            mouseClick(hwnd_1p, 500 * zoom1, 175 * zoom1)
            delay(850)
        # 向左翻页直到找到目标关卡
        while not find_pic(hwnd_1p, level_pic, [230, 150, 450, 360]):
            # 若当前已经是最左一页，则说明未能找到截图对应的关卡
            if not find_pic(hwnd_1p, WARRIOR_CHALLENGE_TURN_LEFT_PATH, [100, 150, 200, 200]):
                mouseClick(hwnd_1p, 845 * zoom1, 60 * zoom1)
                delay(500)
                raise BusinessError("未找到所选“勇士挑战BOSS”截图对应的关卡！")
            # 否则继续翻页
            mouseClick(hwnd_1p, 150 * zoom1, 175 * zoom1)
            delay(850)
        # 点击创建房间
        mouseClick(hwnd_1p, 450 * zoom1, 530 * zoom1)
        delay(2000)

        # 应用卡组
        roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
        if self.player2_info is not None:
            # 邀请队友
            self.formatBusinessMessage("邀请2P")
            if not teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["current_2p_name_pic"], zoom1, zoom2):
                # 若没找到2P
                exitRoom(hwnd_1p, zoom1)
                raise BusinessError("未找到2P或2P进入房间失败！")
            # self.formatBusinessMessage("应用2P卡片组")
            roomChooseDeck(hwnd_2p, self.player2_info["deck_no"], zoom2)
            # 从点击 准备/开始 到完成翻牌
            try:
                for i in range(loop_count):
                    self.formatBusinessMessage(f"开始第{i + 1}局")
                    self.teamFromStartToFlop()
                    # self.formatBusinessMessage(f"结束第{i + 1}局")
            except BusinessError as business_error:
                business_error_str = business_error.error_info
                if business_error_str.find("超过") != -1:
                    business_error_str = business_error_str + "\n可能是剩余次数不足！"
                    self.formatBusinessMessage(business_error_str, "WARN")
                else:
                    raise business_error
            # 退出房间
            exitRoom(hwnd_1p, zoom1)
            exitRoom(hwnd_2p, zoom2)
        else:
            try:
                for i in range(loop_count):
                    self.formatBusinessMessage(f"开始第{i + 1}局")
                    self.singleFromStartToFlop()
                    # self.formatBusinessMessage(f"结束第{i + 1}局")
            except BusinessError as business_error:
                business_error_str = business_error.error_info
                if business_error_str.find("超过") != -1:
                    business_error_str = business_error_str + "\n可能是剩余次数不足！"
                    self.formatBusinessMessage(business_error_str, "WARN")
                else:
                    raise business_error
            # 退出房间
            exitRoom(hwnd_1p, zoom1)
        # 1P关闭勇士界面
        mouseClick(hwnd_1p, 845 * zoom1, 60 * zoom1)
        delay(500)

    # 功能：公会副本 ------------------------------------------------------------------
    def startUnionDungeon(self, level_name, loop_count):
        def retryInvite2P():
            # 若没找到2P
            # self.formatBusinessMessage("邀请2P失败！正在尝试重新邀请。。。")
            if not teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["current_2p_name_pic"], zoom1, zoom2):
                # 公会副本的特殊处理，重新创建房间邀请可能会成功
                # self.formatBusinessMessage("邀请2P失败！正在尝试重新创建房间，并再次邀请。。。")
                exitRoom(hwnd_1p, zoom1)
                openBottomMenu(hwnd_1p, "跳转", "公会副本", zoom1)
                # 点击“进入地图”
                mouseClick(hwnd_1p, level_x_pos * zoom1, 415 * zoom1)
                delay(1000)
                # 创建房间
                createPwdRoom(hwnd_1p, zoom=zoom1)
                # 应用卡组
                roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
                # raise BusinessError("未找到2P或2P进入房间失败！")
                if not teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["current_2p_name_pic"], zoom1, zoom2):
                    # self.formatBusinessMessage("邀请2P失败！正在尝试重新进入地图，并再次邀请。。。")
                    exitRoom(hwnd_1p, zoom1)
                    switchWorldZone(hwnd_1p, "美味岛", zoom=zoom1)
                    switchWorldZone(hwnd_2p, "美味岛", zoom=zoom2)
                    openBottomMenu(hwnd_1p, "跳转", "公会副本", zoom1)
                    # 点击“进入地图”
                    mouseClick(hwnd_1p, level_x_pos * zoom1, 415 * zoom1)
                    delay(1000)
                    # 创建房间
                    createPwdRoom(hwnd_1p, zoom=zoom1)
                    # 应用卡组
                    roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
                    if not teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["current_2p_name_pic"], zoom1, zoom2):
                        # exitRoom(hwnd_1p, zoom1)
                        return False
            return True
        # 切换地图
        self.formatBusinessMessage("正在切换到关卡")
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        switchWorldZone(hwnd_1p, "美味岛", zoom1)
        if self.player2_info is not None:
            hwnd_2p = self.player2_info["hwnd"]
            zoom2 = self.player2_info["zoom"]
            switchWorldZone(hwnd_2p, "美味岛", zoom2)
        # 选择关卡
        if level_name == "月光果园":
            level_x_pos = 155
        elif level_name == "堕落深渊":
            level_x_pos = 365
        elif level_name == "死亡之棘":
            level_x_pos = 575
        else:
            closeCommonTipDialog(hwnd_1p, zoom1)
            raise BusinessError(f"未知的公会副本关卡名称{level_name}")
        openBottomMenu(hwnd_1p, "跳转", "公会副本", zoom1)
        # 点击“进入地图”
        mouseClick(hwnd_1p, level_x_pos * zoom1, 415 * zoom1)
        delay(1000)
        # 由于公会副本每次点击“进入地图”后会自动跳转至美味岛，导致被换线。此处主动换线至美味8区
        # switchLine(hwnd_1p, 8, zoom1)
        # 创建房间
        createPwdRoom(hwnd_1p, zoom=zoom1)
        # 应用卡组
        roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
        if self.player2_info is not None:
            # 邀请队友
            self.formatBusinessMessage("邀请2P")
            if not teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["current_2p_name_pic"], zoom1, zoom2):
                max_try_time = 3
                flag_invite_success = False
                while max_try_time > 0 and not flag_invite_success:
                    flag_invite_success = retryInvite2P()
                    max_try_time -= 1
                if max_try_time == 0 and not flag_invite_success:
                    raise BusinessError("已尝试3轮，每轮3次重新邀请2P，均失败！")
            # self.formatBusinessMessage("应用2P卡片组")
            roomChooseDeck(hwnd_2p, self.player2_info["deck_no"], zoom2)
            # 从点击 准备/开始 到完成翻牌
            for i in range(loop_count):
                self.formatBusinessMessage(f"开始第{i + 1}局")
                self.teamFromStartToFlop()
                # self.formatBusinessMessage(f"结束第{i + 1}局")
            # 退出房间
            exitRoom(hwnd_1p, zoom1)
            exitRoom(hwnd_2p, zoom2)
        else:
            for i in range(loop_count):
                self.formatBusinessMessage(f"开始第{i + 1}局")
                self.singleFromStartToFlop()
                # self.formatBusinessMessage(f"结束第{i + 1}局")
            # 退出房间
            exitRoom(hwnd_1p, zoom1)

    # 功能：使用物品 ------------------------------------------------------------------
    def startOperateStuff(self, hwnd, stuff_path, panel, operation, use_times, count_chest_stuff, second_psw='', zoom=1):
        """对文件夹中所有物品执行相同操作
        """
        function_name = USE_STUFF_PANEL_IO_DICT[panel][0]
        menu_name = USE_STUFF_PANEL_IO_DICT[panel][1][0]
        sub_menu_name = operation if panel in ["假期特惠"] else USE_STUFF_PANEL_IO_DICT[panel][1][1]
        panel_close_pos = USE_STUFF_PANEL_IO_DICT[panel][2]

        # 打开对应界面
        function_name(hwnd, menu_name, sub_menu_name, zoom)
        # 对物品图片，或文件夹中所有图片执行操作
        if path.isdir(stuff_path):
            for stuff_pic in listdir(stuff_path):
                stuff_pic_abstract_path = stuff_path + "\\" + stuff_pic
                if not USE_STUFF_SUB_FUNCTION_DICT[panel][operation](
                        hwnd, stuff_pic_abstract_path, use_times,
                        second_psw=second_psw, zoom=zoom, count_chest_stuff=count_chest_stuff
                ):
                    self.formatBusinessMessage(f"未解锁二级密码，无法{operation}物品", "WARN")
                    break
        else:
            if not USE_STUFF_SUB_FUNCTION_DICT[panel][operation](
                    hwnd, stuff_path, use_times,
                    second_psw=second_psw, zoom=zoom, count_chest_stuff=count_chest_stuff
            ):
                self.formatBusinessMessage(f"未解锁二级密码，无法{operation}物品", "WARN")

        # 关闭界面
        for close_pos in panel_close_pos:
            mouseClick(hwnd, close_pos[0] * zoom, close_pos[1] * zoom)
            delay(500)

    # 功能：刷熟练度 ------------------------------------------------------------------
    def startLoopSkill(self, hwnd, zone, level, loop_count, exit_delay, zoom=1):
        if loop_count <= 0:
            return
        createLoopSkillRoom(hwnd, zone, level, zoom)
        delay(500)
        self.executeLoopSkill(exit_delay)
        for i in range(2, loop_count + 1):
            reEnterLoopSkillRoom(hwnd, zone, level, zoom)
            self.executeLoopSkill(exit_delay)
            # 提醒进度
            if i % 500 == 0:
                self.formatBusinessMessage(f"已循环进入关卡刷熟练度{i}次")
        self.formatBusinessMessage(f"正常完成{loop_count}次循环刷熟练度")
        closeLoopSkillRoom(hwnd, zone, level, zoom)

    def executeLoopSkill(self, exit_delay):
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        # 应用卡片组
        roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
        # 1P开始
        mouseClick(hwnd_1p, 872 * zoom1, 480 * zoom1)
        # 检测进入关卡
        if not loopCheckStartGame(hwnd_1p, zoom1=zoom1):
            raise BusinessError("超过2min未检测到进入关卡！")
        # self.formatBusinessMessage("检测到进入关卡")
        # 放置1P
        delay(100)
        placeCard(hwnd_1p, self.player1_info["player_pos"], zoom1)
        # 启动放卡线程
        self.startPlacingCard(self.player1_info["cards_plan"], 1)
        # 一定时间后关闭放卡线程并退出关卡
        delay(exit_delay)
        self.endAllPlacingWorker()
        delay(300)
        exitGame(hwnd_1p, zoom1)

    # 线程执行相关 -------------------------------------------------------------------
    def run(self) -> None:
        try:
            self.executeBusinessFlow()
        except Exception as exception:
            business_error_str = repr(exception) + "\n" + str(exception)
            if business_error_str.find("无效的窗口句柄") != -1:
                self.formatBusinessMessage("结束流程")
                self.signal_send_business_error.emit("请先在[开始]功能中获取正确的游戏窗口句柄！")
                self.signal_flow_finished.emit(False)
                return
            self.signal_send_business_error.emit(business_error_str)
            self.formatBusinessMessage(business_error_str, "ERROR")

    def executeBusinessFlow(self):
        def handleFuncException(func_name, exc_error, player_hwnd_info_list):
            if exc_error.error_info.find("未找到世界地图") != -1 or exc_error.error_info.find("超过2min还未进入区域") != -1:
                for hwnd_info in player_hwnd_info_list:
                    closeExecExceptionDlg(hwnd_info[0], zoom=hwnd_info[1])
                self.formatBusinessMessage(exc_error.error_info, "ERROR")
                return True
            else:
                business_error_str = f"执行[{func_name}]功能时出错！\n\n{business_error.error_info}"
                self.signal_send_business_error.emit(business_error_str)
                self.formatBusinessMessage(business_error_str, "ERROR")
                return False

        self.formatBusinessMessage("开始依次执行流程列表中可用功能")
        # 先从“开始”功能获取流程全局变量
        start_param = self.func_flow[0]
        # self.formatBusinessMessage(f"流程列表以及参数：{self.func_flow}")
        enable_2p = start_param["enable_2p"]
        deck_path = start_param["deck_path"]
        plan_path = start_param["plan_path"]
        self.setGlobalFlowInfo({
            "1p_2nd_psw": start_param["1p_2nd_psw"],
            "2p_2nd_psw": start_param["2p_2nd_psw"],
            "current_2p_name_pic": start_param["2p_name_pic_path"],
            "current_1p_cross_room_pic": start_param["1p_cross_room_pic"],
            "deck_path": deck_path,
            "plan_path": plan_path
        })
        self.level_info["max_check_time"] = start_param["max_check_time"]
        self.player_deck_procs.setFilePath(deck_path)
        self.place_plan_procs.setFilePath(plan_path)
        # 完成”开始“功能
        self.signal_send_func_status.emit(0, "completed")

        # 再执行每个功能
        func_no = 1  # 功能在流程中的序号

        # 发生异常时重新尝试的次数
        exception_handle_time = 3

        # 若第二个是[自动登录]，则执行
        if len(self.func_flow) >= 2 and self.func_flow[1]["func_name"] == "自动登录":
            func_param = self.func_flow[1]
            # 获取顶层句柄
            top_hwnd_1p = func_param["1p_top_hwnd"]
            # 获取区服
            server_no_1p = func_param["1p_server_no"]

            autoLoginPreCheck(func_param["1p_top_hwnd"], func_param["1p_login_way"])
            if enable_2p and func_param["2p_top_hwnd"] != 0:
                autoLoginPreCheck(func_param["2p_top_hwnd"], func_param["2p_login_way"])

            # 启动延时（单位min）
            if func_param["start_way"] == "time":
                waitUntilSpecificTime(func_param["start_time"])
            else:
                delay(func_param["start_delay"] * 60000)

            # 调用自动登录函数，更新可操作句柄
            start_param["1p_hwnd"] = AUTO_LOGIN_WAY_FUNC_DICT[func_param["1p_login_way"]](
                top_hwnd_1p,
                server_no_1p,
                start_param["1p_zoom"]
            )
            # 应对刚登录游戏的弹窗
            closeJustLoginDialog(start_param["1p_hwnd"], start_param["1p_zoom"])
            if enable_2p and func_param["2p_top_hwnd"] != 0:
                # 获取顶层句柄
                top_hwnd_2p = func_param["2p_top_hwnd"]
                # 获取区服
                server_no_2p = func_param["2p_server_no"]
                # 调用自动登录函数，更新可操作句柄
                start_param["2p_hwnd"] = AUTO_LOGIN_WAY_FUNC_DICT[func_param["2p_login_way"]](
                    top_hwnd_2p,
                    server_no_2p,
                    start_param["2p_zoom"]
                )
                # 应对刚登录游戏的弹窗
                closeJustLoginDialog(start_param["2p_hwnd"], start_param["2p_zoom"])
            # 完成”自动登录“功能
            self.signal_send_func_status.emit(func_no, "completed")
            # 下一个功能从数组下标2开始执行
            func_no += 1

        # for func_param in self.func_flow[func_no:]:
        while func_no < len(self.func_flow):
            func_param = self.func_flow[func_no]
            if exception_handle_time < 3:
                self.formatBusinessMessage(f"重新尝试功能[{func_param['func_name']}]")
            else:
                self.formatBusinessMessage(f"开始功能[{func_param['func_name']}]")
            self.signal_send_func_status.emit(func_no, "executing")
            # 当前功能执行结果，默认为“完成”，当捕捉到异常后改为“错误”
            func_final_status = "completed"

            if func_param["func_name"] == "日常领取":
                # 获取操作目标 窗口句柄 和 缩放比例
                hwnd = start_param[f"{func_param['player'] + 1}p_hwnd"]
                zoom = start_param[f"{func_param['player'] + 1}p_zoom"]
                second_psw = start_param[f"{func_param['player'] + 1}p_2nd_psw"]
                print("日常领取的句柄与缩放：", hwnd, zoom)
                # 去除干扰项
                del func_param["func_name"]
                del func_param["player"]
                # 对于每个任务，调用对应的方法
                for key, value in func_param.items():
                    try:
                        if isinstance(value, list) and value[0]:
                            self.formatBusinessMessage(f"开始[{key}]...")
                            # 特殊方法中，添加入参
                            if key == "赠送鲜花":
                                value[1]["second_psw"] = second_psw
                            result_str = DAILY_AWARD_FUNC_DICT[key](hwnd=hwnd, zoom=zoom, **value[1])
                            self.formatBusinessMessage(result_str)
                        elif isinstance(value, bool) and value:
                            self.formatBusinessMessage(f"开始[{key}]...")
                            result_str = DAILY_AWARD_FUNC_DICT[key](hwnd=hwnd, zoom=zoom)
                            self.formatBusinessMessage(result_str)
                        else:
                            # self.formatBusinessMessage(f"跳过[{key}]")
                            pass
                    except BusinessError as business_error:
                        business_error_str = f"执行[{key}]功能时出错！\n\n{business_error.error_info}"
                        func_final_status = "wrong"
                        self.signal_send_business_error.emit(business_error_str)
                        self.formatBusinessMessage(business_error_str, "ERROR")
                # 加回该键值对，便于之后的输出
                func_param["func_name"] = "日常领取"
            elif func_param["func_name"] == "日常收尾":
                # 获取操作目标 窗口句柄 和 缩放比例
                hwnd = start_param[f"{func_param['player'] + 1}p_hwnd"]
                zoom = start_param[f"{func_param['player'] + 1}p_zoom"]
                second_psw = start_param[f"{func_param['player'] + 1}p_2nd_psw"]
                # 去除干扰项
                del func_param["func_name"]
                del func_param["player"]
                # 对于每个任务，调用对应的方法
                for key, value in func_param.items():
                    try:
                        if isinstance(value, list) and value[0]:
                            self.formatBusinessMessage(f"开始[{key}]...")
                            result_str = DAILY_END_FUNC_DICT[key](hwnd=hwnd, zoom=zoom, **value[1])
                            self.formatBusinessMessage(result_str)
                        elif isinstance(value, bool) and value:
                            self.formatBusinessMessage(f"开始[{key}]...")
                            result_str = DAILY_END_FUNC_DICT[key](hwnd=hwnd, zoom=zoom)
                            self.formatBusinessMessage(result_str)
                        else:
                            # self.formatBusinessMessage(f"跳过[{key}]")
                            pass
                    except BusinessError as business_error:
                        business_error_str = f"执行[{key}]功能时出错！\n\n{business_error.error_info}"
                        func_final_status = "wrong"
                        self.signal_send_business_error.emit(business_error_str)
                        self.formatBusinessMessage(business_error_str, "ERROR")
                # 加回该键值对，便于之后的输出
                func_param["func_name"] = "日常收尾"
            elif func_param["func_name"] == "刷指定关卡":
                # 先判断单人还是组队模式
                if func_param["player2"] != 0:
                    single_mode = False
                else:
                    single_mode = True
                self.setLevelInfo({
                    "has_stage2": func_param["has_stage2"],
                    "shall_continue": func_param["shall_continue"],
                    "max_check_time": start_param["max_check_time"],
                    "skip_choose_level": func_param["skip_choose_level"],
                    "loop_count": func_param["loop_count"],
                    "exit_delay": -1
                })
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], func_param["player1"], single_mode=single_mode)
                player2_info_dict = None
                if not single_mode:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], func_param["player2"])
                    self.global_flow_info["current_2p_name_pic"] = start_param[
                        f'{func_param["player2"]}p_name_pic_path']
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                try:
                    # 定时启动
                    if func_param["timing_start"]:
                        if func_param["start_way"] == "time":
                            if not waitUntilSpecificTime(func_param["start_time"]):
                                raise BusinessError(f"设置的启动时间{func_param['start_time']}小于当前时间，跳过该功能")
                        else:
                            delay(func_param["start_delay"] * 60000)
                    # 启动 循环刷指定关卡 的功能
                    self.loopSpecificLevel(
                        func_param["zone_name"],
                        func_param["level_name"],
                        func_param["loop_count"])
                except BusinessError as business_error:
                    player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                    if not single_mode:
                        player_hwnd_info.append((self.player2_info["hwnd"], self.player2_info["zoom"]))
                    if exception_handle_time > 0 and handleFuncException(
                        func_param["func_name"], business_error, player_hwnd_info
                    ):
                        # 若需要重新尝试，则直接进入下一次循环
                        exception_handle_time -= 1
                        func_param["loop_count"] = self.level_info["loop_count"]
                        continue
                    else:
                        func_final_status = "wrong"
            elif func_param["func_name"] == "刷序列关卡":
                # 先判断单人还是组队模式
                if func_param["player2"] != 0:
                    single_mode = False
                else:
                    single_mode = True

                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"],
                    "loop_count": -1,
                    "exit_delay": -1
                })
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = {
                    "hwnd": start_param[f"{func_param['player1']}p_hwnd"],
                    "zoom": start_param[f"{func_param['player1']}p_zoom"],
                    "flop_pos": func_param["flop_pos"]
                }
                player2_info_dict = None
                if not single_mode:
                    player2_info_dict = {
                        "hwnd": start_param[f"{func_param['player2']}p_hwnd"],
                        "zoom": start_param[f"{func_param['player2']}p_zoom"],
                        "flop_pos": func_param["flop_pos"]
                    }
                    self.global_flow_info["current_2p_name_pic"] = start_param[
                        f'{func_param["player2"]}p_name_pic_path']
                    self.global_flow_info["current_1p_cross_room_pic"] = start_param[
                        f'{func_param["player1"]}p_cross_room_pic']
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                try:
                    # 启动 刷序列关卡 的功能
                    self.startSerialLevel(
                        func_param["series_path"],
                        func_param["plan_path_team"],
                        func_param["plan_path_1p"],
                        func_param["plan_path_2p"],
                        func_param["quest_panel"]
                    )
                except BusinessError as business_error:
                    player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                    if not single_mode:
                        player_hwnd_info.append((self.player2_info["hwnd"], self.player2_info["zoom"]))
                    if exception_handle_time > 0 and handleFuncException(
                            func_param["func_name"], business_error, player_hwnd_info
                    ):
                        # 若需要重新尝试，则直接进入下一次循环
                        exception_handle_time -= 1
                        func_param["loop_count"] = self.level_info["loop_count"]
                        continue
                    else:
                        func_final_status = "wrong"
            elif func_param["func_name"] == "公会任务":
                # 先判断单人还是组队模式
                if func_param["player2"] != 0:
                    single_mode = False
                else:
                    single_mode = True
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"],
                    "loop_count": -1,
                    "exit_delay": -1
                })
                plan_path = func_param["plan_path"]
                # 使用该文件路径初始化放卡方案处理器
                self.place_plan_procs.setFilePath(plan_path)

                # 获取"默认方案"放卡方案信息
                plan_info = self.place_plan_procs.readPlan("默认方案")
                if isinstance(plan_info, tuple):
                    business_error_str = f"执行[{func_param['func_name']}]功能时出错！\n\n放卡方案ini文件中不存在“默认方案”"
                    func_final_status = "wrong"
                    self.signal_send_business_error.emit(business_error_str)
                    self.formatBusinessMessage(business_error_str, "ERROR")
                else:
                    # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                    player1_info_dict = self.convertToExecute(
                        start_param, plan_info, "1;2", func_param["player1"], single_mode=single_mode)
                    player2_info_dict = None
                    if not single_mode:
                        player2_info_dict = self.convertToExecute(
                            start_param, plan_info, "1;2", func_param["player2"])
                        self.global_flow_info["current_2p_name_pic"] = start_param[
                            f'{func_param["player2"]}p_name_pic_path']
                    self.setPlayerInfo(player1_info_dict, player2_info_dict)
                    try:
                        self.startUnionQuest(
                            func_param["quest_no_list"],
                            plan_path,
                            func_param["roam_plan_path"],
                            func_param["roam_type"]
                        )
                    except BusinessError as business_error:
                        player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                        if not single_mode:
                            player_hwnd_info.append((self.player2_info["hwnd"], self.player2_info["zoom"]))
                        if exception_handle_time > 0 and handleFuncException(
                                func_param["func_name"], business_error, player_hwnd_info
                        ):
                            # 若需要重新尝试，则直接进入下一次循环
                            exception_handle_time -= 1
                            continue
                        else:
                            func_final_status = "wrong"
            elif func_param["func_name"] == "情侣任务":
                # [情侣任务]只能组队模式
                single_mode = False
                if not enable_2p:
                    business_message_str = f"单人模式不支持[{func_param['func_name']}]功能！"
                    self.formatBusinessMessage(business_message_str, "WARN")
                    self.formatBusinessMessage(f"结束功能[{func_param['func_name']}]")
                    self.signal_send_func_status.emit(func_no, func_final_status)
                    func_no += 1
                    continue
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"],
                    "loop_count": -1,
                    "exit_delay": -1
                })
                plan_path = func_param["plan_path"]
                # 使用该文件路径初始化放卡方案处理器
                self.place_plan_procs.setFilePath(plan_path)

                # 获取"默认方案"放卡方案信息
                plan_info = self.place_plan_procs.readPlan("默认方案")
                if isinstance(plan_info, tuple):
                    business_error_str = f"执行[{func_param['func_name']}]功能时出错！\n\n放卡方案ini文件中不存在“默认方案”"
                    func_final_status = "wrong"
                    self.signal_send_business_error.emit(business_error_str)
                    self.formatBusinessMessage(business_error_str, "ERROR")
                else:
                    # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                    player1_info_dict = self.convertToExecute(
                        start_param, plan_info, "1;2", func_param["player1"])
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, "1;2", func_param["player2"])
                    self.global_flow_info["current_2p_name_pic"] = start_param[
                        f'{func_param["player2"]}p_name_pic_path']
                    self.setPlayerInfo(player1_info_dict, player2_info_dict)
                    try:
                        self.startLoversQuest(plan_path)
                    except BusinessError as business_error:
                        player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"]),
                                            (self.player2_info["hwnd"], self.player2_info["zoom"])]
                        if exception_handle_time > 0 and handleFuncException(
                                func_param["func_name"], business_error, player_hwnd_info
                        ):
                            # 若需要重新尝试，则直接进入下一次循环
                            exception_handle_time -= 1
                            continue
                        else:
                            func_final_status = "wrong"
            elif func_param["func_name"] == "火山遗迹":
                # 先判断单人还是组队模式
                if func_param["player2"] != 0:
                    single_mode = False
                else:
                    single_mode = True
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"],
                    "loop_count": func_param["loop_count"],
                    "exit_delay": -1
                })
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], func_param["player1"], single_mode=single_mode)
                player2_info_dict = None
                if not single_mode:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], func_param["player2"])
                    self.global_flow_info["current_2p_name_pic"] = start_param[
                        f'{func_param["player2"]}p_name_pic_path']
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                try:
                    # 启动 循环刷指定关卡 的功能
                    self.startVolcanicRelic(
                        func_param["level_name"],
                        func_param["loop_count"])
                except BusinessError as business_error:
                    player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                    if not single_mode:
                        player_hwnd_info.append((self.player2_info["hwnd"], self.player2_info["zoom"]))
                    if exception_handle_time > 0 and handleFuncException(
                            func_param["func_name"], business_error, player_hwnd_info
                    ):
                        # 若需要重新尝试，则直接进入下一次循环
                        exception_handle_time -= 1
                        func_param["loop_count"] = self.level_info["loop_count"]
                        continue
                    else:
                        func_final_status = "wrong"
            elif func_param["func_name"] == "魔塔蛋糕":
                # 先判断单人还是组队模式
                if func_param["player2"] != 0:
                    single_mode = False
                else:
                    single_mode = True
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"],
                    "loop_count": func_param["loop_count"],
                    "exit_delay": -1
                })
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], func_param["player1"], single_mode=single_mode)
                player2_info_dict = None
                if not single_mode:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], func_param["player2"])
                    self.global_flow_info["current_2p_name_pic"] = start_param[
                        f'{func_param["player2"]}p_name_pic_path']
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                try:
                    # 启动 循环刷指定关卡 的功能
                    self.startMagicTower(
                        func_param["level_num"],
                        func_param["loop_count"])
                except BusinessError as business_error:
                    player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                    if not single_mode:
                        player_hwnd_info.append((self.player2_info["hwnd"], self.player2_info["zoom"]))
                    if exception_handle_time > 0 and handleFuncException(
                            func_param["func_name"], business_error, player_hwnd_info
                    ):
                        # 若需要重新尝试，则直接进入下一次循环
                        exception_handle_time -= 1
                        func_param["loop_count"] = self.level_info["loop_count"]
                        continue
                    else:
                        func_final_status = "wrong"
            elif func_param["func_name"] == "跨服远征":
                # 先判断单人还是组队模式
                if func_param["player2"] != 0:
                    single_mode = False
                else:
                    single_mode = True
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"],
                    "loop_count": func_param["loop_count"],
                    "exit_delay": -1
                })
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], func_param["player1"], single_mode=single_mode)
                player2_info_dict = None
                if not single_mode:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], func_param["player2"])
                    self.global_flow_info["current_2p_name_pic"] = start_param[
                        f'{func_param["player2"]}p_name_pic_path']
                    self.global_flow_info["current_1p_cross_room_pic"] = start_param[
                        f'{func_param["player1"]}p_cross_room_pic']
                    if not path.exists(self.global_flow_info["current_1p_cross_room_pic"]):
                        self.global_flow_info["current_1p_cross_room_pic"] = func_param["player1_room_name_path"]
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                try:
                    # 启动 循环刷指定关卡 的功能
                    self.startCrossService(
                        self.global_flow_info["current_1p_cross_room_pic"],
                        func_param["level_type"],
                        func_param["level_num"],
                        func_param["loop_count"])
                except BusinessError as business_error:
                    player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                    if not single_mode:
                        player_hwnd_info.append((self.player2_info["hwnd"], self.player2_info["zoom"]))
                    if exception_handle_time > 0 and handleFuncException(
                            func_param["func_name"], business_error, player_hwnd_info
                    ):
                        # 若需要重新尝试，则直接进入下一次循环
                        exception_handle_time -= 1
                        func_param["loop_count"] = self.level_info["loop_count"]
                        continue
                    else:
                        func_final_status = "wrong"
            elif func_param["func_name"] == "悬赏三连":
                # 先判断单人还是组队模式
                if func_param["player2"] != 0:
                    single_mode = False
                else:
                    single_mode = True
                self.setLevelInfo({
                    "has_stage2": True,
                    "shall_continue": True,
                    "max_check_time": start_param["max_check_time"],
                    "loop_count": -1,
                    "exit_delay": -1
                })
                plan_path = func_param["plan_path"]
                # 使用该文件路径初始化放卡方案处理器
                self.place_plan_procs.setFilePath(plan_path)
                # 获取"默认方案"放卡方案信息
                plan_info = self.place_plan_procs.readPlan("默认方案")
                if isinstance(plan_info, tuple):
                    business_error_str = f"执行[{func_param['func_name']}]功能时出错！\n\n放卡方案ini文件中不存在“默认方案”"
                    func_final_status = "wrong"
                    self.signal_send_business_error.emit(business_error_str)
                    self.formatBusinessMessage(business_error_str, "ERROR")
                else:
                    # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                    player1_info_dict = self.convertToExecute(
                        start_param, plan_info, "1;2", func_param["player1"], single_mode=single_mode)
                    player2_info_dict = None
                    if not single_mode:
                        player2_info_dict = self.convertToExecute(
                            start_param, plan_info, "1;2", func_param["player2"])
                        self.global_flow_info["current_2p_name_pic"] = start_param[
                            f'{func_param["player2"]}p_name_pic_path']
                    self.setPlayerInfo(player1_info_dict, player2_info_dict)
                    try:
                        self.startWanted(func_param["active_level_dict"])
                    except BusinessError as business_error:
                        player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                        if not single_mode:
                            player_hwnd_info.append((self.player2_info["hwnd"], self.player2_info["zoom"]))
                        if exception_handle_time > 0 and handleFuncException(
                                func_param["func_name"], business_error, player_hwnd_info
                        ):
                            # 若需要重新尝试，则直接进入下一次循环
                            exception_handle_time -= 1
                            continue
                        else:
                            func_final_status = "wrong"
            elif func_param["func_name"] == "勇士挑战":
                # 先判断单人还是组队模式
                if func_param["player2"] != 0:
                    single_mode = False
                else:
                    single_mode = True
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"],
                    "loop_count": func_param["loop_count"],
                    "exit_delay": -1
                })
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], func_param["player1"], single_mode=single_mode)
                player2_info_dict = None
                if not single_mode:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], func_param["player2"])
                    self.global_flow_info["current_2p_name_pic"] = start_param[
                        f'{func_param["player2"]}p_name_pic_path']
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                try:
                    # 启动 循环刷指定关卡 的功能
                    self.startWarriorChallenge(
                        func_param["boss_pic"],
                        func_param["loop_count"])
                except BusinessError as business_error:
                    player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                    if not single_mode:
                        player_hwnd_info.append((self.player2_info["hwnd"], self.player2_info["zoom"]))
                    if exception_handle_time > 0 and handleFuncException(
                            func_param["func_name"], business_error, player_hwnd_info
                    ):
                        # 若需要重新尝试，则直接进入下一次循环
                        exception_handle_time -= 1
                        func_param["loop_count"] = self.level_info["loop_count"]
                        continue
                    else:
                        func_final_status = "wrong"
            elif func_param["func_name"] == "公会副本":
                # 先判断单人还是组队模式
                if func_param["player2"] != 0:
                    single_mode = False
                else:
                    single_mode = True
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"],
                    "loop_count": func_param["loop_count"],
                    "exit_delay": -1
                })
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], func_param["player1"], single_mode=single_mode)
                player2_info_dict = None
                if not single_mode:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], func_param["player2"])
                    self.global_flow_info["current_2p_name_pic"] = start_param[
                        f'{func_param["player2"]}p_name_pic_path']
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                try:
                    self.startUnionDungeon(
                        func_param["level_name"],
                        func_param["loop_count"])
                except BusinessError as business_error:
                    player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                    if not single_mode:
                        player_hwnd_info.append((self.player2_info["hwnd"], self.player2_info["zoom"]))
                    if exception_handle_time > 0 and handleFuncException(
                            func_param["func_name"], business_error, player_hwnd_info
                    ):
                        # 若需要重新尝试，则直接进入下一次循环
                        exception_handle_time -= 1
                        func_param["loop_count"] = self.level_info["loop_count"]
                        continue
                    else:
                        func_final_status = "wrong"
            elif func_param["func_name"] == "使用物品":
                # 获取操作目标 窗口句柄 和 缩放比例
                hwnd = start_param[f"{func_param['player'] + 1}p_hwnd"]
                zoom = start_param[f"{func_param['player'] + 1}p_zoom"]
                second_psw = start_param[f"{func_param['player'] + 1}p_2nd_psw"]
                # 对于每个物品执行操作
                for stuff_info in func_param["stuff_list"]:
                    stuff_name = stuff_info["pic_path"].rsplit('\\', 1)[1]
                    self.formatBusinessMessage(f"开始{stuff_info['operation']}物品或文件夹中所有物品：[{stuff_name}]...")
                    try:
                        self.startOperateStuff(
                            hwnd,
                            stuff_info["pic_path"],
                            stuff_info["panel"],
                            stuff_info["operation"],
                            stuff_info["opt_times"],
                            func_param["count_chest_stuff"],
                            second_psw,
                            zoom=zoom
                        )
                    except BusinessError as business_error:
                        player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                        if exception_handle_time > 0 and handleFuncException(
                                func_param["func_name"], business_error, player_hwnd_info
                        ):
                            # 若需要重新尝试，则直接进入下一次循环
                            exception_handle_time -= 1
                            continue
                        else:
                            func_final_status = "wrong"
            elif func_param["func_name"] == "刷熟练度":
                # [刷熟练度]只能单人模式
                single_mode = True
                # 获取操作目标 窗口句柄 和 缩放比例
                hwnd = start_param[f"{func_param['player'] + 1}p_hwnd"]
                zoom = start_param[f"{func_param['player'] + 1}p_zoom"]
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"],
                    "loop_count": func_param["loop_count"],
                    "exit_delay": -1
                })
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, '1', 1)
                # 选2P时，convertToExecute()只能从放卡方案中获取2P相关信息，单人模式下，发生冲突
                player1_info_dict["hwnd"] = hwnd
                player1_info_dict["zoom"] = zoom
                player2_info_dict = None
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                try:
                    # 启动 循环刷熟练度 的功能
                    self.startLoopSkill(
                        hwnd,
                        func_param["zone_name"],
                        func_param["level_name"],
                        func_param["loop_count"],
                        func_param["exit_delay"],
                        zoom
                    )
                except BusinessError as business_error:
                    player_hwnd_info = [(self.player1_info["hwnd"], self.player1_info["zoom"])]
                    if not single_mode:
                        player_hwnd_info.append((self.player2_info["hwnd"], self.player2_info["zoom"]))
                    if exception_handle_time > 0 and handleFuncException(
                            func_param["func_name"], business_error, player_hwnd_info
                    ):
                        # 若需要重新尝试，则直接进入下一次循环
                        exception_handle_time -= 1
                        func_param["loop_count"] = self.level_info["loop_count"]
                        continue
                    else:
                        func_final_status = "wrong"
            else:
                self.formatBusinessMessage(f"功能[{func_param['func_name']}]不存在！或该功能处于错误的位置！", "ERROR")
                func_final_status = "wrong"
                self.signal_send_func_status.emit(func_no, func_final_status)
                func_no += 1
                continue

            if exception_handle_time == 0:
                self.formatBusinessMessage(f"执行功能[{func_param['func_name']}]时发生异常，且重新尝试了3次仍无法解决！")
            self.formatBusinessMessage(f"结束功能[{func_param['func_name']}]")
            self.signal_send_func_status.emit(func_no, func_final_status)
            func_no += 1
            # 重置
            exception_handle_time = 3
            self.place_plan_procs.setFilePath(plan_path)
        self.formatBusinessMessage("流程执行完成")
        self.signal_flow_finished.emit(True)

    def convertToExecute(self, start_param, plan_info, flop_pos, player, single_mode=False):
        player_no_in_file = player
        if single_mode and player == 2:
            # 当为单人模式，且房主选择的是2P时，解析放卡方案中的"1P"信息
            player_no_in_file = 1
        # 获取该账号使用的 卡片组名称
        deck_info = self.player_deck_procs.readDeck(plan_info[f"{player_no_in_file}P所用卡片组"])
        if isinstance(deck_info, tuple):
            deck_name = plan_info[f"{player_no_in_file}P所用卡片组"]
            raise BusinessError(f"放卡方案[{plan_info['plan_name']}]中{player_no_in_file}P所用卡片组“{deck_name}”在账号卡片组ini文件中不存在")
        # 用来存放可执行dict格式中，cards_plan的内容
        cards_plan = []
        # 从卡1到卡n依次存放（这要求放卡方案配置文件里必须保证递增的顺序）
        card_no = 1
        print("转义前放卡计划\n", plan_info[f"{player_no_in_file}p_card_plan"])
        for card_info in plan_info[f"{player_no_in_file}p_card_plan"]:
            # 获取该卡名称，以便在deck_info中得到对应的slot值
            card_name = card_info[f"{player_no_in_file}P卡{card_no}"]
            card_slot = deck_info["deck_slot_info"][card_name]
            # 卡片CD以放卡方案配置文件中的为准
            card_cd = card_info[f"{player_no_in_file}P卡{card_no}CD"]
            if card_cd == "CD":
                card_cd = deck_info["deck_cd_info"][card_name]
            # 组装dict
            card_plan = {
                "card_pos_series": card_info[f"{player_no_in_file}P卡{card_no}放置位置"].replace(",CD", f',{deck_info["deck_cd_info"][card_name]}'),
                "card_replenish_series": card_info[f"{player_no_in_file}P卡{card_no}补卡位置"].replace(",CD", f',{deck_info["deck_cd_info"][card_name]}'),
                "card_slot": int(card_slot),
                "card_cd": int(card_cd)}
            # 加入cards_plan
            cards_plan.append(card_plan)
            card_no += 1
        if "定时退出关卡" in plan_info:
            self.level_info["exit_delay"] = int(plan_info["定时退出关卡"])
        else:
            self.level_info["exit_delay"] = -1
        return {
            "hwnd": start_param[f"{player}p_hwnd"],
            "zoom": start_param[f"{player}p_zoom"],
            "player_pos": plan_info[f"{player_no_in_file}P放置位置"],
            "cards_plan": cards_plan,
            "deck_no": int(deck_info["卡片组编号"]),
            "flop_pos": flop_pos
        }

    def formatBusinessMessage(self, message_str, message_type="INFO"):
        """向主窗口发送 代表 业务执行情况 的文字消息

        Args:
            message_str: str
                消息内容
            message_type: str["DEBUG", "INFO", "WARN", "ERROR"]
                消息类型。分为 调式[DEBUG]、信息[INFO]、警告[WARN]、错误[ERROR]
        """
        print_str = "{} [{}]: {}".format(
            QDateTime.currentDateTime().toString("yyyy/MM/dd hh:mm:ss"),
            message_type, message_str)
        self.signal_send_business_message.emit(print_str, message_type)

    def terminate(self) -> None:
        self.endAllPlacingWorker()
        self.formatBusinessMessage("提前终止流程！", "WARN")
        for i in range(len(self.func_flow)):
            self.signal_send_func_status.emit(i, "hanging")
        super().terminate()


class CardPlaceWorker(QRunnable):
    def __init__(self, thread_obj: QThread):
        super().__init__()
        # threading.Thread.__init__(self)

        self._thread = thread_obj

    def run(self) -> None:
        self._thread.start()
        self._thread.wait()


class CardPlaceThread(QThread):
    def __init__(self, hwnd, zoom, card_info: dict, parent=None):
        super().__init__(parent=parent)
        # threading.Thread.__init__(self)

        self.stop_flag = [False]

        self.hwnd = hwnd
        self.zoom = zoom
        self.card_info = card_info

    def run(self) -> None:
        try:
            card_pos_series = self.card_info["card_pos_series"]
            card_slot = self.card_info["card_slot"]
            card_cd = self.card_info["card_cd"]
            loopPlaceCardForThread(self.hwnd, card_pos_series, card_slot, card_cd, self.stop_flag, self.zoom)
        except Exception as e:
            print(e.args)
            win32gui.ReleaseDC(self.hwnd, win32gui.GetWindowDC(self.hwnd))
            print("释放了", self.hwnd)

    def stop(self):
        self.stop_flag[0] = True


if __name__ == "__main__":
    cards_plan_1p = [{
        "card_pos_series": "3,9,18000;5,9;1,9",
        "card_slot": 7,
        "card_cd": 15000
    }, {
        "card_pos_series": "2,9,25000;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9",
        "card_slot": 3,
        "card_cd": 7000
    }, {
        "card_pos_series": "1,9,29500;6,9",
        "card_slot": 6,
        "card_cd": 10000
    }, {
        "card_pos_series": "2,8,30000;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8",
        "card_slot": 14,
        "card_cd": 29000
    }]
    cards_plan_2p = [{
        "card_pos_series": "2,9,5500;4,9;6,9",
        "card_slot": 7,
        "card_cd": 15000
    }, {
        "card_pos_series": "2,8,41500;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8",
        "card_slot": 13,
        "card_cd": 29000,
        "shovel": True
    }]
    player1_info = {"hwnd": 6096884,
                    "zoom": 1,
                    "player_pos": "4,4",
                    "cards_plan": cards_plan_1p,
                    "deck_no": 2,
                    "flop_pos": "1"}
    player2_info = {"hwnd": 4917062,
                    "zoom": 1,
                    "player_pos": "6,4",
                    "cards_plan": cards_plan_2p,
                    "deck_no": 2,
                    "flop_pos": "1"}
    level_info = {"has_stage2": False,
                  "shall_continue": False,
                  "max_check_time": 10}
    business_bus = BusinessBus()
    business_bus.setPlayerInfo(player1_info, player2_info)
    business_bus.setLevelInfo(level_info)
    business_bus.setGlobalFlowInfo({
            "current_2p_name_pic": r"D:\PycharmProjects\FVM_Backstage_Assistant_LFBY\resources\images\用户图片\组队房间2P截图示例.bmp",
            "deck_path": r"D:\PycharmProjects\FVM_Backstage_Assistant_LFBY\config\卡片放置方案\账号预设卡片组.ini",
            "plan_path": r"D:\PycharmProjects\FVM_Backstage_Assistant_LFBY\config\卡片放置方案\升级版组队常用方案_V1.00.ini"
        })
    business_bus.player_deck_procs.setFilePath(business_bus.global_flow_info["deck_path"])
    business_bus.place_plan_procs.setFilePath(business_bus.global_flow_info["plan_path"])
    business_bus.startWanted({"美味岛": (True, "默认配置"), "火山岛": (True, "默认配置"), "浮空岛": (False, "默认配置")})

    # # 测试一键日常领取
    # waitClick()
    # x, y = getCursorPos()
    # hwnd = mousePosHwnd(x, y)
    # print(hwnd)

    # hwnd1 = 986252
    # executeVipSignin(hwnd1)
    # executeDailySignin(hwnd1)
    # executeFreeWish(hwnd1)
    # executePharaohTreasure(hwnd1, 1)
    # executeTarotTreasure(hwnd1)
    # executeReceiveBottomQuest(hwnd1)
    # executeUnionGarden(hwnd1, True, 1)
    # executeReceiveCampsiteKey(hwnd1)
    # executeReceiveUnionQuest(hwnd1, True)
    # executeReceiveTeamMagicTower(hwnd1)
    # executeGiveFlowers(
    #     hwnd1,
    #     r"D:\PycharmProjects\FVM_Backstage_Assistant_LFBY\resources\images\用户图片\好友界面小号昵称.bmp",
    #     True,
    #     5
    # )
    # executeReceiveDestinyTree(hwnd1)
    # hwnd2 = 2296822
    # executeVipSignin(hwnd2)
    # executeDailySignin(hwnd2)
    # executeFreeWish(hwnd2)
    # executePharaohTreasure(hwnd2, 1)
    # executeTarotTreasure(hwnd2)
    # executeReceiveBottomQuest(hwnd2)
    # executeUnionGarden(hwnd2, True)
    # executeReceiveCampsiteKey(hwnd2)
    # executeReceiveUnionQuest(hwnd2, False)
    # executeReceiveTeamMagicTower(hwnd2)
    # executeGiveFlowers(
    #     hwnd2,
    #     r"D:\PycharmProjects\FVM_Backstage_Assistant_LFBY\resources\images\用户图片\好友界面大号昵称.bmp",
    #     True,
    #     5
    # )
    # executeReceiveDestinyTree(hwnd2)
