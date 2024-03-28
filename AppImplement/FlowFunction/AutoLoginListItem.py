#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtCore import QThread, QTime

from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.AutoLoginParam import Ui_AutoLoginParam
from Common.Backstage.Others import waitClick, mousePosHwnd

import os
from re import match

from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH


class AutoLoginListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = AutoLoginParamWidget()

    def getFuncParam(self, get_for_json=False):
        return self.func_widget.getAllParam(get_for_json)


class AutoLoginParamWidget(Ui_AutoLoginParam, BaseParamWidget):
    def __init__(self):
        super(AutoLoginParamWidget, self).__init__()
        self.setupUi(self)

        self.cwd = ROOT_PATH  # 程序当前工作目录
        self.get_hwnd_thread = WaitClickThread()  # 获取句柄的子线程

        self.bindSignal()

    def initWidget(self):
        pass

    def bindSignal(self):
        self.pushButton_1p_hwnd.clicked.connect(lambda: self.setPlayerHwnd(self.lineEdit_1p_hwnd))
        self.pushButton_2p_hwnd.clicked.connect(lambda: self.setPlayerHwnd(self.lineEdit_2p_hwnd))

    def setPlayerHwnd(self, lineEdit):
        # win32api.GetKeyState()方法只能在子线程中正常工作
        self.get_hwnd_thread.lineEdit = lineEdit
        self.get_hwnd_thread.start()

    def getAllParam(self, get_for_json=False):
        top_hwnd_1p = self.lineEdit_1p_hwnd.text()
        top_hwnd_2p = self.lineEdit_2p_hwnd.text()
        global_info = {
            "start_way": "time" if self.radioButton_start_time.isChecked() else "delay",
            "start_time": self.timeEdit_start_time.text(),
            "start_delay": self.doubleSpinBox_start_delay.value(),
            "1p_top_hwnd": int(top_hwnd_1p) if not get_for_json and top_hwnd_1p != '' else 0,
            "1p_server_no": self.lineEdit_1p_server_no.text(),
            "1p_login_way": self.comboBox_1p_login_way.currentText(),
            "2p_top_hwnd": int(top_hwnd_2p) if not get_for_json and top_hwnd_2p != '' else 0,
            "2p_server_no": self.lineEdit_2p_server_no.text(),
            "2p_login_way": self.comboBox_2p_login_way.currentText()
        }
        return global_info

    def setAllParam(self, param_dict):
        if "start_way" not in param_dict or param_dict["start_way"] == "delay":
            self.radioButton_start_delay.setChecked(True)
        start_time_lst = param_dict["start_time"].split(":") if "start_time" in param_dict else ["00", "01", "00"]
        start_time = QTime(int(start_time_lst[0]), int(start_time_lst[1]), int(start_time_lst[2]))
        self.timeEdit_start_time.setTime(start_time)
        self.doubleSpinBox_start_delay.setValue(float(param_dict["start_delay"]))
        self.lineEdit_1p_hwnd.setText(str(param_dict["1p_top_hwnd"]))
        self.lineEdit_2p_hwnd.setText(str(param_dict["2p_top_hwnd"]))
        self.lineEdit_1p_server_no.setText(param_dict["1p_server_no"])
        self.lineEdit_2p_server_no.setText(param_dict["2p_server_no"])
        self.comboBox_1p_login_way.setCurrentText(param_dict["1p_login_way"])
        self.comboBox_2p_login_way.setCurrentText(param_dict["2p_login_way"])
        return True

    def checkInputValidity(self):
        if not match("^[0-9]+$", self.lineEdit_1p_hwnd.text()):
            return False, "未获取正确的1P窗口句柄！"
        if not match("^[0-9]+$", self.lineEdit_2p_hwnd.text()):
            return False, "未获取正确的2P窗口句柄！"
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
