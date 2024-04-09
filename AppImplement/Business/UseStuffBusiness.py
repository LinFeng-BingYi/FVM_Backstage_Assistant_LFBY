#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : UseStuffBusiness.py
# @Time    : 2024/3/31 15:54
# @Dsc     : [使用物品]功能中的方法
from os import rename, makedirs
from shutil import rmtree

from AppImplement.Business.Foundation import acceptInvitationOrNot, check2ndPsw, openBottomMenu, openTopMenu
from AppImplement.Business.OrdinaryBusiness import match_one_pic_of_dir
from AppImplement.Business.CustomException import BusinessError
from AppImplement.GlobalValue.StaticValue import *
from Common.Backstage import *


# 使用物品相关 -----------------------------------------------------------------------
# 背包 -----------------------------------
def backpackUseFirstPage(hwnd, stuff_pic, use_times, second_psw='', zoom=1, **kwargs):
    # 解包可变参数字典
    count_chest_stuff = kwargs["count_chest_stuff"]
    capture_range = None
    count_statistic_dict = {}
    stuff_pic_name = path.basename(stuff_pic).rsplit(".", 1)[0]
    temp_dir = ROOT_PATH + "\\" + r"temp\use_stuff" + f"\\{stuff_pic_name}"
    # 关闭背包图格区域的遮挡界面
    cover_dialog_close_btn = find_pic(hwnd, COMMON_TIP_DIALOG_CLOSE_PATH, [435, 90, 950, 485])
    if cover_dialog_close_btn:
        mouseClick(hwnd, cover_dialog_close_btn[0] * zoom, cover_dialog_close_btn[1] * zoom)
        delay(500)
    # 重置滑动条位置
    mouseClick(hwnd, 920 * zoom, 115 * zoom)
    delay(500)
    flag_need_execute = True        # 识图标志
    flag_first_time_use = True      # 首次使用标志
    for bar_y_pixel in range(110, 410):
        if find_color(hwnd, [916, bar_y_pixel, 916, bar_y_pixel], 0x724705):
            mouseClick(hwnd, 916 * zoom, (bar_y_pixel + 10) * zoom)
            delay(100)
            flag_need_execute = True
        if flag_need_execute:
            # 查找物品
            acceptInvitationOrNot(hwnd, False, zoom)
            stuff_pos = find_pic(hwnd, stuff_pic)
            while stuff_pos and use_times != 0:
                # 点击物品
                mouseClick(hwnd, stuff_pos[0] * zoom, stuff_pos[1] * zoom)
                delay(200)
                # 点击使用
                mouseClick(hwnd, (stuff_pos[0] + 32) * zoom, (stuff_pos[1] + 12) * zoom)
                delay(500)
                # 首次执行时的特殊处理：处理二级密码框、判断开宝箱物品截图位置
                if flag_first_time_use:
                    # 关闭二级密码框
                    check_2nd_psw_result = check2ndPsw(hwnd, second_psw, zoom)
                    if check_2nd_psw_result is not None:
                        if not check_2nd_psw_result:
                            return False
                        else:
                            # 若首次执行时遇到二级密码框，则本次会执行失败，下次执行仍算首次执行
                            stuff_pos = find_pic(hwnd, stuff_pic)
                            continue
                    # 获取截图范围
                    if count_chest_stuff:
                        if find_pic(hwnd, BACKPACK_1ST_PAGE_USE_STUFF_PIC1_PATH, [240, 190, 320, 220]):
                            capture_range = [240, 225, 710, 350]
                        elif find_pic(hwnd, BACKPACK_1ST_PAGE_USE_STUFF_PIC2_PATH, [110, 180, 220, 210]):
                            capture_range = [110, 220, 460, 295]
                        else:
                            # 若没识别的开宝箱的物品展示对话框，则本物品使用过程中不统计
                            count_chest_stuff = False
                        if count_chest_stuff:
                            if path.exists(temp_dir):
                                rmtree(temp_dir)
                            makedirs(temp_dir)
                    # 更新首次执行标志
                    flag_first_time_use = False

                if count_chest_stuff:
                    match_pic_name = match_one_pic_of_dir(hwnd, temp_dir, capture_range)
                    if match_pic_name is None:
                        new_pic_name = f"reward{len(count_statistic_dict) + 1}"
                        count_statistic_dict[new_pic_name] = 1
                        new_pic_abs_name = temp_dir + "\\" + new_pic_name + f"-{count_statistic_dict[new_pic_name]}.bmp"
                        save_captured_pic(new_pic_abs_name, hwnd, capture_range)
                    else:
                        this_pic_name, this_pic_count = match_pic_name.rsplit("-", 1)
                        count_statistic_dict[this_pic_name] += 1
                        update_pic_abs_name = temp_dir + "\\" + this_pic_name + f"-{count_statistic_dict[this_pic_name]}.bmp"
                        rename(temp_dir + "\\" + f"{match_pic_name}.bmp", update_pic_abs_name)
                pop_dialog_close_btn = find_pic(hwnd, COMMON_TIP_DIALOG_CLOSE_PATH, [435, 90, 950, 485])
                # 关闭弹出的对话框
                if pop_dialog_close_btn:
                    mouseClick(hwnd, pop_dialog_close_btn[0] * zoom, pop_dialog_close_btn[1] * zoom)
                    delay(400)
                use_times -= 1
                acceptInvitationOrNot(hwnd, False, zoom)
                stuff_pos = find_pic(hwnd, stuff_pic)
            flag_need_execute = False
            # 当使用次数归零，直接结束
            if use_times == 0:
                break
    return True


