#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.VolcanicRelicParam import Ui_VolcanicRelicParam

from re import match
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor

from AppImplement.GlobalValue.ConfigFilePath import DEFAULT_PLACING_PLAN_INI


class VolcanicRelicListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = VolcanicRelicParamWidget()

    def getFuncParam(self):
        return self.func_widget.getAllParam()


class VolcanicRelicParamWidget(Ui_VolcanicRelicParam, BaseParamWidget):
    def __init__(self):
        super(VolcanicRelicParamWidget, self).__init__()
        self.setupUi(self)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        self.comboBox_1p_plan.addItems(PlacingPlanProcessor(DEFAULT_PLACING_PLAN_INI).getAllSection())

    def bindSignal(self):
        # self.pushButton_view_plan.clicked.connect()
        pass

    def getAllParam(self):
        return {
            "level_name": self.comboBox_level.currentText(),
            "loop_count": int(self.lineEdit_loop_count.text()),
            "flop_pos": self.lineEdit_flop_pos.text(),
            "plan_name": self.comboBox_1p_plan.currentText()
        }

    def checkInputValidity(self):
        if not match("^[0-9]+$", self.lineEdit_loop_count.text()):
            return False, "请填写正确的循环次数！"
        if not match("^([1-6])(;[1-6])*$", self.lineEdit_flop_pos.text()):
            return False, "翻牌位置格式不正确！\n请确保分隔符是英文分号“;”！且仅支持1-6的翻牌位置"
        return True
