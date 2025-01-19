#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : PicColorByCv.py
# @Time    : 2023/11/29 23:33
# @Dsc     : 通过opencv实现找图找色

import win32gui
import win32con
import win32ui
import cv2
import numpy
import math
from time import time, sleep
from datetime import datetime
from os import path, mkdir


# 找图 -----------------------------------------------------------------------------------------------
def capture_pic(hwnd=0, cap_range=None):
    """截取指定窗口中范围为pos的图像。
       不会将截图保存至磁盘，而是返回在内存中的图像数据，以便避免降低速度

    Args:
        hwnd: int
            指定的窗口句柄
        cap_range: list[int]
            指定的截图范围，包含4个元素：[左上角x坐标, 左上角y坐标, 右下角x坐标, 右下角y坐标]

    Returns: cv2.typing.MatLike
        opencv的图像数据，存储于内存中
    """
    # 获取句柄窗口的大小信息
    rect = win32gui.GetWindowRect(hwnd)
    # print("客户区", rect)
    left = 0
    top = 0
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    # print("客户区宽高", width, height)
    if cap_range is not None:
        left = cap_range[0]
        top = cap_range[1]
        width = cap_range[2] - cap_range[0]
        height = cap_range[3] - cap_range[1]
    # print("截取区域", left, top)
    # print("截取区域宽高", width, height)
    # 根据窗口句柄获取窗口的设备上下文DC（Device Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bitmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 从坐标（left，top）作为左上角，截取长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (left, top), win32con.SRCCOPY)
    # 保存图片 ---------------------------------------
    # 方法一:
    # saveBitMap.SaveBitmapFile(saveDC, filename)
    # 第二种方法: CV2+numpy存图，选择CV2存图原因是CV2对图片有较好的处理功能，比如有些图片有亮度等变化的，可以用CV2处理成灰度或调整色阶等后对比查找。
    signedIntsArray = saveBitMap.GetBitmapBits(True)  # 获取位图信息，
    # 返回图片
    im_opencv = numpy.frombuffer(signedIntsArray, dtype='uint8')
    im_opencv.shape = (height, width, 4)
    # cv2.imwrite("D:\\PycharmProjects\\FVM_Backstage_Assistant_LFBY\\temp\\im_opencv.jpg", im_opencv)
    # 清除图片数据，防止内存泄露 ------------------------------
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    # 按键抓抓截取的图片格式为bmp，本质上是BGR图，因此使用 cv2.COLOR_BGRA2BGR 转换为可识别的图像
    return cv2.cvtColor(im_opencv, cv2.COLOR_BGRA2BGR)


def save_captured_pic(pic_path, hwnd=0, cap_range=None):
    """截取指定窗口中范围为pos的图像，并将其保存到指定的路径。路径字符串包含了图像文件名和扩展名

    Args:
        pic_path: str
            保存截取图片的绝对路径。其中的扩展名就是将被保存的图片格式
        hwnd: int
            指定的窗口句柄
        cap_range: list[int]
            指定的截图范围，包含4个元素：[左上角x坐标, 左上角y坐标, 右下角x坐标, 右下角y坐标]

    Returns: cv2.typing.MatLike
        opencv的图像数据，存储于内存中
    """
    img = capture_pic(hwnd, cap_range)
    # cv2.imwrite(pic_path, img)
    ext = pic_path.rsplit('.', 1)[1]
    cv2.imencode(f".{ext}", img)[1].tofile(pic_path)


