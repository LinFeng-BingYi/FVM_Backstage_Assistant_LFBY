#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : Foundation.py
# @Time    : 2023/11/26 22:03
# @Dsc     : 基础操作
from AppImplement.Business.CustomException import BusinessError
from Common.Backstage import *
from AppImplement.GlobalValue.StaticValue import *

from math import floor


# 选择 对应地图 对应关卡 ---------------------------------------------------------------------------
def switchLine(hwnd, line_no, zoom=1):
    """世界地图下方换线功能

    Args:
        line_no: int
            从1开始计数
    """
    # 点击”换线“
    mouseClick(hwnd, 820 * zoom, 85 * zoom)
    delay(500)
    # 点击分区
    # 一区纵坐标82，每个区间隔25
    mouseClick(hwnd, 782 * zoom, (82 + 25 * (line_no - 1)) * zoom)
    delay(2000)


def switchWorldZone(hwnd: int, zone_name, zoom=1):
    """在世界地图中切换地区，地区名必须与世界地图中显示的保持一致
    """
    if not find_pic(hwnd, WORLD_MAP_PATH, [788, 3, 945, 90], record_fail=True, record_name="未找到世界地图"):
        raise BusinessError("未找到世界地图！")
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
    if not find_pic_loop(hwnd, OPEN_WORLD_MAP_PATH, [340, 20, 650, 160], max_time=120):
        raise BusinessError("超过2min还未打开世界地图！")
    delay(500)
    # 点击对应的地图
    mouseClick(hwnd, WORLD_MAP_ZONE_POS[zone_name][0] * zoom, WORLD_MAP_ZONE_POS[zone_name][1] * zoom)
    if not find_pic_loop(hwnd, OPEN_ZONE_PATH_DICT[zone_name][0], OPEN_ZONE_PATH_DICT[zone_name][1], max_time=120):
        raise BusinessError(f"超过2min还未进入区域[{zone_name}]！")
    delay(800)
    if zone_name in need_switch_server:
        switchLine(hwnd, need_switch_server[zone_name], zoom=zoom)
    elif zone_name == "跨服远征":
        # 打开跨服分区列表
        mouseClick(hwnd, 765 * zoom, 30 * zoom)
        delay(500)
        # 点击“跨服三区”
        mouseClick(hwnd, 765 * zoom, 110 * zoom)
        delay(500)


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
    delay(2000)
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


def check2ndPsw(hwnd, psw='', zoom=1):
    """处理二级密码框

    Args:
        hwnd: int
        psw: str
            账号的二级密码。默认为空，表示不解释二级密码
        zoom: float

    Returns:
        未出现密码框时，返回None; 成功解锁时，返回True; 不解锁或解锁失败时，返回False
    """
    if find_pic(hwnd, SECONDARY_PASSWORD_PATH, [360, 170, 510, 220]):
        if psw == '':
            # 为空时不解锁，直接关闭弹窗并返回False
            mouseClick(hwnd, 570 * zoom, 200 * zoom)
            delay(500)
            return False
        else:
            # 点击输入框
            mouseClick(hwnd, 440 * zoom, 300 * zoom)
            delay(300)
            # 输入密码
            keyInputStr(hwnd, psw)
            # 点击“完成”
            mouseClick(hwnd, 440 * zoom, 390 * zoom)
            delay(300)
            # 若密码错误，则关闭弹窗并返回False; 成功解锁，返回True
            if find_pic(hwnd, SECONDARY_PASSWORD_PATH, [360, 170, 510, 220]):
                mouseClick(hwnd, 570 * zoom, 200 * zoom)
                delay(500)
                return False
            else:
                return True
    # 未出现二级密码框，则返回None
    return None


def checkEnterRoom(hwnd):
    if not find_pic_loop(hwnd, ENTER_ROOM_PATH, [375, 20, 430, 50], max_time=10):
        raise BusinessError(f"超过10s还未进入房间！")
    delay(500)


def checkLoginTimeout(hwnd):
    if find_pic(hwnd, LOGIN_TIMEOUT_PATH, [350, 250, 600, 350]):
        return True
    elif find_pic(hwnd, LOGIN_TIMEOUT2_PATH, [350, 250, 600, 350]):
        return True
    return False


