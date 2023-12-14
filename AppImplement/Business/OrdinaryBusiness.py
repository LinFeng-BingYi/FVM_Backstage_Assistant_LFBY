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
from AppImplement.Business.Foundation import switchWorldZone, singleLayerChooseLevel

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
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 821 * zoom, 54 * zoom)
    #     delay(1000)
    return "完成[VIP签到]"


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
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 855 * zoom, 50 * zoom)
    #     delay(1000)
    return "完成[每日签到]"


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
        result_str = f"完成[塔罗寻宝]"
    # 点击”关闭“
    mouseClick(hwnd, 830 * zoom, 80 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 830 * zoom, 80 * zoom)
    #     delay(1000)
    return result_str


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
        delay(100)
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
    mouseClick(hwnd, 640 * zoom, 585 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 640 * zoom, 585 * zoom)
    #     delay(1000)
    return "完成[底部任务]"


def executeUnionGarden(hwnd, need_fertilize: bool, plant_type=0, zoom=1):
    """执行公会花园浇水、施肥

    Args:
        hwnd: int
            窗口句柄
        need_fertilize: bool
            是否需要施肥
        plant_type: int[0 | 1 | 2 | 3]
            当本公会的公会树需要种植时生效。0表示无种植权限，1、2、3表示种植初级、中级、高级公会树
        zoom: float
            缩放比例
    """
    result_str = "完成[公会花园]。已浇水，但未施肥"
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
            delay(500)
            # 寻找是否提示”超过成长上限“
            if not find_pic(hwnd, UNION_GARDEN_MAX_PATH, [350, 180, 450, 400]):
                # 等待完成浇水任务的报幕结束
                delay(4000)
                # 如果需要施肥，则点击 剩余需要施肥次数 次施肥
                if need_fertilize and fertilize_time > 0:
                    result_str = "完成[公会花园]。已浇水，且施肥3次"
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
        if try_num > 4 and (try_num - 1) % 4 == 0:
            # 当尝试次数为4的倍数+1时，需要往上翻一页
            mouseClick(hwnd, 840 * zoom, 194 * zoom)
            delay(1000)
        elif try_num == 1 and False:  # TODO plant_type != 0:
            plant_pos = find_pic(hwnd, UNION_GARDEN_PLANT_PATH, [326, 303, 628, 486])
            if plant_pos:
                # 点击种植
                mouseClick(hwnd, plant_pos[0] * zoom, plant_pos[1] * zoom)
                delay(500)
                # TODO 选择树苗
                mouseClick(hwnd, 0, 0)
                delay(500)
                # TODO 确认种植
                mouseClick(hwnd, 0, 0)
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


def executeReceiveUnionQuest(hwnd, release_quest: bool = False, zoom=1):
    """领取公会任务，若有权限，可以选择发布会长任务
    """
    result_str = "完成[公会任务]"
    # 点击“跳转”
    mouseClick(hwnd, 870 * zoom, 585 * zoom)
    delay(500)
    # 点击“公会任务”
    mouseClick(hwnd, 900 * zoom, 260 * zoom)
    delay(2000)
    # 查找已完成的任务
    complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [340, 120, 410, 540])
    while complete_quest_pos:
        # 点击找到的任务
        mouseClick(hwnd, complete_quest_pos[0] * zoom, complete_quest_pos[1] * zoom)
        delay(100)
        # 点击领取奖励
        mouseClick(hwnd, 640 * zoom, 530 * zoom)
        delay(100)
        # 继续找其他已完成的任务
        complete_quest_pos = find_pic(hwnd, COMPLETE_BOTTOM_QUEST_PATH, [340, 120, 410, 540])
    if release_quest and find_color(hwnd, [75, 36, 174, 75], 0x78E4F4):
        print("抽取")
        # 点击“发布任务”
        mouseClick(hwnd, 127 * zoom, 57 * zoom)
        delay(500)
        # 点击“抽取并发布”
        mouseClick(hwnd, 486 * zoom, 439 * zoom)
        delay(500)
        result_str = "完成[公会任务]。且发布会长任务"
    # 关闭界面
    mouseClick(hwnd, 855 * zoom, 55 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 855 * zoom, 55 * zoom)
    #     delay(1000)
    return result_str


