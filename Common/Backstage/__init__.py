#!/usr/bin/env python3

from Common.Backstage.MouseAndKey import *
from Common.Backstage.Others import *
from Common.Backstage.PicAndColor import *

if __name__ == "__main__":
    # 获取美食游戏窗口句柄
    cursor_x, cursor_y = waitClick()
    hwnd = mousePosHwnd(cursor_x, cursor_y)
    print(hwnd)
    delay(1000)

    # 测试键鼠
    print("注意看，我要点击了")
    # 点击创房界面的启用密码
    mouseClick(hwnd, 490, 450)
    # 点击创房界面的密码框位置
    leftDoubleClick(hwnd, 620, 450)
    delay(500)
    keyPress(hwnd, "backspace")
    delay(500)
    # 输入文本：1111
    keyPress(hwnd, "1", times=4)

    # # 测试找图
    # pic_path = "D:\\PycharmProjects\\FVM_Backstage_Assistant_LFBY\\resources\\images\\application\\情侣任务\\任务1\\美味岛-曲奇岛-领取奖励.bmp"
    # range_list = [115, 118, 306, 158]
    # find_result = find_pic(hwnd, pic_path, range_list)
    # if find_result is None:
    #     print("没找到")
    # else:
    #     # 点击任务
    #     print("找到了")
    #     mouseClick(hwnd, 853, 54)

    # # 测试找色
    # range_list = [40, 10, 90, 50]
    # result = find_color(hwnd, range_list, 0xcaf3fc, 1)
    # if result:
    #     print(result)
    # else:
    #     print("没找到")
