#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : MAKByPywin32.py
# @Time    : 2023/11/26 23:38
# @Dsc     : 通关pywin32模块实现后台键鼠

import win32api
import win32con
from time import sleep

VALUE_KEY = {
    "A": "65", "B": "66", "C": "67", "D": "68", "E": "69", "F": "70", "G": "71", "H": "72", "I": "73", "J": "74",
    "K": "75", "L": "76", "M": "77", "N": "78", "O": "79", "P": "80", "Q": "81", "R": "82", "S": "83", "T": "84",
    "U": "85", "V": "86", "W": "87", "X": "88", "Y": "89", "Z": "90",
    "0": "48", "1": "49", "2": "50", "3": "51", "4": "52", "5": "53", "6": "54", "7": "55", "8": "56", "9": "57",
    "F1": "112", "F2": "113", "F3": "114", "F4": "115", "F5": "116", "F6": "117", "F7": "118", "F8": "119",
    "F9": "120", "F10": "121", "F11": "122", "F12": "123",
    "TAB": "9", "ENTER": "13", "SHIFT": "16", "CTRL": "17", "ALT": "18", "BACKSPACE": "8", "CAPSLOCK": "20"
}


# 鼠标 -----------------------------------------------------------------------------------------------
def mouseClick(hwnd, x: float, y: float, interval=0.001, button='L'):
    """鼠标单次点击

    Args:
        hwnd: int
            目标窗口句柄
        x: int
            操作位置x坐标
        y: int
            操作位置y坐标
        interval: float
            该按键按压时长，最多三位小数
        button: str['L', 'R']
            选择鼠标左键('L') 或鼠标右键('R')，默认鼠标左键
    """
    mouseDown(hwnd, x, y, button)
    sleep(interval)
    mouseUp(hwnd, x, y, button)


def mouseDown(hwnd, x: float, y: float, button='L'):
    """鼠标单次按下

    Args:
        hwnd: int
            目标窗口句柄
        x: int
            操作位置x坐标
        y: int
            操作位置y坐标
        button: str['L', 'R']
            选择鼠标左键('L') 或鼠标右键('R')，默认鼠标左键
    """
    x = int(x)
    y = int(y)
    point = win32api.MAKELONG(x, y)
    wm_button = win32con.WM_LBUTTONDOWN
    mk_button = win32con.MK_LBUTTON
    if button.upper() == 'R':
        wm_button = win32con.WM_RBUTTONDOWN
        mk_button = win32con.MK_RBUTTON
    win32api.PostMessage(hwnd, wm_button, mk_button, point)


def mouseUp(hwnd, x: float, y: float, button='L'):
    """鼠标单次弹起

    Args:
        hwnd: int
            目标窗口句柄
        x: int
            操作位置x坐标
        y: int
            操作位置y坐标
        button: str['L', 'R']
            选择鼠标左键('L') 或鼠标右键('R')，默认鼠标左键
    """
    x = int(x)
    y = int(y)
    point = win32api.MAKELONG(x, y)
    wm_button = win32con.WM_LBUTTONUP
    mk_button = win32con.MK_LBUTTON
    if button.upper() == 'R':
        wm_button = win32con.WM_RBUTTONUP
        mk_button = win32con.MK_RBUTTON
    win32api.PostMessage(hwnd, wm_button, mk_button, point)


def leftDoubleClick(hwnd, x: float, y: float):
    """鼠标左键双击

    Args:
        hwnd: int
            目标窗口句柄
        x: int
            操作位置x坐标
        y: int
            操作位置y坐标
    """
    # x = int(x)
    # y = int(y)
    # point = win32api.MAKELONG(x, y)
    # win32api.PostMessage(hwnd, win32con.WM_LBUTTONDBLCLK, win32con.MK_LBUTTON, point)
    # sleep(0.1)
    # win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, point)
    mouseClick(hwnd, x, y)
    sleep(0.01)
    mouseClick(hwnd, x, y)


def mouseMove(hwnd, x: float, y: float):
    """鼠标移动

    Args:
        hwnd: int
            目标窗口句柄
        x: int
            操作位置x坐标
        y: int
            操作位置y坐标
    """
    x = int(x)
    y = int(y)
    point = win32api.MAKELONG(x, y)
    win32api.PostMessage(hwnd, win32con.WM_MOUSEMOVE, None, point)


def mouseKeepPlace(hwnd, x: float, y: float, times=30):
    """保持鼠标放置在某个位置

    Args:
        hwnd: int
            目标窗口句柄
        x: int
            操作位置x坐标
        y: int
            操作位置y坐标
        times: int
            保持次数(保持时间取决于系统每秒能处理多少次)，建议30起步
    """
    x = int(x)
    y = int(y)
    point = win32api.MAKELONG(x, y)
    for i in range(times):
        win32api.PostMessage(hwnd, win32con.WM_MOUSEMOVE, None, point)


# 键盘 -----------------------------------------------------------------------------------------------
def keyPress(hwnd, key: str, interval=0.05, times=1):
    """键盘单次输入

    Args:
        hwnd: int
            目标窗口句柄
        key: str
            操作的按键名，以键盘上显示的名称为准，均大写。如 "A"、"CTRL"、"ENTER"
        interval: float
            该按键按压时长，最多三位小数
        times: int
            该按键按压次数，默认1次
    """
    key = key.upper()
    key_num = int(VALUE_KEY[key])
    num = win32api.MapVirtualKey(key_num, 0)
    dparam = 1 | (num << 16)
    uparam = 1 | (num << 16) | (1 << 30) | (1 << 31)
    for i in range(times):
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, key_num, dparam)
        sleep(interval)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, key_num, uparam)
        sleep(0.3)


def keyDown(hwnd, key: str):
    """键盘单次按压

    Args:
        hwnd: int
            目标窗口句柄
        key: str
            操作的按键名，以键盘上显示的名称为准，均大写。如 "A"、"CTRL"、"ENTER"
    """
    key = key.upper()
    key_num = int(VALUE_KEY[key])
    num = win32api.MapVirtualKey(key_num, 0)
    dparam = 1 | (num << 16)
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, key_num, dparam)


def keyUp(hwnd, key: str):
    """键盘单次弹起

    Args:
        hwnd: int
            目标窗口句柄
        key: str
            操作的按键名，以键盘上显示的名称为准，均大写。如 "A"、"CTRL"、"ENTER"
    """
    key = key.upper()
    key_num = int(VALUE_KEY[key])
    num = win32api.MapVirtualKey(key_num, 0)
    uparam = 1 | (num << 16) | (1 << 30) | (1 << 31)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, key_num, uparam)


def keyInputStr(hwnd, key_str: str):
    for char in key_str:
        if char.isupper():
            keyDown(hwnd, "SHIFT")
            sleep(0.1)
            keyPress(hwnd, char)
            sleep(0.1)
            keyUp(hwnd, "SHIFT")
        else:
            keyPress(hwnd, char)
        sleep(0.3)
