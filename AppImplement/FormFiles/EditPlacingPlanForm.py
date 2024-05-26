#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : EditPlacingPlanForm.py
# @Time    : 2023/12/2 22:28
# @Dsc     : 实现编辑卡片放置方案的界面功能

from PySide6.QtWidgets import QWidget, QFileDialog, QTableWidget, QComboBox, QTableWidgetItem, QLineEdit, QHeaderView, \
    QMessageBox, QPushButton, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

import os

from AppImplement.FormFiles.EditPlacingPlan import Ui_EditPlacingPlan
from AppImplement.FormFiles.CustomWidgets.Dialog import QDialog, EditCardPosDialog, NewPlacePlanDialog
from AppImplement.FormFiles.CustomWidgets.MessageBox import TipMessageBox
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor
from AppImplement.RWConfigFile.RWPlayerDeck import PlayerDeckProcessor

from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH, DEFAULT_PLACING_PLAN_INI, DEFAULT_DECK_INI


class WidgetEditPlacingPlan(QWidget, Ui_EditPlacingPlan):

    def __init__(self):
        super(WidgetEditPlacingPlan, self).__init__()
        self.setupUi(self)
        self.tableWidget_1p_placing_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_1p_placing_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_2p_placing_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_2p_placing_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        self.cwd = ROOT_PATH                                # 程序当前工作目录
        self.place_plan_procs = PlacingPlanProcessor(None)    # 放卡方案文件读写器
        self.player_deck_procs = PlayerDeckProcessor(None)
        self.tip_messageBox = None

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
        self.displayPlan()
        self.displayDeckList(self.comboBox_1p_deck.currentText(), self.listWidget_1p_deck)
        self.displayDeckList(self.comboBox_2p_deck.currentText(), self.listWidget_2p_deck)

    def bindSignal(self):
        # 账号卡片组ini文件
        self.pushButton_deck_path.clicked.connect(self.chooseDeckFile)
        # 放卡方案ini文件
        self.pushButton_plan_path.clicked.connect(self.choosePlanFile)
        # 显示方案内容
        self.comboBox_choose_section.currentIndexChanged.connect(self.displayPlan)
        # 显示卡片组
        self.comboBox_1p_deck.currentIndexChanged.connect(
            lambda: self.displayDeckList(self.comboBox_1p_deck.currentText(), self.listWidget_1p_deck)
        )
        self.comboBox_2p_deck.currentIndexChanged.connect(
            lambda: self.displayDeckList(self.comboBox_2p_deck.currentText(), self.listWidget_2p_deck)
        )
        # 保存放卡方案
        self.pushButton_save_plan.clicked.connect(self.savePlacePlan)
        # 新建放卡方案
        self.pushButton_new_plan.clicked.connect(self.newPlacePlan)
        # 删除放卡方案
        self.pushButton_delete_plan.clicked.connect(self.deletePlacePlan)

    def chooseDeckFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(self, "选择账号卡片组文件", self.cwd + r"\userdata\卡片放置方案",
                                                             "All Files(*);;INI Files(*.ini)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.' or norm_file_path[-4:] != '.ini':
            print("未选择正确的ini文件！！")
            return
        if self.lineEdit_deck_path.text() == norm_file_path:
            return
        self.lineEdit_deck_path.setText(norm_file_path)
        self.player_deck_procs.setFilePath(norm_file_path)
        self.updateDeckWidgets()

    def choosePlanFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(self, "选择放卡方案文件", self.cwd + r"\userdata\卡片放置方案",
                                                             "All Files(*);;INI Files(*.ini)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.' or norm_file_path[-4:] != '.ini':
            print("未选择正确的ini文件！！")
            return
        self.lineEdit_plan_path.setText(norm_file_path)
        self.place_plan_procs.setFilePath(norm_file_path)
        self.responsePlanPathChange()

    def clearWidgets(self):
        """更换选择的放卡方案后，先清除界面上的控件"""
        self.comboBox_choose_section.clear()
        self.lineEdit_1p_pos.clear()
        self.lineEdit_2p_pos.clear()
        self.tableWidget_1p_placing_table.setRowCount(0)
        self.tableWidget_2p_placing_table.setRowCount(0)

    def updateDeckWidgets(self):
        """选择了新的“账号卡片组ini”文件后，更新账号卡片组相关控件"""
        self.comboBox_1p_deck.clear()
        self.comboBox_2p_deck.clear()
        self.listWidget_1p_deck.clear()
        self.listWidget_2p_deck.clear()

        # 更新comboBox
        all_player_decks = self.player_deck_procs.getAllSection()
        self.comboBox_1p_deck.addItems(all_player_decks)
        self.comboBox_2p_deck.addItems(all_player_decks)
        if len(all_player_decks) <= 0:
            return
        # 更新listWidget
        self.displayDeckList(all_player_decks[0], self.listWidget_1p_deck)
        self.displayDeckList(all_player_decks[0], self.listWidget_2p_deck)

    def displayDeckList(self, deck_name, listWidget):
        listWidget.clear()

        deck_dict = self.player_deck_procs.readDeck(deck_name)
        deck_slot_info = deck_dict["deck_slot_info"]
        deck_cd_info = deck_dict["deck_cd_info"]

        # 根据卡槽位置，将卡片组中的所有卡片排序
        card_sequence_by_slot = []
        current_num = 0     # 当前处理的第几张卡
        for key, value in deck_slot_info.items():
            if current_num == 0:
                card_sequence_by_slot.append([key, value, deck_cd_info[key]])
            else:
                current_slot_pos = 0        # 当前卡正确的顺序
                while current_slot_pos < current_num and card_sequence_by_slot[current_slot_pos][1] < value:
                    current_slot_pos += 1
                card_sequence_by_slot.insert(current_slot_pos, [key, value, deck_cd_info[key]])
            current_num += 1

        # 将卡片卡槽位置等信息添加进卡片组listWidget
        for card_info in card_sequence_by_slot:
            listWidget.addListItem(
                card_info,
                ROOT_PATH + f"\\userdata\\用户图片\\账号卡片截图\\{deck_dict['卡片CD配置'].split('_')[0]}\\{card_info[0]}.bmp"
            )

    def responsePlanPathChange(self):
        self.clearWidgets()
        # 更新文件处理器存储的文件路径
        # self.place_plan_procs.setFilePath(self.lineEdit_plan_path.text())
        # 填充放卡方案comboBox
        all_plan_name = self.place_plan_procs.getAllSection()
        self.comboBox_choose_section.addItems(all_plan_name)

        if len(all_plan_name) <= 0:
            return
        self.displayPlan()

    def displayPlan(self):
        plan_name = self.comboBox_choose_section.currentText()
        if plan_name == '':
            return
        # 解析当前的卡片放置方案
        plan_content = self.place_plan_procs.readPlan(plan_name)
        print(f"displayPlan()获取的方案[{plan_name}]内容:\n", plan_content)
        self.plainTextEdit_plan_dsc.setPlainText(plan_content["描述"])
        # 设置单人/组队模式
        self.checkBox_is_team_mode.setChecked(True if plan_content['player_num'] == 2 else False)
        # 填充区域 -----------------------------------
        # 放置位置
        self.lineEdit_1p_pos.setText(plan_content["1P放置位置"])
        # 所用卡片组
        deck_name_1p = plan_content["1P所用卡片组"]
        self.comboBox_1p_deck.setCurrentText(deck_name_1p)
        # 更新1P卡槽listWidget
        self.updateCardPlacingTable(self.tableWidget_1p_placing_table,
                                    1,
                                    plan_content["1p_card_plan"])
        if self.checkBox_is_team_mode.isChecked():
            self.lineEdit_2p_pos.setText(plan_content["2P放置位置"])
            deck_name_2p = plan_content["2P所用卡片组"]
            self.comboBox_2p_deck.setCurrentText(deck_name_2p)
            self.updateCardPlacingTable(self.tableWidget_2p_placing_table,
                                        2,
                                        plan_content["2p_card_plan"])

    def updateCardPlacingTable(self, tableWidget: QTableWidget, player, card_plan_list):
        tableWidget.setRowCount(0)
        tableWidget.setRowCount(len(card_plan_list) + 1)

        current_row = 0
        for card_dict in card_plan_list:
            self.setExistTableRow(tableWidget, current_row, player, card_dict)
            current_row += 1
        self.setBlankTableRow(tableWidget, current_row)

    def setExistTableRow(self, tableWidget, current_row, player: int, card_dict: dict):
        for key, value in card_dict.items():
            if key == f"{player}P卡{current_row + 1}":
                tableWidget.setItem(current_row, 0, QTableWidgetItem(value))
            elif key == f"{player}P卡{current_row + 1}放置位置":
                tableWidget.setCellWidget(current_row, 1, self.lineEditForCardPos(tableWidget, value))
            elif key == f"{player}P卡{current_row + 1}补卡位置":
                tableWidget.setCellWidget(current_row, 2, self.lineEditForCardPos(tableWidget, value))
            elif key == f"{player}P卡{current_row + 1}CD":
                tableWidget.setItem(current_row, 3, QTableWidgetItem(value))
            else:
                print("未知的记录属性！！: ", key)
                return
        # 设置表格操作列
        tableWidget.setCellWidget(current_row, 4, self.buttonsForExistRow(tableWidget))

    def getTableCardPlan(self, tableWidget, player):
        card_info_list = []
        for row in range(tableWidget.rowCount() - 1):
            card_info_dict = {
                f"{player}P卡{row + 1}": tableWidget.item(row, 0).text(),
                f"{player}P卡{row + 1}放置位置": tableWidget.cellWidget(row, 1).findChild(QLineEdit).text(),
                f"{player}P卡{row + 1}补卡位置": tableWidget.cellWidget(row, 2).findChild(QLineEdit).text(),
                f"{player}P卡{row + 1}CD": tableWidget.item(row, 3).text()
            }
            card_info_list.append(card_info_dict)

        return card_info_list

    def setBlankTableRow(self, tableWidget, current_row):
        tableWidget.setItem(current_row, 0, QTableWidgetItem(''))
        tableWidget.setCellWidget(current_row, 1, self.lineEditForCardPos(tableWidget, ''))
        tableWidget.setCellWidget(current_row, 2, self.lineEditForCardPos(tableWidget, ''))
        tableWidget.setItem(current_row, 3, QTableWidgetItem(''))
        tableWidget.setCellWidget(current_row, 4, self.buttonsForNewRow(tableWidget))

    def lineEditForCardPos(self, tableWidget, card_pos_str):
        def zoomUpLineEdit(lineEdit):
            card_pos_str = lineEdit.text()
            dialog = EditCardPosDialog(card_pos_str, tableWidget)
            dialog.signal_send_card_pos_str.connect(lineEdit.setText)
            dialog.show()

        widget = QWidget()
        lineEdit = QLineEdit(widget)
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)
        font.setFamily("Times New Roman")
        lineEdit.setFont(font)
        lineEdit.setText(card_pos_str)
        # 放大按钮
        zoom_up_btn = QPushButton('⨠')
        zoom_up_btn.setMaximumWidth(20)
        zoom_up_btn.clicked.connect(lambda: zoomUpLineEdit(lineEdit))

        hLayout = QHBoxLayout(widget)
        hLayout.addWidget(lineEdit)
        hLayout.addWidget(zoom_up_btn)
        hLayout.setContentsMargins(0, 0, 0, 0)
        hLayout.setSpacing(2)
        return widget

    def buttonsForExistRow(self, tableWidget):
        def deleteTableRow(triggeredBtn):
            # print("触发了删除按钮")
            # 获取触发信号的控件所在行号
            current_row = tableWidget.indexAt(triggeredBtn.parent().pos()).row()
            tableWidget.removeRow(current_row)

        widget = QWidget()
        # 删除
        deleteBtn = QPushButton('删除')
        deleteBtn.clicked.connect(lambda: deleteTableRow(deleteBtn))

        hLayout = QHBoxLayout(widget)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        return widget

    def buttonsForNewRow(self, tableWidget):
        def newTableRow():
            # 插入新空行
            insert_pos = tableWidget.rowCount()
            tableWidget.insertRow(insert_pos)
            # 新空行初始化
            self.setBlankTableRow(tableWidget, insert_pos)
            # 新增行"操作"列转换按钮
            tableWidget.setCellWidget(insert_pos - 1, tableWidget.columnCount() - 1,
                                      self.buttonsForExistRow(tableWidget))
        widget = QWidget()
        # 新增
        newBtn = QPushButton('新增')
        newBtn.clicked.connect(newTableRow)

        hLayout = QHBoxLayout(widget)
        hLayout.addWidget(newBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        return widget

    def organizePlacePlan(self, plan_name):
        plan_dict = {
            "plan_name": plan_name,
            "player_num": 2 if self.checkBox_is_team_mode.isChecked() else 1,
            "描述": self.plainTextEdit_plan_dsc.toPlainText(),
            "1P放置位置": self.lineEdit_1p_pos.text()
        }
        if self.checkBox_is_team_mode.isChecked():
            plan_dict["2P放置位置"] = self.lineEdit_2p_pos.text()
        plan_dict["1P所用卡片组"] = self.comboBox_1p_deck.currentText()
        if self.checkBox_is_team_mode.isChecked():
            plan_dict["2P所用卡片组"] = self.comboBox_2p_deck.currentText()
        # 获取放卡信息
        plan_dict["1p_card_plan"] = self.getTableCardPlan(self.tableWidget_1p_placing_table, 1)
        if self.checkBox_is_team_mode.isChecked():
            plan_dict["2p_card_plan"] = self.getTableCardPlan(self.tableWidget_2p_placing_table, 2)
        # print(plan_dict)
        return plan_dict

    def savePlacePlan(self):
        temp_messageBox = QMessageBox(
            QMessageBox.Icon.NoIcon,
            "提示",
            "确定保存当前放卡方案的修改？",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        temp_messageBox.button(QMessageBox.StandardButton.Ok).setText("确定")
        temp_messageBox.button(QMessageBox.StandardButton.Cancel).setText("取消")
        if temp_messageBox.exec_() == QMessageBox.StandardButton.Cancel:
            return
        plan_dict = self.organizePlacePlan(self.comboBox_choose_section.currentText())
        self.place_plan_procs.writePlan(plan_dict)
        self.tip_messageBox = TipMessageBox("提示", f"方案[{plan_dict['plan_name']}]保存成功")
        self.tip_messageBox.show()
        
    def newPlacePlan(self):
        new_place_plan_dialog = NewPlacePlanDialog()
        if new_place_plan_dialog.exec_() == QDialog.DialogCode.Accepted:
            new_plan_name = new_place_plan_dialog.plan_name
            # print("获取到的方案名称: ", new_plan_name)
            if new_plan_name in self.place_plan_procs.getAllSection():
                self.tip_messageBox = TipMessageBox("错误", f"方案[{new_plan_name}]已存在！")
                self.tip_messageBox.show()
                return
            plan_dict = self.organizePlacePlan(new_plan_name)
            self.place_plan_procs.writePlan(plan_dict)
            self.comboBox_choose_section.addItem(new_plan_name)
            self.comboBox_choose_section.setCurrentText(new_plan_name)
            self.tip_messageBox = TipMessageBox("提示", f"方案[{new_plan_name}]新建成功")
            self.tip_messageBox.show()

    def deletePlacePlan(self):
        temp_messageBox = QMessageBox(
            QMessageBox.Icon.NoIcon,
            "提示",
            "确定删除当前放卡方案？",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        temp_messageBox.button(QMessageBox.StandardButton.Ok).setText("确定")
        temp_messageBox.button(QMessageBox.StandardButton.Cancel).setText("取消")
        if temp_messageBox.exec_() != QMessageBox.StandardButton.Ok:
            return
        delete_plan_name = self.comboBox_choose_section.currentText()
        self.place_plan_procs.deletePlan(delete_plan_name)
        item_index = self.comboBox_choose_section.findText(delete_plan_name)
        self.comboBox_choose_section.removeItem(item_index)


# class SaveDeckDialog(QWidget):
#     def __init__(self):
#         super().__init__()
#
#     def