def checkFoodContestQuestFinish(hwnd):
    if find_pic_loop(hwnd, FOOD_CONTEST_QUEST_FINISH_TIP_PATH, [380, 320, 580, 420], max_time=1, internal=0):
        print("检测到触发美食大赛任务完成")
        delay(5000)


def openMagicTowerDialog(hwnd, tab_num, open_dialog=True, zoom=1):
    switchWorldZone(hwnd, "美味岛", zoom=zoom)
    if open_dialog:
        switchWorldZone(hwnd, "魔塔蛋糕", zoom)
        # 等待魔塔加载完毕
        while find_pic(hwnd, MAGIC_TOWER_LOADING_PATH, [5, 80, 220, 160]):
            delay(300)
        # 选择tab页
        mouseClick(hwnd, (45 + 73 * tab_num) * zoom, 70 * zoom)
        delay(500)


def chooseMagicTowerLevel(hwnd, level_num: int, zoom=1):
    """在已打开魔塔界面的情况下，根据魔塔层数 level_num 选择对应的魔塔关卡，并创建进入房间"""
    if level_num >= 0:
        right_num = floor((level_num - 1) / 15)
        down_to_up_num = (level_num - 1) % 15 + 1
        # 点击跳转到第一页
        mouseClick(hwnd, 46 * zoom, 576 * zoom)
        delay(100)
        # 向右翻页，跳转到目标页
        for i in range(right_num):
            mouseClick(hwnd, 149 * zoom, 576 * zoom)
            delay(100)
        # 选择层数
        mouseClick(hwnd, 113 * zoom, (542 - 30 * (down_to_up_num - 1)) * zoom)
        delay(500)
    else:
        # 选择关卡
        mouseClick(hwnd, 60 * zoom, (140 + 95 * (-1 * level_num - 1)) * zoom)
        delay(500)
    # 点击”开始挑战“
    mouseClick(hwnd, 588 * zoom, 560 * zoom)
    delay(500)
    # checkEnterRoom(hwnd)


def chooseCrossServiceLevel(hwnd, level_type: str, level_num: str, zoom=1):
    """在已打开跨服界面的情况下，选择跨服关卡

    Args:
        hwnd: int
            ...
        level_type: str
            关卡类型
        level_num: str
            关卡难度，表示关卡星级(8星到15星)
        zoom: float
            ...

    Returns:
        ...
        example:
        ...
    """
    level_num_dict = {
        "8星": 1, "9星": 2, "10星": 3, "11星": 4, "12星": 5, "13星": 6, "14星": 7, "15星": 8
    }
    level_num = level_num_dict[level_num]
    level_type_no = CROSS_SERVER_LEVEL_TYPE_NO[level_type]
    # 点击”创建房间“
    mouseClick(hwnd, 850 * zoom, 550 * zoom)
    delay(500)
    # 选择关卡类型
    mouseClick(hwnd, (60 + 100 * level_type_no) * zoom, 70 * zoom)
    delay(500)
    # 启用对应难度序号的密码框: 第一个密码坐标位置是(123, 244)，左右两个相隔226，上下两个相隔220
    mouseClick(hwnd, (123 + ((level_num - 1) % 4) * 226) * zoom, (244 + floor((level_num - 1) / 4) * 220) * zoom)
    delay(500)
    # 点击密码框
    mouseClick(hwnd, (123 + ((level_num - 1) % 4) * 226 + 80) * zoom, (244 + floor((level_num - 1) / 4) * 220) * zoom)
    delay(500)
    # 输入密码
    keyPress(hwnd, "0", times=2)
    # 点击”创建“
    mouseClick(hwnd, (123 + ((level_num - 1) % 4) * 226 + 50) * zoom, (244 + floor((level_num - 1) / 4) * 220 + 40) * zoom)
    checkEnterRoom(hwnd)