def executeOpenFoodContest(hwnd, zoom=1):
    return "目前暂未实现[打开美食大赛]"


def executeOpenBackpack(hwnd, zoom=1):
    # 点击界面下方”背包“
    mouseClick(hwnd, 595 * zoom, 585 * zoom)
    if not find_pic_loop(hwnd, OPEN_BACKPACK_PATH, [33, 123, 122, 184], max_time=120):
        raise BusinessError("超过2min还未打开背包界面！")
    delay(1000)
    # 点击“道具”
    mouseClick(hwnd, 780 * zoom, 70 * zoom)
    delay(500)
    # 关闭界面
    mouseClick(hwnd, 917 * zoom, 60 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 917 * zoom, 60 * zoom)
    #     delay(1000)
    return "完成[打开背包]"


def executeReceiveTeamMagicTower(hwnd, zoom=1):
    """领取双人魔塔奖励"""
    switchWorldZone(hwnd, "魔塔蛋糕", zoom)
    # 点击双人tab页
    mouseClick(hwnd, 117 * zoom, 70 * zoom)
    delay(500)
    # 点击“领取”
    mouseClick(hwnd, 907 * zoom, 470 * zoom)
    delay(1000)
    # 退出界面
    mouseClick(hwnd, 930 * zoom, 30 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 930 * zoom, 30 * zoom)
    #     delay(1000)
    return "完成[领取双人魔塔奖励]"


def executeGiveFlowers(hwnd, receiver_name_path: str, use_gift_coupon: bool = False, use_times: int = 0, zoom=1):
    """赠送免费鲜花，可选择使用礼券
    """
    result_str = "完成[赠送鲜花]"
    # 点击“好友”
    mouseClick(hwnd, 40 * zoom, 105 * zoom)
    if not find_pic_loop(hwnd, OPEN_FRIEND_PATH, [434, 87, 543, 122], max_time=120):
        raise BusinessError("超过2min还未打开好友签到界面！")
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
    delay(500)
    if find_pic(hwnd, SECONDARY_PASSWORD, [360, 170, 510, 220]):
        # 关闭二级密码框
        mouseClick(hwnd, 570 * zoom, 200 * zoom)
        delay(500)
        # 关闭鲜花界面
        mouseClick(hwnd, 715 * zoom, 150 * zoom)
        delay(500)
        # 关闭好友界面
        mouseClick(hwnd, 760 * zoom, 100 * zoom)
        delay(500)
        raise BusinessError("未解锁二级密码，送花失败！")
    if use_gift_coupon:
        # 选择礼券鲜花
        mouseClick(hwnd, 500 * zoom, 308 * zoom)
        delay(500)
        for i in range(use_times):
            # 点击”送出“
            mouseClick(hwnd, 500 * zoom, 400 * zoom)
            delay(500)
        result_str = f"完成[赠送鲜花]。并使用了{use_times}次礼券赠送"
    # 关闭鲜花界面
    mouseClick(hwnd, 715 * zoom, 150 * zoom)
    delay(500)
    # 关闭好友界面
    mouseClick(hwnd, 760 * zoom, 100 * zoom)
    delay(500)
    return result_str


def executeReceiveDestinyTree(hwnd, zoom=1):
    """领取缘分树奖励
    """
    # 点击“跳转”
    mouseClick(hwnd, 870 * zoom, 585 * zoom)
    delay(500)
    # 点击“缘分树”
    mouseClick(hwnd, 900 * zoom, 340 * zoom)
    delay(2000)
    # 点击”领取“
    mouseClick(hwnd, 315 * zoom, 505 * zoom)
    delay(500)
    # 关闭界面
    mouseClick(hwnd, 930 * zoom, 30 * zoom)
    delay(1000)
    # if not checkCloseActivity(hwnd):
    #     mouseClick(hwnd, 930 * zoom, 30 * zoom)
    #     delay(1000)
    return "完成[领取缘分树奖励]"


def checkCloseActivity(hwnd):
    delay(500)
    return find_pic(hwnd, SWITCH_LINE_PATH, [791, 70, 840, 98])
