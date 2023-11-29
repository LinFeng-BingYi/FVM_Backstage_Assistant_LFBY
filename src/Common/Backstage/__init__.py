#!/usr/bin/env python3

from MouseAndKey import *
from Others import *
from PicAndColor import *

if __name__ == "__main__":
    # 获取美食游戏窗口句柄
    x1, y1 = waitClick()
    hwnd = mousePosHwnd(x1, y1)
    print(hwnd)
    delay(1)
    print("注意看，我要点击了")
    # 点击创房界面的启用密码
    mouseClick(hwnd, 490, 450)
    # 点击创房界面的密码框位置
    leftDoubleClick(hwnd, 620, 450)
    sleep(0.1)
    # 输入文本：1111
    keyPress(hwnd, "1", times=4)