def searchAndEnter1pRoom(hwnd, player1_room_name_pic_path, level_type, zoom=1):
    level_type_no = CROSS_SERVER_LEVEL_TYPE_NO[level_type]
    # 打开右上角关卡类型下拉框
    mouseClick(hwnd, 620 * zoom, 80 * zoom)
    delay(500)
    # 选择关卡类型
    mouseClick(hwnd, 630 * zoom, (135 + 25 * level_type_no) * zoom)
    delay(1000)
    # 找1P房间
    result_1p_room = find_pic(hwnd, player1_room_name_pic_path, [400, 100, 925, 470])
    search_limit = 15       # 查找时，最大翻页次数，超过后则查找失败
    while not result_1p_room:
        # 点击“下一页”
        mouseClick(hwnd, 699 * zoom, 488 * zoom)
        delay(500)
        if search_limit <= 0:
            return False
        search_limit -= 1
        result_1p_room = find_pic(hwnd, player1_room_name_pic_path, [400, 100, 925, 470])
    # 点击房间
    mouseClick(hwnd, result_1p_room[0] * zoom, result_1p_room[1] * zoom)
    delay(500)
    # 点击密码框
    mouseClick(hwnd, 480 * zoom, 300 * zoom)
    delay(500)
    # 输入密码
    keyPress(hwnd, "0", times=2)
    # 点击“确认”
    mouseClick(hwnd, 490 * zoom, 360 * zoom)
    checkEnterRoom(hwnd)


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
    checkEnterRoom(hwnd)


def teamInvite(hwnd_1p, hwnd_2p, player2_name_path, zoom1=1, zoom2=1):
    # 打开"邀请"
    mouseClick(hwnd_1p, 410 * zoom1, 550 * zoom1)
    delay(300)
    # 选择"好友"分页
    mouseClick(hwnd_1p, 530 * zoom1, 130 * zoom1)
    delay(1000)

    player2_result = find_pic(hwnd_1p, player2_name_path, [418, 133, 638, 448])
    # print(player2_result)
    if player2_result:
        # 2P先拒绝其他邀请
        acceptInvitationOrNot(hwnd_2p, False, zoom2)
        # 1P点击"邀请"
        mouseClick(hwnd_1p, 600 * zoom1, player2_result[1] * zoom1)
        delay(1000)
        # 2P接受邀请
        acceptInvitationOrNot(hwnd_2p, True, zoom2)
        # 1P退出邀请界面
        mouseClick(hwnd_1p, 590 * zoom1, 490 * zoom1)
        try:
            checkEnterRoom(hwnd_2p)
        except BusinessError:
            return False
        return True
    # 1P退出邀请界面
    mouseClick(hwnd_1p, 590 * zoom1, 490 * zoom1)
    return False


def acceptInvitationOrNot(hwnd, accept: bool, zoom=1):
    # 查找邀请接受弹窗
    if find_pic(hwnd, INVITATION_ACCEPT_PATH, [500, 200, 560, 250]):
        click_x_pos = 450 if accept else 610
        mouseClick(hwnd, click_x_pos * zoom, 405 * zoom)
        delay(80)


def roomChooseDeck(hwnd, deck_no, zoom=1):
    deck_x = [420, 500, 580, 660, 740, 820]
    deck_y = 120

    mouseClick(hwnd, deck_x[deck_no - 1] * zoom, deck_y * zoom)
    delay(1000)


