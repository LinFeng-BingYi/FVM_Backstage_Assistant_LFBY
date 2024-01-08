#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : NonGameBusiness.py
# @Time    : 2024/1/2 22:00
# @Dsc     : 实现非游戏相关的功能

from Common.Backstage import *
from AppImplement.GlobalValue.StaticValue import *
from AppImplement.Business.CustomException import BusinessError


def autoLoginMicroTerminal(hwnd, server_no: str, zoom=1):
    y_offset = 25

    enter_server_btn = find_pic(hwnd, AUTO_LOGIN_ENTER_SERVER_BTN)
    if not enter_server_btn:
        raise BusinessError("使用自动登录时，请抓取窗口顶层句柄！并且初始界面必须为选择服务器的界面！")
    print(enter_server_btn)
    # 双击服务器输入框
    leftDoubleClick(hwnd, (enter_server_btn[0] - 65) * zoom, (enter_server_btn[1] - y_offset) * zoom)
    delay(500)
    # 输入区服
    keyInputStr(hwnd, server_no)
    # 点击“进入”
    mouseClick(hwnd, enter_server_btn[0] * zoom, (enter_server_btn[1] - y_offset) * zoom)
    # 获取游戏内窗口
    print("正在获取游戏内窗口")
    if not find_pic_loop(hwnd, FRIEND_LIST_PATH, [0, 0, 300, 200], max_time=120, internal=0.2):
        raise BusinessError("超过2min还未检测到启动游戏！")
    delay(500)
    # hwnd_child = findHwndEx(hwnd, "Sandbox:New_Box:ApolloRuntimeContentWindow")
    # print("子窗口句柄：", hwnd_child)
    hwnd_child = getAllChildrenHwnd(hwnd)[0]
    return hwnd_child


def autoLogin360GameHall(hwnd_top, server_no: str, zoom=1):
    hwnd_click = findChildHwnd(hwnd_top, 'Chrome_WidgetWin')
    print(hwnd_click)
    if hwnd_click == 0:
        raise BusinessError("该版本的360游戏大厅句柄结构与软件不适配！\n\n请联系作者处理")
    y_offset = 75

    enter_server_btn = find_pic(hwnd_top, AUTO_LOGIN_ENTER_SERVER_BTN)
    if not enter_server_btn:
        raise BusinessError("使用自动登录时，请抓取窗口顶层句柄！并且初始界面必须为选择服务器的界面！")
    print(enter_server_btn)
    # 双击服务器输入框
    leftDoubleClick(hwnd_click, (enter_server_btn[0] - 65) * zoom, (enter_server_btn[1] - y_offset) * zoom)
    delay(500)
    # 输入区服
    keyInputStr(hwnd_click, server_no)
    # 点击“进入”
    mouseClick(hwnd_click, enter_server_btn[0] * zoom, (enter_server_btn[1] - y_offset) * zoom)
    # 获取游戏内窗口
    print("正在获取游戏内窗口")
    if not find_pic_loop(hwnd_top, FRIEND_LIST_PATH, [0, 0, 300, 300], max_time=120, internal=0.2):
        raise BusinessError("超过2min还未检测到启动游戏！")
    delay(500)

    hwnd_wrapper = findChildHwnd(hwnd_click, 'WrapperNativeWindowClass')
    hwnd_game = findChildHwnd(hwnd_wrapper, 'NativeWindowClass')
    print(hwnd_game)
    return hwnd_game
