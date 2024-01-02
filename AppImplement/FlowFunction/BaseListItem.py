#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : BaseListItem.py
# @Time    : 2023/12/4 22:48
# @Dsc     : 实现可加入流程列表的item基类

from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import QFont

from abc import abstractmethod


class BaseListWidget(QWidget):

    def __init__(self, func_name, parent=None):
        super().__init__(parent)
        self.setupUi()

        # 状态：挂起(军蓝)、等待、执行、完成、禁用、错误
        self.status_color_dict = {"hanging": "color: #5F9EA0",
                                  "waiting": "color: green;",
                                  "executing": "color: blue;",
                                  "completed": "color: yellow;",
                                  "banned": "color: gray;",
                                  "wrong": "color: red;"}
        # 初始为挂起状态
        self.status = "hanging"

        # item关联的widget，用于在右侧“功能参数配置”tab页展示
        self.func_widget = BaseParamWidget()

        # 初始化
        self.changeStatus(self.status)
        self.label_function_name.setText(func_name)

    def setupUi(self):
        # 整个widget的设置
        self.setMaximumHeight(30)
        # 状态
        self.label_status = QLabel(self)
        self.label_status.setObjectName("label_status")
        self.label_status.setFixedSize(30, 30)
        self.label_status.setText("●")
        font_status = QFont()
        font_status.setBold(True)
        font_status.setPointSize(25)
        self.label_status.setFont(font_status)
        # 功能名称
        self.label_function_name = QLabel(self)
        self.label_function_name.setObjectName("label_function_name")
        self.label_function_name.setMinimumHeight(30)
        font_func_name = QFont()
        font_func_name.setBold(True)
        font_func_name.setPointSize(15)
        self.label_function_name.setFont(font_func_name)
        # 拖拽图标
        self.label_drag = QLabel(self)
        self.label_drag.setObjectName("label_drag")
        self.label_drag.setFixedSize(30, 30)
        self.label_drag.setText("=")
        font_drag = QFont()
        font_drag.setFamily("等线")
        font_drag.setPointSize(25)
        self.label_drag.setFont(font_drag)
        self.label_drag.setStyleSheet("color: orange")

        # 布局
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 0, 2)
        self.horizontalLayout.addWidget(self.label_status)
        self.horizontalLayout.addWidget(self.label_function_name)
        self.horizontalLayout.addWidget(self.label_drag)

    def changeStatus(self, status):
        """改变该控件的状态

        Args:
            status: str
                改变的状态, 取值范围为 ["hanging", "waiting", "executing", "completed", "banned", "wrong"]
                分别表示：挂起、等待、执行、完成、禁用、错误
        """
        if status not in self.status_color_dict:
            raise ValueError
        self.status = status
        self.label_status.setStyleSheet(self.status_color_dict[self.status])

    def getFuncName(self):
        return self.label_function_name.text()

    def getStatus(self):
        return self.status

    def getFuncWidget(self):
        return self.func_widget

    @abstractmethod
    def getFuncParam(self, get_for_json=False):
        """获取属性 self.func_widget 的界面参数
        """
        pass

    def setFuncParam(self, param_dict):
        self.func_widget.setAllParam(param_dict)

    # @abstractmethod
    # def executeFunc(self):
    #     """执行该功能
    #     """
    #     pass


class BaseParamWidget(QWidget):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def getAllParam(self, get_for_json=False):
        pass

    @abstractmethod
    def setAllParam(self, param_dict):
        pass

    @abstractmethod
    def checkInputValidity(self):
        pass
