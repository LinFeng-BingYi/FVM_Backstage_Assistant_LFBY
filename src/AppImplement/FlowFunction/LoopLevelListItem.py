#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFileDialog, QMessageBox
from src.AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from src.AppImplement.FormFiles.LoopLevelParam import Ui_LoopLevelParam

import os
from re import match
from src.AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor

from src.AppImplement.GlobalValue.StaticValue import SINGLE_HIERARCHY_ZONE, MULTI_HIERARCHY_ZONE
from src.AppImplement.GlobalValue.ConfigFilePath import DEFAULT_PLACING_PLAN_INI


class LoopLevelListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = LoopLevelParamWidget()

    def getFuncParam(self):
        return self.func_widget.getAllParam()


class LoopLevelParamWidget(Ui_LoopLevelParam, BaseParamWidget):
    def __init__(self):
        super(LoopLevelParamWidget, self).__init__()
        self.setupUi(self)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        # 在 地图 下拉框中填入可选的地图
        self.comboBox_zone.addItems(SINGLE_HIERARCHY_ZONE)
        self.comboBox_zone.addItems(MULTI_HIERARCHY_ZONE)
        # 在 关卡 下拉框中填入可选的关卡
        self.comboBox_level.addItems(self.getLevelsOfZone(self.comboBox_zone.currentText()))

        self.comboBox_1p_plan.addItems(PlacingPlanProcessor(DEFAULT_PLACING_PLAN_INI).getAllSection())

    def bindSignal(self):
        self.comboBox_zone.currentIndexChanged.connect(self.showCorrespondLevels)
        # self.pushButton_view_plan.clicked.connect()

    def getLevelsOfZone(self, zone):
        if zone in SINGLE_HIERARCHY_ZONE:
            return list(SINGLE_HIERARCHY_ZONE[zone])
        else:
            return list(MULTI_HIERARCHY_ZONE[zone])

    def showCorrespondLevels(self):
        self.comboBox_level.clear()
        self.comboBox_level.addItems(self.getLevelsOfZone(self.comboBox_zone.currentText()))

    def getAllParam(self):
        return {
            "zone_name": self.comboBox_zone.currentText(),
            "level_name": self.comboBox_level.currentText(),
            "loop_count": int(self.lineEdit_loop_count.text()),
            "flop_pos": self.lineEdit_flop_pos.text(),
            "has_stage2": self.checkBox_has_stage2.isChecked(),
            "shall_continue": self.checkBox_continue.isChecked(),
            "plan_name": self.comboBox_1p_plan.currentText()
        }

    def checkInputValidity(self):
        if not match("^[0-9]+$", self.lineEdit_loop_count.text()):
            return False, "请填写正确的循环次数！"
        if not match("^([1-6])(;[1-6])*$", self.lineEdit_flop_pos.text()):
            return False, "翻牌位置格式不正确！\n请确保分隔符是英文分号“;”！且仅支持1-6的翻牌位置"
        return True