def backpackUseThirdPage(hwnd, stuff_pic, use_times, second_psw='', zoom=1, **kwargs):
    # 关闭背包图格区域的遮挡界面
    cover_dialog_close_btn = find_pic(hwnd, COMMON_TIP_DIALOG_CLOSE_PATH, [435, 90, 950, 485])
    if cover_dialog_close_btn:
        mouseClick(hwnd, cover_dialog_close_btn[0] * zoom, cover_dialog_close_btn[1] * zoom)
        delay(500)
    # 重置滑动条位置
    mouseClick(hwnd, 920 * zoom, 115 * zoom)
    delay(500)
    flag_need_execute = True  # 识图标志
    for bar_y_pixel in range(110, 410):
        if find_color(hwnd, [916, bar_y_pixel, 916, bar_y_pixel], 0x724705):
            mouseClick(hwnd, 916 * zoom, (bar_y_pixel + 10) * zoom)
            delay(100)
            flag_need_execute = True
        if flag_need_execute:
            # 查找物品
            acceptInvitationOrNot(hwnd, False, zoom)
            stuff_pos = find_pic(hwnd, stuff_pic)
            # 技能书类别物品提前结束的标志
            flag_skip = False
            while stuff_pos and use_times != 0 and not flag_skip:
                # 点击物品
                mouseClick(hwnd, stuff_pos[0] * zoom, stuff_pos[1] * zoom)
                delay(200)
                # 点击使用
                mouseClick(hwnd, (stuff_pos[0] + 32) * zoom, (stuff_pos[1] + 12) * zoom)
                delay(500)
                if find_pic(hwnd, BACKPACK_PROP_USE_SKILL_BOOK_DIALOG_PATH, [750, 255, 865, 285]):
                    # 双击数量输入框
                    leftDoubleClick(hwnd, 790 * zoom, 300 * zoom)
                    delay(200)
                    # 输入使用数量
                    this_batch_times = use_times if 0 <= use_times < 50 else 50
                    if 0 <= this_batch_times < 50:
                        flag_skip = True
                    use_times = use_times - this_batch_times if use_times > 0 else -1
                    keyInputStr(hwnd, str(this_batch_times))
                    # 点击“确定”
                    mouseClick(hwnd, 630 * zoom, 335 * zoom)
                    delay(300 * (this_batch_times + 1))
                else:
                    use_times -= 1
                # 关闭二级密码框
                check_2nd_psw_result = check2ndPsw(hwnd, second_psw, zoom)
                if check_2nd_psw_result is not None and not check_2nd_psw_result:
                    return False
                acceptInvitationOrNot(hwnd, False, zoom)
                stuff_pos = find_pic(hwnd, stuff_pic)
            flag_need_execute = False
            # 当使用次数归零，直接结束
            if use_times == 0:
                break
    return True


def backpackDelete(hwnd, stuff_pic, use_times, second_psw='', zoom=1, **kwargs):
    # 关闭背包图格区域的遮挡界面
    cover_dialog_close_btn = find_pic(hwnd, COMMON_TIP_DIALOG_CLOSE_PATH, [435, 90, 950, 485])
    if cover_dialog_close_btn:
        mouseClick(hwnd, cover_dialog_close_btn[0] * zoom, cover_dialog_close_btn[1] * zoom)
        delay(500)
    # 重置滑动条位置
    mouseClick(hwnd, 920 * zoom, 115 * zoom)
    delay(500)
    flag_need_execute = True  # 识图标志
    for bar_y_pixel in range(110, 410):
        if find_color(hwnd, [916, bar_y_pixel, 916, bar_y_pixel], 0x724705):
            mouseClick(hwnd, 916 * zoom, (bar_y_pixel + 10) * zoom)
            delay(100)
            flag_need_execute = True
        if flag_need_execute:
            # 查找物品
            acceptInvitationOrNot(hwnd, False, zoom)
            stuff_pos = find_pic(hwnd, stuff_pic)
            while stuff_pos:
                # 点击“删除”
                mouseClick(hwnd, 850 * zoom, 473 * zoom)
                delay(200)
                # 点击物品
                mouseClick(hwnd, stuff_pos[0] * zoom, stuff_pos[1] * zoom)
                delay(200)
                # 点击“确定”
                mouseClick(hwnd, 430 * zoom, 350 * zoom)
                delay(200)
                # 点击“删除”
                mouseClick(hwnd, 850 * zoom, 473 * zoom)
                delay(200)
                # 关闭二级密码框
                check_2nd_psw_result = check2ndPsw(hwnd, second_psw, zoom)
                if check_2nd_psw_result is not None and not check_2nd_psw_result:
                    return False
                # 继续查找物品
                acceptInvitationOrNot(hwnd, False, zoom)
                stuff_pos = find_pic(hwnd, stuff_pic)
            flag_need_execute = False
    return True