# 游戏内循环检测 --------------------------------------------------------------------------------
def loopCheckStartGame(hwnd_1p, hwnd_2p=0, zoom1=1, zoom2=1):
    """循环检测进入游戏

    Args:
        hwnd_1p: type
            账号1窗口句柄
        hwnd_2p:
            账号2窗口句柄，默认为0。为0时表示单人模式，仅操作账号1的窗口
        zoom1: float
            窗口缩放比例
        zoom2: float
            窗口缩放比例

    Returns: bool
        检测成功返回True，超过2min仍未检测到则返回False
    """
    time_sum = 0
    while True:
        delay(500)
        if find_pic(hwnd_1p, START_GAME_PATH, [0, 0, 200, 70]):
            return True
        # 交替点击准备和开始
        if (time_sum % 1000) == 500:
            mouseClick(hwnd_1p, 872 * zoom1, 480 * zoom1)
            delay(100)
            if find_pic(hwnd_1p, BACKPACK_FULL_PATH, [345, 205, 615, 395]):
                mouseClick(hwnd_1p, 430 * zoom1, 350 * zoom1)
            elif find_pic(hwnd_1p, WITHOUT_SPECIFIC_CARD_PATH, [345, 205, 615, 395]):
                mouseClick(hwnd_1p, 430 * zoom1, 350 * zoom1)
        elif (time_sum % 1000) == 0:
            if hwnd_2p > 0:
                mouseClick(hwnd_2p, 879 * zoom2, 481 * zoom2)
                delay(100)
                if find_pic(hwnd_2p, BACKPACK_FULL_PATH, [345, 205, 615, 395]):
                    mouseClick(hwnd_2p, 430 * zoom2, 350 * zoom2)
                elif find_pic(hwnd_2p, WITHOUT_SPECIFIC_CARD_PATH, [345, 205, 615, 395]):
                    mouseClick(hwnd_2p, 430 * zoom2, 350 * zoom2)
        # 判断结束
        time_sum += 500
        if time_sum >= 120000:
            return False


def loopCheckContinue(hwnd, max_time=15):
    start_time = time()
    while True:
        if find_color(hwnd, [60, 20, 80, 40], 0x3D4A4C):
            return 1
        if find_pic(hwnd, END_GAME_PATH, [420, 45, 530, 80]):
            return 2
        sleep(1)
        if (time() - start_time) >= max_time * 60:
            return 0


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
    if find_pic_loop(hwnd, END_GAME_PATH, [420, 45, 550, 120], max_time=max_time * 60, internal=2):
        # # 开始结算得分 到 开始翻牌页面 有8s左右的间隔
        # delay(8200)
        return True
    else:
        return False


def loopCheckFlipChest(hwnd, max_time=0.5):
    """循环检测翻宝箱界面

    Args:
        hwnd: int
            窗口句柄
        max_time: int
            最大容忍时间，超过该时间直接返回False，单位为分钟(min)

    Returns: bool
        成功检测到则返回True，超出最大容忍时间max_time仍未检测到直接返回False
    """
    # 查询是否出现翻宝箱界面
    if find_pic_loop(hwnd, FLIP_CHEST_PATH, [430, 40, 520, 70], max_time=max_time * 60):
        return True
    else:
        return False


def executeFlop(hwnd, flop_pos: str, zoom=1):
    if find_color(hwnd, [650, 500, 650, 500], 0xC57A32):
        mouseClick(hwnd, 708 * zoom, 498 * zoom)
        delay(200)
        return False
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
    mouseClick(hwnd, 708 * zoom, 498 * zoom)
    delay(200)
    mouseClick(hwnd, 708 * zoom, 498 * zoom)
    delay(200)
    return True


def exitGame(hwnd, zoom=1):
    mouseClick(hwnd, 925 * zoom, 580 * zoom)
    delay(300)
    if not find_pic(hwnd, EXIT_GAME_TIP_PATH, [370, 200, 460, 270]):
        mouseClick(hwnd, 925 * zoom, 580 * zoom)
        delay(300)
    mouseClick(hwnd, 450 * zoom, 385 * zoom)
    delay(300)


def exitRoom(hwnd, zoom=1):
    if find_pic(hwnd, ENTER_ROOM_PATH, [375, 20, 430, 50]):
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

            # 取卡
            mouseClick(hwnd, card_slot_x * zoom, card_slot_y * zoom)
            # 放卡
            mouseClick(hwnd, (left_top_pos[0] + (pos_y - 1) * grid_width) * zoom, (left_top_pos[1] + (pos_x - 1) * grid_height) * zoom)
            # 放回失败的卡
            mouseClick(hwnd, 80 * zoom, 130 * zoom)


