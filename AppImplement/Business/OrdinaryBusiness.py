#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : OrdinaryBusiness.py
# @Time    : 2023/12/10 15:29
# @Dsc     : 一般业务，过程中不用输出信息到主界面

from PySide6.QtCore import QDate, QTime, QDateTime

from Common.Backstage import *
from AppImplement.GlobalValue.StaticValue import *
from AppImplement.Business.CustomException import BusinessError
from AppImplement.Business.Foundation import (
    switchWorldZone, singleLayerChooseLevel, createPwdRoom, openBottomMenu, openTopMenu,
    chooseSingleOrMultiZone, chooseCrossServiceLevel, chooseMagicTowerLevel, check2ndPsw, checkEnterRoom,
    checkFoodContestQuestFinish, exitRoom, openMagicTowerDialog
)

from math import floor
from os import listdir


# 日常领取、日常收尾相关 -----------------------------------------------------------------------
def executeVipSignin(hwnd, zoom=1):
    if not find_pic(hwnd, VIP_SIGNIN_PATH, [640, 18, 706, 54]):
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        if not find_pic(hwnd, VIP_SIGNIN_PATH, [640, 18, 706, 54], record_fail=True, record_name="未找到VIP签到"):
            raise BusinessError("未能找到VIP签到图标！")
    # 点击图标
    mouseClick(hwnd, 674 * zoom, 30 * zoom)
    if not find_pic_loop(hwnd, OPEN_VIP_SIGNIN_PATH, [392, 35, 566, 72], max_time=120):
        raise BusinessError("超过2min还未打开VIP签到界面！")
    delay(1000)
    # 点击”每日签到“
    mouseClick(hwnd, 740 * zoom, 188 * zoom)
    delay(100)
    # 点击”领取“礼券
    mouseClick(hwnd, 228 * zoom, 281 * zoom)
    delay(100)
    # 点击”关闭“
    mouseClick(hwnd, 821 * zoom, 54 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 821 * zoom, 54 * zoom)
    #     delay(1000)
    return "完成[VIP签到]"


def executeDailySignin(hwnd, zoom=1):
    if not find_pic(hwnd, DAILY_SIGNIN_PATH, [580, 18, 640, 54]):
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        if not find_pic(hwnd, DAILY_SIGNIN_PATH, [580, 18, 640, 54], record_fail=True, record_name="未找到每日签到"):
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
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 855 * zoom, 50 * zoom)
    #     delay(1000)
    return "完成[每日签到]"


def executeFreeWish(hwnd, zoom=1):
    if not find_pic(hwnd, FVM_ACTIVITY_PATH, [512, 18, 579, 54]):
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        if not find_pic(hwnd, FVM_ACTIVITY_PATH, [512, 18, 579, 54], record_fail=True, record_name="未找到美食活动"):
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
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 780 * zoom, 60 * zoom)
    #     delay(1000)
    return "完成[免费许愿]"


def executePharaohTreasure(hwnd, flop_pos: int, zoom=1):
    result_str = "完成[法老宝藏]。没有执行翻牌操作"
    pharaoh_pos = find_pic(hwnd, PHARAOH_TREASURE_PATH, [247, 17, 778, 112])
    if not pharaoh_pos:
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        pharaoh_pos = find_pic(hwnd, PHARAOH_TREASURE_PATH, [247, 17, 778, 112], record_fail=True, record_name="未找到法老宝藏")
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
        delay(700)
        result_str = f"完成[法老宝藏]。翻取了第{flop_pos}张牌"
    # 点击”关闭“
    mouseClick(hwnd, 790 * zoom, 97 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 790 * zoom, 97 * zoom)
    #     delay(1000)
    return result_str


def executeTarotTreasure(hwnd, zoom=1):
    result_str = "完成[塔罗寻宝]。没有执行翻牌操作"
    tarot_pos = find_pic(hwnd, TAROT_TREASURE_PATH, [247, 17, 778, 112])
    if not tarot_pos:
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        tarot_pos = find_pic(hwnd, TAROT_TREASURE_PATH, [247, 17, 778, 112], record_fail=True, record_name="未找到塔罗寻宝")
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
        delay(700)
        result_str = f"完成[塔罗寻宝]"
    # 点击”关闭“
    mouseClick(hwnd, 830 * zoom, 80 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 830 * zoom, 80 * zoom)
    #     delay(1000)
    return result_str


def executeReceiveBottomQuest(hwnd, zoom=1):
    openBottomMenu(hwnd, "任务", zoom=zoom)
    # 收起前三种任务
    # for i in range(3):
    #     print(f"收起第{i}种任务")
    #     if not find_pic(hwnd, FOLD_BOTTOM_QUEST_PATH, [100, 130 + i * 30, 125, 165 + i * 30]):
    #         mouseClick(hwnd, (110 + i * 30) * zoom, (146 + i * 30) * zoom)
    #         delay(100)
    # 先重置滑动条
    mouseClick(hwnd, 414 * zoom, 150 * zoom)
    delay(500)
    # 查找已完成的任务
    complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [340, 120, 410, 540])
    while complete_quest_pos:
        mouseClick(hwnd, complete_quest_pos[0] * zoom, complete_quest_pos[1] * zoom)
        delay(100)
        # 点击领取奖励
        mouseClick(hwnd, 640 * zoom, 530 * zoom)
        delay(500)
        # 继续找其他已完成的任务
        complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [340, 120, 410, 540])
    # 通过在滑动条的横坐标414这一列，遍历每个像素点，从上往下查找滑动条的底部，然后点击这个位置，实现全面覆盖所有任务
    for bar_y_pixel in range(152, 512):
        if find_color(hwnd, [414, bar_y_pixel, 414, bar_y_pixel], 0x724705):
            mouseClick(hwnd, 414 * zoom, (bar_y_pixel + 10) * zoom)
            delay(100)
            # 查找已完成的任务
            complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [340, 120, 410, 540])
            while complete_quest_pos:
                mouseClick(hwnd, complete_quest_pos[0] * zoom, complete_quest_pos[1] * zoom)
                delay(100)
                # 点击领取奖励
                mouseClick(hwnd, 640 * zoom, 530 * zoom)
                delay(100)
                # 继续找其他已完成的任务
                complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [340, 120, 410, 540])
    # 关闭底部任务界面
    mouseClick(hwnd, 855 * zoom, 55 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 855 * zoom, 55 * zoom)
    #     delay(1000)
    return "完成[底部任务]"