def find_pic(hwnd: int, template_path: str, find_range: list = None, threshold: float = 0.98, record_fail=False, record_name=''):
    """在指定窗口中，指定范围内，寻找模板图像，相似度大于等于threshold则表示找到了. 失败返回 False

    Args:
        hwnd: int
            指定的窗口句柄
        template_path: str
            模板图像的绝对路径
        find_range: list[int]
            指定的寻找范围，包含4个元素：[左上角x坐标, 左上角y坐标, 右下角x坐标, 右下角y坐标]
        threshold: float
            判断图像是否找到的阈值
        record_fail: bool
            识图失败时是否保存失败图像
        record_name: str
            识图失败时保存图像的名称

    Returns: tuple[float, float, float, float, float, float] | False
        窗口中与模板图像相似度最高的位置信息。包含6个元素：
            - 匹配成功区域中心x坐标
            - 匹配成功区域中心y坐标
            - 匹配成功区域左上角x坐标
            - 匹配成功区域左上角y坐标
            - 匹配成功区域右下角x坐标
            - 右匹配成功区域下角y坐标
    """
    try:
        target_pic = capture_pic(hwnd, find_range)
        template_pic = cv2.imdecode(numpy.fromfile(template_path, dtype=numpy.uint8), -1)
        result = cv2.matchTemplate(target_pic, template_pic, cv2.TM_SQDIFF_NORMED)
    except cv2.error:
        print('文件错误! 模板图片路径：', template_path)
        return False
    height, width = template_pic.shape[:2]
    # 获取模板匹配结果矩阵中 最小值、最大值、最小值左上角、最大值左上角
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print(min_val)
    if min_val > 1 - threshold:
        if record_fail:
            if not path.exists('temp'):
                mkdir('temp')
            now_time = datetime.now().strftime("%Y-%m-%d")
            find_range = [f'{pos_num}' for pos_num in find_range] if find_range is not None else ['0', '0', '0', '0']
            file_name = f"./temp/{now_time}_{record_name}_{'-'.join(find_range)}_{1 - min_val:.3f}.bmp"
            cv2.imencode(".bmp", target_pic)[1].tofile(file_name)
        return False

    # 若指定了找图范围，则匹配位置的真实左上角需要加回找图范围的左上角的偏移值
    if find_range is not None:
        min_loc = (min_loc[0] + find_range[0], min_loc[1] + find_range[1])
    coordinate = (min_loc[0] + width / 2, min_loc[1] + height / 2, min_loc[0], min_loc[1], min_loc[0] + width, min_loc[1] + height)
    # print(template_path, min_val, min_loc)
    # print(min_loc[0], min_loc[1])
    return coordinate


def find_pic_loop(hwnd: int, template_path: str, find_range: list = None, threshold: float = 0.98, max_time=600, internal=0.01):
    """在指定窗口中，指定范围内，寻找模板图像，相似度大于等于threshold则表示找到了. 失败返回 False
       超过 max_time 后仍未找到则直接返回 False，其单位为秒(s)

    Args:
        hwnd: int
            指定的窗口句柄
        template_path: str
            模板图像的绝对路径
        find_range: list[int]
            指定的寻找范围，包含4个元素：[左上角x坐标, 左上角y坐标, 右下角x坐标, 右下角y坐标]
        threshold: float
            判断图像是否找到的阈值
        max_time: int
            寻找时间限制，单位为秒(s)
        internal: float
            寻找时间间隔，单位为秒(s)

    Returns: tuple[float, float, float, float, float, float] | False
        窗口中与模板图像相似度最高的位置信息。包含6个元素：
            - 匹配成功区域中心x坐标
            - 匹配成功区域中心y坐标
            - 匹配成功区域左上角x坐标
            - 匹配成功区域左上角y坐标
            - 匹配成功区域右下角x坐标
            - 右匹配成功区域下角y坐标
    """
    # 截图准备 -------------------------------------------------
    # 获取句柄窗口的大小信息
    rect = win32gui.GetWindowRect(hwnd)
    # print("客户区", rect)
    left = 0
    top = 0
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    # print("客户区宽高", width, height)
    if find_range is not None:
        left = find_range[0]
        top = find_range[1]
        width = find_range[2] - find_range[0]
        height = find_range[3] - find_range[1]
    # print("截取区域", left, top)
    # print("截取区域宽高", width, height)
    # 根据窗口句柄获取窗口的设备上下文DC（Device Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bitmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 开始截图 -------------------------------------------------
    try:
        start_time = time()
        while True:
            # 从坐标（left，top）作为左上角，截取长宽为（w，h）的图片
            saveDC.BitBlt((0, 0), (width, height), mfcDC, (left, top), win32con.SRCCOPY)
            # 保存图片 ---------------------------------------
            signedIntsArray = saveBitMap.GetBitmapBits(True)  # 获取位图信息，
            # 返回图片
            im_opencv = numpy.frombuffer(signedIntsArray, dtype='uint8')
            im_opencv.shape = (height, width, 4)
            # 待对比图片
            target_pic = cv2.cvtColor(im_opencv, cv2.COLOR_BGRA2BGR)
            # 模板图片
            template_pic = cv2.imdecode(numpy.fromfile(template_path, dtype=numpy.uint8), -1)
            result = cv2.matchTemplate(target_pic, template_pic, cv2.TM_SQDIFF_NORMED)
            # 对比图像 ---------------------------------------
            # 获取模板匹配结果矩阵中 最小值、最大值、最小值左上角、最大值左上角
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            # print(min_val)
            if min_val <= 1 - threshold:
                # 若指定了找图范围，则匹配位置的真实左上角需要加回找图范围的左上角的偏移值
                if find_range is not None:
                    min_loc = (min_loc[0] + find_range[0], min_loc[1] + find_range[1])
                template_height, template_width = template_pic.shape[:2]
                coordinate = (min_loc[0] + template_width / 2, min_loc[1] + template_height / 2, min_loc[0], min_loc[1],
                              min_loc[0] + template_width, min_loc[1] + template_height)
                return coordinate
            if (time() - start_time) >= max_time:
                return False

            sleep(internal)
    except cv2.error:
        print('文件错误! 模板图片路径：', template_path)
        return False
    finally:
        # 清除图片数据，防止内存泄露 ------------------------------
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)


