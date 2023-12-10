#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : OrdinaryBusiness.py
# @Time    : 2023/12/10 15:29
# @Dsc     : 一般业务，过程中不用输出信息到主界面

from Common.Backstage import *
from AppImplement.GlobalValue.StaticValue import *
from AppImplement.Business.CustomException import BusinessError

from math import floor


# 一键签到相关 -----------------------------------------------------------------------
def executeVipSignin(hwnd, zoom=1):
    if not find_pic(hwnd, VIP_SIGNIN_PATH, [640, 18, 706, 54]):
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        if not find_pic(hwnd, VIP_SIGNIN_PATH, [640, 18, 706, 54]):
            raise BusinessError("未能找到VIP签到图标！")
    # 点击图标
    mouseClick(hwnd, 674 * zoom, 30 * zoom)
    if not find_pic_loop(hwnd, OPEN_VIP_SIGNIN_PATH, [392, 35, 566, 72], max_time=120):
        raise BusinessError("超过2min还未打开VIP签到界面！")
    delay(500)
    # 点击”每日签到“
    mouseClick(hwnd, 740 * zoom, 188 * zoom)
    delay(100)
    # 点击”领取“礼券
    mouseClick(hwnd, 228 * zoom, 281 * zoom)
    delay(100)
    # 点击”关闭“
    mouseClick(hwnd, 821 * zoom, 54 * zoom)
    delay(1000)
    if not checkCloseActivity(hwnd):
        mouseClick(hwnd, 821 * zoom, 54 * zoom)
        delay(1000)


def executeDailySignin(hwnd, zoom=1):
    if not find_pic(hwnd, DAILY_SIGNIN_PATH, [580, 18, 640, 54]):
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        if not find_pic(hwnd, DAILY_SIGNIN_PATH, [580, 18, 640, 54]):
            raise BusinessError("未能找到每日签到图标！")
    # 点击图标
    mouseClick(hwnd, 612 * zoom, 30 * zoom)
    if not find_pic_loop(hwnd, OPEN_DAILY_SIGNIN_PATH, [387, 35, 460, 63], max_time=120):
        raise BusinessError("超过2min还未打开每日签到界面！")
    delay(1000)
    # 查找是否待领取位置
    green_pos = find_pic(hwnd, DAILY_SIGNIN_BUTTON_PATH, [351, 108, 854, 489])
    if green_pos:
        mouseClick(hwnd, green_pos[0] * zoom, green_pos[1] * zoom)
        delay(100)
    # 点击下方四个累积宝箱
    for i in range(4):
        print(f"点击下方第{i}个累积宝箱")
        mouseClick(hwnd, (464 + 110 * i) * zoom, 527 * zoom)
        delay(100)
    # 点击”关闭“
    mouseClick(hwnd, 855 * zoom, 50 * zoom)
    delay(1000)
    if not checkCloseActivity(hwnd):
        mouseClick(hwnd, 855 * zoom, 50 * zoom)
        delay(1000)


def executeFreeWish(hwnd, zoom=1):
    if not find_pic(hwnd, FVM_ACTIVITY_PATH, [512, 18, 579, 54]):
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        if not find_pic(hwnd, FVM_ACTIVITY_PATH, [512, 18, 579, 54]):
            raise BusinessError("未能找到美食活动图标！")
    # 点击图标
    mouseClick(hwnd, 545 * zoom, 30 * zoom)
    if not find_pic_loop(hwnd, OPEN_FVM_ACTIVITY_PATH, [394, 45, 560, 75], max_time=120):
        raise BusinessError("超过2min还未打开美食活动界面！")
    delay(500)
    # 点击许愿
    mouseClick(hwnd, 360 * zoom, 480 * zoom)
    delay(100)
    # 点击”关闭“
    mouseClick(hwnd, 780 * zoom, 60 * zoom)
    delay(1000)
    if not checkCloseActivity(hwnd):
        mouseClick(hwnd, 780 * zoom, 60 * zoom)
        delay(1000)


