#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QDate
from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.DailyEndParam import Ui_DailyEndParam

import os
from re import match

from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH


class DailyEndListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = DailyEndParamWidget()

    def getFuncParam(self, get_for_json=False):
        return self.func_widget.getAllParam(get_for_json)


class DailyEndParamWidget(Ui_DailyEndParam, BaseParamWidget):
    def __init__(self):
        super(DailyEndParamWidget, self).__init__()
        self.setupUi(self)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        pass

    def bindSignal(self):
        self.pushButton_backpack_item_pic.clicked.connect(self.chooseDir)

    def chooseDir(self):
        chosen_dir = QFileDialog.getExistingDirectory(
            self, "选择文件夹",
            ROOT_PATH + "\\userdata\\用户图片\\")
        norm_file_path = os.path.normpath(chosen_dir)
        if norm_file_path == '.':
            print("未选择文件夹！！")
            return
        self.lineEdit_backpack_item_pic.setText(norm_file_path)

    def getAllParam(self, get_for_json=False):
        return {
            "player": self.comboBox_select_player.currentIndex(),
            "底部任务": self.checkBox_bottom_quest.isChecked(),
            "公会任务": self.checkBox_union_quest.isChecked(),
            "情侣任务": self.checkBox_lover_quest.isChecked(),
            "悬赏活动": self.checkBox_wanted.isChecked(),
            "大富翁": [self.checkBox_monopoly.isChecked(), {
                "use_dice": self.checkBox_monopoly_use_dice.isChecked()
            }]
            # "背包兑换": [self.checkBox_backpack_exchange.isChecked(), {
            #     "item_pic_path": self.lineEdit_backpack_item_pic.text()
            # }]
        }

    def setAllParam(self, param_dict):
        flag_set_success = True
        error_msg_list = []
        self.comboBox_select_player.setCurrentIndex(param_dict["player"])
        self.checkBox_bottom_quest.setChecked(param_dict["底部任务"])
        self.checkBox_union_quest.setChecked(param_dict["公会任务"])
        self.checkBox_lover_quest.setChecked(param_dict["情侣任务"])
        self.checkBox_wanted.setChecked(param_dict["悬赏活动"])
        self.checkBox_monopoly.setChecked(param_dict["大富翁"][0])
        self.checkBox_monopoly_use_dice.setChecked(param_dict["大富翁"][1]["use_dice"])
        # self.checkBox_backpack_exchange.setChecked(param_dict["背包兑换"][0])
        # self.lineEdit_backpack_item_pic.setText(param_dict["背包兑换"][1]["item_pic_path"])
        # if self.checkBox_backpack_exchange.isChecked() and not os.path.exists(self.lineEdit_backpack_item_pic.text()):
        #     flag_set_success = False
        #     error_msg_list.append('[背包兑换]功能中条目截图文件夹不存在')
        if not flag_set_success:
            return False, "\n".join(error_msg_list)
        return True

    def checkInputValidity(self):
        # if self.checkBox_backpack_exchange.isChecked() and not os.path.exists(self.lineEdit_backpack_item_pic.text()):
        #     return False, "未找到背包兑换条目截图文件夹！"
        return True
