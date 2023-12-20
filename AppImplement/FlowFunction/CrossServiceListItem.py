#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from PySide6.QtWidgets import QFileDialog

from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.CrossServiceParam import Ui_CrossServiceParam

from re import match
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor

from AppImplement.GlobalValue.ConfigFilePath import DEFAULT_PLACING_PLAN_INI, ROOT_PATH


class CrossServiceListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = CrossServiceParamWidget()

    def getFuncParam(self):
        return self.func_widget.getAllParam()


class CrossServiceParamWidget(Ui_CrossServiceParam, BaseParamWidget):
    def __init__(self):
        super(CrossServiceParamWidget, self).__init__()
        self.setupUi(self)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        self.comboBox_1p_plan.addItems(PlacingPlanProcessor(DEFAULT_PLACING_PLAN_INI).getAllSection())

    def bindSignal(self):
        self.pushButton_1p_room_name_path.clicked.connect(self.chooseFile)

    def chooseFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\resources\\images\\用户图片\\",
            "All Files(*);;BMP Files(*.bmp)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        self.lineEdit_1p_room_name_path.setText(norm_file_path)

    def getAllParam(self):
        return {
            "level_type": self.comboBox_level_type.currentText(),
            "level_num": self.comboBox_level_num.currentText(),
            "player1_room_name_path": self.lineEdit_1p_room_name_path.text(),
            "loop_count": int(self.lineEdit_loop_count.text()),
            "flop_pos": self.lineEdit_flop_pos.text(),
            "plan_name": self.comboBox_1p_plan.currentText()
        }

    def checkInputValidity(self):
        if not os.path.exists(self.lineEdit_1p_room_name_path.text()):
            return False, "未找到1P跨服房间昵称截图！"
        if not match("^[0-9]+$", self.lineEdit_loop_count.text()):
            return False, "请填写正确的循环次数！"
        if not match("^([1-6])(;[1-6])*$", self.lineEdit_flop_pos.text()):
            return False, "翻牌位置格式不正确！\n请确保分隔符是英文分号“;”！且仅支持1-6的翻牌位置"
        return True
