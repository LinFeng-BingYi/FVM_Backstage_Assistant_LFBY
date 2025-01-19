#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from PySide6.QtWidgets import QFileDialog

from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.WantedParam import Ui_WantedParam

from re import match
from AppImplement.RWConfigFile.RWPlacingPlan import PlacingPlanProcessor

from AppImplement.GlobalValue.ConfigFilePath import DEFAULT_PLACING_PLAN_INI, ROOT_PATH


class WantedListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = WantedParamWidget()

    def getFuncParam(self, get_for_json=False):
        return self.func_widget.getAllParam(get_for_json)


class WantedParamWidget(Ui_WantedParam, BaseParamWidget):
    def __init__(self):
        super(WantedParamWidget, self).__init__()
        self.setupUi(self)
        self.place_plan_procs = PlacingPlanProcessor(None)

        self.three_island_widget_dict = {
            "美味岛": (self.checkBox_enable_mwd, self.comboBox_plan_mwd),
            "火山岛": (self.checkBox_enable_hsd, self.comboBox_plan_hsd),
            "浮空岛": (self.checkBox_enable_fkd, self.comboBox_plan_fkd),
            "星际穿越": (self.checkBox_enable_xjcy, self.comboBox_plan_xjcy)
        }

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        self.comboBox_plan_mwd.view().setFixedWidth(160)
        self.comboBox_plan_hsd.view().setFixedWidth(160)
        self.comboBox_plan_fkd.view().setFixedWidth(160)
        self.comboBox_plan_xjcy.view().setFixedWidth(160)

    def bindSignal(self):
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
        all_plan = self.place_plan_procs.getAllSection()
        self.comboBox_plan_mwd.clear()
        self.comboBox_plan_mwd.addItems(all_plan)
        self.comboBox_plan_hsd.clear()
        self.comboBox_plan_hsd.addItems(all_plan)
        self.comboBox_plan_fkd.clear()
        self.comboBox_plan_fkd.addItems(all_plan)
        self.comboBox_plan_xjcy.clear()
        self.comboBox_plan_xjcy.addItems(all_plan)

    def getAllParam(self, get_for_json=False):
        active_level_dict = dict()
        """
        active_level_dict格式：{
            "美味岛": (bool, "悬赏美味方案名称"),
            "火山岛": (bool, "悬赏火山方案名称"),
            "浮空岛": (bool, "悬赏浮空方案名称"),
            "星际穿越": (bool, "悬赏星际方案名称")
        }
        """
        for key, value in self.three_island_widget_dict.items():
            active_level_dict[key] = (value[0].isChecked(), value[1].currentText())
        return {
            "player1": self.comboBox_select_1p.currentIndex() + 1,
            "player2": self.comboBox_select_2p.currentIndex(),      # 取值为0说明该功能为单人模式
            "active_level_dict": active_level_dict,
            "flop_pos": self.lineEdit_flop_pos.text(),
            "plan_path": self.lineEdit_plan_path.text()
        }

    def setAllParam(self, param_dict):
        self.comboBox_select_1p.setCurrentIndex(param_dict["player1"] - 1)
        self.comboBox_select_2p.setCurrentIndex(param_dict["player2"])
        self.lineEdit_flop_pos.setText(param_dict["flop_pos"])
        self.lineEdit_plan_path.setText(param_dict["plan_path"])
        flag_set_success = True
        error_msg_list = []
        if os.path.exists(param_dict["plan_path"]):
            self.showAllPlan()
            all_plan = self.place_plan_procs.getAllSection()
            for key, value in self.three_island_widget_dict.items():
                flag_checked = param_dict["active_level_dict"][key][0]
                plan_name = param_dict["active_level_dict"][key][1]
                if flag_checked:
                    if plan_name not in all_plan:
                        flag_set_success = False
                        error_msg_list.append(f"放卡方案[{plan_name}]在ini文件中不存在")
                        continue
                    self.three_island_widget_dict[key][0].setChecked(flag_checked)
                    self.three_island_widget_dict[key][1].setCurrentText(plan_name)
        else:
            return False, "放卡方案ini文件不存在"
        if flag_set_success:
            return True
        else:
            return False, "\n".join(error_msg_list)

    def checkInputValidity(self):
        if self.comboBox_select_1p.currentText() == self.comboBox_select_2p.currentText():
            return False, "房主与房客不能选择同一个！"
        if not os.path.exists(self.lineEdit_plan_path.text()):
            return False, "未找到放卡方案ini文件！"
        if not match("^([1-6])(;[1-6])*$", self.lineEdit_flop_pos.text()):
            return False, "翻牌位置格式不正确！\n请确保分隔符是英文分号“;”！且仅支持1-6的翻牌位置"
        return True
