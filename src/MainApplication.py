#!/usr/bin/env python3
import ctypes
import sys

from PySide6.QtWidgets import QApplication

from src.AppImplement.FormFiles.MyMainWindowForm import MainMyMainWindow


if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        app = QApplication([])
        myMainWindow = MainMyMainWindow()
        myMainWindow.show()
        app.exec()
    else:
        # 获取管理员权限
        # 打包时将 __file__ 替换为 ""
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        print("请以管理员身份运行程序！！！")
