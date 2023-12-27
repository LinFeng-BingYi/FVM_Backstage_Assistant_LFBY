#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFileDialog, QMessageBox
from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.LoopLevelParam import Ui_LoopLevelParam

import os
from re import match
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor

from AppImplement.GlobalValue.StaticValue import SINGLE_HIERARCHY_ZONE, MULTI_HIERARCHY_ZONE
from AppImplement.GlobalValue.ConfigFilePath import DEFAULT_PLACING_PLAN_INI, ROOT_PATH


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
        self.place_plan_procs = PlacingPlanProcessor(None)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        # 在 地图 下拉框中填入可选的地图
        self.comboBox_zone.addItems(SINGLE_HIERARCHY_ZONE)
        self.comboBox_zone.addItems(MULTI_HIERARCHY_ZONE)
        # 在 关卡 下拉框中填入可选的关卡
        self.comboBox_level.addItems(self.getLevelsOfZone(self.comboBox_zone.currentText()))
        # 放卡方案
        if DEFAULT_PLACING_PLAN_INI != "":
            self.lineEdit_plan_path.setText(DEFAULT_PLACING_PLAN_INI)
            self.showAllPlan()

    def bindSignal(self):
        self.comboBox_zone.currentIndexChanged.connect(self.showCorrespondLevels)
        self.pushButton_plan_path.clicked.connect(self.choosePlanFile)
        # self.pushButton_view_plan.clicked.connect()

    def getLevelsOfZone(self, zone):
        if zone in SINGLE_HIERARCHY_ZONE:
            return list(SINGLE_HIERARCHY_ZONE[zone])
        else:
            return list(MULTI_HIERARCHY_ZONE[zone])

    def showCorrespondLevels(self):
        self.comboBox_level.clear()
        self.comboBox_level.addItems(self.getLevelsOfZone(self.comboBox_zone.currentText()))

    def choosePlanFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\userdata\\卡片放置方案\\",
            "All Files(*);;INI Files(*.ini)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        self.lineEdit_plan_path.setText(norm_file_path)
        self.showAllPlan()

    def showAllPlan(self):
        self.place_plan_procs.setFilePath(self.lineEdit_plan_path.text())
        self.comboBox_1p_plan.clear()
        self.comboBox_1p_plan.addItems(self.place_plan_procs.getAllSection())

    def getAllParam(self):
        return {
            "player1": self.comboBox_select_1p.currentIndex() + 1,
            "player2": self.comboBox_select_2p.currentIndex(),      # 取值为0说明该功能为单人模式
            "zone_name": self.comboBox_zone.currentText(),
            "level_name": self.comboBox_level.currentText(),
            "loop_count": int(self.lineEdit_loop_count.text()),
            "flop_pos": self.lineEdit_flop_pos.text(),
            "has_stage2": self.checkBox_has_stage2.isChecked(),
            "shall_continue": self.checkBox_continue.isChecked(),
            "plan_path": self.lineEdit_plan_path.text(),
            "plan_name": self.comboBox_1p_plan.currentText()
        }

    def setAllParam(self, param_dict):
        self.comboBox_select_1p.setCurrentIndex(param_dict["player1"] - 1)
        self.comboBox_select_2p.setCurrentIndex(param_dict["player2"])
        self.comboBox_zone.setCurrentText(param_dict["zone_name"])
        self.comboBox_level.setCurrentText(param_dict["level_name"])
        self.lineEdit_loop_count.setText(str(param_dict["loop_count"]))
        self.lineEdit_flop_pos.setText(param_dict["flop_pos"])
        self.checkBox_has_stage2.setChecked(param_dict["has_stage2"])
        self.checkBox_continue.setChecked(param_dict["shall_continue"])
        self.lineEdit_plan_path.setText(param_dict["plan_path"])
        if os.path.exists(param_dict["plan_path"]):
            self.showAllPlan()
            if param_dict["plan_name"] in self.place_plan_procs.getAllSection():
                self.comboBox_1p_plan.setCurrentText(param_dict["plan_name"])
            else:
                return False, f"放卡方案[{param_dict['plan_name']}]在ini文件中不存在"
        else:
            return False, "放卡方案ini文件不存在"
        return True

    def checkInputValidity(self):
        if self.comboBox_select_1p.currentText() == self.comboBox_select_2p.currentText():
            return False, "房主与房客不能选择同一个！"
        if not os.path.exists(self.lineEdit_plan_path.text()):
            return False, "未找到放卡方案ini文件！"
        if not match("^[0-9]+$", self.lineEdit_loop_count.text()):
            return False, "请填写正确的循环次数！"
        if not match("^([1-6])(;[1-6])*$", self.lineEdit_flop_pos.text()):
            return False, "翻牌位置格式不正确！\n请确保分隔符是英文分号“;”！且仅支持1-6的翻牌位置"
        return True