def unfoldUnionQuest(hwnd, zoom=1):
    for i in range(2):
        check_quest_folded = find_pic(hwnd, FOLD_BOTTOM_QUEST_PATH, [100, 130, 125, 315])
        if check_quest_folded:
            mouseClick(hwnd, check_quest_folded[0] * zoom, check_quest_folded[1] * zoom)
            delay(500)
        else:
            break


def executeUnionGarden(hwnd, fertilize_date: str, plant_type=0, zoom=1):
    """执行公会花园浇水、施肥

    Args:
        hwnd: int
            窗口句柄
        fertilize_date: str
            公会花园施肥日期范围。格式："yyyy/MM/dd-yyyy/MM/dd"
        plant_type: int[0 | 1 | 2 | 3]
            当本公会的公会树需要种植时生效。0表示无种植权限，1、2、3表示种植初级、中级、高级公会树
        zoom: float
            缩放比例
    """
    result_str = "完成[公会花园]。已浇水，但未施肥"
    need_fertilize = determineDateRangeEvent(fertilize_date)
    if need_fertilize:
        # 先查看公会任务中施肥任务的状态，若不是“进行中”，则无需施肥
        openBottomMenu(hwnd, "跳转", "公会任务", zoom)
        # 展开公会任务
        unfoldUnionQuest(hwnd, zoom)
        # 识别施肥3次的任务是否已完成，注意根据有无发布过会长任务而变化识图范围
        if find_color(hwnd, [377, 470, 377, 470], 0x512D00):
            if not find_pic(hwnd, TODO_BOTTOM_QUEST_PATH, [355, 190 + 30 * 7, 400, 220 + 30 * 7]):
                need_fertilize = False
        else:
            if not find_pic(hwnd, TODO_BOTTOM_QUEST_PATH, [355, 190 + 30 * 9, 400, 220 + 30 * 9]):
                need_fertilize = False
        # 关闭公会任务
        mouseClick(hwnd, 855 * zoom, 55 * zoom)
        delay(500)
    # 点击底部“公会”
    mouseClick(hwnd, 777 * zoom, 585 * zoom)
    if not find_pic_loop(hwnd, OPEN_UNION_PATH, [218, 95, 292, 111], max_time=120):
        mouseClick(hwnd, 909 * zoom, 70 * zoom)
        delay(100)
        raise BusinessError("超过2min还未打开公会界面！也许该账号没有加入公会！")
    delay(1000)

    try_click_garden_time = 5
    while try_click_garden_time > 0:
        # 点击公会活动
        mouseKeepPlace(hwnd, 748 * zoom, 429 * zoom, 30)
        # 点击公会花园
        mouseClick(hwnd, 777 * zoom, 346 * zoom)
        if find_pic_loop(hwnd, OPEN_UNION_GARDEN_PATH, [416, 44, 563, 69], max_time=5):
            break
        try_click_garden_time -= 1
    if try_click_garden_time == 0:
        # 关闭公会
        mouseClick(hwnd, 909 * zoom, 70 * zoom)
        delay(1000)
        raise BusinessError("尝试打开公会花园界面超过5次，均失败！请手动执行！")

    delay(1000)
    # 点击摘果
    mouseClick(hwnd, 784 * zoom, 475 * zoom)
    delay(200)
    # 打开全部公会
    mouseClick(hwnd, 800 * zoom, 125 * zoom)
    delay(500)
    # 跳转到最后一页
    mouseClick(hwnd, 840 * zoom, 306 * zoom)
    delay(500)
    # 查看下方进度条颜色，最左侧是绿色 同时 最右侧是灰色，则满足浇水施肥条件
    try_num = 1  # 跳转公会 寻找适合浇水 的 尝试次数
    fertilize_time = 3 if need_fertilize else 0     # 需要施肥的次数
    # 是否刚种下（刚种下是指 try_num=1 且本公会不满足施肥条件，且可以种植时，选择了种植），如果是，则不再判断下方进度条，直接进入施肥
    just_plant = False
    while True:
        if just_plant or (find_color(hwnd, [255, 550, 255, 550], 0x40A77D) and find_color(
                hwnd, [690, 550, 690, 550], 0x7E6A4A)):
            # 点击浇水
            mouseClick(hwnd, 784 * zoom, 360 * zoom)
            # delay(500)
            checkFoodContestQuestFinish(hwnd)
            # 寻找是否提示”超过成长上限“
            if not find_pic(hwnd, UNION_GARDEN_MAX_PATH, [350, 180, 450, 400]):
                # 等待完成浇水任务的报幕结束
                delay(4000)
                # 如果需要施肥，则点击 剩余需要施肥次数 次施肥
                if need_fertilize and fertilize_time > 0:
                    result_str = "完成[公会花园]。已浇水，且施肥3次"
                    for i in range(fertilize_time):
                        mouseClick(hwnd, 784 * zoom, 420 * zoom)
                        # delay(500)
                        # 判断是否触发美食大赛任务完成
                        checkFoodContestQuestFinish(hwnd)
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
        if try_num > 4 and (try_num - 1) % 4 == 0:
            # 当尝试次数为4的倍数+1时，需要往上翻一页
            mouseClick(hwnd, 840 * zoom, 194 * zoom)
            delay(1000)
        elif try_num == 1 and plant_type != 0:
            plant_pos = find_pic(hwnd, UNION_GARDEN_PLANT_PATH, [400, 350, 600, 450])
            if plant_pos:
                # 点击种植
                mouseClick(hwnd, plant_pos[0] * zoom, plant_pos[1] * zoom)
                delay(500)
                # 选择树苗
                mouseClick(hwnd, (360 + 115 * (plant_type - 1)) * zoom, 340 * zoom)
                delay(500)
                # 确认种植
                mouseClick(hwnd, 475 * zoom, 420 * zoom)
                delay(500)
                # 设置“刚种植”标志，并直接继续下一次循环，避免点击“前往”导致离开本公会
                just_plant = True
                continue
        elif try_num >= 120:
            # 如果尝试次数超过了120次（假设最多30页，每页4个公会），则宣告失败
            break
        click_y_pos = 300 - (try_num - 1) % 4 * 30
        # 点击”前往“
        mouseClick(hwnd, 810 * zoom, click_y_pos * zoom)
        delay(700)
        try_num += 1
    # 等待完成施肥3次任务的报幕结束
    if need_fertilize:
        delay(4000)
    # 关闭公会花园
    mouseClick(hwnd, 854 * zoom, 54 * zoom)
    delay(500)
    # 关闭公会
    mouseClick(hwnd, 909 * zoom, 70 * zoom)
    delay(1000)
    if try_num >= 120:
        raise BusinessError("已尝试过120个公会，均超过成长上限，无法正常完成浇水施肥！")
    return result_str