# 找色 -----------------------------------------------------------------------------------------------
def get_pix_color(hwnd, x, y):
    """获取窗口指定坐标像素点颜色，颜色格式为BGR形式的int

    Args:
        hwnd: int
            指定的窗口句柄
        x: int
        y: int

    Returns:
        BGR形式的int值

        example:
            像素颜色值： 13300732
            像素16进制表示： 0xcaf3fc
            转换方式：
             - R = pixel & 0xff
             - G = (pixel >> 8) & 0xff
             - B = pixel >> 16
            像素转换成RGB形式： 252 243 202
    """
    # 根据窗口句柄获取窗口的设备上下文DC（Device Context）
    hwndDC = win32gui.GetDC(hwnd)
    pixel = win32gui.GetPixel(hwndDC, x, y)
    # 释放
    win32gui.ReleaseDC(hwnd, hwndDC)
    print("像素颜色值：", pixel)
    print("像素16进制表示：", hex(pixel))
    print("像素转换成RGB形式：", pixel & 0xff, (pixel >> 8) & 0xff, pixel >> 16)
    # 返回 R, G, B
    return pixel & 0xff, (pixel >> 8) & 0xff, pixel >> 16


def find_color(hwnd: int, find_range: list, color: hex, threshold: float = 1):
    """在指定窗口，指定范围内寻找与目标颜色相似度大于阈值的坐标点，未找到则返回False

    Args:
        hwnd: int
            指定的窗口句柄
        find_range: list[int]
            指定的寻找范围，包含4个元素：[左上角x坐标, 左上角y坐标, 右下角x坐标, 右下角y坐标]
        color: hex
            目标颜色，格式为BGR形式的16进制hex值，如：0xcaf3fc
        threshold: float
            判断颜色是否找到的阈值

    Returns: tuple[int, int] | bool[False]
        查找成功则返回位置坐标；失败则返回False
    """
    # 根据窗口句柄获取窗口的设备上下文DC（Device Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    for x in range(find_range[0], find_range[2]+1):
        for y in range(find_range[1], find_range[3] + 1):
            pixel = win32gui.GetPixel(hwndDC, x, y)
            if threshold == 1:
                # 完全匹配时直接对比数值
                # print("当前坐标:", x, y, "\t颜色:", pixel, "\t目标颜色:", color)
                if pixel == color:
                    win32gui.ReleaseDC(hwnd, hwndDC)
                    return x, y
            if computeBGRColorSimilar(color, pixel) <= 1 - threshold:
                # print("当前坐标:", x, y, "\t颜色:", hex(pixel), "\t相似度:", computeBGRColorSimilar(color, pixel))
                # 释放
                win32gui.ReleaseDC(hwnd, hwndDC)
                return x, y
    # 释放
    win32gui.ReleaseDC(hwnd, hwndDC)
    return False


