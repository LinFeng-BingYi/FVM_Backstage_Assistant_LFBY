#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : RWPlacingPlan.py
# @Time    : 2023/12/3 2:01
# @Dsc     : 实现对卡片放置方案文件的读写

from Common.FileProcess.INIProcess import INIProcessor

COMMON_1P_KEY = ["描述", "1P放置位置", "1P所用卡片组"]
COMMON_2P_KEY = ["描述", "1P放置位置", "2P放置位置", "1P所用卡片组", "2P所用卡片组"]
CARD_KEY = ["{}P卡{}", "{}P卡{}放置位置", "{}P卡{}CD"]


class PlacingPlanProcessor:

    def __init__(self, file_path, encoding='utf-8'):
        self.ini_procs: INIProcessor = None
        self.file_path = None
        self.encoding = encoding

        self.setFilePath(file_path, encoding)

    def setFilePath(self, file_path, encoding='utf-8'):
        """设置属性 file_path、encoding，使同一个类可以处理不同的文件

        Args:
            file_path: str
                文件路径
            encoding: str
                文件编码. 默认为 'utf-8'
        """
        if file_path is None:
            return
        # 文件没改变则直接退出
        if file_path == self.file_path:
            return
        try:
            self.ini_procs = INIProcessor(file_path, encoding)
        except Exception as e:
            raise e
        # 出现异常则不更新属性file_path
        self.file_path = file_path
        self.encoding = encoding

    def getAllSection(self):
        return self.ini_procs.getAllSection()

    def readPlan(self, plan_name):
        """解析指定的卡片放置方案配置

        Args:
            plan_name: str
                卡片放置方案的名称

        Returns: dict | tuple[None, str['section']]
            解析结果。方案配置名称不存在时返回一个tuple。
            解析成功时返回的格式如下
            example:
                {
                    "plan_name": "方案的名称",
                    "player_num": 2,
                    "描述": "方案的描述",
                    "1P放置位置": "1,1",
                    "2P放置位置": "2,1",
                    "1P所用卡片组": "大号_综合挂机",
                    "2P所用卡片组": "小号_综合挂机",
                    "1p_card_plan": list[dict[str, str]],
                    "2p_card_plan": list[dict[str, str]]
                }
        """
        if plan_name not in self.ini_procs.getAllSection():
            return None, 'section'
        plan_dict = dict()
        # 设置软件运行时的中间变量 plan_name, player_num
        plan_dict['plan_name'] = plan_name
        plan_dict['player_num'] = 1     # 默认为1
        if self.ini_procs.hasKey(plan_name, "2P放置位置"):
            plan_dict['player_num'] = 2
        # 单人配置
        if plan_dict['player_num'] == 1:
            for key in COMMON_1P_KEY:
                plan_dict[key] = self.ini_procs.getSpecificValue(plan_name, key)
            plan_dict['1p_card_plan'] = self.readPlayerCardPlan(plan_name, 1)
        # 组队配置
        else:
            for key in COMMON_2P_KEY:
                plan_dict[key] = self.ini_procs.getSpecificValue(plan_name, key)
            plan_dict['1p_card_plan'] = self.readPlayerCardPlan(plan_name, 1)
            plan_dict['2p_card_plan'] = self.readPlayerCardPlan(plan_name, 2)
        print(plan_dict)
        return plan_dict

    def readPlayerCardPlan(self, plan_name, player):
        """解析玩家1(房主) 或 家2(房客)的卡片放置方案

        Args:
            plan_name: str
                卡片放置方案的名称
            player: int[1 | 2]
                表示 玩家1(房主) 或 家2(房客) 的数字

        Returns: list[dict[str, str]]
            卡片放置方案
             example:
                [
                    {
                        "1P卡1": "海星",
                        "1P卡1放置位置": "3,9,0;5,9;2,9;4,9",
                        "1P卡1CD": "7000"
                    }, {
                        "1P卡2": "狮子座",
                        "1P卡2放置位置": "3,7,52000;5,7",
                        "1P卡2CD": "35000"
                    }
                ]
        """
        parse_list = []
        if plan_name not in self.getAllSection():
            return
        card_num = self.findPlanCardNum(plan_name, player)
        for i in range(1, card_num + 1):
            card_dict = dict()
            for key in CARD_KEY:
                key = key.format(player, i)
                card_dict[key] = self.ini_procs.getSpecificValue(plan_name, key)
            parse_list.append(card_dict)
        return parse_list

    def findPlanCardNum(self, plan_name, player):
        """查找指定方案中，玩家使用卡片的数量

        Args:
            plan_name: str
                卡片放置方案的名称
            player: int[1 | 2]
                表示 玩家1(房主) 或 家2(房客) 的数字

        Returns: int
        """
        card_num = 0
        for i in range(1, 22):
            if self.ini_procs.hasKey(plan_name, f"{player}P卡{i}"):
                card_num = i
            else:
                break
        return card_num

    def writePlan(self, plan_dict):
        plan_name = plan_dict['plan_name']
        # 先删除所有key，避免新增的键值对顺序不对
        self.ini_procs.deleteBatchValue(plan_name, self.ini_procs.getAllKey(plan_dict['plan_name']))
        # 单人配置
        if plan_dict['player_num'] == 1:
            for key in COMMON_1P_KEY:
                self.ini_procs.setSpecificValue(plan_name, key, plan_dict[key])
            self.writePlayerCardPlan(plan_name, plan_dict['1p_card_plan'], 1)
        # 组队配置
        else:
            for key in COMMON_2P_KEY:
                self.ini_procs.setSpecificValue(plan_name, key, plan_dict[key])
            self.writePlayerCardPlan(plan_name, plan_dict['1p_card_plan'], 1)
            self.writePlayerCardPlan(plan_name, plan_dict['2p_card_plan'], 2)

    def writePlayerCardPlan(self, plan_name, card_plan):
        for card_dict in card_plan:
            self.ini_procs.setBatchValue(plan_name, card_dict)


if __name__ == '__main__':
    file_name = r"D:\Softwares\按键精灵\美食组队脚本\TeamConfig-V6.04-utf8.ini"
    procs = PlacingPlanProcessor(file_name)
    result = procs.readPlan("曲奇岛")
    print(result)
    procs.writePlan(result)