def executeReceiveCampsiteKey(hwnd, zoom=1):
    singleLayerChooseLevel(hwnd, "探险营地", "营地钥匙", zoom)
    return "完成[营地钥匙]"


def executeMonthlyCardWelfare(hwnd, zoom=1):
    if not openTopMenu(hwnd, "月卡福利", zoom=zoom):
        raise BusinessError("未能找到月卡福利图标！")
    if find_color(hwnd, [665, 495, 760, 535], 0x0078DD):
        mouseClick(hwnd, 715 * zoom, 515 * zoom)
        delay(500)
        result_str = "完成[月卡福利]。成功领取礼包"
    else:
        result_str = "完成[月卡福利]。没有领取礼包"
    mouseClick(hwnd, 830 * zoom, 60 * zoom)
    delay(300)
    return result_str


def executeReceiveUnionQuest(hwnd, release_quest: bool = False, zoom=1):
    """领取公会任务，若有权限，可以选择发布会长任务
    """
    result_str = "完成[公会任务]"
    openBottomMenu(hwnd, "跳转", "公会任务", zoom)
    unfoldUnionQuest(hwnd, zoom)
    # 查找已完成的任务
    complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [340, 120, 410, 540])
    while complete_quest_pos:
        # 点击找到的任务
        mouseClick(hwnd, complete_quest_pos[0] * zoom, complete_quest_pos[1] * zoom)
        delay(100)
        # 点击领取奖励
        mouseClick(hwnd, 640 * zoom, 530 * zoom)
        # delay(500)
        checkFoodContestQuestFinish(hwnd)
        # 继续找其他已完成的任务
        complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [340, 120, 410, 540])
    if release_quest and find_color(hwnd, [75, 36, 174, 75], 0x78E4F4):
        print("抽取")
        # 点击“发布任务”
        mouseClick(hwnd, 127 * zoom, 57 * zoom)
        delay(500)
        # 点击“抽取并发布”
        mouseClick(hwnd, 486 * zoom, 439 * zoom)
        delay(3000)
        # 点击关闭抽取任务界面
        mouseClick(hwnd, 650 * zoom, 200 * zoom)
        delay(500)
        result_str = "完成[公会任务]。且发布会长任务"
    # 关闭界面
    mouseClick(hwnd, 855 * zoom, 55 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 855 * zoom, 55 * zoom)
    #     delay(1000)
    return result_str


def executeReceiveLoversQuest(hwnd, zoom=1):
    """领取情侣任务
    """
    result_str = "完成[情侣任务]"
    openBottomMenu(hwnd, "跳转", "情侣任务", zoom)
    # 领取已完成的任务
    for i in [0, 1, 2]:
        if find_color(hwnd, [175 + 250 * i, 410, 280 + 250 * i, 440], 0x2B95FF):
            mouseClick(hwnd, (230 + 250 * i) * zoom, 425 * zoom)
            delay(500)
            # 若点击“领取”没有反应，则重新打开一次情侣任务界面
            if find_color(hwnd, [175 + 250 * i, 410, 280 + 250 * i, 440], 0x2B95FF):
                mouseClick(hwnd, 850 * zoom, 60 * zoom)
                delay(500)
                openBottomMenu(hwnd, "跳转", "情侣任务", zoom)
                mouseClick(hwnd, (230 + 250 * i) * zoom, 425 * zoom)
                delay(500)
    # 领取甜蜜奖励
    for i in range(3):
        mouseClick(hwnd, 800 * zoom, 525 * zoom)
        delay(500)
    # 关闭界面
    mouseClick(hwnd, 850 * zoom, 60 * zoom)
    delay(1000)
    return result_str


