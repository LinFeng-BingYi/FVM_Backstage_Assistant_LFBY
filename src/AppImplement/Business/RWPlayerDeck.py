#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : RWPlayerDeck.py
# @Time    : 2023/12/3 16:22
# @Dsc     : 实现对账号预设卡组信息的读写

from src.Common.FileProcess.INIProcess import INIProcessor

EXCLUDE_SECTION = ['Default', 'CD配置']
DECK_COMMON_KEY = ["描述", "卡片组编号", "卡片CD配置"]


class PlayerDeckProcessor:

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
        """返回排除"CD配置"等section后的所有预设卡片组section

        Returns: list[str]
        """
        sections = self.ini_procs.getAllSection()
        result = list()
        for section_ex in EXCLUDE_SECTION:
            result = [section_str
                      for i, section_str in enumerate(sections)
                      if section_str.find(section_ex) == -1]
        return result

    def readCardCd(self, cd_section):
        """返回指定的"CD配置"节中的信息

        Args:
            cd_section: str
                卡片CD配置section

        Returns: dict
            example:
                {
                    "默认": 7000,
                    "狮子座": 35000
                }
        """
        if cd_section not in self.ini_procs.getAllSection():
            return None, 'section'
        # 获取卡片组内CD
        card_cd_dict = dict()
        for key in self.ini_procs.getAllKey(cd_section):
            # print(key)
            cd_info = int(self.ini_procs.getSpecificValue(cd_section, key))
            card_cd_dict[key] = cd_info
        return card_cd_dict

    def readDeck(self, deck_name):
        """解析指定的"预设卡片组"信息

        Args:
            deck_name: str

        Returns: dict | tuple[None, str['section']]
            解析结果。预设卡片组名称不存在时返回一个tuple。
            解析成功时返回的格式如下
            example:
                {
                    "deck_name": "预设卡片组名称",
                    "描述": "预设卡片组描述",
                    "卡片组编号": "2",    // 选卡界面中的卡片组所在顺序
                    "卡片CD配置": "大号_CD配置",
                    "deck_slot_info": {”小火“： 1， “海星”： 3}
                    "deck_cd_info": {”小火“： 7000， “海星”： 7000}
                }
            其中"deck_slot_info"的值 dict[str, int] 中第一个元素是卡片的名称, 第二个是卡槽位置
        """
        if deck_name not in self.ini_procs.getAllSection():
            return None, 'section'
        deck_dict = dict()
        # 设置软件运行时的中间变量 deck_name
        deck_dict['deck_name'] = deck_name
        # 获取通用设置
        for key in DECK_COMMON_KEY:
            deck_dict[key] = self.ini_procs.getSpecificValue(deck_name, key)
        # 获取卡片组内各卡片的 卡槽位置信息
        deck_slot_info = dict()
        # 获取卡片组内CD
        deck_cd_info = dict()
        card_cd_dict = self.readCardCd(deck_dict["卡片CD配置"])
        # 获取属于卡片的键名
        # card_name_list = list(set(self.ini_procs.getAllKey(deck_name)) - set(DECK_COMMON_KEY))
        card_name_list = self.ini_procs.getAllKey(deck_name)
        card_name_list = [card_name for card_name in card_name_list if card_name not in DECK_COMMON_KEY]
        for key in card_name_list:
            slot_info = self.ini_procs.getSpecificValue(deck_name, key)
            deck_slot_info[key] = slot_info
            # 添加到卡组内CD字典
            deck_cd_info[key] = card_cd_dict[key] if key in list(card_cd_dict) else card_cd_dict["默认"]
        deck_dict['deck_slot_info'] = deck_slot_info
        deck_dict['deck_cd_info'] = deck_cd_info
        # print("卡片组信息：\n", deck_dict)
        return deck_dict

    def writeDeck(self, deck_dict):
        deck_name = deck_dict['deck_name']
        # 先删除所有key，避免新增的键值对顺序不对
        self.ini_procs.deleteBatchValue(deck_name, self.ini_procs.getAllKey(deck_dict['plan_name']))
        # 写入通用设置
        for key in DECK_COMMON_KEY:
            self.ini_procs.setSpecificValue(deck_name, key, deck_dict[key])
        # 写入各卡片卡槽信息
        deck_slot_dict = deck_dict['deck_slot_info']
        for key in deck_slot_dict:
            self.ini_procs.setSpecificValue(deck_name, key, deck_dict[key])
