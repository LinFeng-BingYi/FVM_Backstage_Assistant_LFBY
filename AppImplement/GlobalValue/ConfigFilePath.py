#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Common.FileProcess.INIProcess import INIProcessor


try:
    global_ini_procs = INIProcessor(r"userdata\AppGlobalSetting.ini")
    # 软件相关
    ROOT_PATH = global_ini_procs.getSpecificValue("path", "ROOT_DIR")
    DEFAULT_PLACING_PLAN_INI = ROOT_PATH + "\\" + global_ini_procs.getSpecificValue("path", "DEFAULT_PLACING_PLAN_INI")
    DEFAULT_DECK_INI = ROOT_PATH + "\\" + global_ini_procs.getSpecificValue("path", "DEFAULT_DECK_INI")
    DEFAULT_FUNC_FLOW_JSON = ROOT_PATH + "\\" + global_ini_procs.getSpecificValue("path", "DEFAULT_FUNC_FLOW_JSON")

    # 用户变量
    ZOOM = global_ini_procs.getSpecificValue("user_setting", "ZOOM")
except FileExistsError:
    print("未找到配置文件")
    # 软件相关
    ROOT_PATH = ""
    DEFAULT_PLACING_PLAN_INI = ""
    DEFAULT_DECK_INI = ""
    DEFAULT_FUNC_FLOW_JSON = ""

    # 用户变量
    ZOOM = "1.25"
