#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : StaticValue.py
# @Time    : 2023/11/26 22:10
# @Dsc     : 游戏中的固定值
from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH


# 软件相关
APP_WINDOW_ICON = ROOT_PATH + r"\resources\images\软件图标\icon_nobkg.ico"

# 地图相关 -------------------------------------------------------------------------
# 世界地图坐标
WORLD_MAP_POS = (860, 50)
WORLD_MAP_ZONE_POS = {
    "美味岛": (280, 270),
    "火山岛": (680, 460),
    "浮空岛": (700, 200),
    "火山遗迹": (750, 460),
    "海底漩涡": (700, 270),
    "竞技岛": (211, 391),
    "魔塔蛋糕": (318, 452),
    "勇士挑战": (493, 402),
    "跨服远征": (425, 332),
    "探险营地": (578, 338)
}

# 美味岛关卡坐标
MWD_LEVEL_POS = {
    "曲奇岛": (666, 166),
    "色拉岛陆": (706, 263),
    "色拉岛水": (720, 350),
    "慕斯岛": (669, 410),
    "香槟岛陆": (538, 470),
    "香槟岛水": (433, 432),
    "神殿": (295, 406),
    "布丁岛日": (164, 406),
    "布丁岛夜": (97, 330),
    "可可岛日": (129, 277),
    "可可岛夜": (154, 209),
    "咖喱岛日": (194, 142),
    "咖喱岛夜": (261, 125),
    "深渊岛": (356, 76),
    "美味漫游": (366, 180)
}

# 火山岛关卡坐标
HSD_LEVEL_POS = {
    "芥末小屋日": (730, 257),
    "芥末小屋夜": (652, 302),
    "薄荷海滩日": (713, 368),
    "薄荷海滩夜": (647, 413),
    "芝士城堡": (539, 419),
    "炭烧雨林日": (368, 408),
    "炭烧雨林夜": (292, 380),
    "抹茶庄园日": (231, 267),
    "抹茶庄园夜": (299, 244),
    "玛奇朵港": (473, 181),
    "棉花糖天空日": (383, 162),
    "棉花糖天空夜": (305, 156),
    "果酱部落日": (220, 137),
    "果酱部落夜": (266, 118),
    "雪顶火山": (350, 72),
    "勇士挑战": (190, 410),
    "火山漫游": (352, 235)
}

# 浮空岛关卡坐标
FKD_LEVEL_POS = {
    "茴香竹筏日": (446, 430),
    "茴香竹筏夜": (565, 424),
    "孜然断桥日": (737, 337),
    "孜然断桥夜": (644, 334),
    "卤料花园": (511, 295),
    "月桂天空日": (410, 293),
    "月桂天空夜": (332, 280),
    "香叶空港日": (262, 257),
    "香叶空港夜": (171, 223),
    "香料飞船": (97, 168),
    "花椒浮岛日": (213, 138),
    "花椒浮岛夜": (309, 177),
    "丁香彩虹日": (539, 164),
    "丁香彩虹夜": (458, 203),
    "十三香中心岛": (477, 97),
    "浮空漫游": (60, 400)
}

# 火山遗迹关卡坐标
HSYJ_LEVEL_POS = {
    "果仁瀑布": (657, 355),
    "榛子瀑布": (569, 385),
    "黑提丛林": (314, 376),
    "蓝莓丛林": (241, 371),
    "奶昔基地": (347, 128),
    "圣代基地": (444, 91)
}

# 海底漩涡关卡坐标
HDXW_LEVEL_POS = {
    "金枪鱼洋流": (171, 157),
    "珊瑚洋流日": (107, 307),
    "珊瑚洋流夜": (241, 287),
    "北极贝湍流": (402, 380),
    "海葵洋流日": (537, 354),
    "海葵洋流夜": (600, 460),
    "天妇罗漩涡": (760, 270)
}

