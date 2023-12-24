#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QDate
from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.DailyAwardParam import Ui_DailyAwardParam

import os

from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH


class DailyAwardListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = DailyAwardParamWidget()

    def getFuncParam(self):
        return self.func_widget.getAllParam()


class DailyAwardParamWidget(Ui_DailyAwardParam, BaseParamWidget):
    def __init__(self):
        super(DailyAwardParamWidget, self).__init__()
        self.setupUi(self)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        pass

    def bindSignal(self):
        self.pushButton_flowers_receiver.clicked.connect(self.chooseFile)

    def chooseFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\resources\\images\\用户图片\\",
            "All Files(*);;BMP Files(*.bmp)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        self.lineEdit_flowers_receiver.setText(norm_file_path)

    def getAllParam(self):
        execute_team_magic_tower = False
        execute_destiny_tree = False
        # 在勾选主体复选框的情况下，若勾选"强制执行"，则永远返回True，否则只有星期一时返回True
        if self.checkBox_team_magic_tower.isChecked() and (
                self.checkBox_force_team_magic_tower.isChecked() or QDate.currentDate().dayOfWeek() == 1):
            execute_team_magic_tower = True
        if self.checkBox_destiny_tree.isChecked() and (
                self.checkBox_force_destiny_tree.isChecked() or QDate.currentDate().dayOfWeek() == 1):
            execute_destiny_tree = True
        return {
            "player": self.comboBox_select_player.currentIndex(),
            "VIP签到": self.checkBox_vip_signin.isChecked(),
            "每日签到": self.checkBox_daily_signin.isChecked(),
            "免费许愿": self.checkBox_free_wish.isChecked(),
            "底部任务": self.checkBox_bottom_quest.isChecked(),
            "塔罗寻宝": self.checkBox_tarot_treasure.isChecked(),
            "营地钥匙": self.checkBox_campsite_key.isChecked(),
            "法老宝藏": [self.checkBox_pharaoh_treasure.isChecked(), {
                "flop_pos": int(self.comboBox_pharaoh_flop_pos.currentText())
            }],
            "公会花园": [self.checkBox_union_garden.isChecked(), {
                "need_fertilize": self.checkBox_need_fertilize.isChecked(),
                "plant_type": self.comboBox_garden_plant_type.currentIndex()
            }],
            "公会任务": [self.checkBox_union_quest.isChecked(), {
                "release_quest": self.checkBox_release_quest.isChecked()
            }],
            "打开美食大赛": self.checkBox_open_food_contest.isChecked(),
            "打开背包": self.checkBox_open_backpack.isChecked(),
            "领取双人魔塔奖励": execute_team_magic_tower,
            "领取缘分树奖励": execute_destiny_tree,
            "赠送鲜花": [self.checkBox_give_flowers.isChecked(), {
                "receiver_name_path": self.lineEdit_flowers_receiver.text(),
                "use_gift_coupon": self.checkBox_use_gift_coupon.isChecked(),
                "use_times": int(self.comboBox_use_coupon_times.currentText())
            }]
        }

    def setAllParam(self, param_dict):
        self.comboBox_select_player.setCurrentIndex(param_dict["player"])
        self.checkBox_vip_signin.setChecked(param_dict["VIP签到"])
        self.checkBox_daily_signin.setChecked(param_dict["每日签到"])
        self.checkBox_free_wish.setChecked(param_dict["免费许愿"])
        self.checkBox_bottom_quest.setChecked(param_dict["底部任务"])
        self.checkBox_tarot_treasure.setChecked(param_dict["塔罗寻宝"])
        self.checkBox_campsite_key.setChecked(param_dict["营地钥匙"])
        self.checkBox_pharaoh_treasure.setChecked(param_dict["法老宝藏"][0])
        self.comboBox_pharaoh_flop_pos.setCurrentText(str(param_dict["法老宝藏"][1]["flop_pos"]))
        self.checkBox_union_garden.setChecked(param_dict["公会花园"][0])
        self.checkBox_need_fertilize.setChecked(param_dict["公会花园"][1]["need_fertilize"])
        self.comboBox_garden_plant_type.setCurrentIndex(param_dict["公会花园"][1]["plant_type"])
        self.checkBox_union_quest.setChecked(param_dict["公会任务"][0])
        self.checkBox_release_quest.setCurrentText(param_dict["公会任务"][1]["release_quest"])
        self.checkBox_open_food_contest.setChecked(param_dict["打开美食大赛"])
        self.checkBox_open_backpack.setChecked(param_dict["打开背包"])
        self.checkBox_team_magic_tower.setChecked(param_dict["领取双人魔塔奖励"])
        self.checkBox_destiny_tree.setChecked(param_dict["领取缘分树奖励"])
        self.checkBox_give_flowers.setChecked(param_dict["赠送鲜花"][0])
        self.lineEdit_flowers_receiver.setText(param_dict["赠送鲜花"][1]["receiver_name_path"])
        self.checkBox_use_gift_coupon.setChecked(param_dict["赠送鲜花"][1]["use_gift_coupon"])
        self.comboBox_use_coupon_times.setCurrentText(str(param_dict["赠送鲜花"][1]["use_times"]))
        if self.checkBox_give_flowers.isChecked() and not os.path.exists(self.lineEdit_flowers_receiver.text()):
            return False, "未找到鲜花接收方昵称截图！"
        return True

    def checkInputValidity(self):
        if self.checkBox_give_flowers.isChecked() and not os.path.exists(self.lineEdit_flowers_receiver.text()):
            return False, "未找到鲜花接收方昵称截图！"
        return True
