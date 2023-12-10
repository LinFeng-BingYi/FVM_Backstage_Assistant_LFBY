#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : Foundation.py
# @Time    : 2023/11/26 22:03
# @Dsc     : 基础操作

from Common.Backstage import *

from AppImplement.GlobalValue.StaticValue import *


# 选择 对应地图 对应关卡 ---------------------------------------------------------------------------
def switchWorldZone(hwnd: int, zone_name, zoom=1):
    """在世界地图中切换地区，地区名必须与世界地图中显示的保持一致
    """
    if zone_name not in WORLD_MAP_ZONE_POS:
        raise KeyError
    need_switch_server = {
        "美味岛": 8,
        "火山岛": 2,
        "浮空岛": 2,
        "海底漩涡": 2,
        "竞技岛": 2,
        "探险营地": 2
    }
    # 打开世界地图
    mouseClick(hwnd, WORLD_MAP_POS[0] * zoom, WORLD_MAP_POS[1] * zoom)
    delay(2000)
    # 检查是否打开成功
    find_result = find_pic(hwnd, WORLD_MAP_TITTLE_PATH)
    if not find_result:
        print("未能检测到打开世界地图！正在重新尝试...")
        # 打开世界地图
        mouseClick(hwnd, WORLD_MAP_POS[0] * zoom, WORLD_MAP_POS[1] * zoom)
        delay(2000)
        # 检查是否打开成功
        find_result = find_pic(hwnd, WORLD_MAP_TITTLE_PATH)
        if not find_result:
            print("打开世界地图失败！！！")
            return
    # 点击对应的地图
    mouseClick(hwnd, WORLD_MAP_ZONE_POS[zone_name][0] * zoom, WORLD_MAP_ZONE_POS[zone_name][0] * zoom)
    delay(1000)
    if zone_name in need_switch_server:
        # 点击”换线“
        mouseClick(hwnd, 820 * zoom, 85 * zoom)
        delay(500)
        # 点击分区
        # 一区纵坐标82，每个区间隔25
        # print("换区坐标：", 782 * zoom, (82 + 25 * (need_switch_server[zone_name] - 1)) * zoom)
        # print("100%坐标：", 782, (82 + 25 * (need_switch_server[zone_name] - 1)))
        mouseClick(hwnd, 782 * zoom, (82 + 25 * (need_switch_server[zone_name] - 1)) * zoom)
        delay(2000)


def singleLayerChooseLevel(hwnd, zone_name, level_name, zoom=1):
    # 切换地图
    switchWorldZone(hwnd, zone_name, zoom)
    # 选择关卡
    if level_name in ["深渊岛", "雪顶火山", "十三香中心岛", "圣代基地"]:
        # 可能被挡住的关卡
        if find_color(hwnd, [254, 56, 778, 105], 0xB827FF, 0.85):
            # 如果被遮挡，则点击切换上方活动页
            mouseClick(hwnd, 790 * zoom, 27 * zoom)
            delay(500)
    # 选择 单层级地图 关卡
    mouseClick(hwnd,
               SINGLE_HIERARCHY_ZONE[zone_name][level_name][0] * zoom,
               SINGLE_HIERARCHY_ZONE[zone_name][level_name][1] * zoom)
    delay(2000)


def multiLayerChooseLevel(hwnd, zone_name, level_name, zoom=1):
    """写死的方法
    """
    # 切换到探险营地-探险港口
    singleLayerChooseLevel(hwnd, "探险营地", "探险港口", zoom)
    # 选择副本地图
    mouseClick(hwnd,
               TXGK_ZONE_POS[zone_name][0] * zoom,
               TXGK_ZONE_POS[zone_name][1] * zoom)
    delay(2000)
    # 选择 副本地图 关卡
    mouseClick(hwnd,
               MULTI_HIERARCHY_ZONE[zone_name][level_name][0] * zoom,
               MULTI_HIERARCHY_ZONE[zone_name][level_name][1] * zoom)
    delay(2000)


def chooseSingleOrMultiZone(hwnd, zone_name, level_name, zoom=1):
    if zone_name in SINGLE_HIERARCHY_ZONE:
        singleLayerChooseLevel(hwnd, zone_name, level_name, zoom)
    elif zone_name in MULTI_HIERARCHY_ZONE:
        multiLayerChooseLevel(hwnd, zone_name, level_name, zoom)
    else:
        raise KeyError