# 竞技岛关卡坐标
JJD_LEVEL_POS = {
    "爆米花草地": (617, 268),
    "伏特加": (706, 343),
    "威士忌": (377, 335),
    "火龙果": (211, 390)
}

# 探险营地关卡坐标
TXYD_LEVEL_POS = {
    "戚风营地日": (290, 330),
    "戚风营地夜": (244, 197),
    "冰啤酒吧日": (348, 144),
    "冰啤酒吧夜": (500, 133),
    "坚果高台日": (609, 122),
    "坚果高台夜": (690, 140),
    "探险港口": (621, 369),
    "营地钥匙": (400, 444)
}

# 探险营地港口坐标
TXGK_ZONE_POS = {
    "沙漠之旅": (144, 374),
    "雪山探险": (346, 136),
    "雷城探险": (616, 341),
    "漫游奇境": (788, 188)
}

# 雪山探险关卡坐标
XSTX_LEVEL_POS = {
    "动感街区日": (280, 384),
    "动感街区夜": (325, 320),
    "蛋糕钟楼日": (223, 261),
    "蛋糕钟楼夜": (200, 180),
    "莓莓音乐节日": (300, 175),
    "莓莓音乐节夜": (387, 214),
    "雪宝棒棒冰日": (465, 129),
    "雪宝棒棒冰夜": (542, 148),
    "冰巨人雪芭日": (648, 155),
    "冰巨人雪芭夜": (700, 256),
    "艾莎星冰乐": (616, 325)
}

# 雷城探险关卡坐标
LCTX_LEVEL_POS = {
    "动感街区日": (280, 384),
    "动感街区夜": (325, 320),
    "蛋糕钟楼日": (223, 261),
    "蛋糕钟楼夜": (200, 180),
    "莓莓音乐节日": (300, 175),
    "莓莓音乐节夜": (387, 214),
    "雪宝棒棒冰日": (465, 129),
    "雪宝棒棒冰夜": (542, 148),
    "冰巨人雪芭日": (648, 155),
    "冰巨人雪芭夜": (700, 256),
    "艾莎星冰乐": (616, 325)
}

# 单层级地图
SINGLE_HIERARCHY_ZONE = {
    "美味岛": MWD_LEVEL_POS,
    "火山岛": HSD_LEVEL_POS,
    "浮空岛": FKD_LEVEL_POS,
    "火山遗迹": HSYJ_LEVEL_POS,
    "海底漩涡": HDXW_LEVEL_POS,
    "竞技岛": JJD_LEVEL_POS,
    "探险营地": TXYD_LEVEL_POS,
}

# 多层级地图
MULTI_HIERARCHY_ZONE = {
    "雪山探险": XSTX_LEVEL_POS,
    "雷城探险": LCTX_LEVEL_POS
}

