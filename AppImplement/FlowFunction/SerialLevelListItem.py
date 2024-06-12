#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QFileDialog
from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.SerialLevelParam import Ui_SerialLevelParam

import os
from re import match
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor

from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH


class SerialLevelListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = SerialLevelParamWidget()

    def getFuncParam(self, get_for_json=False):
        return self.func_widget.getAllParam(get_for_json)


class SerialLevelParamWidget(Ui_SerialLevelParam, BaseParamWidget):
    def __init__(self):
        super(SerialLevelParamWidget, self).__init__()
        self.setupUi(self)
        self.place_plan_procs = PlacingPlanProcessor(None)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        pass

    def bindSignal(self):
        self.pushButton_series_path.clicked.connect(self.chooseSeriesFile)
        self.pushButton_plan_path_team.clicked.connect(lambda: self.choosePlanFile(self.lineEdit_plan_path_team))
        self.pushButton_plan_path_1p.clicked.connect(lambda: self.choosePlanFile(self.lineEdit_plan_path_1p))
        self.pushButton_plan_path_2p.clicked.connect(lambda: self.choosePlanFile(self.lineEdit_plan_path_2p))
        # self.pushButton_view_plan.clicked.connect()

    def chooseSeriesFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\userdata\\序列关卡文件\\",
            "All Files(*);;TXT Files(*.txt)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        self.lineEdit_series_path.setText(norm_file_path)

    def choosePlanFile(self, lineEdit):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\userdata\\卡片放置方案\\",
            "All Files(*);;INI Files(*.ini)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        lineEdit.setText(norm_file_path)

    def getAllParam(self, get_for_json=False):
        return {
            "player1": self.comboBox_select_1p.currentIndex() + 1,
            "player2": self.comboBox_select_2p.currentIndex(),      # 取值为0说明该功能为单人模式
            "series_path": self.lineEdit_series_path.text(),
            "plan_path_team": self.lineEdit_plan_path_team.text(),
            "plan_path_1p": self.lineEdit_plan_path_1p.text(),
            "plan_path_2p": self.lineEdit_plan_path_2p.text(),
            "flop_pos": self.lineEdit_flop_pos.text(),
            "quest_panel": self.comboBox_quest_panel.currentText()
        }

    def setAllParam(self, param_dict):
        self.comboBox_select_1p.setCurrentIndex(param_dict["player1"] - 1)
        self.comboBox_select_2p.setCurrentIndex(param_dict["player2"])
        self.lineEdit_series_path.setText(param_dict["series_path"])
        self.lineEdit_plan_path_team.setText(param_dict["plan_path_team"])
        self.lineEdit_plan_path_1p.setText(param_dict["plan_path_1p"])
        self.lineEdit_plan_path_2p.setText(param_dict["plan_path_2p"])
        if not os.path.exists(param_dict["series_path"]):
            return False, "关卡序列文件不存在！"
        if param_dict["plan_path_team"] != "" and not os.path.exists(param_dict["plan_path_team"]):
            return False, "组队放卡方案ini文件不存在！"
        if param_dict["plan_path_1p"] != "" and not os.path.exists(param_dict["plan_path_1p"]):
            return False, "房主放卡方案ini文件不存在！"
        if param_dict["plan_path_2p"] != "" and not os.path.exists(param_dict["plan_path_2p"]):
            return False, "房客放卡方案ini文件不存在！"
        self.lineEdit_flop_pos.setText(param_dict["flop_pos"])
        self.comboBox_quest_panel.setCurrentText(param_dict["quest_panel"])
        return True

    def checkInputValidity(self):
        if self.comboBox_select_1p.currentText() == self.comboBox_select_2p.currentText():
            return False, "房主与房客不能选择同一个！"
        if self.lineEdit_series_path.text() != "" and not os.path.exists(self.lineEdit_series_path.text()):
            return False, "未找到关卡序列文件！"
        if self.lineEdit_plan_path_team.text() != "" and not os.path.exists(self.lineEdit_plan_path_team.text()):
            return False, "未找到组队放卡方案ini文件！"
        if self.lineEdit_plan_path_1p.text() != "" and not os.path.exists(self.lineEdit_plan_path_1p.text()):
            return False, "未找到房主放卡方案ini文件！"
        if self.lineEdit_plan_path_2p.text() != "" and not os.path.exists(self.lineEdit_plan_path_2p.text()):
            return False, "未找到房客放卡方案ini文件！"
        if not match("^([1-6])(;[1-6])*$", self.lineEdit_flop_pos.text()):
            return False, "翻牌位置格式不正确！\n请确保分隔符是英文分号“;”！且仅支持1-6的翻牌位置"
        return True