# 创建房间 -----------------------------------------------------------------------------------
def createPwdRoom(hwnd, pwd: str = "0000", zoom=1):
    # 查看是否已勾选使用密码
    if not find_pic(hwnd, CREATE_ROOM_PSW_PATH, [470, 430, 510, 470]):
        # 勾选使用密码
        mouseClick(hwnd, 490 * zoom, 450 * zoom)
    delay(500)
    # 双击密码框
    leftDoubleClick(hwnd, 620 * zoom, 450 * zoom)
    delay(500)
    # 输入密码
    for char in pwd:
        keyPress(hwnd, char)
        delay(200)
    # 点击 "创建"
    mouseClick(hwnd, 525 * zoom, 488 * zoom)
    delay(2000)


def teamInvite(hwnd_1p, hwnd_2p, player2_name_path, zoom1=1, zoom2=1):
    # 打开"邀请"
    mouseClick(hwnd_1p, 410 * zoom1, 550 * zoom1)
    delay(300)
    # 选择"好友"分页
    mouseClick(hwnd_1p, 530 * zoom1, 130 * zoom1)
    delay(1000)

    player2_result = find_pic(hwnd_1p, player2_name_path, [418, 133, 638, 448])
    print(player2_result)
    if player2_result:
        # 2P先拒绝其他邀请
        mouseClick(hwnd_2p, 610 * zoom2, 400 * zoom2)
        delay(50)
        # 1P点击"邀请"
        mouseClick(hwnd_1p, 600 * zoom1, player2_result[1] * zoom1)
        delay(1000)
        # 2P接受邀请
        mouseClick(hwnd_2p, 450 * zoom2, 400 * zoom2)
        delay(100)
        # 1P退出邀请界面
        mouseClick(hwnd_1p, 590 * zoom1, 490 * zoom1)
        delay(1000)
        return True
    return False


def roomChooseDeck(hwnd, deck_no, zoom=1):
    deck_x = [420, 500, 580, 660, 740, 820]
    deck_y = 120

    mouseClick(hwnd, deck_x[deck_no - 1] * zoom, deck_y * zoom)
    delay(1000)


# 游戏内循环检测 --------------------------------------------------------------------------------
def loopCheckStartGame(hwnd_1p, hwnd_2p=0, zoom=1):
    """循环检测进入游戏

    Args:
        hwnd_1p: type
            账号1窗口句柄
        hwnd_2p:
            账号2窗口句柄，默认为0。为0时表示单人模式，仅操作账号1的窗口
        zoom: float
            窗口缩放比例

    Returns: bool
        检测成功返回True，超过2min仍未检测到则返回False
    """
    time_sum = 0
    while True:
        delay(50)
        if find_pic(hwnd_1p, START_GAME_PATH, [0, 0, 200, 70]):
            return True
        # 交替点击准备和开始
        if (time_sum % 1500) == 0:
            mouseClick(hwnd_1p, 872 * zoom, 480 * zoom)
        elif (time_sum % 1500) == 750:
            if hwnd_2p > 0:
                mouseClick(hwnd_2p, 879 * zoom, 481 * zoom)
        # 判断结束
        time_sum += 50
        if time_sum >= 120000:
            return False


def loopCheckContinue(hwnd, max_time=15):
    return find_color_loop(hwnd, [60, 20, 80, 40], 0x3D4A4C, max_time=max_time * 60)


def loopCheckEndGame(hwnd, max_time=15):
    """循环检测是否结束游戏。
        注意：本函数检测的界面是计算得分界面，该界面刚出现 到 结算翻牌界面 刚出现，之间间隔8秒左右，
        建议调用该方法后，再delay(8200)

    Args:
        hwnd: int
            窗口句柄
        max_time: int
            最大容忍时间，超过该时间直接返回False，单位为分钟(min)

    Returns: bool
        成功检测到则返回True，超出最大容忍时间max_time仍未检测到直接返回False
    """
    # 查询是否出现结算得分界面
    if find_color_loop(hwnd, [60, 20, 80, 40], 0x6E2F0F, max_time=max_time * 60):
        # # 开始结算得分 到 开始翻牌页面 有8s左右的间隔
        # delay(8200)
        return True
    else:
        return False