# 游戏主界面公共操作 ------------------------------------------------------------------------------
def openBottomMenu(hwnd, menu_name: str, sub_menu_name='', zoom=1):
    """打开底部菜单，支持背包、合成屋、跳转的子菜单
    """
    # 点击主界面底部菜单
    menu_pos = BOTTOM_MENU_POS[menu_name]
    mouseClick(hwnd, menu_pos[0] * zoom, menu_pos[1] * zoom)
    delay(500)

    # 获取对应的“打开xx界面”图片路径与识图范围
    final_dialog_name = menu_name
    if menu_name == "跳转":
        final_dialog_name = sub_menu_name
        # 如果所选底部菜单是“跳转”，则还需再点击一次
        sub_menu_pos = BOTTOM_SUB_MENU_POS[menu_name][sub_menu_name]
        mouseClick(hwnd, sub_menu_pos[0] * zoom, sub_menu_pos[1] * zoom)
        delay(500)
        
    # 若最终打开的界面存在于该dict，则需要识图判断是否成功打开
    if final_dialog_name in OPEN_BOTTOM_MENU_DICT:
        open_menu_pic_info = OPEN_BOTTOM_MENU_DICT[final_dialog_name]
        # 判断是否成功打开界面
        if not find_pic_loop(hwnd, open_menu_pic_info[0], open_menu_pic_info[1], max_time=120):
            raise BusinessError(f"超过2min还未打开{final_dialog_name}界面！")
        delay(1000)
    
    if menu_name != "跳转" and menu_name in BOTTOM_SUB_MENU_POS:
        # 如果所选底部菜单不是“跳转”，且还有子菜单（背包、合成屋），则还需再点击一次
        sub_menu_pos = BOTTOM_SUB_MENU_POS[menu_name][sub_menu_name]
        mouseClick(hwnd, sub_menu_pos[0] * zoom, sub_menu_pos[1] * zoom)
        delay(500)


def openTopMenu(hwnd, menu_name: str, sub_menu_name='', zoom=1):
    """打开顶部菜单，支持美食活动、法老宝藏、塔罗寻宝、假期特惠、积分商城的子菜单
    """
    # 寻找顶部菜单
    menu_pic = FIND_AND_OPEN_TOP_MENU_DICT[menu_name][0]
    open_menu_pic = FIND_AND_OPEN_TOP_MENU_DICT[menu_name][1]
    open_menu_range = FIND_AND_OPEN_TOP_MENU_DICT[menu_name][2]
    if menu_name == '好友列表':
        menu_pos = find_pic(hwnd, menu_pic, [0, 75, 250, 150])
    else:
        menu_pos = find_pic(hwnd, menu_pic, [245, 0, 780, 120])
        if not menu_pos:
            # 若没找到，则点击切换上方活动按钮
            mouseClick(hwnd, 785 * zoom, 30 * zoom)
            delay(500)
            menu_pos = find_pic(hwnd, menu_pic, [245, 0, 780, 120])
    # 没找到则返回False
    if not menu_pos:
        return False
    # 点击图标
    mouseClick(hwnd, menu_pos[0] * zoom, menu_pos[1] * zoom)
    # 等待界面加载完成
    if not find_pic_loop(hwnd, open_menu_pic, open_menu_range, max_time=120):
        raise BusinessError(f"超过2min还未打开{menu_name}界面！")
    delay(1000)

    # 处理某些特殊界面
    if menu_name == "假期特惠":
        # 点击“兑换特惠”
        mouseClick(hwnd, 300 * zoom, 350 * zoom)
        delay(300)
    elif menu_name == "欢乐假期":
        # 点击“立即挑战”
        mouseClick(hwnd, 655 * zoom, 200 * zoom)
        delay(300)

    # 如果还有子菜单，则还需再点击一次
    if menu_name in TOP_SUB_MENU_POS:
        sub_menu_pos = TOP_SUB_MENU_POS[menu_name][sub_menu_name]
        mouseClick(hwnd, sub_menu_pos[0] * zoom, sub_menu_pos[1] * zoom)
        delay(500)

        # 处理特殊界面
        if menu_name == "假期特惠":
            for jump_times in range(30):
                mouseClick(hwnd, 640 * zoom, 480 * zoom)
                delay(50)

    return True
