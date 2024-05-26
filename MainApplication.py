#!/usr/bin/env python3
import ctypes
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from AppImplement.FormFiles.MyMainWindowForm import MainMyMainWindow
from AppImplement.GlobalValue.StaticValue import APP_WINDOW_ICON


if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        app = QApplication([])
        app_icon = QIcon(APP_WINDOW_ICON)
        app.setWindowIcon(app_icon)
        myMainWindow = MainMyMainWindow()
        myMainWindow.show()
        app.exec_()
    else:
        # 获取管理员权限
        # 打包时将 __file__ 替换为 ""
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        print("请以管理员身份运行程序！！！")