def executeFlop(hwnd, flop_pos: str, zoom=1):
    card_pos = [(550, 267), (707, 267), (856, 267), (550, 469), (707, 469), (856, 469)]

    select_card = flop_pos.split(';')
    print(select_card)
    for card in select_card:
        click_pos = card_pos[int(card) - 1]
        print(click_pos)
        mouseClick(hwnd, click_pos[0] * zoom, click_pos[1] * zoom)
        delay(30)
    # 返回房间
    delay(200)
    mouseClick(hwnd, 708 * zoom, 505 * zoom)
    delay(200)
    mouseClick(hwnd, 708 * zoom, 505 * zoom)
    delay(200)


def exitRoom(hwnd, zoom=1):
    mouseClick(hwnd, 920 * zoom, 560 * zoom)
    delay(1000)


# 游戏内放卡相关 --------------------------------------------------------------------------------
def placeCard(hwnd, pos_tuple: str, zoom=1):
    # 关卡内左上角(1, 1)格子坐标
    left_top_pos = (332, 144)
    grid_width = 60
    grid_height = 64

    pos_info = pos_tuple.split(',')

    pos_x, pos_y = int(pos_info[0]), int(pos_info[1])
    place_delay = 0
    if len(pos_info) == 3:
        place_delay = int(pos_info[2])

    delay(place_delay)
    mouseClick(hwnd, (left_top_pos[0] + (pos_y - 1) * grid_width) * zoom, (left_top_pos[1] + (pos_x - 1) * grid_height) * zoom)


def loopPlaceCard(hwnd, pos_series: str, card_slot: int, card_cd: int, zoom=1):
    # 卡槽坐标列表
    card_slot_x_list = [225, 277, 330, 383, 437, 490, 542, 595, 649, 702, 754, 807, 861, 914, 914, 914, 914, 914, 914, 914, 914]
    card_slot_y_list = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 83, 151, 219, 287, 355, 423, 491]

    # 关卡内左上角(1, 1)格子坐标
    left_top_pos = (332, 144)
    grid_width = 60
    grid_height = 64

    # 所选的卡槽坐标
    card_slot_x = card_slot_x_list[card_slot - 1]
    card_slot_y = card_slot_y_list[card_slot - 1]
    # 卡片放置序列
    pos_series = pos_series.split(';')

    for pos_tuple in pos_series:
        # 延时
        if pos_tuple == '-':
            delay(card_cd)
        elif pos_tuple == '1':
            delay(1000)
        elif pos_tuple == '10':
            delay(10000)
        else:
            pos_info = pos_tuple.split(',')

            pos_x, pos_y = int(pos_info[0]), int(pos_info[1])
            if len(pos_info) == 3:
                place_delay = int(pos_info[2])
                delay(place_delay)
            else:
                delay(card_cd)

            if card_slot == 3:
                print(f"放置位置：({pos_x}, {pos_y})")
            # 取卡
            mouseClick(hwnd, card_slot_x * zoom, card_slot_y * zoom)
            # 放卡
            mouseClick(hwnd, (left_top_pos[0] + (pos_y - 1) * grid_width) * zoom, (left_top_pos[1] + (pos_x - 1) * grid_height) * zoom)
            # 放回失败的卡
            mouseClick(hwnd, 80 * zoom, 130 * zoom)