# 进入区域相关 -----------------------------------------------------------------------
# 世界地图
WORLD_MAP_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\世界地图.bmp"
# 进入世界地图
OPEN_WORLD_MAP_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入世界地图.bmp"
# 进入美味岛
OPEN_MWD_ZONE_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入美味岛.bmp"
# 进入火山岛
OPEN_HSD_ZONE_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入火山岛.bmp"
# 进入浮空岛
OPEN_FKD_ZONE_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入浮空岛.bmp"
# 进入火山遗迹
OPEN_HSYJ_ZONE_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入火山遗迹.bmp"
# 进入海底漩涡
OPEN_HDXW_ZONE_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入海底漩涡.bmp"
# 进入竞技岛
OPEN_JJD_ZONE_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入竞技岛.bmp"
# 进入魔塔蛋糕
OPEN_MTDG_ZONE_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入魔塔蛋糕.bmp"
# 进入勇士挑战
OPEN_YSTZ_ZONE_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入勇士挑战.bmp"
# 进入跨服远征
OPEN_KFYZ_ZONE_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入跨服远征.bmp"
# 进入探险营地
OPEN_TXYD_ZONE_PATH = ROOT_PATH + r"\resources\images\界面图标\地图相关\进入探险营地.bmp"
# 判断是否进入区域
OPEN_ZONE_PATH_DICT = {
    "美味岛": (OPEN_MWD_ZONE_PATH, [230, 150, 320, 220]),
    "火山岛": (OPEN_HSD_ZONE_PATH, [70, 250, 140, 350]),
    "浮空岛": (OPEN_FKD_ZONE_PATH, [100, 260, 200, 370]),
    "火山遗迹": (OPEN_HSYJ_ZONE_PATH, [120, 250, 250, 320]),
    "海底漩涡": (OPEN_HDXW_ZONE_PATH, [360, 100, 440, 160]),
    "竞技岛": (OPEN_JJD_ZONE_PATH, [80, 180, 180, 280]),
    "魔塔蛋糕": (OPEN_MTDG_ZONE_PATH, [320, 10, 670, 60]),
    "勇士挑战": (OPEN_YSTZ_ZONE_PATH, [380, 20, 570, 100]),
    "跨服远征": (OPEN_KFYZ_ZONE_PATH, [380, 20, 570, 100]),
    "探险营地": (OPEN_TXYD_ZONE_PATH, [250, 100, 320, 200])
}

# 悬赏 ---------------------------------------------------------------------------
# 悬赏活动图标
WANTED_PATH = ROOT_PATH + r"\resources\images\界面图标\悬赏三连\悬赏活动图标.bmp"
# 进入悬赏活动
OPEN_WANTED_PATH = ROOT_PATH + r"\resources\images\界面图标\悬赏三连\进入悬赏活动.bmp"
# 悬赏美味挑战按钮
WANTED_MWD_GOTO_BUTTON_PATH = ROOT_PATH + r"\resources\images\界面图标\悬赏三连\悬赏美味挑战按钮.bmp"
# 悬赏火山挑战按钮
WANTED_HSD_GOTO_BUTTON_PATH = ROOT_PATH + r"\resources\images\界面图标\悬赏三连\悬赏火山挑战按钮.bmp"
# 悬赏浮空挑战按钮
WANTED_FKD_GOTO_BUTTON_PATH = ROOT_PATH + r"\resources\images\界面图标\悬赏三连\悬赏浮空挑战按钮.bmp"
# 创建三岛悬赏房间对应按钮
GOTO_BUTTON_PIC_DICT = {
    "美味岛": WANTED_MWD_GOTO_BUTTON_PATH,
    "火山岛": WANTED_HSD_GOTO_BUTTON_PATH,
    "浮空岛": WANTED_FKD_GOTO_BUTTON_PATH
}

# 通关相关 -------------------------------------------------------------------------
# 创房勾选密码
CREATE_ROOM_PSW_PATH = ROOT_PATH + r"\resources\images\界面图标\通关相关\创房勾选密码.bmp"
# 进入关卡
START_GAME_PATH = ROOT_PATH + r"\resources\images\界面图标\通关相关\进入关卡.bmp"
# 背包空间不足
BACKPACK_FULL_PATH = ROOT_PATH + r"\resources\images\界面图标\通关相关\背包空间不足.bmp"
# 邀请接受弹窗
INVITATION_ACCEPT_PATH = ROOT_PATH + r"\resources\images\界面图标\通关相关\邀请接受弹窗.bmp"
# 魔塔第三页次数耗尽
MAGIC_TOWER_TAB3_NO_RESIDUAL_PATH = ROOT_PATH + r"\resources\images\界面图标\通关相关\魔塔第三页次数耗尽.bmp"

