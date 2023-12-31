#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : EditPlacingPlanForm.py
# @Time    : 2023/12/2 22:28
# @Dsc     : 实现编辑卡片放置方案的界面功能

from PySide6.QtWidgets import QWidget, QFileDialog, QTableWidget, QComboBox, QTableWidgetItem, QLineEdit, QHeaderView, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

import os

from AppImplement.FormFiles.EditPlacingPlan import Ui_EditPlacingPlan
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor
from AppImplement.RWConfigFile.RWPlayerDeck import PlayerDeckProcessor

from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH, DEFAULT_PLACING_PLAN_INI, DEFAULT_DECK_INI


class WidgetEditPlacingPlan(QWidget, Ui_EditPlacingPlan):

    def __init__(self):
        super(WidgetEditPlacingPlan, self).__init__()
        self.setupUi(self)
        self.tableWidget_1p_placing_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_1p_placing_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_2p_placing_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_2p_placing_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        self.cwd = ROOT_PATH                                # 程序当前工作目录
        self.place_plan_procs = PlacingPlanProcessor(None)    # 放卡方案文件读写器
        self.player_deck_procs = PlayerDeckProcessor(None)

        self.initWidgets()
        self.bindSignal()

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

    def initWidgets(self):
        # 默认路径
        self.lineEdit_plan_path.setText(DEFAULT_PLACING_PLAN_INI)
        self.lineEdit_deck_path.setText(DEFAULT_DECK_INI)
        # 初始化本窗口的文件处理器
        self.place_plan_procs.setFilePath(DEFAULT_PLACING_PLAN_INI)
        self.player_deck_procs.setFilePath(DEFAULT_DECK_INI)
        # 填充放卡方案、卡片组comboBox
        self.comboBox_choose_section.addItems(self.place_plan_procs.getAllSection())
        all_player_decks = self.player_deck_procs.getAllSection()
        self.comboBox_1p_deck.addItems(all_player_decks)
        self.comboBox_2p_deck.addItems(all_player_decks)

        # 更新界面
        self.responsePlanPathChange()

    def bindSignal(self):
        # 放卡方案ini文件
        self.pushButton_plan_path.clicked.connect(self.chooseFile)
        # 显示方案内容
        self.comboBox_choose_section.currentIndexChanged.connect(self.displayPlan)

    def chooseFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(self, "选择文件", self.cwd + "\\userdata\\卡片放置方案",
                                                             "All Files(*);;INI Files(*.ini)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.' or norm_file_path[-4:] != '.ini':
            print("未选择正确的ini文件！！")
            return
        self.lineEdit_plan_path.setText(norm_file_path)
        self.responsePlanPathChange()

    def clearWidgets(self):
        """更换选择的放卡方案后，先清除界面上的控件"""
        self.comboBox_choose_section.clear()
        self.lineEdit_1p_pos.clear()
        self.lineEdit_2p_pos.clear()
        self.listWidget_1p_deck.clear()
        self.listWidget_2p_deck.clear()
        self.tableWidget_1p_placing_table.setRowCount(0)
        self.tableWidget_2p_placing_table.setRowCount(0)

    def responsePlanPathChange(self):
        self.clearWidgets()
        # 更新文件处理器存储的文件路径
        self.place_plan_procs.setFilePath(self.lineEdit_plan_path.text())
        # 填充放卡方案comboBox
        print(self.place_plan_procs.getAllSection())
        self.comboBox_choose_section.addItems(self.place_plan_procs.getAllSection())

        self.displayPlan()

    def displayPlan(self):
        plan_name = self.comboBox_choose_section.currentText()
        if plan_name == '':     # 表示文件中没有方案
            return
        # 解析当前的卡片放置方案
        plan_content = self.place_plan_procs.readPlan(plan_name)
        print(plan_content)
        # 设置单人/组队模式
        self.checkBox_is_team_mode.setChecked(True if plan_content['player_num'] == 2 else False)
        # 填充区域 -----------------------------------
        # 放置位置
        self.lineEdit_1p_pos.setText(plan_content["1P放置位置"])
        # 所用卡片组
        # 解析该放卡方案中1P所用卡片组
        deck_1p = self.player_deck_procs.readDeck(plan_content["1P所用卡片组"])
        # print(deck_1p)
        self.comboBox_1p_deck.setCurrentText(deck_1p["deck_name"])
        # 更新1P卡槽listWidget
        self.updateCardPlacingTable(self.tableWidget_1p_placing_table,
                                    1,
                                    plan_content["1p_card_plan"],
                                    deck_1p)
        if self.checkBox_is_team_mode.isChecked():
            self.lineEdit_2p_pos.setText(plan_content["2P放置位置"])
            deck_2p = self.player_deck_procs.readDeck(plan_content["2P所用卡片组"])
            # print(deck_2p)
            self.comboBox_2p_deck.setCurrentText(deck_2p["deck_name"])
            self.updateCardPlacingTable(self.tableWidget_2p_placing_table,
                                        2,
                                        plan_content["2p_card_plan"],
                                        deck_2p)

    def updateCardPlacingTable(self, tableWidget: QTableWidget, player, card_plan_list, deck_info):
        tableWidget.setRowCount(0)
        tableWidget.setRowCount(len(card_plan_list) + 1)

        current_row = 0
        for card_dict in card_plan_list:
            self.setExistTableCell(tableWidget, current_row, player, card_dict, deck_info)
            current_row += 1

    def setExistTableCell(self, tableWidget, current_row, player: int, card_dict: dict, deck_info: dict):
        for key, value in card_dict.items():
            if key == f"{player}P卡{current_row + 1}":
                comboBox = QComboBox(tableWidget)
                comboBox.setEditable(True)
                comboBox.addItems(list(deck_info["deck_slot_info"]))
                comboBox.setCurrentText(value)
                tableWidget.setCellWidget(current_row, 0, comboBox)
            elif key == f"{player}P卡{current_row + 1}放置位置":
                lineEdit = QLineEdit(tableWidget)
                font = QFont()
                font.setBold(True)
                font.setPointSize(12)
                font.setFamily("Times New Roman")
                lineEdit.setFont(font)
                lineEdit.setText(value)
                tableWidget.setCellWidget(current_row, 2, lineEdit)
            elif key == f"{player}P卡{current_row + 1}CD":
                tableWidget.setItem(current_row, 3, QTableWidgetItem(value))
            else:
                print("未知的记录属性！！: ", key)
                return
            # 设置卡片卡槽位置
            card_slot = deck_info["deck_slot_info"][card_dict[f"{player}P卡{current_row + 1}"]]
            # card_cd = deck_info["deck_cd_info"][card_dict[f"{player}P卡{current_row + 1}"]]
            tableWidget.setItem(current_row, 1, QTableWidgetItem(card_slot))
            # TODO 设置表格操作列
