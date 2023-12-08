#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QThread, Signal

from src.AppImplement.FlowFunction.BaseListItem import BaseListWidget
from src.AppImplement.FormFiles.StartParam import Ui_StartParam
from src.Common.Backstage.Others import waitClick, mousePosHwnd

from src.AppImplement.GlobalValue.StaticValue import ROOT_PATH


class StartListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = StartParamWidget()

    def getFormParam(self):
        return self.func_widget.getAllParam()


class StartParamWidget(Ui_StartParam, QWidget):
    def __init__(self):
        super(StartParamWidget, self).__init__()
        self.setupUi(self)

        self.cwd = ROOT_PATH                      # 程序当前工作目录
        self.get_hwnd_thread = WaitClickThread()    # 获取句柄的子线程

        self.bindSignal()

    def bindSignal(self):
        self.pushButton_1p_hwnd.clicked.connect(lambda: self.setPlayerHwnd(self.lineEdit_1p_hwnd))
        self.pushButton_2p_hwnd.clicked.connect(lambda: self.setPlayerHwnd(self.lineEdit_2p_hwnd))
        self.pushButton_2p_name_pic.clicked.connect(self.chooseFile)

    def setPlayerHwnd(self, lineEdit):
        # win32api.GetKeyState()方法只能在子线程中正常工作
        self.get_hwnd_thread.lineEdit = lineEdit
        self.get_hwnd_thread.start()

    def chooseFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            self.cwd + "\\resources\\image\\用户图片\\",
            "All Files(*);;BMP Files(*.bmp)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        self.lineEdit_2p_name_pic.setText(norm_file_path)

    def getAllParam(self):
        hwnd_1p = self.lineEdit_1p_hwnd.text()
        hwnd_2p = self.lineEdit_2p_hwnd.text()
        global_info = {
            "1p_hwnd": int(hwnd_1p) if hwnd_1p != '' else None,
            "1p_zoom": 1,
            "2p_hwnd": int(hwnd_2p) if hwnd_2p != '' else None,
            "2p_zoom": 1,
            "2p_name_pic_path": self.lineEdit_2p_name_pic.text()
        }
        return global_info


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
