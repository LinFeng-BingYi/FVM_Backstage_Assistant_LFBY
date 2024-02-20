#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFileDialog, QMessageBox
from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.LoopSkillParam import Ui_LoopSkillParam

import os
from re import match
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor

from AppImplement.GlobalValue.StaticValue import (
    SINGLE_HIERARCHY_ZONE, MULTI_HIERARCHY_ZONE, CROSS_SERVER_LEVEL_TYPE_NO, LOOP_SKILL_ZONE, LAB_LEVEL)
from AppImplement.GlobalValue.ConfigFilePath import DEFAULT_PLACING_PLAN_INI, ROOT_PATH

from AppImplement.Business.OrdinaryBusiness import TOP_MENU_LEVEL_OPEN_FUNC


class LoopSkillListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = LoopSkillParamWidget()

    def getFuncParam(self, get_for_json=False):
        return self.func_widget.getAllParam(get_for_json)


class LoopSkillParamWidget(Ui_LoopSkillParam, BaseParamWidget):
    def __init__(self):
        super(LoopSkillParamWidget, self).__init__()
        self.setupUi(self)
        self.place_plan_procs = PlacingPlanProcessor(None)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        # 在 地图 下拉框中填入可选的地图
        self.comboBox_zone.addItems(LOOP_SKILL_ZONE)
        # 在 关卡 下拉框中填入可选的关卡
        self.comboBox_level.addItems(self.getLevelsOfZone(self.comboBox_zone.currentText()))

    def bindSignal(self):
        self.comboBox_zone.currentIndexChanged.connect(self.showCorrespondLevels)
        self.pushButton_plan_path.clicked.connect(self.choosePlanFile)
        # self.pushButton_view_plan.clicked.connect()

    def getLevelsOfZone(self, zone):
        if zone in SINGLE_HIERARCHY_ZONE:
            return list(SINGLE_HIERARCHY_ZONE[zone])
        elif zone in MULTI_HIERARCHY_ZONE:
            return list(MULTI_HIERARCHY_ZONE[zone])
        elif zone == "魔塔蛋糕":
            return ['1', '-2', '-3', '-4', '-5']
        elif zone == "跨服远征":
            return list(CROSS_SERVER_LEVEL_TYPE_NO)
        elif zone == "实验室":
            # 注意 self.checkInputValidity() 方法中校验时也使用了该列表(被写死)
            return LAB_LEVEL
        else:
            pass

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

    def getAllParam(self, get_for_json=False):
        return {
            "player": self.comboBox_select_player.currentIndex(),
            "zone_name": self.comboBox_zone.currentText(),
            "level_name": self.comboBox_level.currentText(),
            "plan_path": self.lineEdit_plan_path.text(),
            "plan_name": self.comboBox_1p_plan.currentText(),
            "loop_count": int(self.lineEdit_loop_count.text()),
            "exit_delay": int(self.lineEdit_exit_delay.text())
        }

    def setAllParam(self, param_dict):
        self.comboBox_select_player.setCurrentIndex(param_dict["player"])
        self.comboBox_zone.setCurrentText(param_dict["zone_name"])
        self.comboBox_level.setCurrentText(param_dict["level_name"])
        self.lineEdit_loop_count.setText(str(param_dict["loop_count"]))
        self.lineEdit_exit_delay.setText(str(param_dict["exit_delay"]))
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
        if not os.path.exists(self.lineEdit_plan_path.text()):
            return False, "未找到放卡方案ini文件！"
        if not match("^[0-9]+$", self.lineEdit_loop_count.text()):
            return False, "请填写正确的循环次数！"
        if not match("^[0-9]+$", self.lineEdit_exit_delay.text()):
            return False, "请填写正确的退出游戏延时！单位为毫秒"
        # 验证地图和关卡名称合法性
        zone = self.comboBox_zone.currentText()
        level = self.comboBox_level.currentText()
        if zone == "魔塔蛋糕":
            if not match("^(-?[2-5])|[0-9]+$", level):
                return False, "请填写正确的魔塔层数！当为负数时，表示魔塔第三页从上往下对应的关卡。例如-5表示威望屋"
        elif zone == "跨服远征":
            if level not in CROSS_SERVER_LEVEL_TYPE_NO:
                return False, f"未找到该跨服远征关卡类型！[{level}]"
        elif zone == "实验室":
            if level not in LAB_LEVEL:
                return False, "选择实验室时，请勿修改“关卡”中的文本！"
        elif zone in SINGLE_HIERARCHY_ZONE:
            if level not in SINGLE_HIERARCHY_ZONE[zone]:
                return False, f"未找到该关卡！[{level}]"
        elif zone in MULTI_HIERARCHY_ZONE:
            if level not in MULTI_HIERARCHY_ZONE[zone]:
                return False, f"未找到该关卡！[{level}]"
        else:
            return False, f"未找到该地图！[{zone}]"
        return True
