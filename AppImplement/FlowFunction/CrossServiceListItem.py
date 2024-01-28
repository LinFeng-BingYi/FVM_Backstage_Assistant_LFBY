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

    def getFuncParam(self, get_for_json=False):
        return self.func_widget.getAllParam(get_for_json)


class CrossServiceParamWidget(Ui_CrossServiceParam, BaseParamWidget):
    def __init__(self):
        super(CrossServiceParamWidget, self).__init__()
        self.setupUi(self)
        self.place_plan_procs = PlacingPlanProcessor(None)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        pass

    def bindSignal(self):
        self.pushButton_1p_room_name_path.clicked.connect(self.chooseFile)
        # self.pushButton_view_plan.clicked.connect()
        self.pushButton_plan_path.clicked.connect(self.choosePlanFile)

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

    def chooseFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\userdata\\用户图片\\",
            "All Files(*);;BMP Files(*.bmp)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        self.lineEdit_1p_room_name_path.setText(norm_file_path)

    def getAllParam(self, get_for_json=False):
        return {
            "player1": self.comboBox_select_1p.currentIndex() + 1,
            "player2": self.comboBox_select_2p.currentIndex(),      # 取值为0说明该功能为单人模式
            "level_type": self.comboBox_level_type.currentText(),
            "level_num": self.comboBox_level_num.currentText(),
            "player1_room_name_path": self.lineEdit_1p_room_name_path.text(),
            "loop_count": int(self.lineEdit_loop_count.text()),
            "flop_pos": self.lineEdit_flop_pos.text(),
            "plan_path": self.lineEdit_plan_path.text(),
            "plan_name": self.comboBox_1p_plan.currentText()
        }

    def setAllParam(self, param_dict):
        self.comboBox_select_1p.setCurrentIndex(param_dict["player1"] - 1)
        self.comboBox_select_2p.setCurrentIndex(param_dict["player2"])
        self.comboBox_level_type.setCurrentText(param_dict["level_type"])
        self.comboBox_level_num.setCurrentText(param_dict["level_num"])
        self.lineEdit_1p_room_name_path.setText(param_dict["player1_room_name_path"])
        self.lineEdit_loop_count.setText(str(param_dict["loop_count"]))
        self.lineEdit_flop_pos.setText(param_dict["flop_pos"])
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
        if self.comboBox_select_2p.currentIndex() != 0 and not os.path.exists(self.lineEdit_1p_room_name_path.text()):
            return False, "未找到1P跨服房间昵称截图！"
        if not match("^[0-9]+$", self.lineEdit_loop_count.text()):
            return False, "请填写正确的循环次数！"
        if not match("^([1-6])(;[1-6])*$", self.lineEdit_flop_pos.text()):
            return False, "翻牌位置格式不正确！\n请确保分隔符是英文分号“;”！且仅支持1-6的翻牌位置"
        return True
