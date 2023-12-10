#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QThread

from src.AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from src.AppImplement.FormFiles.StartParam import Ui_StartParam
from src.Common.Backstage.Others import waitClick, mousePosHwnd

import os
from re import match

from src.AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH, ZOOM


class StartListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = StartParamWidget()

    def getFuncParam(self):
        return self.func_widget.getAllParam()


class StartParamWidget(Ui_StartParam, BaseParamWidget):
    def __init__(self):
        super(StartParamWidget, self).__init__()
        self.setupUi(self)

        self.cwd = ROOT_PATH  # 程序当前工作目录
        self.get_hwnd_thread = WaitClickThread()  # 获取句柄的子线程

        self.bindSignal()

    def bindSignal(self):
        self.pushButton_1p_hwnd.clicked.connect(lambda: self.setPlayerHwnd(self.lineEdit_1p_hwnd))
        self.pushButton_2p_hwnd.clicked.connect(lambda: self.setPlayerHwnd(self.lineEdit_2p_hwnd))
        self.pushButton_2p_name_pic.clicked.connect(self.chooseFile)
        self.pushButton_deck_file.clicked.connect(lambda: self.chooseIniFile(self.lineEdit_deck_file))
        self.pushButton_plan_file.clicked.connect(lambda: self.chooseIniFile(self.lineEdit_plan_file))

    def setPlayerHwnd(self, lineEdit):
        # win32api.GetKeyState()方法只能在子线程中正常工作
        self.get_hwnd_thread.lineEdit = lineEdit
        self.get_hwnd_thread.start()

    def chooseFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\resources\\images\\用户图片\\",
            "All Files(*);;BMP Files(*.bmp)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        self.lineEdit_2p_name_pic.setText(norm_file_path)

    def chooseIniFile(self, lineEdit):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\config\\卡片放置方案\\",
            "All Files(*);;INI Files(*.ini)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        lineEdit.setText(norm_file_path)

    def getAllParam(self):
        hwnd_1p = self.lineEdit_1p_hwnd.text()
        hwnd_2p = self.lineEdit_2p_hwnd.text()
        global_info = {
            "1p_hwnd": int(hwnd_1p) if hwnd_1p != '' else None,
            "1p_zoom": float(ZOOM),
            "2p_hwnd": int(hwnd_2p) if hwnd_2p != '' else None,
            "2p_zoom": float(ZOOM),
            "2p_name_pic_path": self.lineEdit_2p_name_pic.text(),
            "deck_path": self.lineEdit_deck_file.text(),
            "plan_path": self.lineEdit_plan_file.text(),
            "max_check_time": int(self.lineEdit_max_check_time.text())
        }
        return global_info

    def checkInputValidity(self):
        if not match("^[0-9]+$", self.lineEdit_1p_hwnd.text()) or \
                not match("^[0-9]+$", self.lineEdit_2p_hwnd.text()):
            return False, "未获取正确的窗口句柄！"
        if not os.path.exists(self.lineEdit_deck_file.text()):
            return False, "未找到预设卡片组ini文件！"
        if not os.path.exists(self.lineEdit_plan_file.text()):
            return False, "未找到放卡方案ini文件！"
        if not os.path.exists(self.lineEdit_2p_name_pic.text()):
            return False, "未找到2P昵称截图！"
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
