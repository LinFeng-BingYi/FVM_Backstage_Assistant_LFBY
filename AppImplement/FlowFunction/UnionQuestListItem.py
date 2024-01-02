#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QFileDialog
from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.UnionQuestParam import Ui_UnionQuestParam

import os

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
        self.pushButton_file_path.clicked.connect(self.chooseFile)

    def chooseFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\userdata\\卡片放置方案\\",
            "All Files(*);;INI Files(*.ini)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        self.lineEdit_file_path.setText(norm_file_path)

    def getAllParam(self, get_for_json=False):
        return {
            "player1": self.comboBox_select_1p.currentIndex() + 1,
            "player2": self.comboBox_select_2p.currentIndex(),      # 取值为0说明该功能为单人模式
            "plan_path": self.lineEdit_file_path.text()
        }
    
    def setAllParam(self, param_dict):
        self.comboBox_select_1p.setCurrentIndex(param_dict["player1"] - 1)
        self.comboBox_select_2p.setCurrentIndex(param_dict["player2"])
        self.lineEdit_file_path.setText(param_dict["plan_path"])

    def checkInputValidity(self):
        if self.comboBox_select_1p.currentText() == self.comboBox_select_2p.currentText():
            return False, "房主与房客不能选择同一个！"
        if not os.path.exists(self.lineEdit_file_path.text()):
            return False, "未找到放卡方案ini文件！"
        return True
