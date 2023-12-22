#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.WantedParam import Ui_WantedParam

from re import match
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor

from AppImplement.GlobalValue.ConfigFilePath import DEFAULT_PLACING_PLAN_INI


class WantedListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = WantedParamWidget()

    def getFuncParam(self):
        return self.func_widget.getAllParam()


class WantedParamWidget(Ui_WantedParam, BaseParamWidget):
    def __init__(self):
        super(WantedParamWidget, self).__init__()
        self.setupUi(self)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        self.comboBox_plan_mwd.addItems(PlacingPlanProcessor(DEFAULT_PLACING_PLAN_INI).getAllSection())
        self.comboBox_plan_hsd.addItems(PlacingPlanProcessor(DEFAULT_PLACING_PLAN_INI).getAllSection())
        self.comboBox_plan_fkd.addItems(PlacingPlanProcessor(DEFAULT_PLACING_PLAN_INI).getAllSection())

    def bindSignal(self):
        # self.pushButton_view_plan.clicked.connect()
        pass

    def getAllParam(self):
        active_level_dict = {
            "美味岛": (self.checkBox_enable_mwd.isChecked(), self.comboBox_plan_mwd.currentText()),
            "火山岛": (self.checkBox_enable_hsd.isChecked(), self.comboBox_plan_hsd.currentText()),
            "浮空岛": (self.checkBox_enable_fkd.isChecked(), self.comboBox_plan_fkd.currentText())
        }
        return {
            "active_level_dict": active_level_dict,
            "flop_pos": self.lineEdit_flop_pos.text()
        }

    def checkInputValidity(self):
        if not match("^([1-6])(;[1-6])*$", self.lineEdit_flop_pos.text()):
            return False, "翻牌位置格式不正确！\n请确保分隔符是英文分号“;”！且仅支持1-6的翻牌位置"
        return True
