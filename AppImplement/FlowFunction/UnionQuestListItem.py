#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QFileDialog
from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.UnionQuestParam import Ui_UnionQuestParam

import os
from re import match

from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH


class UnionQuestListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = UnionQuestParamWidget()

    def getFuncParam(self, get_for_json=False):
        return self.func_widget.getAllParam(get_for_json)


class UnionQuestParamWidget(Ui_UnionQuestParam, BaseParamWidget):
    def __init__(self):
        super(UnionQuestParamWidget, self).__init__()
        self.setupUi(self)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        pass

    def bindSignal(self):
        self.pushButton_file_path.clicked.connect(lambda: self.chooseFile(self.lineEdit_file_path))
        self.pushButton_roam_file_path.clicked.connect(lambda: self.chooseFile(self.lineEdit_roam_file_path))

    def chooseFile(self, lineEdit):
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
            "plan_path": self.lineEdit_file_path.text(),
            "roam_plan_path": self.lineEdit_roam_file_path.text(),
            "roam_type": self.comboBox_roam_type.currentText(),
            "quest_no_list": self.lineEdit_quest_no.text()
        }
    
    def setAllParam(self, param_dict):
        self.comboBox_select_1p.setCurrentIndex(param_dict["player1"] - 1)
        self.comboBox_select_2p.setCurrentIndex(param_dict["player2"])
        self.lineEdit_file_path.setText(param_dict["plan_path"])
        if not os.path.exists(param_dict["plan_path"]):
            return False, "放卡方案ini文件不存在"
        if "roam_plan_path" in param_dict:
            self.lineEdit_roam_file_path.setText(param_dict["roam_plan_path"])
        if "quest_no_list" in param_dict:
            self.lineEdit_quest_no.setText(param_dict["quest_no_list"])
        if self.lineEdit_quest_no.text().find("7") != -1 and not os.path.exists(param_dict["roam_plan_path"]):
            return False, "漫游关卡放卡方案ini文件不存在"
        if "roam_type" in param_dict:
            self.comboBox_roam_type.setCurrentText(param_dict["roam_type"])
        return True

    def checkInputValidity(self):
        if self.comboBox_select_1p.currentText() == self.comboBox_select_2p.currentText():
            return False, "房主与房客不能选择同一个！"
        if not os.path.exists(self.lineEdit_file_path.text()):
            return False, "未找到放卡方案ini文件！"
        if not match("^([1-7])(;[1-7])*$", self.lineEdit_quest_no.text()):
            return False, "任务编号格式不正确！\n请确保分隔符是英文分号“;”！且仅支持1-7的公会任务编号"
        if self.lineEdit_quest_no.text().find("7") != -1 and not os.path.exists(self.lineEdit_roam_file_path.text()):
            return False, "未找到漫游关卡放卡方案ini文件！"
        return True
