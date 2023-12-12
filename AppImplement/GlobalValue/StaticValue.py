#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : StaticValue.py
# @Time    : 2023/11/26 22:10
# @Dsc     : 游戏中的固定值
from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH

# 地图相关 -------------------------------------------------------------------------
# 世界地图坐标
WORLD_MAP_POS = (860, 50)
WORLD_MAP_TITTLE_PATH = ROOT_PATH + "\\resources\\images\\application\\界面图标\\地图相关\\世界地图标题.bmp"
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
    "深渊岛": (356, 76)
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
    "雪顶火山": (350, 72)
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
    "十三香中心岛": (477, 97)
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

# 日常签到领奖相关 ---------------------------------------------------------------------
# VIP签到
VIP_SIGNIN_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\VIP签到.bmp"
# 进入VIP
OPEN_VIP_SIGNIN_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\进入VIP.bmp"
# 每日签到
DAILY_SIGNIN_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\每日签到.bmp"
# 进入每日签到
OPEN_DAILY_SIGNIN_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\进入每日签到.bmp"
# 每日签到按钮
DAILY_SIGNIN_BUTTON_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\每日签到按钮.bmp"
# 美食活动
FVM_ACTIVITY_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\美食活动.bmp"
# 进入美食活动
OPEN_FVM_ACTIVITY_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\进入美食活动.bmp"
# 法老宝藏
PHARAOH_TREASURE_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\法老宝藏.bmp"
# 进入法老宝藏
OPEN_PHARAOH_TREASURE_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\进入法老宝藏.bmp"
# 法老宝藏免费
PHARAOH_FREE_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\法老宝藏免费.bmp"
# 塔罗寻宝
TAROT_TREASURE_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\塔罗寻宝.bmp"
# 进入塔罗寻宝
OPEN_TAROT_TREASURE_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\进入塔罗寻宝.bmp"
# 塔罗寻宝免费
TAROT_FREE_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\塔罗寻宝免费.bmp"
# 换线，用来判断活动界面是否关闭成功
SWITCH_LINE_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\换线.bmp"
# 进入底部任务
OPEN_BOTTOM_QUEST_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\进入底部任务.bmp"
# 底部任务收起
FOLD_BOTTOM_QUEST_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\底部任务收起.bmp"
# 底部任务完成
COMPLETE_BOTTOM_QUEST_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\底部任务完成.bmp"
# 进入公会
OPEN_UNION_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\进入公会.bmp"
# 进入公会花园
OPEN_UNION_GARDEN_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\进入公会花园.bmp"
# 公会花园成长值满
UNION_GARDEN_MAX_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\公会花园成长值满.bmp"
# 公会花园待种植
UNION_GARDEN_PLANT_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\公会花园待种植.bmp"
# 进入好友
OPEN_FRIEND_PATH = ROOT_PATH + r"\resources\images\application\界面图标\日常活动领取\进入好友.bmp"

# 通关相关 -------------------------------------------------------------------------
# 创房勾选密码
CREATE_ROOM_PSW_PATH = ROOT_PATH + "\\resources\\images\\application\\界面图标\\通关相关\\创房勾选密码.bmp"
# 进入关卡
START_GAME_PATH = ROOT_PATH + "\\resources\\images\\application\\界面图标\\通关相关\\进入关卡.bmp"