def executeOpenFoodContest(hwnd, close_dialog=True, zoom=1):
    contest_pos = find_pic(hwnd, FOOD_CONTEST_PATH, [247, 17, 778, 112])
    if not contest_pos:
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        contest_pos = find_pic(hwnd, FOOD_CONTEST_PATH, [247, 17, 778, 112])
        if not contest_pos:
            return "跳过[打开美食大赛]。未找到美食大赛图标"
    # 点击图标
    mouseClick(hwnd, contest_pos[0] * zoom, contest_pos[1] * zoom)
    if not find_pic_loop(hwnd, OPEN_FOOD_CONTEST_PATH, [390, 40, 600, 150], max_time=120):
        raise BusinessError("超过2min还未打开美食大赛界面！")
    # delay(1000)
    checkFoodContestQuestFinish(hwnd)
    if close_dialog:
        mouseClick(hwnd, 890 * zoom, 50 * zoom)
        delay(500)
    return "完成[打开美食大赛]"


def executeOpenBackpack(hwnd, zoom=1):
    openBottomMenu(hwnd, "背包", "道具", zoom)
    # 关闭界面
    mouseClick(hwnd, 917 * zoom, 60 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 917 * zoom, 60 * zoom)
    #     delay(1000)
    return "完成[打开背包]"


def executeReceiveTeamMagicTower(hwnd, box_checked: bool, force_execute: bool, zoom=1):
    if not determineMondayEvent(box_checked, force_execute):
        return "跳过[领取双人魔塔奖励]"
    """领取双人魔塔奖励"""
    switchWorldZone(hwnd, "魔塔蛋糕", zoom)
    # 点击双人tab页
    mouseClick(hwnd, 117 * zoom, 70 * zoom)
    delay(500)
    # 点击“领取”
    mouseClick(hwnd, 907 * zoom, 470 * zoom)
    # delay(1000)
    checkFoodContestQuestFinish(hwnd)
    # 退出界面
    mouseClick(hwnd, 930 * zoom, 30 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 930 * zoom, 30 * zoom)
    #     delay(1000)
    return "完成[领取双人魔塔奖励]"


def executeGiveFlowers(hwnd, receiver_name_path: str, use_gift_coupon: bool = False, use_times: int = 0, second_psw='', zoom=1):
    """赠送免费鲜花，可选择使用礼券
    """
    result_str = "完成[赠送鲜花]"
    # 点击“好友”
    mouseClick(hwnd, 40 * zoom, 105 * zoom)
    if not find_pic_loop(hwnd, OPEN_FRIEND_PATH, [434, 87, 543, 122], max_time=120):
        raise BusinessError("超过2min还未打开好友界面！")
    delay(500)
    # 点击“我的好友”tab页，避免被好友申请干扰
    mouseClick(hwnd, 280 * zoom, 140 * zoom)
    delay(500)
    # 先重置滑动条
    if not find_color(hwnd, [758, 195, 758, 210], 0xFCE683):
        mouseClick(hwnd, 758 * zoom, 200 * zoom)
        delay(500)
    # 找一次目标好友
    receiver_pos = find_pic(hwnd, receiver_name_path, [247, 170, 372, 486], 0.95)
    for bar_y_pixel in range(203, 457):
        if not receiver_pos:
            # 对于滑动条纵向范围，若本次没找到，就更新一次滑动条位置，再找图，直到成功找到或遍历完滑动条范围
            if find_color(hwnd, [758, bar_y_pixel, 758, bar_y_pixel], 0x724705):
                mouseClick(hwnd, 758 * zoom, (bar_y_pixel + 10) * zoom)
                delay(100)
                receiver_pos = find_pic(hwnd, receiver_name_path, [247, 170, 372, 486], 0.95)
    # 若结束循环时仍没找到
    if not receiver_pos:
        raise BusinessError("未能找到目标好友！")
    # 否则，点击目标好友
    mouseClick(hwnd, receiver_pos[0] * zoom, receiver_pos[1] * zoom)
    delay(100)
    # 点击“给他送花”
    mouseClick(hwnd, (receiver_pos[0] + 70) * zoom, (receiver_pos[1] + 203) * zoom)
    delay(500)
    # 选择免费鲜花
    mouseClick(hwnd, 350 * zoom, 308 * zoom)
    delay(500)
    # 点击”送出“
    mouseClick(hwnd, 500 * zoom, 400 * zoom)
    # delay(1000)
    checkFoodContestQuestFinish(hwnd)
    check_2nd_psw_result = check2ndPsw(hwnd, second_psw, zoom)
    if check_2nd_psw_result is not None and not check_2nd_psw_result:
        result_str = "[赠送鲜花]失败！未解锁二级密码"
    else:
        if check_2nd_psw_result is not None:
            # 点击”送出“
            mouseClick(hwnd, 500 * zoom, 400 * zoom)
            checkFoodContestQuestFinish(hwnd)
        if use_gift_coupon:
            # 选择礼券鲜花
            mouseClick(hwnd, 500 * zoom, 308 * zoom)
            delay(500)
            for i in range(use_times):
                # 点击”送出“
                mouseClick(hwnd, 500 * zoom, 400 * zoom)
                # delay(500)
                checkFoodContestQuestFinish(hwnd)
            result_str = f"完成[赠送鲜花]。并使用了{use_times}次礼券赠送"
    # 关闭鲜花界面
    mouseClick(hwnd, 715 * zoom, 150 * zoom)
    delay(500)
    # 关闭好友界面
    mouseClick(hwnd, 760 * zoom, 100 * zoom)
    delay(500)
    return result_str


def executeReceiveDestinyTree(hwnd, box_checked: bool, force_execute: bool, zoom=1):
    """领取缘分树奖励
    """
    if not determineMondayEvent(box_checked, force_execute):
        return "跳过[领取缘分树奖励]"
    openBottomMenu(hwnd, "跳转", "缘分树", zoom)
    # 点击”领取“
    mouseClick(hwnd, 375 * zoom, 505 * zoom)
    # delay(500)
    checkFoodContestQuestFinish(hwnd)
    # 关闭界面
    mouseClick(hwnd, 930 * zoom, 30 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 930 * zoom, 30 * zoom)
    #     delay(1000)
    return "完成[领取缘分树奖励]"


