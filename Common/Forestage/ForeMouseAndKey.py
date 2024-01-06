#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : ForeMouseAndKey.py
# @Time    : 2024/1/2 22:36
# @Dsc     : 前端键鼠

import win32api
import win32con
from time import sleep

from Common.Backstage.MouseAndKey.MAKByPywin32 import VALUE_KEY


# 鼠标 -----------------------------------------------------------------------------------------------
def foreMouseClick(x, y, interval=0.005, button='L'):
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x, y))

    m_event_down = win32con.MOUSEEVENTF_LEFTDOWN if button.upper() == 'L' else win32con.MOUSEEVENTF_RIGHTDOWN
    m_event_up = win32con.MOUSEEVENTF_LEFTUP if button.upper() == 'L' else win32con.MOUSEEVENTF_RIGHTUP
    win32api.mouse_event(m_event_down, 0, 0, 0, 0)
    sleep(interval)
    win32api.mouse_event(m_event_up, 0, 0, 0, 0)


def foreMouseDown(x, y, button='L'):
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x, y))
    m_event_down = win32con.MOUSEEVENTF_LEFTDOWN if button.upper() == 'L' else win32con.MOUSEEVENTF_RIGHTDOWN
    win32api.mouse_event(m_event_down, 0, 0, 0, 0)


def foreMouseUp(x, y, button='L'):
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x, y))
    m_event_up = win32con.MOUSEEVENTF_LEFTUP if button.upper() == 'L' else win32con.MOUSEEVENTF_RIGHTUP
    win32api.mouse_event(m_event_up, 0, 0, 0, 0)


def foreMouseMove(x, y):
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x, y))


def foreLeftDoubleClick(x, y):
    foreMouseClick(x, y)
    sleep(0.01)
    foreMouseClick(x, y)


# 键盘 -----------------------------------------------------------------------------------------------
def foreKeyPress(key: str, interval=0.05, times=1):
    key = key.upper()
    key_num = int(VALUE_KEY[key])
    for i in range(times):
        win32api.keybd_event(key_num, 0, 0, 0)
        sleep(interval)
        win32api.keybd_event(key_num, 0, win32con.KEYEVENTF_KEYUP, 0)
        sleep(0.3)


def foreKeyDown(key: str):
    key = key.upper()
    key_num = int(VALUE_KEY[key])
    win32api.keybd_event(key_num, 0, 0, 0)


def foreKeyUp(key: str):
    key = key.upper()
    key_num = int(VALUE_KEY[key])
    win32api.keybd_event(key_num, 0, win32con.KEYEVENTF_KEYUP, 0)
