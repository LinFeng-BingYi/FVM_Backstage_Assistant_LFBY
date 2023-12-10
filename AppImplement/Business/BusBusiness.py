#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : BusBusiness.py
# @Time    : 2023/12/7 1:24
# @Dsc     : 总线业务线程类，需要在执行过程中输出信息，能够接受中断的业务
import ctypes

from PySide6.QtCore import QThread, QThreadPool, QRunnable, Signal, QDateTime

from AppImplement.RWConfigFile.RWPlayerDeck import PlayerDeckProcessor
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor
from AppImplement.Business.Foundation import *
from AppImplement.Business.OrdinaryBusiness import *

import threading


class BusinessBus(QThread):
    # 向主窗口发送待打印日志
    signal_send_business_message = Signal(str)
    # 向主窗口发送功能执行情况（功能在流程中的序号，功能的状态）
    # 状态：['hanging'(挂起)、'waiting'(等待)、'executing'(执行)、'completed'(完成)、'banned'(禁用)、'wrong'(错误)]
    signal_send_func_status = Signal(int, str)
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
        if player2_info is not None:
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
        print("设置了内部参数：\n", self.func_flow)

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
        if not loopCheckStartGame(hwnd_1p, hwnd_2p, zoom1):
            self.formatBusinessMessage("2min未检测到进入关卡！", "ERROR")
            return
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
            if not loopCheckContinue(hwnd_1p):
                # 超过容忍时间 还未检测到“继续挑战”
                self.formatBusinessMessage(
                    f"超过{self.level_info['max_check_time']}分钟还未检测到“继续挑战”！！！",
                    "ERROR")
                return
            # 成功检测到“继续挑战”
            if self.level_info["shall_continue"]:
                # 1P、2P先后点击“继续挑战”
                mouseClick(hwnd_1p, 424 * zoom1, 344 * zoom1)
                delay(500)
                mouseClick(hwnd_2p, 424 * zoom2, 344 * zoom2)
                self.formatBusinessMessage("选择继续挑战")

                delay(1000)

                # 如果没能点击成功，则再点击一次
                if find_color(hwnd_1p, [60, 20, 80, 40], 0x3D4A4C):
                    self.formatBusinessMessage("继续挑战点击失效，正在重新尝试", "WARN")
                    mouseClick(hwnd_1p, 424 * zoom1, 344 * zoom1)
                    delay(500)
                    mouseClick(hwnd_2p, 424 * zoom2, 344 * zoom2)
                    delay(20000)
            else:
                # 1P、2P先后点击“领取奖励”
                mouseClick(hwnd_1p, 512 * zoom1, 344 * zoom1)
                delay(500)
                mouseClick(hwnd_2p, 512 * zoom2, 344 * zoom2)
                self.formatBusinessMessage("选择领取奖励")

        self.formatBusinessMessage("开始检测结算")
        if not loopCheckEndGame(hwnd_1p, self.level_info["max_check_time"]):
            self.formatBusinessMessage(
                f"超过{self.level_info['max_check_time']}分钟还未检测到“结算翻牌”！！！"
                "ERROR")
            return
        # 关闭所有放卡线程
        self.endAllPlacingWorker()
        delay(8200)

        # 成功检测到结算翻牌
        executeFlop(hwnd_1p, self.player1_info["flop_pos"], zoom1)
        executeFlop(hwnd_2p, self.player1_info["flop_pos"], zoom2)
        self.formatBusinessMessage(f"翻取了第{self.player1_info['flop_pos']}张牌")

    def singleFromStartToFlop(self):
        """单人, 从点击 (准备/开始) 到 (结算完成翻牌)
        """
        hwnd_1p = self.player1_info["hwnd"]
        zoom1 = self.player1_info["zoom"]
        # 1P开始
        delay(500)
        mouseClick(hwnd_1p, 872 * zoom1, 480 * zoom1)
        # 检测进入关卡
        if not loopCheckStartGame(hwnd_1p, zoom1):
            self.formatBusinessMessage("2min未检测到进入关卡！", "ERROR")
            return
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
            if not loopCheckContinue(hwnd_1p):
                # 超过容忍时间 还未检测到“继续挑战”
                self.formatBusinessMessage(
                    f"超过{self.level_info['max_check_time']}分钟还未检测到“继续挑战”！！！",
                    "ERROR")
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
                    delay(20000)
            else:
                # 1P点击“领取奖励”
                mouseClick(hwnd_1p, 512 * zoom1, 344 * zoom1)
                self.formatBusinessMessage("选择领取奖励")

        self.formatBusinessMessage("开始检测结算")
        if not loopCheckEndGame(hwnd_1p, self.level_info["max_check_time"]):
            self.formatBusinessMessage(
                f"超过{self.level_info['max_check_time']}分钟还未检测到“结算翻牌”！！！",
                "ERROR")
            return
        # 关闭所有放卡线程
        self.endAllPlacingWorker()
        delay(8200)

        # 成功检测到结算翻牌
        executeFlop(hwnd_1p, self.player1_info["flop_pos"], zoom1)
        self.formatBusinessMessage(f"翻取了第{self.player1_info['flop_pos']}张牌")

    # 最关键的 启用翻牌 或 结束翻牌 ---------------------------------------------------------
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
        self.formatBusinessMessage("启动[刷指定关卡]功能")
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
        self.formatBusinessMessage("应用1P卡片组")
        roomChooseDeck(hwnd_1p, self.player1_info["deck_no"], zoom1)
        if self.player2_info is not None:
            # 邀请队友
            self.formatBusinessMessage("邀请2P")
            teamInvite(hwnd_1p, hwnd_2p, self.global_flow_info["2p_name_pic_path"], zoom1, zoom2)
            self.formatBusinessMessage("应用2P卡片组")
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
        self.formatBusinessMessage("完成[刷指定关卡]功能")

    # 功能：一键签到 ------------------------------------------------------------------
    def signinAndActivity(self, activity_list: list):
        pass

    def run(self) -> None:
        self.formatBusinessMessage("开始依次执行流程列表中可用功能")
        # 先从“开始”功能获取流程全局变量
        start_param = self.func_flow[0]
        player2_name_pic_path = start_param["2p_name_pic_path"]
        deck_path = start_param["deck_path"]
        plan_path = start_param["plan_path"]
        self.setGlobalFlowInfo({
            "2p_name_pic_path": player2_name_pic_path,
            "deck_path": deck_path,
            "plan_path": plan_path
        })
        self.player_deck_procs.setFilePath(deck_path)
        self.place_plan_procs.setFilePath(plan_path)
        # 完成”开始“功能
        self.signal_send_func_status.emit(0, "completed")

        # 再执行每个功能
        func_no = 1     # 功能在流程中的序号
        for func_param in self.func_flow[1:]:
            self.formatBusinessMessage(f"开始功能[{func_param['func_name']}]")
            self.signal_send_func_status.emit(func_no, "executing")
            if func_param["func_name"] == "刷指定关卡":
                # 获取放卡方案信息
                plan_info = self.place_plan_procs.readPlan(func_param["plan_name"])
                # 将 从文件读取的放卡配置的dict格式 转化成可以使用该类的函数执行的dict格式
                player1_info_dict = self.convertToExecute(
                    start_param, plan_info, func_param["flop_pos"], 1)
                player2_info_dict = None
                if plan_info["player_num"] == 2:
                    player2_info_dict = self.convertToExecute(
                        start_param, plan_info, func_param["flop_pos"], 2)
                self.setPlayerInfo(player1_info_dict, player2_info_dict)
                self.setLevelInfo({
                    "has_stage2": func_param["has_stage2"],
                    "shall_continue": func_param["shall_continue"],
                    "max_check_time": start_param["max_check_time"]
                })
                # 启动 循环刷指定关卡 的功能
                self.loopSpecificLevel(
                    func_param["zone_name"],
                    func_param["level_name"],
                    func_param["loop_count"])

            self.formatBusinessMessage(f"结束功能[{func_param['func_name']}]")
            self.signal_send_func_status.emit(func_no, "completed")
        self.formatBusinessMessage("流程执行完成")

    def convertToExecute(self, start_param, plan_info, flop_pos, player):
        # 获取该账号使用的 卡片组名称
        deck_info = self.player_deck_procs.readDeck(plan_info[f"{player}P所用卡片组"])
        # 用来存放可执行dict格式中，cards_plan的内容
        cards_plan = []
        # 从卡1到卡n依次存放（这要求放卡方案配置文件里必须保证递增的顺序）
        card_no = 1
        for card_info in plan_info[f"{player}p_card_plan"]:
            # 获取该卡名称，以便在deck_info中得到对应的slot值
            card_name = card_info[f"{player}P卡{card_no}名称"]
            card_slot = deck_info["deck_slot_info"][card_name]
            # 卡片CD以放卡方案配置文件中的为准
            card_cd = card_info[f"{player}P卡{card_no}CD"]
            # 组装dict
            card_plan = {
                "card_pos_series": card_info[f"{player}P卡{card_no}放置位置"],
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
    # cards_plan_1p = [{
    #     "card_pos_series": "3,9,18000;5,9;1,9",
    #     "card_slot": 7,
    #     "card_cd": 15000
    # }, {
    #     "card_pos_series": "2,9,25000;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9;2,9;3,9;4,9;5,9",
    #     "card_slot": 3,
    #     "card_cd": 7000
    # }, {
    #     "card_pos_series": "1,9,29500;6,9",
    #     "card_slot": 6,
    #     "card_cd": 10000
    # }, {
    #     "card_pos_series": "2,8,30000;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8",
    #     "card_slot": 14,
    #     "card_cd": 29000
    # }]
    # cards_plan_2p = [{
    #     "card_pos_series": "2,9,5500;4,9;6,9",
    #     "card_slot": 7,
    #     "card_cd": 15000
    # }, {
    #     "card_pos_series": "2,8,41500;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8;2,8",
    #     "card_slot": 13,
    #     "card_cd": 29000,
    #     "shovel": True
    # }]
    # player1_info = {"hwnd": 1640472,
    #                 "zoom": 1,
    #                 "player_pos": "4,4",
    #                 "cards_plan": cards_plan_1p,
    #                 "flop_pos": "1"}
    # player2_info = {"hwnd": 1247762,
    #                 "zoom": 1,
    #                 "player_pos": "6,4",
    #                 "cards_plan": cards_plan_2p,
    #                 "flop_pos": "1"}
    # level_info = {"has_stage2": True,
    #               "shall_continue": False,
    #               "max_check_time": 10}
    # business_bus = BusinessBus()
    # business_bus.setPlayerInfo(player1_info, player2_info)
    # business_bus.setLevelInfo(level_info)
    # business_bus.teamFromStartToFlop()

    hwnd1 = 22218732
    hwnd1 = 1709372
    executeVipSignin(hwnd1)
    executeDailySignin(hwnd1)
    executeFreeWish(hwnd1)
    executePharaohTreasure(hwnd1, 1)
    executeTarotTreasure(hwnd1)
    executeReceiveBottomQuest(hwnd1)
    executeUnionGarden(hwnd1, True)