def executeReceiveMonopoly(hwnd, use_dice=False, zoom=1):
    result_str = "完成[大富翁]。未使用骰子"
    if not openTopMenu(hwnd, "大富翁", "", zoom):
        result_str = "跳过[大富翁]"
        return result_str
    # 领取骰子
    for page in range(3):
        for btn in range(6):
            mouseClick(hwnd, 765 * zoom, (165 + btn * 50) * zoom)
            delay(500)
        mouseClick(hwnd, 875 * zoom, 456 * zoom)
        delay(500)
    # 使用骰子
    if use_dice:
        if not find_color(hwnd, [375, 200, 375, 200], 0x61FF73):
            mouseClick(hwnd, 375 * zoom, 200 * zoom)
            delay(500)
        while not find_pic(hwnd, MONOPOLY_ZERO_DICE_PATH, [380, 240, 566, 348]):
            mouseClick(hwnd, 380 * zoom, 160 * zoom)
            # 摇中点数6走路耗时8.7s, 传送耗时0.8s, 战利品飘字4s
            delay(3500)
        result_str = "完成[大富翁]。且使用骰子"
    # 关闭界面
    mouseClick(hwnd, 930 * zoom, 20 * zoom)
    delay(300)
    return result_str


def executeReceiveFoodContest(hwnd, zoom=1):
    executeOpenFoodContest(hwnd, close_dialog=False, zoom=zoom)
    # 重置滑块位置
    mouseClick(hwnd, 537 * zoom, 360 * zoom)
    delay(500)
    # 查找已完成的任务
    complete_quest_pos = find_pic(hwnd, COMPLETE_FOOD_CONTEST_PATH, [450, 355, 530, 575])
    while complete_quest_pos:
        # 领取奖励
        mouseClick(hwnd, complete_quest_pos[0] * zoom, complete_quest_pos[1] * zoom)
        delay(100)
        # 继续找其他已完成的任务
        complete_quest_pos = find_pic_loop(hwnd, COMPLETE_FOOD_CONTEST_PATH, [450, 355, 530, 575], max_time=3)
    # 通过在滑动条的横坐标414这一列，遍历每个像素点，从上往下查找滑动条的底部，然后点击这个位置，实现全面覆盖所有任务
    for bar_y_pixel in range(390, 565):
        if find_color(hwnd, [536, bar_y_pixel, 536, bar_y_pixel], 0x1A3D85, 0.95):
            mouseClick(hwnd, 536 * zoom, (bar_y_pixel + 7) * zoom)
            delay(100)
            # 查找已完成的任务
            complete_quest_pos = find_pic(hwnd, COMPLETE_FOOD_CONTEST_PATH, [450, 355, 530, 575])
            while complete_quest_pos:
                # 领取奖励
                mouseClick(hwnd, complete_quest_pos[0] * zoom, complete_quest_pos[1] * zoom)
                delay(100)
                # 继续找其他已完成的任务
                complete_quest_pos = find_pic_loop(hwnd, COMPLETE_FOOD_CONTEST_PATH, [450, 355, 530, 575], max_time=3)
    # 关闭界面
    mouseClick(hwnd, 890 * zoom, 50 * zoom)
    delay(500)


def executeReceiveTXYDQuest(hwnd, zoom=1):
    switchWorldZone(hwnd, "探险营地", zoom)
    # 点击探险任务
    mouseClick(hwnd, 515 * zoom, 215 * zoom)
    if not find_pic_loop(hwnd, OPEN_EXPLORE_QUEST_PATH, [400, 50, 530, 80], max_time=120):
        raise BusinessError("超过2min还未打开探险任务界面！")
    # 重置滑块位置
    mouseClick(hwnd, 455 * zoom, 155 * zoom)
    delay(300)
    mouseClick(hwnd, 815 * zoom, 160 * zoom)
    delay(300)
    # 领取左侧任务
    while find_pic(hwnd, COMPLETE_EXPLORE_QUEST_1_PATH, [360, 150, 450, 200]):
        mouseClick(hwnd, 400 * zoom, 175 * zoom)
        delay(500)
    # 领取右侧任务
    for i in range(12):
        btn_quest2_pos = find_pic(hwnd, COMPLETE_EXPLORE_QUEST_2_PATH, [700, 150, 800, 440])
        if btn_quest2_pos:
            mouseClick(hwnd, btn_quest2_pos[0] * zoom, btn_quest2_pos[1] * zoom)
            delay(500)
        else:
            break
    # 关闭界面
    mouseClick(hwnd, 870 * zoom, 55 * zoom)
    delay(500)


def checkCloseActivity(hwnd):
    delay(500)
    return find_pic(hwnd, SWITCH_LINE_PATH, [791, 70, 840, 98])


# 会长任务相关 -----------------------------------------------------------------------
def match_one_pic_of_dir(hwnd, abs_dir_path, find_range, threshold=0.999):
    """在窗口中匹配指定目录下的任一图片

    Args:
        hwnd: int
        abs_dir_path: str
            指定目标目录的绝对路径，路径分隔符用反斜杠，注意结尾不加
        find_range: list[int]
            窗口中识图范围
        threshold: float

    Returns:
        返回匹配到的第一张图片文件名，不包含扩展名和路径; 未找到时返回None
        example:
            假设目录 "D:\abc" 下有截图文件 "123.bmp" , 当匹配到该文件时，返回字符串 "123"
    """
    for pic in listdir(abs_dir_path):
        pic_abs_path = abs_dir_path + "\\" + pic
        if find_pic(hwnd, pic_abs_path, find_range, threshold):
            return pic.rsplit('.', 1)[0]
    return None


