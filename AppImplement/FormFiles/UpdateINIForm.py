#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : UpdateINIForm.py
# @Time    : 2023/11/27 21:08
# @Dsc     : 实现升级ini文件到V6.05的界面和操作逻辑

from PySide6.QtWidgets import QWidget, QFileDialog, QApplication
from AppImplement.FormFiles.CustomWidgets.MessageBox import TipMessageBox

import os
from shutil import copyfile

from AppImplement.FormFiles.UpdateINI import Ui_UpdateINI
from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH
from AppImplement.RWConfigFile.RWPlayerDeck import DECK_COMMON_KEY, PlayerDeckProcessor
from Common.FileProcess.INIProcess import INIProcessor


class WidgetUpdateINI(QWidget, Ui_UpdateINI):
    def __init__(self):
        super(WidgetUpdateINI, self).__init__()
        self.setupUi(self)

        self.file_processor: INIProcessor = None    # ini文件读写器
        self.player_deck_procs = None
        self.cwd = ROOT_PATH                      # 程序当前工作目录
        self.tip_dialog = None

        self.bindSignal()

    def bindSignal(self):
        # <简易组队脚本>
        self.pushButton_file_path.clicked.connect(lambda: self.chooseIniFile(self.lineEdit_file_path))
        self.pushButton_execute.clicked.connect(self.updateIniFileToV6_05)
        # <一键日常助手>
        self.pushButton_deck_path_new_v001.clicked.connect(self.chooseDeckFile)
        self.pushButton_file_path_new_v001.clicked.connect(lambda: self.chooseIniFile(self.lineEdit_file_path_new_v001))
        self.pushButton_execute_new_v001.clicked.connect(self.updateIniFileToNewV0_01)

    def chooseIniFile(self, lineEdit):
        chosen_file, file_type = QFileDialog.getOpenFileName(self, "选择文件",
                                                             self.cwd,
                                                             "All Files(*);;INI Files(*.ini)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        lineEdit.setText(norm_file_path)

    def chooseDeckFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(self, "选择文件",
                                                             self.cwd,
                                                             "All Files(*);;INI Files(*.ini)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        self.lineEdit_deck_path_new_v001.setText(norm_file_path)
        player_deck_procs = PlayerDeckProcessor(norm_file_path)
        deck_name_list = player_deck_procs.getAllSection()
        self.comboBox_deck_select_1p_new_v001.clear()
        self.comboBox_deck_select_1p_new_v001.addItems(deck_name_list)
        self.comboBox_deck_select_2p_new_v001.clear()
        self.comboBox_deck_select_2p_new_v001.addItems(deck_name_list)

    # 简易组队脚本 -------------------------------------------------------------------
    def updateIniFileToV6_05(self):
        if not self.lineEdit_file_path.text():
            print("还未选择文件！!")
            return
        if ".ini" != self.lineEdit_file_path.text()[-4:]:
            print("请选择INI文件！！")
            return
        current_section = ""
        new_abstract_file_path = ""
        try:
            abstract_file_path = self.lineEdit_file_path_new_v001.text()
            file_dir = os.path.dirname(abstract_file_path)
            pure_file_name = os.path.basename(abstract_file_path)
            new_pure_file_name = pure_file_name.rsplit('.', 1)[0] + "_V6.05.ini"
            new_abstract_file_path = file_dir + "\\" + new_pure_file_name

            copyfile(abstract_file_path, new_abstract_file_path)
            self.file_processor = INIProcessor(new_abstract_file_path)

            for section in self.file_processor.getAllSection():
                if self.file_processor.hasKey(section, "2P放置位置"):
                    self.updateTeamConfigToV6_05(section)
                else:
                    self.updateSingleConfigToV6_05(section)

            self.tip_dialog = TipMessageBox("提示", f"成功转换INI文件！！\n请在同级目录查看文件：\n{new_pure_file_name}")
            self.tip_dialog.show()
        except Exception as e:
            if new_abstract_file_path != "":
                os.remove(new_abstract_file_path)
            dialog_text_tittle = "INI文件格式有误：\n错误信息如下" if current_section == "" else f"处理放卡方案[{current_section}]时发生错误"
            except_tuple = e.args
            print(except_tuple)
            error_message = ''
            for i in range(len(except_tuple)):
                error_message = error_message + str(except_tuple[i].decode('gbk') if isinstance(except_tuple[i], bytes) else except_tuple[i])
                error_message = error_message + '\n'
            if except_tuple[0] == 'utf-8':
                self.tip_dialog = TipMessageBox("错误", f"请先通过记事本将INI文件另存为UTF-8格式")
            else:
                self.tip_dialog = TipMessageBox("错误", f"{dialog_text_tittle}：\n\n{error_message}")
            self.tip_dialog.show()

    def updateTeamConfigToV6_05(self, section):
        # 获取卡1-卡5各自前置延时列表
        delay_1p = []
        delay_2p = []
        for i in range(1, 6):
            delay_1p.append(int(self.file_processor.getSpecificValue(section, f"1P卡{i}前置延时")))
            delay_2p.append(int(self.file_processor.getSpecificValue(section, f"2P卡{i}前置延时")))
        # 获取卡1-卡5各自开局多久放卡
        for i in range(4):
            delay_1p[i + 1] += delay_1p[i]
            delay_2p[i + 1] += delay_2p[i]
        # 更新放卡位置
        for i in range(1, 6):
            # 若1P卡i激活，则更新放置位置和CD
            if self.file_processor.getSpecificValue(section, f"1P卡{i}") == '1':
                self.updateCardPosToV6_05(section, 1, i, delay_1p)
                self.updateCardCdToV6_05(section, 1, i)
            # 若2P卡i激活，则更新放置位置和CD
            if self.file_processor.getSpecificValue(section, f"2P卡{i}") == '1':
                self.updateCardPosToV6_05(section, 2, i, delay_2p)
                self.updateCardCdToV6_05(section, 2, i)
            # 删除前置延时
            self.file_processor.deleteSectionOrValue(section, f"1P卡{i}前置延时")
            self.file_processor.deleteSectionOrValue(section, f"2P卡{i}前置延时")

    def updateSingleConfigToV6_05(self, section):
        # 获取卡1-卡8各自前置延时列表
        delay_1p = []
        for i in range(1, 9):
            delay_1p.append(int(self.file_processor.getSpecificValue(section, f"1P卡{i}前置延时")))
        # 获取卡1-卡8各自开局多久放卡
        for i in range(7):
            delay_1p[i + 1] += delay_1p[i]
        # 更新放卡位置
        for i in range(1, 9):
            # 若1P卡i激活，则更新放置位置和CD
            if self.file_processor.getSpecificValue(section, f"1P卡{i}") == '1':
                self.updateCardPosToV6_05(section, 1, i, delay_1p)
                self.updateCardCdToV6_05(section, 1, i)
            # 删除前置延时
            self.file_processor.deleteSectionOrValue(section, f"1P卡{i}前置延时")

    def updateCardPosToV6_05(self, section, player: int, card_no: int, delay_list: list):
        """更新配置方案中的卡片放置位置

        Args:
            section: str
                方案名称，ini文件中的节section
            player: int[1, 2]
                玩家，1代表1P，2代表2P
            card_no: int
                卡片编号，从1开始
            delay_list: list[int]
                前置延时列表
        """
        # 更新放卡位置字符串
        card_pos_str = self.file_processor.getSpecificValue(section, f"{player}P卡{card_no}放置位置")
        card_pos_split_list = card_pos_str.split(';', 1)
        # 放卡位置坐标数量大于2
        if len(card_pos_split_list) > 1:
            card_pos_new = card_pos_split_list[0] + f",{delay_list[card_no - 1]};" + card_pos_split_list[1]
        # 放卡位置坐标数量为1
        elif len(card_pos_split_list) == 1:
            card_pos_new = card_pos_str + f",{delay_list[card_no - 1]}"
        # 激活但是没有位置
        else:
            self.tip_dialog = TipMessageBox("错误", f"INI文件格式有误：\n方案[{section}]中，{player}P卡{card_no}被激活，但是放置位置为空！！")
            self.tip_dialog.show()
            return
        self.file_processor.setSpecificValue(section, f"{player}P卡{card_no}放置位置", card_pos_new)

    def updateCardCdToV6_05(self, section, player: int, card_no: int):
        """更新配置方案中的卡片CD

        Args:
            section: str
                方案名称，ini文件中的节section
            player: int[1, 2]
                玩家，1代表1P，2代表2P
            card_no: int
                卡片编号，从1开始
        """
        card_cd_dict = {'0': '7000', '1': '3000', '2': '4000', '3': '9000', '4': '15000',
                        '5': '25000', '6': '30000', '7': '40000', '8': '50000'}
        current_cd = self.file_processor.getSpecificValue(section, f"{player}P卡{card_no}CD")
        self.file_processor.setSpecificValue(section, f"{player}P卡{card_no}CD", card_cd_dict[current_cd])

    # 一键日常助手 -------------------------------------------------------------------
    def updateIniFileToNewV0_01(self):
        if not self.lineEdit_file_path_new_v001.text():
            print("还未选择文件！!")
            return
        if ".ini" != self.lineEdit_file_path_new_v001.text()[-4:]:
            print("请选择INI文件！！")
            return
        current_section = ""
        new_abstract_file_path = ""
        try:
            abstract_file_path = self.lineEdit_file_path_new_v001.text()
            file_dir = os.path.dirname(abstract_file_path)
            pure_file_name = os.path.basename(abstract_file_path)
            new_pure_file_name = "升级版" + pure_file_name.rsplit('.', 1)[0] + "_V1.00.ini"
            new_abstract_file_path = file_dir + "\\" + new_pure_file_name

            copyfile(abstract_file_path, new_abstract_file_path)
            self.file_processor = INIProcessor(new_abstract_file_path)

            for section in self.file_processor.getAllSection():
                current_section = section
                if self.file_processor.hasKey(section, "2P放置位置"):
                    self.updateTeamConfigToNewV0_01(section,
                                                    self.comboBox_deck_select_1p_new_v001.currentText(),
                                                    self.lineEdit_deck_path_new_v001.text(),
                                                    self.comboBox_deck_select_2p_new_v001.currentText())
                else:
                    self.updateTeamConfigToNewV0_01(section,
                                                    self.comboBox_deck_select_1p_new_v001.currentText(),
                                                    self.lineEdit_deck_path_new_v001.text())

            # 添加[默认配置]
            if "默认方案" not in self.file_processor.getAllSection():
                if self.file_processor.hasKey(self.file_processor.getAllSection()[0], "2P放置位置"):
                    default_plan_dict = {
                        "描述": "当未找到目标方案时，软件会自动使用该方案",
                        "1P放置位置": "6,1",
                        "2P放置位置": "2,1",
                        "1P所用卡片组": f"{self.comboBox_deck_select_1p_new_v001.currentText()}",
                        "2P所用卡片组": f"{self.comboBox_deck_select_2p_new_v001.currentText()}"
                    }
                else:
                    default_plan_dict = {
                        "描述": "当未找到目标方案时，软件会自动使用该方案",
                        "1P放置位置": "6,1",
                        "1P所用卡片组": f"{self.comboBox_deck_select_1p_new_v001.currentText()}"
                    }
                self.file_processor.setBatchValue("默认方案", default_plan_dict)

            self.tip_dialog = TipMessageBox("提示", f"成功转换INI文件！！\n请在同级目录查看文件：\n{new_pure_file_name}")
            self.tip_dialog.show()
        except KeyError as keyError:
            if new_abstract_file_path != "":
                os.remove(new_abstract_file_path)
            dialog_text_tittle = "INI文件格式有误：\n错误信息如下" if current_section == "" else f"处理放卡方案[{current_section}]时发生错误"
            self.tip_dialog = TipMessageBox(
                "错误",
                f"{dialog_text_tittle}: \n\n卡槽位置{keyError.args}在所用卡组中不存在"
            )
            self.tip_dialog.show()
        except Exception as e:
            if new_abstract_file_path != "":
                os.remove(new_abstract_file_path)
            dialog_text_tittle = "INI文件格式有误：\n错误信息如下" if current_section == "" else f"处理放卡方案[{current_section}]时发生错误"
            except_tuple = e.args
            print(except_tuple)
            error_message = ''
            for i in range(len(except_tuple)):
                error_message = error_message + str(except_tuple[i].decode('gbk') if isinstance(except_tuple[i], bytes) else except_tuple[i])
                error_message = error_message + '\n'
            if except_tuple[0] == 'utf-8':
                self.tip_dialog = TipMessageBox("错误", f"请先通过记事本将INI文件另存为UTF-8格式")
            else:
                self.tip_dialog = TipMessageBox("错误", f"{dialog_text_tittle}：\n\n{e.__repr__()}\n{error_message}")
            self.tip_dialog.show()

    def getNewCardInfo(self, player_deck_path, deck_name):
        """获取<一键日常助手>中卡片组文件中对应卡片组的信息

        Args:
            player_deck_path: str
                文件路径
            deck_name: str
                卡片组名称

        Returns:
            卡槽位置对应的卡片名称字典
            example:
            {
                "1": "小火",
                "3": "海星",
                "5": "狮子座"
            }
        """
        self.player_deck_procs = INIProcessor(player_deck_path)
        card_name_list = self.player_deck_procs.getAllKey(deck_name)
        card_name_list = [card_name for card_name in card_name_list if card_name not in DECK_COMMON_KEY]
        deck_slot_info = {}
        for key in card_name_list:
            slot_no = self.player_deck_procs.getSpecificValue(deck_name, key)
            deck_slot_info[slot_no] = key
        return deck_slot_info

    def updateTeamConfigToNewV0_01(self, section, player1_deck_name, player_deck_path, player2_deck_name=None):
        """将<简易组队脚本>V6.05及以上的ini文件更新，以适配<一键日常助手>

        Args:
            section: str
                放卡方案名称
            player1_deck_name: str
                1P所用卡片组名称
            player_deck_path: str
                卡片组文件路径
            player2_deck_name: str
                2P所用卡片组名称
        """
        enable_2p = True
        if player2_deck_name is None:
            enable_2p = False

        plan_dict = dict()
        plan_dict["描述"] = self.file_processor.getSpecificValue(section, "描述")
        plan_dict["1P放置位置"] = self.file_processor.getSpecificValue(section, "1P放置位置")
        if enable_2p:
            plan_dict["2P放置位置"] = self.file_processor.getSpecificValue(section, "2P放置位置")
        plan_dict["1P所用卡片组"] = player1_deck_name
        if enable_2p:
            plan_dict["2P所用卡片组"] = player2_deck_name

        # 获取1P卡槽位置信息
        deck_info_1p = self.getNewCardInfo(player_deck_path, player1_deck_name)
        # 获取1P每张卡的信息
        card_no = 0
        for i in range(1, 6):
            if not self.file_processor.hasKey(section, f"1P卡{i}") or \
                    self.file_processor.getSpecificValue(section, f"1P卡{i}") == '0':
                continue
            card_no += 1
            plan_dict[f"1P卡{card_no}"] = deck_info_1p[self.file_processor.getSpecificValue(section, f"1P卡{i}卡槽位置")]
            plan_dict[f"1P卡{card_no}放置位置"] = self.file_processor.getSpecificValue(section, f"1P卡{i}放置位置")
            plan_dict[f"1P卡{card_no}CD"] = self.file_processor.getSpecificValue(section, f"1P卡{i}CD")
        if enable_2p:
            # 获取2P卡槽位置信息
            deck_info_2p = self.getNewCardInfo(player_deck_path, player2_deck_name)
            # 获取2P每张卡的信息
            card_no = 0
            for i in range(1, 6):
                if not self.file_processor.hasKey(section, f"2P卡{i}") or \
                        self.file_processor.getSpecificValue(section, f"2P卡{i}") == '0':
                    continue
                card_no += 1
                plan_dict[f"2P卡{card_no}"] = deck_info_2p[self.file_processor.getSpecificValue(section, f"2P卡{i}卡槽位置")]
                plan_dict[f"2P卡{card_no}放置位置"] = self.file_processor.getSpecificValue(section, f"2P卡{i}放置位置")
                plan_dict[f"2P卡{card_no}CD"] = self.file_processor.getSpecificValue(section, f"2P卡{i}CD")

        # 先删除所有key，避免新增的键值对顺序不对
        self.file_processor.deleteBatchValue(section, self.file_processor.getAllKey(section))
        # 批量写入
        self.file_processor.setBatchValue(section, plan_dict)


if __name__ == "__main__":
    deck_path = r"D:\PycharmProjects\FVM_Backstage_Assistant_LFBY\config\卡片放置方案\账号预设卡片组.ini"
    plan_path = r"D:\PycharmProjects\FVM_Backstage_Assistant_LFBY\config\卡片放置方案\组队常用方案_utf-8.ini"

    app = QApplication([])
    widget = WidgetUpdateINI()
    widget.file_processor = INIProcessor(plan_path)
    widget.updateTeamConfigToNewV0_01(
        "深渊岛",
        "大号_综合挂机",
        deck_path,
        "小号_综合挂机")
    widget.show()
    app.exec()