def executePharaohTreasure(hwnd, flop_pos: int, zoom=1):
    pharaoh_pos = find_pic(hwnd, PHARAOH_TREASURE_PATH, [247, 17, 778, 112])
    if not pharaoh_pos:
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        pharaoh_pos = find_pic(hwnd, PHARAOH_TREASURE_PATH, [247, 17, 778, 112])
        if not pharaoh_pos:
            raise BusinessError("未能找到法老宝藏图标！")
    # 点击图标
    mouseClick(hwnd, pharaoh_pos[0] * zoom, pharaoh_pos[1] * zoom)
    if not find_pic_loop(hwnd, OPEN_PHARAOH_TREASURE_PATH, [337, 94, 434, 142], max_time=120):
        raise BusinessError("超过2min还未打开法老宝藏界面！")
    delay(1000)
    # 查找是否免费
    free_pos = find_pic(hwnd, PHARAOH_FREE_PATH, [410, 153, 532, 174])
    print("法老免费结果: ", free_pos)
    if free_pos and 1 <= flop_pos <= 8:
        # 点击选择的宝藏位置：第一个宝藏位置正中心是(300, 257)，左右两个相隔120，上下两个相隔140
        mouseClick(hwnd, (301 + ((flop_pos - 1) % 4) * 120) * zoom, (257 + floor((flop_pos - 1) / 4) * 140) * zoom)
        delay(100)
    # 点击”关闭“
    mouseClick(hwnd, 790 * zoom, 97 * zoom)
    delay(1000)
    if not checkCloseActivity(hwnd):
        mouseClick(hwnd, 790 * zoom, 97 * zoom)
        delay(1000)


def executeTarotTreasure(hwnd, zoom=1):
    tarot_pos = find_pic(hwnd, TAROT_TREASURE_PATH, [247, 17, 778, 112])
    if not tarot_pos:
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        tarot_pos = find_pic(hwnd, TAROT_TREASURE_PATH, [247, 17, 778, 112])
        if not tarot_pos:
            raise BusinessError("未能找到塔罗寻宝图标！")
    # 点击图标
    mouseClick(hwnd, tarot_pos[0] * zoom, tarot_pos[1] * zoom)
    if not find_pic_loop(hwnd, OPEN_TAROT_TREASURE_PATH, [393, 58, 477, 82], max_time=120):
        raise BusinessError("超过2min还未打开塔罗寻宝界面！")
    delay(1000)
    # 查找是否免费
    free_pos = find_pic(hwnd, TAROT_FREE_PATH, [288, 451, 412, 477])
    print("塔罗免费结果: ", free_pos)
    if free_pos:
        mouseClick(hwnd, free_pos[0] * zoom, free_pos[1] * zoom)
        delay(100)
    # 点击”关闭“
    mouseClick(hwnd, 830 * zoom, 80 * zoom)
    delay(1000)
    if not checkCloseActivity(hwnd):
        mouseClick(hwnd, 830 * zoom, 80 * zoom)
        delay(1000)


def executeReceiveBottomQuest(hwnd, zoom=1):
    # 点击界面下方”任务“
    mouseClick(hwnd, 640 * zoom, 585 * zoom)
    if not find_pic_loop(hwnd, OPEN_BOTTOM_QUEST_PATH, [422, 41, 525, 68], max_time=120):
        raise BusinessError("超过2min还未打开底部任务界面！")
    delay(1000)
    # 收起前三种任务
    for i in range(3):
        print(f"收起第{i}种任务")
        if not find_pic(hwnd, FOLD_BOTTOM_QUEST_PATH, [100, 130 + i * 30, 125, 165 + i * 30]):
            mouseClick(hwnd, (110 + i * 30) * zoom, (146 + i * 30) * zoom)
            delay(100)
    # 查找已完成的任务
    complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [342, 124, 410, 540])
    while complete_quest_pos:
        mouseClick(hwnd, complete_quest_pos[0] * zoom, complete_quest_pos[1] * zoom)
        delay(100)
        # 点击领取奖励
        mouseClick(hwnd, 640 * zoom, 530 * zoom)
        delay(100)
        # 继续找其他已完成的任务
        complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [342, 124, 410, 540])
    # 通过在滑动条的横坐标414这一列，遍历每个像素点，从上往下查找滑动条的底部，然后点击这个位置，实现全面覆盖所有任务
    for bar_y_pixel in range(152, 512):
        if find_color(hwnd, [414, bar_y_pixel, 414, bar_y_pixel], 0x724705):
            mouseClick(hwnd, 414 * zoom, (bar_y_pixel + 10) * zoom)
            delay(100)
            # 查找已完成的任务
            complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [342, 124, 410, 540])
            while complete_quest_pos:
                mouseClick(hwnd, complete_quest_pos[0] * zoom, complete_quest_pos[1] * zoom)
                delay(100)
                # 点击领取奖励
                mouseClick(hwnd, 640 * zoom, 530 * zoom)
                delay(100)
                # 继续找其他已完成的任务
                complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [342, 124, 410, 540])
    # 关闭底部任务界面
    mouseClick(hwnd, 640 * zoom, 585 * zoom)
    delay(1000)
    if not checkCloseActivity(hwnd):
        mouseClick(hwnd, 640 * zoom, 585 * zoom)
        delay(1000)