def findUnionPresidentQuest(hwnd, zoom=1):
    """在已打开公会任务面板的前提下，开始遍历查找公会任务，将任务查找结果存入列表

    Args:
        hwnd: int
            ...
        zoom: float
            ...

    Returns: list
        任务查找结果列表，查找成功则返回任务截图文件名，没找到则返回”没找到“，已完成则返回”已完成“
        example:
            ["浮空岛-卤料花园-继续挑战", "浮空岛-十三香中心岛-跳过", "没找到", "已完成"]
    """
    # 先检查两种任务是否被收起
    unfoldUnionQuest(hwnd, zoom)
    quest_result_list = []
    # 逐个检查
    for i in [0, 1, 2]:
        # 点击对应任务
        mouseClick(hwnd, 160 * zoom, (205 + 30 * i) * zoom)
        delay(800)
        # 若该任务状态不是“进行中”，则跳过
        if not find_pic(hwnd, TODO_BOTTOM_QUEST_PATH, [355, 190 + 30 * i, 400, 220 + 30 * i]):
            quest_result_list.append("已完成")
            continue
        # 否则，查找任务结果，默认值为”没找到“
        quest_find_result = "没找到"
        quest_pic_dir_path = ROOT_PATH + r"\resources\images\任务图片\公会任务\任务" + f"{i + 1}"
        # for quest_pic in listdir(quest_pic_dir_path):
        #     quest_pic_abstract_path = quest_pic_dir_path + "\\" + quest_pic
        #     if find_pic(hwnd, quest_pic_abstract_path, [432, 90, 855, 367], 0.999):
        #         # 若找到了，则将 任务结果 改为 纯文件名
        #         quest_find_result = quest_pic.rsplit('.', 1)[0]
        #         break
        match_pic = match_one_pic_of_dir(hwnd, quest_pic_dir_path, [432, 90, 855, 367])
        if match_pic is not None:
            quest_find_result = match_pic
        quest_result_list.append(quest_find_result)
    print(quest_result_list)
    return quest_result_list


# 情侣任务相关 -----------------------------------------------------------------------
def findLoversQuest(hwnd, zoom=1):
    """在已打开情侣任务面板的前提下，开始遍历查找情侣任务，将任务查找结果存入列表

    Args:
        hwnd: int
            ...
        zoom: float
            ...

    Returns: list
        任务查找结果列表，查找成功则返回任务截图文件名，没找到则返回”没找到“，已完成则返回”已完成“
        example:
            ["浮空岛-卤料花园-继续挑战", "浮空岛-十三香中心岛-跳过", "没找到", "已完成"]
    """
    quest_result_list = []
    # 逐个检查
    for i in [0, 1, 2]:
        # 若发现已完成，则跳过
        if find_color(hwnd, [100 + 250 * i, 155, 170 + 250 * i, 190], 0x53C967):
            quest_result_list.append("已完成")
            continue
        if find_color(hwnd, [175 + 250 * i, 410, 280 + 250 * i, 440], 0x2B95FF):
            quest_result_list.append("已完成")
            continue
        # 否则，查找任务结果，默认值为”没找到“
        quest_find_result = "没找到"
        quest_pic_dir_path = ROOT_PATH + r"\resources\images\任务图片\情侣任务\任务" + f"{i + 1}"
        for quest_pic in listdir(quest_pic_dir_path):
            quest_pic_abstract_path = quest_pic_dir_path + "\\" + quest_pic
            if find_pic(hwnd, quest_pic_abstract_path, [100 + 250 * i, 100, 345 + 250 * i, 350], 0.999):
                # 若找到了，则将 任务结果 改为 纯文件名
                quest_find_result = quest_pic.rsplit('.', 1)[0]
                break
        quest_result_list.append(quest_find_result)
    print(quest_result_list)
    return quest_result_list


# 悬赏三连相关 -----------------------------------------------------------------------
def openWantedDialog(hwnd, zoom=1):
    wanted_pos = find_pic(hwnd, WANTED_PATH, [247, 17, 778, 112])
    if not wanted_pos:
        # 若没找到，则点击切换上方活动按钮
        mouseClick(hwnd, 780 * zoom, 30 * zoom)
        delay(500)
        wanted_pos = find_pic(hwnd, WANTED_PATH, [247, 17, 778, 112], record_fail=True, record_name="未找到悬赏活动")
        if not wanted_pos:
            raise BusinessError("未能找到悬赏活动图标！")
    # 点击悬赏活动图标
    mouseClick(hwnd, wanted_pos[0] * zoom, wanted_pos[1] * zoom)
    if not find_pic_loop(hwnd, OPEN_WANTED_PATH, max_time=120):
        raise BusinessError("超过2min还未打开悬赏活动界面！")
    delay(1000)


def createWantedRoom(hwnd, three_island_zone, zoom=1):
    openWantedDialog(hwnd, zoom)
    goto_button_pos = find_pic(hwnd, GOTO_BUTTON_PIC_DICT[three_island_zone])
    # 点击“挑战”
    mouseClick(hwnd, goto_button_pos[0] * zoom, goto_button_pos[1] * zoom)
    delay(500)
    # 创建房间
    createPwdRoom(hwnd, "0000", zoom)


def executeReceiveWanted(hwnd, zoom=1):
    """领取悬赏活动
    """
    result_str = "完成[悬赏活动]"
    openTopMenu(hwnd, "悬赏活动", "", zoom)
    close_btn_pos = find_pic(hwnd, CLOSE_WANTED_PATH)
    # 领取悬赏奖励
    complete_btn_pos = find_pic(hwnd, WANTED_COMPLETE_PATH)
    old_pos = []
    while complete_btn_pos:
        if len(old_pos) == 2 and abs(complete_btn_pos[0] - old_pos[0]) < 5 and abs(complete_btn_pos[1] - old_pos[1]) < 5:
            mouseClick(hwnd, close_btn_pos[0] * zoom, close_btn_pos[1] * zoom)
            delay(500)
            openTopMenu(hwnd, "悬赏活动", "", zoom)
        mouseClick(hwnd, complete_btn_pos[0] * zoom, complete_btn_pos[1] * zoom)
        delay(500)
        old_pos = complete_btn_pos[0:2]
        complete_btn_pos = find_pic(hwnd, WANTED_COMPLETE_PATH)
    # 关闭界面
    mouseClick(hwnd, close_btn_pos[0] * zoom, close_btn_pos[1] * zoom)
    delay(500)
    return result_str


