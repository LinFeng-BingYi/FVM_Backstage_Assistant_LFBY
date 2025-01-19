#!/usr/bin/env python3

from Common.Backstage.MouseAndKey import *
from Common.Backstage.Others import *
from Common.Backstage.PicAndColor import *

if __name__ == "__main__":
    # # 获取美食游戏窗口句柄
    # cursor_x, cursor_y = waitClick()
    # hwnd = mousePosHwnd(cursor_x, cursor_y)
    # print(hwnd)
    # delay(1000)
    #
    # # 测试键鼠
    # print("注意看，我要点击了")
    # # 点击创房界面的启用密码
    # mouseClick(hwnd, 490, 450)
    # # 点击创房界面的密码框位置
    # leftDoubleClick(hwnd, 620, 450)
    # delay(500)
    # keyPress(hwnd, "backspace")
    # delay(500)
    # # 输入文本：1111
    # keyPress(hwnd, "1", times=4)

    # # 测试找图
    # pic_path = r"D:\PycharmProjects\FVM_Backstage_Assistant_LFBY\resources\images\application\情侣任务\任务1\美味岛-曲奇岛-领取奖励.bmp"
    # range_list = [115, 118, 306, 158]
    # find_result = find_pic(hwnd, pic_path, range_list)
    # if find_result is None:
    #     print("没找到")
    # else:
    #     # 点击任务
    #     print("找到了")
    #     mouseClick(hwnd, 853, 54)

    # 测试找色
    hwnd = 197522
    # range_list = [400, 210, 480, 240]
    # result = find_color(hwnd, range_list, 0x31da70, 1)
    # print("target color info: ", get_pix_color(hwnd, 415, 230))
    # if result:
    #     print(result)
    # else:
    #     print("没找到")

    # “兑换”按钮水平位置: 左列440，右列820
    i = 1
    while i <= 8:
        stuff_pos = (270 + ((i - 1) % 2) * 380, 220 + ((i - 1) // 2) * 90)
        print("兑换物品截图位置: ", stuff_pos)
        stuff_x_pos = int(stuff_pos[0])
        stuff_y_pos = int(stuff_pos[1])
        convert_btn_x_pos = 440 + (stuff_x_pos // 440) * 380
        # 若没有兑换次数，则提前结束
        result = find_color(hwnd, [convert_btn_x_pos - 40, stuff_y_pos - 15, convert_btn_x_pos + 40, stuff_y_pos + 15],0x31da70)
        if result:
            print(result)
        else:
            print("没找到")
        i += 1