# 主界面各种活动窗口相关 ------------------------------------------------------------------
# 顶部活动 -------------------------------------------------------------------------
# VIP签到
VIP_SIGNIN_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\VIP签到.bmp"
# 进入VIP
OPEN_VIP_SIGNIN_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入VIP.bmp"
# 每日签到
DAILY_SIGNIN_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\每日签到.bmp"
# 进入每日签到
OPEN_DAILY_SIGNIN_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入每日签到.bmp"
# 每日签到按钮
DAILY_SIGNIN_BUTTON_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\每日签到按钮.bmp"
# 美食活动
FVM_ACTIVITY_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\美食活动.bmp"
# 进入美食活动
OPEN_FVM_ACTIVITY_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入美食活动.bmp"
# 美食大赛
FOOD_CONTEST_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\美食大赛.bmp"
# 进入美食大赛
OPEN_FOOD_CONTEST_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入美食大赛.bmp"
# 法老宝藏
PHARAOH_TREASURE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\法老宝藏.bmp"
# 进入法老宝藏
OPEN_PHARAOH_TREASURE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入法老宝藏.bmp"
# 法老宝藏免费
PHARAOH_FREE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\法老宝藏免费.bmp"
# 塔罗寻宝
TAROT_TREASURE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\塔罗寻宝.bmp"
# 进入塔罗寻宝
OPEN_TAROT_TREASURE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入塔罗寻宝.bmp"
# 塔罗寻宝免费
TAROT_FREE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\塔罗寻宝免费.bmp"
# 假期特惠
HOLIDAY_DISCOUNT_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\假期特惠.bmp"
# 进入假期特惠
OPEN_HOLIDAY_DISCOUNT_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入假期特惠.bmp"
# 月卡福利
MONTHLY_CARD_WELFARE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\月卡福利.bmp"
# 进入月卡福利
OPEN_MONTHLY_CARD_WELFARE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入月卡福利.bmp"
# 欢乐假期
JOYFUL_HOLIDAY_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\欢乐假期.bmp"
# 进入欢乐假期
OPEN_JOYFUL_HOLIDAY_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入欢乐假期.bmp"
# 实验室
LABORATORY_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\实验室.bmp"
# 进入实验室
OPEN_LABORATORY_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入实验室.bmp"
# 积分商城
CREDIT_SHOPPING_MALL_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\积分商城.bmp"
# 进入积分商城
OPEN_CREDIT_SHOPPING_MALL_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入积分商城.bmp"
# 萌宠神殿
CUTE_PET_TEMPLE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\萌宠神殿.bmp"
# 进入萌宠神殿
OPEN_CUTE_PET_TEMPLE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入萌宠神殿.bmp"
# 好友列表
FRIEND_LIST_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\好友列表.bmp"
# 进入好友
OPEN_FRIEND_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\顶部菜单\进入好友.bmp"
# 顶部菜单图标以及判断是否进入顶部菜单
FIND_AND_OPEN_TOP_MENU_DICT = {
    "VIP签到": (
        VIP_SIGNIN_PATH,
        OPEN_VIP_SIGNIN_PATH,
        [392, 35, 566, 72]
    ),
    "每日签到": (
        DAILY_SIGNIN_PATH,
        OPEN_DAILY_SIGNIN_PATH,
        [387, 35, 460, 63]
    ),
    "美食活动": (
        FVM_ACTIVITY_PATH,
        OPEN_FVM_ACTIVITY_PATH,
        [394, 45, 560, 75]
    ),
    "美食大赛": (
        FOOD_CONTEST_PATH,
        OPEN_FOOD_CONTEST_PATH,
        [390, 40, 600, 150]
    ),
    "悬赏活动": (
        WANTED_PATH,
        OPEN_WANTED_PATH,
        None
    ),
    "法老宝藏": (
        PHARAOH_TREASURE_PATH,
        OPEN_PHARAOH_TREASURE_PATH,
        [337, 94, 434, 142]
    ),
    "塔罗寻宝": (
        TAROT_TREASURE_PATH,
        OPEN_TAROT_TREASURE_PATH,
        [393, 58, 477, 82]
    ),
    "假期特惠": (
        HOLIDAY_DISCOUNT_PATH,
        OPEN_HOLIDAY_DISCOUNT_PATH,
        [450, 80, 700, 120]
    ),
    "月卡福利": (
        MONTHLY_CARD_WELFARE_PATH,
        OPEN_MONTHLY_CARD_WELFARE_PATH,
        [360, 30, 560, 70]
    ),
    "欢乐假期": (
        JOYFUL_HOLIDAY_PATH,
        OPEN_JOYFUL_HOLIDAY_PATH,
        [210, 90, 320, 130]
    ),
    "实验室": (
        LABORATORY_PATH,
        OPEN_LABORATORY_PATH,
        [400, 25, 580, 50]
    ),
    "积分商城": (
        CREDIT_SHOPPING_MALL_PATH,
        OPEN_CREDIT_SHOPPING_MALL_PATH,
        [400, 30, 580, 60]
    ),
    "萌宠神殿": (
        CUTE_PET_TEMPLE_PATH,
        OPEN_CUTE_PET_TEMPLE_PATH,
        [400, 25, 580, 60]
    ),
    "好友列表": (
        FRIEND_LIST_PATH,
        OPEN_FRIEND_PATH,
        [434, 87, 543, 122]
    )
}
# 顶部子菜单坐标
TOP_SUB_MENU_POS = {
    "美食活动": {
        "美食福利": (280, 200),
        "奖品兑换": (480, 200),
        "活动日历": (680, 200)
    },
    "法老宝藏": {
        "法老商店": (710, 150),
        "连抽": (730, 500)
    },
    "塔罗寻宝": {
        "积分奖励": (210, 100),
        "连抽": (600, 470)
    },
    "假期特惠": {
        "节日兑换": (400, 170),
        "限时兑换": (490, 170),
        "长期兑换": (580, 170),
        "其他兑换": (670, 170)
    },
    "积分商城": {
        "神秘商人": (100, 150),
        "黑市商人": (800, 150)
    }
}