# 汇总关卡创建 -----------------------------------------------------------------------
# 顶部副本关卡
TOP_MENU_LEVEL_OPEN_FUNC = {
    "悬赏美味": (createWantedRoom, {"three_island_zone": "美味岛"}),
    "悬赏火山": (createWantedRoom, {"three_island_zone": "火山岛"}),
    "悬赏浮空": (createWantedRoom, {"three_island_zone": "浮空岛"}),
    "欢乐假期": (openTopMenu, {"menu_name": "欢乐假期", "sub_menu_name": ""}),
    "实验室": (openTopMenu, {"menu_name": "实验室", "sub_menu_name": ""})
}


def createMagicTowerRoom(hwnd, level_num: int, tab_num, enter_room=True, zoom=1):
    openMagicTowerDialog(hwnd, tab_num, enter_room, zoom=zoom)
    if enter_room:
        # 选择魔塔关卡，并进入房间
        chooseMagicTowerLevel(hwnd, level_num, zoom)


def createAnyRoom(hwnd, zone, level, enter_room=True, team_mode=False, zoom=1):
    """从跳转地图区域到进入房间。可以通过设置enter_room=False使得仅跳转，而不进入房间"""
    if zone == "顶部关卡":
        # 顶部关卡支持 悬赏活动、欢乐假期、实验室
        target_zone = "美味岛"
        if level.find("悬赏") != -1:
            target_zone = TOP_MENU_LEVEL_OPEN_FUNC[level][1]["three_island_zone"]
        switchWorldZone(hwnd, target_zone, zoom)
        if enter_room:
            create_room_func, func_args = TOP_MENU_LEVEL_OPEN_FUNC[level]
            create_room_func(hwnd=hwnd, zoom=zoom, **func_args)
    elif zone == "魔塔蛋糕":
        tab_num = 0
        if team_mode:
            tab_num = 1
        if int(level) < 0:
            tab_num = 2
        createMagicTowerRoom(hwnd, int(level), tab_num, enter_room, zoom)
    elif zone in CROSS_SERVER_LEVEL_TYPE_NO:
        switchWorldZone(hwnd, "跨服远征", zoom)
        if enter_room:
            chooseCrossServiceLevel(hwnd, zone, level, zoom)
    else:
        chooseSingleOrMultiZone(hwnd, zone, level, zoom)
        if enter_room:
            createPwdRoom(hwnd, zoom=zoom)


def createLoopSkillRoom(hwnd, zone, level, zoom=1):
    if zone not in LOOP_SKILL_ZONE:
        return
    if zone == "魔塔蛋糕":
        level = int(level)
        switchWorldZone(hwnd, "魔塔蛋糕", zoom)
        # 等待魔塔加载完毕
        while find_pic(hwnd, MAGIC_TOWER_LOADING_PATH, [5, 80, 220, 160]):
            delay(300)
        tab_num = 0
        if level < 0:
            tab_num = 2
        # 选择tab页
        mouseClick(hwnd, (45 + 73 * tab_num) * zoom, 70 * zoom)
        delay(500)
        # 选择魔塔关卡，并进入房间
        chooseMagicTowerLevel(hwnd, level, zoom)
        # 若提示次数不足
        if find_pic(hwnd, MAGIC_TOWER_TAB3_NO_RESIDUAL_PATH, [300, 210, 650, 400]):
            # 关闭次数不足提示框
            mouseClick(hwnd, 585 * zoom, 250 * zoom)
            delay(500)
            # 关闭魔塔界面
            mouseClick(hwnd, 925 * zoom, 32 * zoom)
            delay(500)
            return False
    elif zone == "跨服远征":
        createAnyRoom(hwnd, level, "8星", True, zoom=zoom)
    elif zone == "实验室":
        createAnyRoom(hwnd, "顶部关卡", "实验室", True, zoom=zoom)
        delay(2000)
        # 点击“我的关卡”
        mouseClick(hwnd, 660 * zoom, 550 * zoom)
        delay(2000)
        if level.split('-')[1] == "草稿箱":
            mouseClick(hwnd, 250 * zoom, 90 * zoom)
            delay(300)
            # 点击”测试关卡“
            mouseClick(hwnd, 650 * zoom, 295 * zoom)
            delay(500)
        else:
            mouseClick(hwnd, 370 * zoom, 90 * zoom)
            delay(300)
            # 点击”游玩关卡“
            mouseClick(hwnd, 540 * zoom, 155 * zoom)
            delay(500)
    else:
        switchWorldZone(hwnd, zone, zoom)
        # 选择 单层级地图 关卡
        mouseClick(hwnd,
                   SINGLE_HIERARCHY_ZONE[zone][level][0] * zoom,
                   SINGLE_HIERARCHY_ZONE[zone][level][1] * zoom)
        delay(300)
        # 点击 "创建"
        mouseClick(hwnd, 525 * zoom, 488 * zoom)
        delay(300)