# 假期特惠
def holidayDiscountConvert(hwnd, stuff_pic, use_times, second_psw='', zoom=1, **kwargs):
    # 跳转到第一页
    for jump_times in range(30):
        mouseClick(hwnd, 525 * zoom, 480 * zoom)
        delay(50)
    # 每右转一次识图一次
    flag_not_found = True      # 只要找到过一次，便不再继续向右翻页
    while flag_not_found:
        # 查找物品
        acceptInvitationOrNot(hwnd, False, zoom)
        stuff_pos = find_pic(hwnd, stuff_pic, [360, 200, 700, 460])
        while stuff_pos and use_times != 0:
            stuff_y_pos = int(stuff_pos[1])
            flag_not_found = False
            # 若没有兑换次数，则提前结束
            if not find_color(hwnd, [715, stuff_y_pos - 15, 810, stuff_y_pos + 15], 0x2D90F3):
                break
            # 点击“领取”
            mouseClick(hwnd, 760 * zoom, stuff_y_pos * zoom)
            delay(1100)
            # 关闭二级密码框
            check_2nd_psw_result = check2ndPsw(hwnd, second_psw, zoom)
            if check_2nd_psw_result is not None:
                if not check_2nd_psw_result:
                    return False
                else:
                    use_times += 1
            use_times -= 1
            acceptInvitationOrNot(hwnd, False, zoom)
            stuff_pos = find_pic(hwnd, stuff_pic)
        # 当使用次数归零，直接结束
        if use_times == 0:
            break
        # 向右一页
        mouseClick(hwnd, 640 * zoom, 480 * zoom)
        delay(3000)
    return True


# 公会副本-暗晶兑换
def unionDungeonCrystalConvert(hwnd, stuff_pic, use_times, second_psw='', zoom=1, **kwargs):
    # 点击“暗晶商店”
    mouseClick(hwnd, 800 * zoom, 500 * zoom)
    if not find_pic_loop(hwnd, OPEN_DARK_CRYSTAL_SHOP_PATH, [360, 25, 540, 55], max_time=120):
        raise BusinessError("超过2min还未打开暗晶商店界面！")
    delay(1000)
    # 点击“暗晶兑换”
    mouseClick(hwnd, 180 * zoom, 70 * zoom)
    delay(500)
    stuff_pic_result = find_pic(hwnd, stuff_pic)
    if stuff_pic_result:
        stuff_x_pos, stuff_y_pos = stuff_pic_result[0], stuff_pic_result[1]
        if stuff_x_pos < 475:
            exchange_x_pos = 400
        else:
            exchange_x_pos = 860
        if use_times < 0 or use_times > 100:
            # 由于该界面兑换次数耗尽后不会变灰，因此控制单次最大兑换次数为100
            use_times = 100
        while use_times != 0:
            # 点击“兑换”
            mouseClick(hwnd, exchange_x_pos * zoom, stuff_y_pos * zoom)
            delay(500)
            # 关闭二级密码框
            check_2nd_psw_result = check2ndPsw(hwnd, second_psw, zoom)
            if check_2nd_psw_result is not None:
                if not check_2nd_psw_result:
                    return False
                else:
                    use_times += 1
            use_times -= 1


# [使用物品]功能中，支持的界面和操作
USE_STUFF_SUB_FUNCTION_DICT = {
    "背包装备": {
        "使用": backpackUseFirstPage,
        "删除": backpackDelete
    },
    "背包道具": {
        "使用": backpackUseThirdPage,
        "删除": backpackDelete
    },
    "假期特惠": {
        "节日兑换": holidayDiscountConvert,
        "限时兑换": holidayDiscountConvert,
        "长期兑换": holidayDiscountConvert,
        "其他兑换": holidayDiscountConvert
    },
    "公会副本": {
        "暗晶兑换": unionDungeonCrystalConvert
    }
}

# [使用物品]功能中，支持的界面对应的打开和关闭函数
USE_STUFF_PANEL_IO_DICT = {
    "背包装备": [
        openBottomMenu,
        ("背包", "装备"),
        [(917, 60)]
    ],
    "背包道具": [
        openBottomMenu,
        ("背包", "道具"),
        [(917, 60)]
    ],
    "假期特惠": [
        openTopMenu,
        ("假期特惠", ""),
        [(770, 130)]
    ],
    "公会副本": [
        openBottomMenu,
        ("跳转", "公会副本"),
        [(920, 40), (914, 80)]
    ]
}

