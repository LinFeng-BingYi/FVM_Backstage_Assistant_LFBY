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


def autoLoginPreCheck(hwnd_top, login_way):
    if login_way == "微端":
        enter_server_btn = find_pic(hwnd_top, AUTO_LOGIN_ENTER_SERVER_BTN, record_fail=True, record_name="自动登录初始界面")
        if not enter_server_btn:
            raise BusinessError("使用自动登录时，请抓取窗口顶层句柄！并且初始界面必须为选择服务器的界面！")
    elif login_way == "360游戏大厅-4399服":
        hwnd_click = findChildHwnd(hwnd_top, 'Chrome_WidgetWin')
        print(hwnd_click)
        if hwnd_click == 0:
            raise BusinessError("该版本的360游戏大厅句柄结构与软件不适配！\n\n请联系作者处理")
        enter_server_btn = find_pic(hwnd_top, AUTO_LOGIN_ENTER_SERVER_BTN, record_fail=True, record_name="自动登录初始界面")
        if not enter_server_btn:
            raise BusinessError("使用自动登录时，请抓取窗口顶层句柄！并且初始界面必须为选择服务器的界面！")
    elif login_way == "360游戏大厅-空间3366服":
        hwnd_click = findChildHwnd(hwnd_top, 'Chrome_WidgetWin_0')
        print(hwnd_click)
        if hwnd_click == 0:
            raise BusinessError("该版本的360游戏大厅句柄结构与软件不适配！\n\n请联系作者处理")
        enter_server_btn = find_pic(hwnd_top, AUTO_LOGIN_3366_LAST_SERVER, record_fail=True, record_name="自动登录初始界面")
        if not enter_server_btn:
            raise BusinessError("使用自动登录时，请抓取窗口顶层句柄！并且初始界面必须为选择服务器的界面！")


def autoLoginMicroTerminal(hwnd_top, server_no: str, zoom=1):
    y_offset = 25

    enter_server_btn = find_pic(hwnd_top, AUTO_LOGIN_ENTER_SERVER_BTN, record_fail=True, record_name="自动登录初始界面")
    if not enter_server_btn:
        raise BusinessError("使用自动登录时，请抓取窗口顶层句柄！并且初始界面必须为选择服务器的界面！")
    print(enter_server_btn)
    # 双击服务器输入框
    leftDoubleClick(hwnd_top, (enter_server_btn[0] - 65) * zoom, (enter_server_btn[1] - y_offset) * zoom)
    delay(500)
    # 输入区服
    keyInputStr(hwnd_top, server_no)
    # 点击“进入”
    mouseClick(hwnd_top, enter_server_btn[0] * zoom, (enter_server_btn[1] - y_offset) * zoom)
    # 获取游戏内窗口
    print("正在获取游戏内窗口")
    if not find_pic_loop(hwnd_top, CHAT_BOX_CURRENT_PATH, max_time=120, internal=0.3):
        raise BusinessError("超过2min还未检测到启动游戏！")
    delay(500)
    # hwnd_child = findHwndEx(hwnd_top, "Sandbox:New_Box:ApolloRuntimeContentWindow")
    # print("子窗口句柄：", hwnd_child)
    hwnd_child = getAllChildrenHwnd(hwnd_top)[0]
    return hwnd_child


def autoLogin360GameHall4399(hwnd_top, server_no: str, zoom=1):
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
    if not find_pic_loop(hwnd_top, CHAT_BOX_CURRENT_PATH, max_time=120, internal=0.3):
        raise BusinessError("超过2min还未检测到启动游戏！")
    delay(500)

    hwnd_wrapper = findChildHwnd(hwnd_click, 'WrapperNativeWindowClass')
    hwnd_game = findChildHwnd(hwnd_wrapper, 'NativeWindowClass')
    print(hwnd_game)
    return hwnd_game


def autoLogin360GameHall3366(hwnd_top, server_no: str, zoom=1):
    hwnd_click = findChildHwnd(hwnd_top, 'Chrome_WidgetWin_0')
    print(hwnd_click)
    if hwnd_click == 0:
        raise BusinessError("该版本的360游戏大厅句柄结构与软件不适配！\n\n请联系作者处理")
    y_offset = 60

    enter_server_btn = find_pic(hwnd_top, AUTO_LOGIN_3366_LAST_SERVER)
    if not enter_server_btn:
        raise BusinessError("使用自动登录时，请抓取窗口顶层句柄！并且初始界面必须为选择服务器的界面！")
    print(enter_server_btn)
    # 点击“最近登录服务器”
    mouseClick(hwnd_click, (enter_server_btn[0] + 110) * zoom, (enter_server_btn[1] + 40 - y_offset) * zoom)
    # 获取游戏内窗口
    print("正在获取游戏内窗口")
    if not find_pic_loop(hwnd_top, CHAT_BOX_CURRENT_PATH, max_time=120, internal=0.3):
        raise BusinessError("超过2min还未检测到启动游戏！")
    delay(500)

    hwnd_wrapper = findChildHwnd(hwnd_click, 'WrapperNativeWindowClass')
    hwnd_game = findChildHwnd(hwnd_wrapper, 'NativeWindowClass')
    print(hwnd_game)
    return hwnd_game


# [自动登录]登录方式与函数名映射关系dict
AUTO_LOGIN_WAY_FUNC_DICT = {
    "微端": autoLoginMicroTerminal,
    "360游戏大厅-4399服": autoLogin360GameHall4399,
    "360游戏大厅-空间3366服": autoLogin360GameHall3366
}
