#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : EditPlacingPlanForm.py
# @Time    : 2023/12/2 22:28
# @Dsc     : 实现编辑卡片放置方案的界面功能
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QFileDialog, QTableWidget, QComboBox, QTableWidgetItem, QLineEdit, QHeaderView, QMessageBox
from PySide6.QtCore import Qt

import os

from src.AppImplement.FormFiles.EditPlacingPlan import Ui_EditPlacingPlan
from src.AppImplement.RWConfigFile.RWPlacingPlan import PlacingFileProcessor
from src.AppImplement.RWConfigFile.RWPlayerDeck import PlayerDeckProcessor

from src.AppImplement.GlobalValue.StaticValue import ROOT_PATH


class WidgetEditPlacingPlan(QWidget, Ui_EditPlacingPlan):

    def __init__(self):
        super(WidgetEditPlacingPlan, self).__init__()
        self.setupUi(self)
        self.tableWidget_1p_placing_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_2p_placing_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        self.cwd = ROOT_PATH                                # 程序当前工作目录
        self.file_processor: PlacingFileProcessor = None    # 收支记录文件读写器
        self.player_deck_procs = PlayerDeckProcessor(ROOT_PATH + r"\config\账号预设卡片组.ini")
        self.edit_enable = False

        self.initWidgets()
        self.bindSignal()

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

    def initWidgets(self):
        # 初始化时，禁用编辑模式
        self.checkBox_is_team_mode.setEnabled(False)
        self.tab_1p_placing_config.setEnabled(self.edit_enable)
        self.tab_2p_placing_config.setEnabled(self.edit_enable)
        init_file_path = ROOT_PATH + r"\config\卡片放置方案\升级版组队常用方案_V1.00.ini"
        # 初始化本窗口的文件处理器
        self.file_processor = PlacingFileProcessor(init_file_path)
        # 默认路径
        self.lineEdit_file_path.setText(init_file_path)
        # 填充卡片组comboBox
        all_player_decks = self.player_deck_procs.getAllSection()
        self.comboBox_1p_deck.addItems(all_player_decks)
        self.comboBox_2p_deck.addItems(all_player_decks)

        # 更新界面
        self.responseFilePathChange()

    def bindSignal(self):
        # 文件
        self.pushButton_file_path.clicked.connect(self.chooseFile)
        # 显示方案内容
        self.comboBox_choose_section.currentIndexChanged.connect(self.displayPlan)
        # 编辑按钮
        self.pushButton_modify_config.clicked.connect(self.changeEditStatus)

    def chooseFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(self, "选择文件", self.cwd + "\\config\\卡片放置方案",
                                                             "All Files(*);;XML Files(*.xml)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        self.lineEdit_file_path.setText(norm_file_path)
        self.responseFilePathChange()

    def changeEditStatus(self):
        """响应"修改"按钮的函数
        """
        if self.edit_enable:    # 当处于启用编辑状态触发该按钮时，询问是否保存修改
            msgBox = QMessageBox()
            msgBox.setText("是否要保存修改？")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Cancel)
            msgBox.button(QMessageBox.StandardButton.Save).setText("保存")
            msgBox.button(QMessageBox.StandardButton.Cancel).setText("取消")
            result = msgBox.exec()
            if result == QMessageBox.StandardButton.Save:
                pass  # TODO 实现保存配置
        self.edit_enable = not self.edit_enable
        # 设置账号放卡方案区的编辑状态
        self.tab_1p_placing_config.setEnabled(self.edit_enable)
        if self.checkBox_is_team_mode.isChecked():
            self.tab_2p_placing_config.setEnabled(self.edit_enable)
        else:  # 单人模式不能编辑2P
            self.tab_2p_placing_config.setEnabled(False)
        # 设置其他两个按钮的状态
        self.pushButton_new_config.setEnabled(not self.edit_enable)
        self.pushButton_delete_config.setEnabled(not self.edit_enable)
        # 设置切换配置comboBox的状态
        self.comboBox_choose_section.setEnabled(not self.edit_enable)
        # 设置"浏览"按钮的状态，修改时不能切换文件
        self.lineEdit_file_path.setEnabled(not self.edit_enable)
        self.pushButton_file_path.setEnabled(not self.edit_enable)

        # 设置"修改"按钮的样式
        if self.edit_enable:
            self.pushButton_modify_config.setText("退出保存")
            self.pushButton_modify_config.setStyleSheet('background-color: green')
        else:
            self.pushButton_modify_config.setText("修改方案")
            self.pushButton_modify_config.setStyleSheet('')

    def clearWidgets(self):
        """更换选择的放卡方案后，先清除界面上的控件"""
        self.comboBox_choose_section.clear()
        self.lineEdit_1p_pos.clear()
        self.lineEdit_2p_pos.clear()
        self.listWidget_1p_deck.clear()
        self.listWidget_2p_deck.clear()
        self.tableWidget_1p_placing_table.setRowCount(0)
        self.tableWidget_2p_placing_table.setRowCount(0)

    def responseFilePathChange(self):
        self.clearWidgets()
        # 更新文件处理器存储的文件路径
        self.file_processor.setFilePath(self.lineEdit_file_path.text())
        # 填充放卡方案comboBox
        print(self.file_processor.getAllSection())
        self.comboBox_choose_section.addItems(self.file_processor.getAllSection())

        self.displayPlan()

    def displayPlan(self):
        plan_name = self.comboBox_choose_section.currentText()
        if plan_name == '':     # 表示文件中没有方案
            return
        # 解析当前的卡片放置方案
        plan_content = self.file_processor.readPlan(plan_name)
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
        # TODO 更新1P卡槽listWidget
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
            if key == f"{player}P卡{current_row + 1}名称":
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
            card_slot = deck_info["deck_slot_info"][card_dict[f"{player}P卡{current_row + 1}名称"]]
            # card_cd = deck_info["deck_cd_info"][card_dict[f"{player}P卡{current_row + 1}名称"]]
            tableWidget.setItem(current_row, 1, QTableWidgetItem(card_slot))
            # TODO 设置表格操作列