# 底部菜单 -------------------------------------------------------------------------
# 进入商城
OPEN_SHOPPING_MALL_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入商城.bmp"
# 进入背包
OPEN_BACKPACK_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入背包.bmp"
# 进入底部任务
OPEN_BOTTOM_QUEST_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入底部任务.bmp"
# 底部任务收起
FOLD_BOTTOM_QUEST_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\底部任务收起.bmp"
# 底部任务完成
COMPLETE_BOTTOM_QUEST_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\底部任务完成.bmp"
# 底部任务进行中
TODO_BOTTOM_QUEST_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\底部任务进行中.bmp"
# 进入合成屋
OPEN_SYNTHESIZING_HOUSE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入合成屋.bmp"
# 进入公会
OPEN_UNION_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入公会.bmp"
# 进入公会花园
OPEN_UNION_GARDEN_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入公会花园.bmp"
# 公会花园成长值满
UNION_GARDEN_MAX_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\公会花园成长值满.bmp"
# 公会花园待种植
UNION_GARDEN_PLANT_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\公会花园待种植.bmp"
# 进入公会副本
OPEN_UNION_DUNGEON_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入公会副本.bmp"
# 进入公会任务
OPEN_UNION_QUEST_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入公会任务.bmp"
# 进入情侣任务
OPEN_LOVERS_QUEST_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入情侣任务.bmp"
# 进入缘分树
OPEN_DESTINY_TREE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入缘分树.bmp"
# 进入邮件
OPEN_MAIL_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入邮件.bmp"
# 进入交易场
OPEN_TRADING_MARKET_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\底部菜单\进入交易场.bmp"
# 判断是否进入底部菜单
OPEN_BOTTOM_MENU_DICT = {
    "商城": (OPEN_SHOPPING_MALL_PATH, [374, 4, 613, 56]),
    "背包": (OPEN_BACKPACK_PATH, [33, 123, 122, 184]),
    "任务": (OPEN_BOTTOM_QUEST_PATH, [422, 41, 525, 68]),
    "合成屋": (OPEN_SYNTHESIZING_HOUSE_PATH, [23, 21, 545, 346]),
    "公会": (OPEN_UNION_PATH, [218, 95, 292, 111]),
    "公会副本": (OPEN_UNION_DUNGEON_PATH, [330, 58, 600, 105]),
    "公会任务": (OPEN_UNION_QUEST_PATH, [392, 35, 566, 72]),
    "情侣任务": (OPEN_LOVERS_QUEST_PATH, [392, 35, 566, 80]),
    "缘分树": (OPEN_DESTINY_TREE_PATH, [380, 10, 570, 80]),
    "邮件": (OPEN_MAIL_PATH, [410, 65, 540, 110]),
    "交易场": (OPEN_TRADING_MARKET_PATH, [300, 25, 670, 100])
}
# 底部菜单坐标  （每个底部菜单x坐标间隔为46）
BOTTOM_MENU_POS = {
    "商城": (550, 583),
    "背包": (596, 583),
    "任务": (642, 583),
    "合成屋": (688, 583),
    "宠物": (734, 583),
    "公会": (780, 583),
    "食神谱": (826, 583),
    "跳转": (872, 583),
    "后退": (918, 583)
}
# 底部子菜单坐标
BOTTOM_SUB_MENU_POS = {
    "背包": {
        "装备": (520, 70),
        "防御卡": (648, 70),
        "道具": (776, 70)
    },
    "合成屋": {
        "卡片制作": (110, 260),
        "卡片强化": (110, 324),
        "卡片转职": (110, 388),
        "卡片回炉": (110, 452),
        "武器开槽镶嵌": (460, 273),
        "宝石强化": (460, 355),
        "宝石分解": (460, 437)
    },
    "跳转": {
        "公会副本": (885, 224),
        "公会任务": (885, 260),
        "情侣任务": (885, 298),
        "缘分树": (885, 336),
        "竞技岛": (885, 383),
        "赛事中心": (885, 426),
        "邮件": (885, 473),
        "交易场": (885, 512)
    }
}