def executeUnionGarden(hwnd, need_fertilize: bool, zoom=1):
    mouseClick(hwnd, 777 * zoom, 585 * zoom)
    if not find_pic_loop(hwnd, OPEN_UNION_PATH, [218, 95, 292, 111], max_time=120):
        mouseClick(hwnd, 909 * zoom, 70 * zoom)
        delay(100)
        raise BusinessError("超过2min还未打开公会界面！也许该账号没有加入公会！")
    delay(1000)
    # 点击公会活动
    mouseMove(hwnd, 748 * zoom, 419 * zoom)
    delay(200)
    # 点击公会花园
    mouseClick(hwnd, 777 * zoom, 346 * zoom)

    if not find_pic_loop(hwnd, OPEN_UNION_GARDEN_PATH, [416, 44, 563, 69], max_time=120):
        raise BusinessError("超过2min还未打开公会界面！也许该账号没有加入公会！")
    delay(1000)
    # 打开全部公会
    mouseClick(hwnd, 800 * zoom, 125 * zoom)
    delay(500)
    # 跳转到最后一页
    mouseClick(hwnd, 840 * zoom, 306 * zoom)
    delay(500)
    # 查看下方进度条颜色，最左侧是绿色 同时 最右侧是灰色，则满足浇水施肥条件
    try_num = 1  # 跳转公会 寻找适合浇水 的 尝试次数
    fertilize_time = 3 if need_fertilize else 0
    while True:
        if find_color(hwnd, [255, 550, 255, 550], 0x40A77D) and find_color(
                hwnd, [690, 550, 690, 550], 0x7E6A4A):
            # 点击浇水
            mouseClick(hwnd, 784 * zoom, 360 * zoom)
            delay(500)
            # 寻找是否提示”超过成长上限“
            if not find_pic(hwnd, UNION_GARDEN_MAX_PATH, [350, 180, 450, 400]):
                delay(5000)
                # 如果需要施肥，则点击 剩余需要施肥次数 次施肥
                if need_fertilize and fertilize_time > 0:
                    for i in range(fertilize_time):
                        mouseClick(hwnd, 784 * zoom, 420 * zoom)
                        delay(500)
                        # 每施一次肥，寻找是否提示”超过成长上限“
                        if not find_pic(hwnd, UNION_GARDEN_MAX_PATH, [350, 180, 450, 400]):
                            # 成功则 需要施肥次数 - 1
                            fertilize_time -= 1
                        else:
                            # 若施肥失败，需要施肥次数未归零，将会继续跳转公会
                            break
                if fertilize_time == 0:
                    # 不需要施肥时，浇水成功后，等待5s直接退出
                    # 需要施肥时，浇水成功后，将剩余需要施肥次数耗尽，再退出
                    break

        print("本公会不满足可浇水条件！")
        if try_num >= 120:
            # 如果尝试次数超过了120次（假设最多30页，每页4个公会），则宣告失败
            break
        if try_num > 4 and (try_num - 1) % 4 == 0:
            # 当尝试次数为4的倍数+1时，需要往上翻一页
            mouseClick(hwnd, 840 * zoom, 194 * zoom)
            delay(1000)
        click_y_pos = 300 - (try_num - 1) % 4 * 30
        # 点击”前往“
        mouseClick(hwnd, 810 * zoom, click_y_pos * zoom)
        delay(700)
        try_num += 1
    delay(5000)
    # 关闭公会花园
    mouseClick(hwnd, 854 * zoom, 54 * zoom)
    delay(500)
    mouseClick(hwnd, 909 * zoom, 70 * zoom)
    delay(1000)
    if try_num >= 120:
        raise BusinessError("已尝试过120个公会，均超过成长上限，无法正常完成浇水施肥！")


def checkCloseActivity(hwnd):
    return find_pic(hwnd, SWITCH_LINE_PATH, [791, 70, 840, 98])
