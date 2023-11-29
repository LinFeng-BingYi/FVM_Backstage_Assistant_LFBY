#!/usr/bin/env python3

import win32gui
import win32api
from time import sleep


def delay(duration):
    """使进程睡眠

    Args:
        duration: float
            睡眠时长，单位秒(s)，最多三个小数位
    """
    sleep(duration)


def waitClick():
    """循环等待鼠标按下左键，最后返回鼠标所在位置

    Returns: tuple[int, int]
        鼠标所在位置
    """
    while win32api.GetKeyState(0x01) >= 0:
        pass
    return getCursorPos()


def getCursorPos():
    """返回鼠标当前所在位置

    Returns: tuple[int, int]
        鼠标所在位置
    """
    pos = win32gui.GetCursorPos()
    return pos[0], pos[1]


def mousePosHwnd(x_pos: int, y_pos: int):
    """获取传入位置的句柄

    Args:
        x_pos: int
            x坐标
        y_pos: int
            y坐标

    Returns: int
        传入位置的句柄
    """
    return win32gui.WindowFromPoint((x_pos, y_pos))