def reEnterLoopSkillRoom(hwnd, zone, level, zoom=1):
    if zone not in LOOP_SKILL_ZONE:
        return
    if zone == "魔塔蛋糕":
        # 点击”开始挑战“
        mouseClick(hwnd, 588 * zoom, 560 * zoom)
    elif zone == "跨服远征":
        chooseCrossServiceLevel(hwnd, level, "8星", zoom)
    elif zone == "实验室":
        # 点击“我的关卡”
        mouseClick(hwnd, 660 * zoom, 550 * zoom)
        delay(300)
        if level.split('-')[1] == "草稿箱":
            # 点击”测试关卡“
            mouseClick(hwnd, 650 * zoom, 295 * zoom)
        else:
            # 点击”游玩关卡“
            mouseClick(hwnd, 540 * zoom, 155 * zoom)
    else:
        # 选择 单层级地图 关卡
        mouseClick(hwnd,
                   SINGLE_HIERARCHY_ZONE[zone][level][0] * zoom,
                   SINGLE_HIERARCHY_ZONE[zone][level][1] * zoom)
        delay(300)
        # 点击 "创建"
        mouseClick(hwnd, 525 * zoom, 488 * zoom)
    # 等待进入房间
    checkEnterRoom(hwnd)


def closeLoopSkillRoom(hwnd, zone, level, zoom=1):
    if zone not in LOOP_SKILL_ZONE:
        return
    if zone == "魔塔蛋糕":
        mouseClick(hwnd, 925 * zoom, 32 * zoom)
        delay(300)
    elif zone == "跨服远征":
        mouseClick(hwnd, 915 * zoom, 30 * zoom)
        delay(300)
    elif zone == "实验室":
        mouseClick(hwnd, 925 * zoom, 32 * zoom)
        delay(300)
    else:
        pass


# 其他相关 -------------------------------------------------------------------------
def closeCommonTipDialog(hwnd, zoom=1):
    tip_dialog_close_btn = find_pic(hwnd, COMMON_TIP_DIALOG_CLOSE_PATH, threshold=0.9)
    if tip_dialog_close_btn:
        mouseClick(hwnd, tip_dialog_close_btn[0] * zoom, tip_dialog_close_btn[1] * zoom)
        delay(200)
    delay(300)


def closeJustLoginDialog(hwnd, zoom=1):
    """关闭刚登录游戏时弹出的对话框
    """
    delay(2000)
    # 健康游戏提示对话框
    closeCommonTipDialog(hwnd, zoom)
    # 假期特惠对话框
    if find_pic(hwnd, OPEN_HOLIDAY_DISCOUNT_PATH):
        mouseClick(hwnd, 770 * zoom, 130 * zoom)
        delay(500)


def closeExecExceptionDlg(hwnd, zoom=1):
    # 查找并关闭3次“常见关闭按钮”
    for i in range(3):
        closeCommonTipDialog(hwnd, zoom=zoom)
    # 判断是否在房间内
    if find_pic(hwnd, ENTER_ROOM_PATH, [375, 20, 430, 50]):
        exitRoom(hwnd, zoom)
        if find_pic(hwnd, ENTER_ROOM_PATH, [375, 20, 430, 50]):
            # 取消准备状态
            mouseClick(hwnd, 872 * zoom, 480 * zoom)
            delay(500)
            exitRoom(hwnd, zoom)
    # 判断并关闭
    DLG_CLS_BTN_POS = {
        "法老宝藏": (790, 97),
        "塔罗寻宝": (830, 80),
        "美食大赛": (890, 50),
        "假期特惠": (770, 130)
    }
    for key, value in DLG_CLS_BTN_POS.items():
        if find_pic(hwnd, FIND_AND_OPEN_TOP_MENU_DICT[key][1], FIND_AND_OPEN_TOP_MENU_DICT[key][2]):
            mouseClick(hwnd, value[0] * zoom, value[1] * zoom)
            delay(500)
    # 查找并关闭3次“常见关闭按钮”
    for i in range(3):
        closeCommonTipDialog(hwnd, zoom=zoom)



# 流程列表功能界面参数加工相关 ---------------------------------------------------------------
def determineMondayEvent(sub_func_checked: bool, force_execute: bool):
    """判断每周一才执行的事件在本日是否需要执行

    适用的事件有：[领取双人魔塔奖励]、[领取缘分树奖励]
    """
    if sub_func_checked and (
            force_execute or QDate.currentDate().dayOfWeek() == 1):
        return True
    return False


def determineDateRangeEvent(execute_date_range: str):
    """判断指定日期范围的事件在本日是否需要执行

    适用的事件有：[公会花园施肥]

    Args:
        execute_date_range: str
            日期范围。格式："yyyy/MM/dd-yyyy/MM/dd"

    Return: bool
    """
    # 获取起止时间，判断当前日期是否需要执行
    start_date_str, end_date_str = execute_date_range.split('-')
    start_year, start_month, start_day = start_date_str.split('/')
    start_date = QDate(int(start_year), int(start_month), int(start_day))
    end_year, end_month, end_day = end_date_str.split('/')
    end_date = QDate(int(end_year), int(end_month), int(end_day))
    if start_date <= QDate.currentDate() <= end_date:
        return True
    return False


def waitUntilSpecificTime(specific_time_str, over_night=True):
    """循环等待直到超过目标时间

    Args:
        specific_time_str: str
            目标时间。格式：HH:mm:ss
        over_night: bool
            是否支持跨午夜0点。当目标时间小于当前时间时，若支持，则一直等到下一天该时间，否则返回False
    """
    specific_time_lst = specific_time_str.split(":")
    specific_time = QTime(int(specific_time_lst[0]), int(specific_time_lst[1]), int(specific_time_lst[2]))
    if QTime.currentTime() < specific_time:
        specific_datetime = QDateTime(QDate.currentDate(), specific_time)
    else:
        if not over_night:
            return False
        specific_datetime = QDateTime(QDate.currentDate().addDays(1), specific_time)
    while QDateTime.currentDateTime() < specific_datetime:
        delay(1)
    return True
