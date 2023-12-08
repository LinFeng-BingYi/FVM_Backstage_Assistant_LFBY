#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : BaseBusiness.py
# @Time    : 2023/12/7 1:24
# @Dsc     : 基本业务线程类

from PySide6.QtCore import QThread, QThreadPool, QRunnable

from src.AppImplement.Business.Foundation import *


class BusinessBus(QThread):

    def __init__(self):
        super().__init__()

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

        # 业务流程字典
        self.func_flow = {}

    def setPlayerInfo(self, player1_info: dict, player2_info: dict = None):
        """设置账号信息属性。2P信息为 None 时表示单人模式

        Args:
            player1_info: dict
                账号1通关信息
                {
                    "hwnd": int,                // 句柄
                    "zoom" float,               // 窗口缩放比例
                    "player_pos": str,          // 角色位置，格式：1,2
                    "cards_plan": list[dict],         // 卡片放置策略
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

    def setFuncFlow(self, func_flow: dict):
        self.func_flow = func_flow

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
            print("2min未检测到进入关卡！")
            return
        print("检测到进入关卡")
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
            print("开始检测进度")
            # 等待检测到"继续挑战"
            if not loopCheckContinue(hwnd_1p):
                # 超过容忍时间 还未检测到“继续挑战”
                print(f"超过{self.level_info['max_check_time']}分钟还未检测到“继续挑战”！！！")
                return
            # 成功检测到“继续挑战”
            if self.level_info["shall_continue"]:
                # 1P、2P先后点击“继续挑战”
                mouseClick(hwnd_1p, 424 * zoom1, 344 * zoom1)
                delay(500)
                mouseClick(hwnd_2p, 424 * zoom2, 344 * zoom2)
                print("选择继续挑战")

                delay(1000)

                # 如果没能点击成功，则再点击一次
                if find_color(hwnd_1p, [60, 20, 80, 40], 0x3D4A4C):
                    print("[Accident]继续挑战点击失效，正在重新尝试")
                    mouseClick(hwnd_1p, 424 * zoom1, 344 * zoom1)
                    delay(500)
                    mouseClick(hwnd_2p, 424 * zoom2, 344 * zoom2)
                    delay(20000)
            else:
                # 1P、2P先后点击“领取奖励”
                mouseClick(hwnd_1p, 512 * zoom1, 344 * zoom1)
                delay(500)
                mouseClick(hwnd_2p, 512 * zoom2, 344 * zoom2)
                print("选择领取奖励")

        print("开始检测结算")
        if not loopCheckEndGame(hwnd_1p, self.level_info["max_check_time"]):
            print(f"超过{self.level_info['max_check_time']}分钟还未检测到“结算翻牌”！！！")
            return
        # 关闭所有放卡线程
        self.endAllPlacingWorker()
        delay(8200)

        # 成功检测到结算翻牌
        executeFlop(hwnd_1p, self.player1_info["flop_pos"], zoom1)
        executeFlop(hwnd_2p, self.player1_info["flop_pos"], zoom2)
        print(f"翻取了第{self.player1_info['flop_pos']}张牌")

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
            print("2min未检测到进入关卡！")
            return
        print("检测到进入关卡")
        # 放置1P
        delay(100)
        placeCard(hwnd_1p, self.player1_info["player_pos"], zoom1)
        # 启动放卡线程
        self.startPlacingCard(self.player1_info["cards_plan"], 1)

        delay(45000)
        # 检测进度
        if self.level_info["has_stage2"]:
            print("开始检测进度")
            # 等待检测到"继续挑战"
            if not loopCheckContinue(hwnd_1p):
                # 超过容忍时间 还未检测到“继续挑战”
                print(f"超过{self.level_info['max_check_time']}分钟还未检测到“继续挑战”！！！")
                return
            # 成功检测到“继续挑战”
            if self.level_info["shall_continue"]:
                # 1P点击“继续挑战”
                mouseClick(hwnd_1p, 424 * zoom1, 344 * zoom1)
                print("选择继续挑战")

                delay(1000)

                # 如果没能点击成功，则再点击一次
                if find_color(hwnd_1p, [60, 20, 80, 40], 0x3D4A4C):
                    print("[Accident]继续挑战点击失效，正在重新尝试")
                    mouseClick(hwnd_1p, 424 * zoom1, 344 * zoom1)
                    delay(20000)
            else:
                # 1P点击“领取奖励”
                mouseClick(hwnd_1p, 512 * zoom1, 344 * zoom1)
                print("选择领取奖励")

        print("开始检测结算")
        if not loopCheckEndGame(hwnd_1p, self.level_info["max_check_time"]):
            print(f"超过{self.level_info['max_check_time']}分钟还未检测到“结算翻牌”！！！")
            return
        # 关闭所有放卡线程
        self.endAllPlacingWorker()
        delay(8200)

        # 成功检测到结算翻牌
        executeFlop(hwnd_1p, self.player1_info["flop_pos"], zoom1)
        print(f"翻取了第{self.player1_info['flop_pos']}张牌")

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
            place_worker = CardPlaceWorker(hwnd, zoom, card_info)
            self.card_place_thread_pool.start(place_worker)

    def endAllPlacingWorker(self, wait_time=5):
        print("尝试结束")
        start_time = time()
        self.card_place_thread_pool.waitForDone(wait_time)
        print("花费时间：", time() - start_time)


class CardPlaceWorker(QRunnable):
    def __init__(self, hwnd, zoom, card_info: dict):
        super().__init__()

        self.hwnd = hwnd
        self.zoom = zoom
        self.card_info = card_info

    def run(self) -> None:
        card_pos_series = self.card_info["card_pos_series"]
        card_slot = self.card_info["card_slot"]
        card_cd = self.card_info["card_cd"]
        if "shovel" in self.card_info:
            loopPlaceCard(self.hwnd, card_pos_series, card_slot, card_cd, self.zoom)
        else:
            loopPlaceCardUpgrade(self.hwnd, card_pos_series, card_slot, card_cd, self.zoom)


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
    player1_info = {"hwnd": 1640472,
                    "zoom": 1,
                    "player_pos": "4,4",
                    "cards_plan": cards_plan_1p,
                    "flop_pos": "1"}
    player2_info = {"hwnd": 1247762,
                    "zoom": 1,
                    "player_pos": "6,4",
                    "cards_plan": cards_plan_2p,
                    "flop_pos": "1"}
    level_info = {"has_stage2": True,
                  "shall_continue": False,
                  "max_check_time": 10}
    business_bus = BusinessBus()
    business_bus.setPlayerInfo(player1_info, player2_info)
    business_bus.setLevelInfo(level_info)
    business_bus.teamFromStartToFlop()
