#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : BusBusiness.py
# @Time    : 2023/12/7 1:24
# @Dsc     : 总线业务线程类，需要在执行过程中输出信息，能够接受中断的业务

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QThread, QThreadPool, QRunnable, Signal, QDateTime

from AppImplement.RWConfigFile.RWPlayerDeck import PlayerDeckProcessor
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor
from AppImplement.Business.Foundation import *
from AppImplement.Business.OrdinaryBusiness import *
from AppImplement.Business.NonGameBusiness import *

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
    "公会任务": executeReceiveUnionQuest,
    "打开美食大赛": executeOpenFoodContest,
    "打开背包": executeOpenBackpack,
    "领取双人魔塔奖励": executeReceiveTeamMagicTower,
    "赠送鲜花": executeGiveFlowers,
    "领取缘分树奖励": executeReceiveDestinyTree
}

# [自动登录]登录方式与函数名映射关系dict
AUTO_LOGIN_WAY_FUNC_DICT = {
    "微端": autoLoginMicroTerminal,
    "360游戏大厅": autoLogin360GameHall
}


class BusinessBus(QThread):
    # 向主窗口发送待打印日志
    signal_send_business_message = Signal(str)
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
                    "2p_name_pic_path": player2_name_pic_path,      // 2P昵称路径
                    "deck_path": deck_path,                         // 卡片组ini文件
                    "plan_path": plan_path                          // 放卡方案ini文件
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
                    "max_check_time": int
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
        # 放置1P
        delay(100)
        placeCard(hwnd_1p, self.player1_info["player_pos"], zoom1)
        # 放置2P
        placeCard(hwnd_2p, self.player2_info["player_pos"], zoom2)
        # 启动放卡线程
        self.startPlacingCard(self.player1_info["cards_plan"], 1)
        self.startPlacingCard(self.player2_info["cards_plan"], 2)

        delay(45000)
        # 检测进度
        if self.level_info["has_stage2"]:
            self.formatBusinessMessage("开始检测进度")
            # 等待检测到"继续挑战"
            if not loopCheckContinue(hwnd_1p, self.level_info["max_check_time"]):
                # 超过容忍时间 还未检测到“继续挑战”
                raise BusinessError(f"超过{self.level_info['max_check_time']}分钟还未检测到“继续挑战”！！！")
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
        delay(8200)

        # 成功检测到结算翻牌
        executeFlop(hwnd_1p, self.player1_info["flop_pos"], zoom1)
        executeFlop(hwnd_2p, self.player1_info["flop_pos"], zoom2)
        self.formatBusinessMessage(f"翻取了第{self.player1_info['flop_pos']}张牌")

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
        # 放置1P
        delay(100)
        placeCard(hwnd_1p, self.player1_info["player_pos"], zoom1)
        # 启动放卡线程
        self.startPlacingCard(self.player1_info["cards_plan"], 1)

        delay(45000)
        # 检测进度
        if self.level_info["has_stage2"]:
            self.formatBusinessMessage("开始检测进度")
            # 等待检测到"继续挑战"
            if not loopCheckContinue(hwnd_1p, self.level_info["max_check_time"]):
                # 超过容忍时间 还未检测到“继续挑战”
                raise BusinessError(f"超过{self.level_info['max_check_time']}分钟还未检测到“继续挑战”！！！")
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
        delay(8200)

        # 成功检测到结算翻牌
        executeFlop(hwnd_1p, self.player1_info["flop_pos"], zoom1)
        self.formatBusinessMessage(f"翻取了第{self.player1_info['flop_pos']}张牌")

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
        print("尝试结束")
        start_time = time()
        self.card_place_thread_pool.clear()
        for place_thread in self.place_card_thread_list:
            print("关闭放卡线程：", place_thread)
            place_thread.stop()
        self.place_card_thread_list.clear()
        self.card_place_thread_pool.waitForDone(wait_time)
        print("花费时间：", time() - start_time)

    # 功能：循环刷指定关卡 ---------------------------------------------------------------
    def loopSpecificLevel(self, zone, level, loop_count):
        # 切换地图
        self.formatBusinessMessage("正在切换到关卡")
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        chooseSingleOrMultiZone(hwnd_1p, zone, level, zoom1)
        if self.player2_info is not None:
            hwnd_2p = self.player2_info["hwnd"]
            zoom2 = self.player2_info["zoom"]
            chooseSingleOrMultiZone(hwnd_2p, zone, level, zoom2)
        # 创建房间
        self.formatBusinessMessage("正在创建房间")
        createPwdRoom(hwnd_1p, zoom=zoom1)
        # 应用卡片组
        # self.formatBusinessMessage("应用1P卡片组")
        roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
        if self.player2_info is not None:
            # 邀请队友
            self.formatBusinessMessage("邀请2P")
            if not teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["2p_name_pic_path"], zoom1, zoom2):
                # 若没找到2P
                raise BusinessError("")
            # self.formatBusinessMessage("应用2P卡片组")
            roomChooseDeck(hwnd_2p, self.player2_info["deck_no"], zoom2)
        # 从点击 准备/开始 到完成翻牌
            for i in range(loop_count):
                self.formatBusinessMessage(f"开始第{i + 1}局")
                self.teamFromStartToFlop()
                self.formatBusinessMessage(f"结束第{i + 1}局")
            # 退出房间
            exitRoom(hwnd_1p, zoom1)
            exitRoom(hwnd_2p, zoom2)
        else:
            for i in range(loop_count):
                self.formatBusinessMessage(f"开始第{i + 1}局")
                self.singleFromStartToFlop()
                self.formatBusinessMessage(f"结束第{i + 1}局")
            # 退出房间
            exitRoom(hwnd_1p, zoom1)

    # 功能：一键签到 ------------------------------------------------------------------
    def signinAndActivity(self, activity_list: list):
        pass

    # 功能：公会任务 ------------------------------------------------------------------
    def startUnionQuest(self, plan_path):
        hwnd1 = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        # 点击“跳转”
        mouseClick(hwnd1, 870 * zoom1, 585 * zoom1)
        delay(500)
        # 点击“公会任务”
        mouseClick(hwnd1, 900 * zoom1, 260 * zoom1)
        if not find_pic_loop(hwnd1, OPEN_UNION_QUEST_PATH, [392, 35, 566, 72], max_time=120):
            raise BusinessError("超过2min还未打开公会任务界面！")
        delay(500)
        # 获取会长任务结果列表
        quest_result_list = findUnionPresidentQuest(hwnd1, zoom1)
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
            self.formatBusinessMessage(f"公会任务{quest_no}: {quest_result}")
            # 执行
            self.executeUnionQuest(quest_result, plan_path)

    def executeUnionQuest(self, quest_result, plan_path):
        parse_result = quest_result.split('-')
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

        # 获取放卡方案信息：所用方案名称 与 关卡名称 相同
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
            plan_info, "1;2", 1)
        player2_info_dict = None
        if self.player2_info is not None and plan_info["player_num"] == 2:
            player2_info_dict = self.convertToExecute(
                {"2p_hwnd": self.player2_info["hwnd"], "2p_zoom": self.player2_info["zoom"]},
                plan_info, "1;2", 2)
        self.setPlayerInfo(player1_info_dict, player2_info_dict)

        self.loopSpecificLevel(zone, level, 1)

    # 功能：情侣任务 ------------------------------------------------------------------
    def startLoversQuest(self, plan_path):
        hwnd1 = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        # 点击“跳转”
        mouseClick(hwnd1, 870 * zoom1, 585 * zoom1)
        delay(500)
        # 点击“情侣任务”
        mouseClick(hwnd1, 900 * zoom1, 300 * zoom1)
        if not find_pic_loop(hwnd1, OPEN_LOVERS_QUEST_PATH, [392, 35, 566, 80], max_time=120):
            raise BusinessError("超过2min还未打开情侣任务界面！")
        delay(500)
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
        chooseSingleOrMultiZone(hwnd_1p, zone, level, zoom1)
        if self.player2_info is not None:
            hwnd_2p = self.player2_info["hwnd"]
            zoom2 = self.player2_info["zoom"]
            chooseSingleOrMultiZone(hwnd_2p, zone, level, zoom2)
        # 创建房间
        self.formatBusinessMessage("正在创建房间")
        createPwdRoom(hwnd_1p, zoom=zoom1)
        # 应用卡片组
        # self.formatBusinessMessage("应用1P卡片组")
        roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
        if self.player2_info is not None:
            # 邀请队友
            self.formatBusinessMessage("邀请2P")
            teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["2p_name_pic_path"], zoom1, zoom2)
            # self.formatBusinessMessage("应用2P卡片组")
            roomChooseDeck(hwnd_2p, self.player2_info["deck_no"], zoom2)
            # 从点击 准备/开始 到完成翻牌
            try:
                for i in range(loop_count):
                    self.formatBusinessMessage(f"开始第{i + 1}局")
                    self.teamFromStartToFlop()
                    self.formatBusinessMessage(f"结束第{i + 1}局")
            except BusinessError as business_error:
                business_error_str = business_error.error_info
                # print(business_error_str)
                # print("查找结果", business_error_str.find("超过"))
                if business_error_str.find("超过") != -1:
                    business_error_str = business_error_str + "\n可能是剩余次数不足！"
                    exitRoom(hwnd_1p, zoom1)
                    exitRoom(hwnd_2p, zoom2)
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
                    self.formatBusinessMessage(f"结束第{i + 1}局")
            except BusinessError as business_error:
                business_error_str = business_error.error_info
                if business_error_str.find("超过") != -1:
                    business_error_str = business_error_str + "\n可能是剩余次数不足！"
                    exitRoom(hwnd_1p, zoom1)
                    self.formatBusinessMessage(business_error_str, "WARN")
                else:
                    raise business_error
            # 退出房间
            exitRoom(hwnd_1p, zoom1)

    # 功能：魔塔蛋糕 ------------------------------------------------------------------
    def startMagicTower(self, level_num, loop_count):
        # 切换地图
        self.formatBusinessMessage("正在切换到关卡")
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        switchWorldZone(hwnd_1p, "美味岛", zoom1)

        tab_num = 0
        if self.player2_info is not None:
            hwnd_2p = self.player2_info["hwnd"]
            zoom2 = self.player2_info["zoom"]
            switchWorldZone(hwnd_2p, "美味岛", zoom2)

            tab_num = 1
        switchWorldZone(hwnd_1p, "魔塔蛋糕", zoom1)
        delay(2000)

        # 选择tab页
        mouseClick(hwnd_1p, (45 + 73 * tab_num) * zoom1, 70 * zoom1)
        delay(500)
        for loop_time in range(loop_count):
            self.formatBusinessMessage(f"开始第{loop_time + 1}局")
            # 选择魔塔关卡，并进入房间
            chooseMagicTowerLevel(hwnd_1p, level_num, zoom1)

            # 应用卡片组
            # self.formatBusinessMessage("应用1P卡片组")
            roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
            if self.player2_info is not None:
                # 邀请队友
                self.formatBusinessMessage("邀请2P")
                teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["2p_name_pic_path"], zoom1, zoom2)
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
            self.formatBusinessMessage(f"结束第{loop_time + 1}局")
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
                self.formatBusinessMessage(f"结束第{i + 1}局")
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
                self.formatBusinessMessage(f"结束第{i + 1}局")
            # 退出房间
            exitRoom(hwnd_1p, zoom1)
            # 退出跨服
            mouseClick(hwnd_1p, 915 * zoom1, 30 * zoom1)

    # 功能：悬赏三连 ------------------------------------------------------------------
    def startWanted(self, active_level_dict):
        """...

        Args:
            active_level_dict: dict[str, tuple[bool, str]]
                三岛悬赏关卡信息。tuple包含两个元素，第一个bool类型元素表示是否执行对应关卡；第二个str类型元素表示通关放卡方案名称
                格式：{
                    "美味岛": (True, "悬赏美味方案名称"),
                    "火山岛": (True, "悬赏火山方案名称"),
                    "浮空岛": (False, "悬赏浮空方案名称")
                }
        """
        flag_2p_opened = False      # 2P是否打开过悬赏界面
        for three_island in ["美味岛", "火山岛", "浮空岛"]:
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
            openWantedDialog(hwnd_1p, zoom1)
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
                teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["2p_name_pic_path"], zoom1, zoom2)
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
        self.formatBusinessMessage("开始依次执行流程列表中可用功能")
        # 先从“开始”功能获取流程全局变量
        start_param = self.func_flow[0]
        enable_2p = start_param["enable_2p"]
        player2_name_pic_path = start_param["2p_name_pic_path"]
        deck_path = start_param["deck_path"]
        plan_path = start_param["plan_path"]
        self.setGlobalFlowInfo({
            "2p_name_pic_path": player2_name_pic_path,
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
        # 若第二个是[自动登录]，则执行
        if self.func_flow[1]["func_name"] == "自动登录":
            func_param = self.func_flow[1]
            # 获取顶层句柄
            top_hwnd_1p = func_param["1p_top_hwnd"]
            # 获取区服
            server_no_1p = func_param["1p_server_no"]

            # 启动延时（单位min）
            delay(func_param["start_delay"] * 60000)

            # 调用自动登录函数，更新可操作句柄
            start_param["1p_hwnd"] = AUTO_LOGIN_WAY_FUNC_DICT[func_param["1p_login_way"]](
                top_hwnd_1p,
                server_no_1p,
                start_param["1p_zoom"]
            )
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
            # 完成”自动登录“功能
            self.signal_send_func_status.emit(func_no, "completed")
            # 下一个功能从数组下标2开始执行
            func_no = 2

        # 应对刚登录游戏的弹窗
        closeJustLoginDialog(start_param["1p_hwnd"], start_param["1p_zoom"])
        if enable_2p and start_param["2p_hwnd"] != 0:
            closeJustLoginDialog(start_param["2p_hwnd"], start_param["2p_zoom"])
        for func_param in self.func_flow[func_no:]:
            self.formatBusinessMessage(f"开始功能[{func_param['func_name']}]")
            self.signal_send_func_status.emit(func_no, "executing")
            # 当前功能执行结果，默认为“完成”，当捕捉到异常后改为“错误”
            func_final_status = "completed"
            if func_param["func_name"] == "日常领取":
                # 获取操作目标 窗口句柄 和 缩放比例
                hwnd = start_param[f"{func_param['player'] + 1}p_hwnd"]
                zoom = start_param[f"{func_param['player'] + 1}p_zoom"]
                print("日常领取的句柄与缩放：", hwnd, zoom)
                # 去除干扰项
                del func_param["func_name"]
                del func_param["player"]
                # 对于每个任务，调用对应的方法
                for key, value in func_param.items():
                    self.formatBusinessMessage(f"开始[{key}]...")
                    try:
                        if isinstance(value, list) and value[0]:
                            result_str = DAILY_AWARD_FUNC_DICT[key](hwnd=hwnd, zoom=zoom, **value[1])
                            self.formatBusinessMessage(result_str)
                        elif isinstance(value, bool) and value:
                            result_str = DAILY_AWARD_FUNC_DICT[key](hwnd=hwnd, zoom=zoom)
                            self.formatBusinessMessage(result_str)
                        else:
                            self.formatBusinessMessage(f"跳过[{key}]")
                    except BusinessError as business_error:
                        business_error_str = f"执行[{key}]功能时出错！\n\n{business_error.error_info}"
                        func_final_status = "wrong"
                        self.signal_send_business_error.emit(business_error_str)
                        self.formatBusinessMessage(business_error_str, "ERROR")
                # 加回该键值对，便于之后的输出
                func_param["func_name"] = "日常领取"
            elif func_param["func_name"] == "刷指定关卡":
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], func_param["player1"])
                player2_info_dict = None
                if func_param["player2"] != 0:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], func_param["player2"])
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                self.setLevelInfo({
                    "has_stage2": func_param["has_stage2"],
                    "shall_continue": func_param["shall_continue"],
                    "max_check_time": start_param["max_check_time"]
                })
                try:
                    # 启动 循环刷指定关卡 的功能
                    self.loopSpecificLevel(
                        func_param["zone_name"],
                        func_param["level_name"],
                        func_param["loop_count"])
                except BusinessError as business_error:
                    business_error_str = f"执行[{func_param['func_name']}]功能时出错！\n\n{business_error.error_info}"
                    func_final_status = "wrong"
                    self.signal_send_business_error.emit(business_error_str)
                    self.formatBusinessMessage(business_error_str, "ERROR")
            elif func_param["func_name"] == "公会任务":
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
                    player2_info_dict = None
                    if func_param["player2"] != 0:
                        player2_info_dict = self.convertToExecute(
                            start_param, plan_info, "1;2", func_param["player2"])
                    self.setPlayerInfo(player1_info_dict, player2_info_dict)
                    self.setLevelInfo({
                        "has_stage2": False,
                        "shall_continue": False,
                        "max_check_time": start_param["max_check_time"]
                    })
                    try:
                        self.startUnionQuest(plan_path)
                    except BusinessError as business_error:
                        business_error_str = f"执行[{func_param['func_name']}]功能时出错！\n\n{business_error.error_info}"
                        func_final_status = "wrong"
                        self.signal_send_business_error.emit(business_error_str)
                        self.formatBusinessMessage(business_error_str, "ERROR")
            elif func_param["func_name"] == "情侣任务":
                if not enable_2p:
                    business_message_str = f"单人模式不支持[{func_param['func_name']}]功能！"
                    self.formatBusinessMessage(business_message_str, "WARN")
                    self.formatBusinessMessage(f"结束功能[{func_param['func_name']}]")
                    self.signal_send_func_status.emit(func_no, func_final_status)
                    func_no += 1
                    continue
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
                    self.setPlayerInfo(player1_info_dict, player2_info_dict)
                    self.setLevelInfo({
                        "has_stage2": False,
                        "shall_continue": False,
                        "max_check_time": start_param["max_check_time"]
                    })
                    try:
                        self.startLoversQuest(plan_path)
                    except BusinessError as business_error:
                        business_error_str = f"执行[{func_param['func_name']}]功能时出错！\n\n{business_error.error_info}"
                        func_final_status = "wrong"
                        self.signal_send_business_error.emit(business_error_str)
                        self.formatBusinessMessage(business_error_str, "ERROR")
            elif func_param["func_name"] == "火山遗迹":
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], func_param["player1"])
                player2_info_dict = None
                if func_param["player2"] != 0:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], func_param["player2"])
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"]
                })
                try:
                    # 启动 循环刷指定关卡 的功能
                    self.startVolcanicRelic(
                        func_param["level_name"],
                        func_param["loop_count"])
                except BusinessError as business_error:
                    business_error_str = f"执行[{func_param['func_name']}]功能时出错！\n\n{business_error.error_info}"
                    func_final_status = "wrong"
                    self.signal_send_business_error.emit(business_error_str)
                    self.formatBusinessMessage(business_error_str, "ERROR")
            elif func_param["func_name"] == "魔塔蛋糕":
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], func_param["player1"])
                player2_info_dict = None
                if func_param["player2"] != 0:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], func_param["player2"])
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"]
                })
                try:
                    # 启动 循环刷指定关卡 的功能
                    self.startMagicTower(
                        func_param["level_num"],
                        func_param["loop_count"])
                except BusinessError as business_error:
                    business_error_str = f"执行[{func_param['func_name']}]功能时出错！\n\n{business_error.error_info}"
                    func_final_status = "wrong"
                    self.signal_send_business_error.emit(business_error_str)
                    self.formatBusinessMessage(business_error_str, "ERROR")
            elif func_param["func_name"] == "跨服远征":
                # 获取放卡方案信息
                plan_path = func_param["plan_path"]
                self.place_plan_procs.setFilePath(plan_path)
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], func_param["player1"])
                player2_info_dict = None
                if func_param["player2"] != 0:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], func_param["player2"])
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                self.setLevelInfo({
                    "has_stage2": False,
                    "shall_continue": False,
                    "max_check_time": start_param["max_check_time"]
                })
                try:
                    # 启动 循环刷指定关卡 的功能
                    self.startCrossService(
                        func_param["player1_room_name_path"],
                        func_param["level_type"],
                        func_param["level_num"],
                        func_param["loop_count"])
                except BusinessError as business_error:
                    business_error_str = f"执行[{func_param['func_name']}]功能时出错！\n\n{business_error.error_info}"
                    func_final_status = "wrong"
                    self.signal_send_business_error.emit(business_error_str)
                    self.formatBusinessMessage(business_error_str, "ERROR")
            elif func_param["func_name"] == "悬赏三连":
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
                    player2_info_dict = None
                    if enable_2p and plan_info["player_num"] == 2:
                        player2_info_dict = self.convertToExecute(
                            start_param, plan_info, "1;2", func_param["player2"])
                    self.setPlayerInfo(player1_info_dict, player2_info_dict)
                    self.setLevelInfo({
                        "has_stage2": True,
                        "shall_continue": True,
                        "max_check_time": start_param["max_check_time"]
                    })
                    try:
                        self.startWanted(func_param["active_level_dict"])
                    except BusinessError as business_error:
                        business_error_str = f"执行[{func_param['func_name']}]功能时出错！\n\n{business_error.error_info}"
                        func_final_status = "wrong"
                        self.signal_send_business_error.emit(business_error_str)
                        self.formatBusinessMessage(business_error_str, "ERROR")
            else:
                self.formatBusinessMessage(f"功能[{func_param['func_name']}]不存在！或该功能处于错误的位置！", "ERROR")
                func_final_status = "wrong"
                self.signal_send_func_status.emit(func_no, func_final_status)
                func_no += 1
                continue

            self.formatBusinessMessage(f"结束功能[{func_param['func_name']}]")
            self.signal_send_func_status.emit(func_no, func_final_status)
            func_no += 1
            self.place_plan_procs.setFilePath(plan_path)
        self.formatBusinessMessage("流程执行完成")
        self.signal_flow_finished.emit(True)

    def convertToExecute(self, start_param, plan_info, flop_pos, player):
        # 获取该账号使用的 卡片组名称
        deck_info = self.player_deck_procs.readDeck(plan_info[f"{player}P所用卡片组"])
        if isinstance(deck_info, tuple):
            deck_name = plan_info[f"{player}P所用卡片组"]
            raise BusinessError(f"放卡方案[{plan_info['plan_name']}]中{player}P所用卡片组“{deck_name}”在账号卡片组ini文件中不存在")
        # 用来存放可执行dict格式中，cards_plan的内容
        cards_plan = []
        # 从卡1到卡n依次存放（这要求放卡方案配置文件里必须保证递增的顺序）
        card_no = 1
        for card_info in plan_info[f"{player}p_card_plan"]:
            # 获取该卡名称，以便在deck_info中得到对应的slot值
            card_name = card_info[f"{player}P卡{card_no}"]
            card_slot = deck_info["deck_slot_info"][card_name]
            # 卡片CD以放卡方案配置文件中的为准
            card_cd = card_info[f"{player}P卡{card_no}CD"]
            # 组装dict
            card_plan = {
                "card_pos_series": card_info[f"{player}P卡{card_no}放置位置"],
                "card_replenish_series": card_info[f"{player}P卡{card_no}补卡位置"],
                "card_slot": int(card_slot),
                "card_cd": int(card_cd)}
            # 加入cards_plan
            cards_plan.append(card_plan)
            card_no += 1
        return {
            "hwnd": start_param[f"{player}p_hwnd"],
            "zoom": start_param[f"{player}p_zoom"],
            "player_pos": plan_info[f"{player}P放置位置"],
            "cards_plan": cards_plan,
            "deck_no": int(deck_info["卡片组编号"]),
            "flop_pos": flop_pos
        }

    def formatBusinessMessage(self, message_str, message_type="INFO"):
        """向主窗口发送 代表 业务执行情况 的文字消息

        Args:
            message_str: str
                消息内容
            message_type: str["INFO", "WARN", "ERROR"]
                消息类型。分为 信息[INFO]、警告[WARN]、错误[ERROR]
        """
        print_str = "{} [{}]: {}\n".format(
            QDateTime.currentDateTime().toString("yyyy/MM/dd hh:mm:ss"),
            message_type, message_str)
        self.signal_send_business_message.emit(print_str)

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
            "2p_name_pic_path": r"D:\PycharmProjects\FVM_Backstage_Assistant_LFBY\resources\images\用户图片\组队房间2P截图示例.bmp",
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