# 其他 ---------------------------------------------------------------------------
# 换线，用来判断活动界面是否关闭成功
SWITCH_LINE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\换线.bmp"
# 换线，用来判断是否从自动登录进入游戏
CHAT_BOX_CURRENT_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\聊天框当前.bmp"
# 常见提示框关闭按钮
COMMON_TIP_DIALOG_CLOSE_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\常见提示框关闭按钮.bmp"
# 二级密码
SECONDARY_PASSWORD_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\二级密码.bmp"
# 背包道具使用技能书时弹窗
BACKPACK_PROP_USE_SKILL_BOOK_DIALOG_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\背包道具使用技能书时弹窗.bmp"
# 魔塔蛋糕未加载完全
MAGIC_TOWER_LOADING_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\魔塔蛋糕未加载完全.bmp"
# 勇士向左翻页
WARRIOR_CHALLENGE_TURN_LEFT_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\勇士向左翻页.bmp"
# 勇士向右翻页
WARRIOR_CHALLENGE_TURN_RIGHT_PATH = ROOT_PATH + r"\resources\images\界面图标\各种界面元素\勇士向右翻页.bmp"

# 自动登录 -------------------------------------------------------------------------
AUTO_LOGIN_USERNAME_BOX = ROOT_PATH + r"\resources\images\界面图标\自动登录相关\用户名输入框.bmp"
AUTO_LOGIN_ENTER_SERVER_BTN = ROOT_PATH + r"\resources\images\界面图标\自动登录相关\进入服务器按钮.bmp"
AUTO_LOGIN_3366_LAST_SERVER = ROOT_PATH + r"\resources\images\界面图标\自动登录相关\空间3366最近区服.bmp"