def find_color_loop(hwnd: int, find_range: list, color: hex, threshold: float = 1, max_time=600):
    """在指定窗口，指定范围内循环寻找与目标颜色相似度大于阈值的坐标点，超过 max_time 还未找到则返回False

    Args:
        hwnd: int
            指定的窗口句柄
        find_range: list[int]
            指定的寻找范围，包含4个元素：[左上角x坐标, 左上角y坐标, 右下角x坐标, 右下角y坐标]
        color: hex
            目标颜色，格式为BGR形式的16进制hex值，如：0xcaf3fc
        threshold: float
            判断颜色是否找到的阈值
        max_time: int
            寻找时间限制，单位为秒(s)

    Returns: tuple[int, int] | bool[False]
        查找成功则返回位置坐标；失败则返回False
    """
    hwndDC = win32gui.GetWindowDC(hwnd)
    print(hwnd, "设备上下文：", hwndDC)
    start_time = time()
    while True:
        for x in range(find_range[0], find_range[2] + 1):
            for y in range(find_range[1], find_range[3] + 1):
                pixel = win32gui.GetPixel(hwndDC, x, y)
                if threshold == 1:
                    # 完全匹配时直接对比数值
                    if pixel == color:
                        win32gui.ReleaseDC(hwnd, hwndDC)
                        return x, y
                if computeBGRColorSimilar(color, pixel) <= 1 - threshold:
                    # print("当前坐标:", x, y, "\t颜色:", hex(pixel))
                    # 释放
                    win32gui.ReleaseDC(hwnd, hwndDC)
                    print("设备上下文释放：", hwndDC)
                    return x, y
        if (time() - start_time) >= max_time:
            win32gui.ReleaseDC(hwnd, hwndDC)
            print("设备上下文释放：", hwndDC)
            return False


def computeBGRColorSimilar(color1, color2):
    """计算BGR形式的int值表示的两个颜色之间的相似度

    Args:
        color1: int
            BGR形式的int值
        color2: int
            BGR形式的int值

    Returns: float
        两者的相似度，越接近0越相似

    Reference:
        https://www.compuphase.com/cmetric.htm
    """
    R_1, G_1, B_1 = (color1 & 0xff, (color1 >> 8) & 0xff, color1 >> 16)
    R_2, G_2, B_2 = (color2 & 0xff, (color2 >> 8) & 0xff, color2 >> 16)
    # print("颜色1:", R_1, G_1, B_1)
    # print("颜色2:", R_2, G_2, B_2)
    r_mean = int((R_1 + R_2) / 2)
    R = R_1 - R_2
    G = G_1 - G_2
    B = B_1 - B_2
    # result = math.sqrt((((512 + r_mean) * R * R) >> 8) + 4 * G * G + (((767 - r_mean) * B * B) >> 8))
    result = math.sqrt((R * R + G * G + B * B) / (255 * 255 * 3))
    # print("相似度", result)
    return result


def bgr_int_to_hsv(color: int):
    """将BGR形式的int值转换为HSV形式，返回格式为 list[H, S, V]

    Args:
        color: int
            BGR形式的int值

    Returns: numpy.Array[int, int, int]
        HSV形式的列表，格式为 numpy.Array[H, S, V]
    """
    rgb_color = (color & 0xff, (color >> 8) & 0xff, color >> 16)
    rgb_color = numpy.uint8([[rgb_color]])
    print(cv2.cvtColor(rgb_color, cv2.COLOR_RGB2HSV))
    return cv2.cvtColor(rgb_color, cv2.COLOR_RGB2HSV)[0][0]