def loopPlaceCardUpgrade(hwnd, pos_series: str, card_slot: int, card_cd: int, zoom=1):
    # 卡槽坐标列表
    card_slot_x_list = [225, 277, 330, 383, 437, 490, 542, 595, 649, 702, 754, 807, 861, 914, 914, 914, 914, 914, 914, 914, 914]
    card_slot_y_list = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 83, 151, 219, 287, 355, 423, 491]

    # 关卡内左上角(1, 1)格子坐标
    left_top_pos = (332, 144)
    grid_width = 60
    grid_height = 64

    # 所选的卡槽坐标
    card_slot_x = card_slot_x_list[card_slot - 1]
    card_slot_y = card_slot_y_list[card_slot - 1]
    card_cd = int(card_cd)
    # 卡片放置序列
    pos_series = pos_series.split(';')

    for pos_tuple in pos_series:
        # 延时
        if pos_tuple == '-':
            delay(card_cd)
        elif pos_tuple == '1':
            delay(1000)
        elif pos_tuple == '10':
            delay(10000)
        else:
            pos_info = pos_tuple.split(',')

            pos_x, pos_y = int(pos_info[0]), int(pos_info[1])
            if len(pos_info) == 3:
                place_delay = int(pos_info[2])
                delay(place_delay)
            else:
                delay(card_cd)

            # 判断该卡片是否准备好了
            # 卡片数小于13：card_slot_x - 5, card_slot_x + 30
            # 卡片数小于13：card_slot_x - 29, card_slot_x + 12
            # 综上，判断范围应选择：[card_slot_x - 5, 66, card_slot_x + 12, 74]
            check_ready_range = [
                card_slot_x - 5, 66, card_slot_x + 12, 74
            ] if card_slot <= 14 else [
                card_slot_x - 29, card_slot_y + 51, card_slot_x - 26, card_slot_y + 59
            ]
            if not find_color_loop(hwnd, check_ready_range, 0xFFFFFF, max_time=420):
                return

            # 取卡
            mouseClick(hwnd, card_slot_x * zoom, card_slot_y * zoom)
            # 放卡
            mouseClick(hwnd,
                       (left_top_pos[0] + (pos_y - 1) * grid_width) * zoom,
                       (left_top_pos[1] + (pos_x - 1) * grid_height) * zoom)
            # 放回失败的卡
            mouseClick(hwnd, 80 * zoom, 130 * zoom)

            # 判断卡片是否放置成功
            delay(2)
            if find_color(hwnd, check_ready_range, 0xFFFFFF):
                # 如果还是白色，说明放置失败，重新放一次
                # 取卡
                mouseClick(hwnd, card_slot_x * zoom, card_slot_y * zoom)
                # 放卡
                mouseClick(hwnd,
                           (left_top_pos[0] + (pos_y - 1) * grid_width) * zoom,
                           (left_top_pos[1] + (pos_x - 1) * grid_height) * zoom)
                # 放回失败的卡
                mouseClick(hwnd, 80 * zoom, 130 * zoom)


def loopPlaceCardForThread(hwnd, pos_series: str, card_slot: int, card_cd: int, stop_flag: list, zoom=1):
    # 卡槽坐标列表
    card_slot_x_list = [225, 277, 330, 383, 437, 490, 542, 595, 649, 702, 754, 807, 861, 914, 914, 914, 914, 914, 914, 914, 914]
    card_slot_y_list = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 83, 151, 219, 287, 355, 423, 491]

    # 关卡内左上角(1, 1)格子坐标
    left_top_pos = (332, 144)
    grid_width = 60
    grid_height = 64

    # 所选的卡槽坐标
    card_slot_x = card_slot_x_list[card_slot - 1]
    card_slot_y = card_slot_y_list[card_slot - 1]
    # 卡片放置序列
    pos_series = pos_series.split(';')

    for pos_tuple in pos_series:
        if stop_flag[0]:
            print("结束了")
            return
        # 延时
        if pos_tuple == '-':
            delay(card_cd)
        elif pos_tuple == '1':
            delay(1000)
        elif pos_tuple == '10':
            delay(10000)
        else:
            pos_info = pos_tuple.split(',')

            pos_x, pos_y = int(pos_info[0]), int(pos_info[1])
            if len(pos_info) == 3:
                place_delay = int(pos_info[2])
                delay(place_delay)
            else:
                delay(card_cd)

            if stop_flag[0]:
                print("结束了")
                return

            if card_slot == 3:
                print(f"放置位置：({pos_x}, {pos_y})")
            # 取卡
            mouseClick(hwnd, card_slot_x * zoom, card_slot_y * zoom)
            # 放卡
            mouseClick(hwnd, (left_top_pos[0] + (pos_y - 1) * grid_width) * zoom, (left_top_pos[1] + (pos_x - 1) * grid_height) * zoom)
            # 放回失败的卡
            mouseClick(hwnd, 80 * zoom, 130 * zoom)
