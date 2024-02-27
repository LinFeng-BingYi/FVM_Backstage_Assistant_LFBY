#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QThread

from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.StartParam import Ui_StartParam
from Common.Backstage.Others import waitClick, mousePosHwnd

import os
from re import match

from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH, ZOOM


class StartListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = StartParamWidget()

    def getFuncParam(self, get_for_json=False):
        return self.func_widget.getAllParam(get_for_json)


class StartParamWidget(Ui_StartParam, BaseParamWidget):
    def __init__(self):
        super(StartParamWidget, self).__init__()
        self.setupUi(self)

        self.cwd = ROOT_PATH  # 程序当前工作目录
        self.get_hwnd_thread = WaitClickThread()  # 获取句柄的子线程

        self.bindSignal()

    def initWidget(self):
        # 最大检测时长
        self.lineEdit_max_check_time.setText("15")
        # 缩放比例
        self.lineEdit_1p_zoom.setText(ZOOM)
        self.lineEdit_2p_zoom.setText(ZOOM)

    def bindSignal(self):
        self.pushButton_1p_hwnd.clicked.connect(lambda: self.setPlayerHwnd(self.lineEdit_1p_hwnd))
        self.pushButton_2p_hwnd.clicked.connect(lambda: self.setPlayerHwnd(self.lineEdit_2p_hwnd))
        self.pushButton_1p_name_pic.clicked.connect(lambda: self.chooseFile(self.lineEdit_1p_name_pic))
        self.pushButton_2p_name_pic.clicked.connect(lambda: self.chooseFile(self.lineEdit_2p_name_pic))
        self.pushButton_deck_file.clicked.connect(lambda: self.chooseIniFile(self.lineEdit_deck_file))
        self.pushButton_plan_file.clicked.connect(lambda: self.chooseIniFile(self.lineEdit_plan_file))

    def setPlayerHwnd(self, lineEdit):
        # win32api.GetKeyState()方法只能在子线程中正常工作
        self.get_hwnd_thread.lineEdit = lineEdit
        self.get_hwnd_thread.start()

    def chooseFile(self, lineedit):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\userdata\\用户图片\\",
            "All Files(*);;BMP Files(*.bmp)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        lineedit.setText(norm_file_path)

    def chooseIniFile(self, lineEdit):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\userdata\\卡片放置方案\\",
            "All Files(*);;INI Files(*.ini)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        lineEdit.setText(norm_file_path)

    def getAllParam(self, get_for_json=False):
        hwnd_1p = self.lineEdit_1p_hwnd.text()
        hwnd_2p = self.lineEdit_2p_hwnd.text()
        global_info = {
            "enable_2p": self.checkBox_enable_2p.isChecked(),
            "max_check_time": int(self.lineEdit_max_check_time.text()),
            "1p_hwnd": int(hwnd_1p) if not get_for_json and hwnd_1p != '' else 0,
            "1p_zoom": float(self.lineEdit_1p_zoom.text()),
            "1p_2nd_psw": self.lineEdit_1p_2nd_psw.text(),
            "1p_name_pic_path": self.lineEdit_1p_name_pic.text(),
            "2p_hwnd": int(hwnd_2p) if not get_for_json and hwnd_2p != '' else 0,
            "2p_zoom": float(self.lineEdit_2p_zoom.text()),
            "2p_2nd_psw": self.lineEdit_2p_2nd_psw.text(),
            "2p_name_pic_path": self.lineEdit_2p_name_pic.text(),
            "deck_path": self.lineEdit_deck_file.text(),
            "plan_path": self.lineEdit_plan_file.text()
        }
        return global_info

    def setAllParam(self, param_dict):
        self.checkBox_enable_2p.setChecked(param_dict["enable_2p"])
        self.lineEdit_max_check_time.setText(str(param_dict["max_check_time"]))
        self.lineEdit_1p_hwnd.setText(str(param_dict["1p_hwnd"]))
        self.lineEdit_1p_zoom.setText(str(param_dict["1p_zoom"]))
        if "1p_2nd_psw" in param_dict:
            self.lineEdit_1p_2nd_psw.setText(param_dict["1p_2nd_psw"])
        if "1p_name_pic_path" in param_dict:
            self.lineEdit_1p_name_pic.setText(param_dict["1p_name_pic_path"])
        self.lineEdit_2p_hwnd.setText(str(param_dict["2p_hwnd"]))
        self.lineEdit_2p_zoom.setText(str(param_dict["2p_zoom"]))
        if "2p_2nd_psw" in param_dict:
            self.lineEdit_2p_2nd_psw.setText(param_dict["2p_2nd_psw"])
        self.lineEdit_2p_name_pic.setText(param_dict["2p_name_pic_path"])
        self.lineEdit_deck_file.setText(param_dict["deck_path"])
        self.lineEdit_plan_file.setText(param_dict["plan_path"])
        flag_set_success = True
        error_msg_list = []
        if not os.path.exists(param_dict["2p_name_pic_path"]):
            flag_set_success = False
            error_msg_list.append("2P昵称截图文件不存在！")
        if not os.path.exists(param_dict["deck_path"]):
            flag_set_success = False
            error_msg_list.append("账号卡片组ini文件不存在！")
        if not os.path.exists(param_dict["plan_path"]):
            flag_set_success = False
            error_msg_list.append("放卡方案ini文件不存在！")
        if flag_set_success:
            return True
        else:
            return False, "\n".join(error_msg_list)

    def checkInputValidity(self):
        if not match("^[0-9]+$", self.lineEdit_1p_hwnd.text()):
            return False, "未获取正确的1P窗口句柄！"
        if self.checkBox_enable_2p.isChecked() and not match("^[0-9]+$", self.lineEdit_2p_hwnd.text()):
            return False, "未获取正确的2P窗口句柄！"
        if not os.path.exists(self.lineEdit_deck_file.text()):
            return False, "未找到预设卡片组ini文件！"
        if not os.path.exists(self.lineEdit_plan_file.text()):
            return False, "未找到放卡方案ini文件！"
        if self.checkBox_enable_2p.isChecked() and (
            not os.path.exists(self.lineEdit_2p_name_pic.text()) or (
                self.lineEdit_1p_name_pic.text() != '' and not os.path.exists(self.lineEdit_1p_name_pic.text())
            )
        ):
            return False, "未找到1P或2P昵称截图！"
        if not match("^[0-9]+$", self.lineEdit_max_check_time.text()):
            return False, "请输入正确的提醒时间，单位为分钟(min)！"
        return True


class WaitClickThread(QThread):

    def __init__(self):
        super().__init__()

        self.lineEdit = None

    def run(self):
        print("开始获取句柄")
        cursor_x, cursor_y = waitClick()
        hwnd = mousePosHwnd(cursor_x, cursor_y)
        print("句柄为：", hwnd)
        self.lineEdit.setText(str(hwnd))
