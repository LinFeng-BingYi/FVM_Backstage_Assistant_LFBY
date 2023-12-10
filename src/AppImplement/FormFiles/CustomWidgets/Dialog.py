#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog, QWidget, QComboBox, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, Signal

from src.AppImplement.FormFiles.CustomWidgets.ListWidget import SUPPORT_FUNC


class AddFuncFlowDialog(QDialog):
    signal_send_func_name = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi()

        self.initWidget()
        self.bindSignal()

        # self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

    def setupUi(self):
        # 设置 自身属性
        self.setWindowTitle("添加流程")
        self.setFixedSize(250, 100)

        # 设置功能下拉框
        self.widget_func_list = QWidget(self)
        self.widget_func_list.setObjectName("widget_func_list")

        self.label_func_list = QLabel(self.widget_func_list)
        self.label_func_list.setObjectName("label_func_list")

        self.comboBox_func_list = QComboBox(self.widget_func_list)
        self.comboBox_func_list.setObjectName("comboBox_func_list")
        self.comboBox_func_list.setMinimumHeight(30)

        # 设置按钮
        self.widget_pushButton = QWidget(self)
        self.widget_pushButton.setObjectName("widget_pushButton")

        self.pushButton_ok = QPushButton(self.widget_pushButton)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_ok.setFixedSize(80, 30)

        self.pushButton_cancel = QPushButton(self.widget_pushButton)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_cancel.setFixedSize(80, 30)

        # 布局
        self.verticalLayout_top = QVBoxLayout(self)
        self.verticalLayout_top.setObjectName("verticalLayout_top")
        self.verticalLayout_top.addWidget(self.widget_func_list)
        self.verticalLayout_top.addWidget(self.widget_pushButton)
        self.verticalLayout_top.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_func_list = QHBoxLayout(self.widget_func_list)
        self.horizontalLayout_func_list.setObjectName("horizontalLayout_func_list")
        self.horizontalLayout_func_list.addWidget(self.label_func_list)
        self.horizontalLayout_func_list.addWidget(self.comboBox_func_list)
        self.horizontalLayout_func_list.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_func_list.setStretch(0, 1)
        self.horizontalLayout_func_list.setStretch(1, 3)

        self.horizontalLayout_pushButton = QHBoxLayout(self.widget_pushButton)
        self.horizontalLayout_pushButton.setObjectName("horizontalLayout_pushButton")
        self.horizontalLayout_pushButton.addStretch()
        self.horizontalLayout_pushButton.addWidget(self.pushButton_ok)
        self.horizontalLayout_pushButton.addStretch()
        self.horizontalLayout_pushButton.addWidget(self.pushButton_cancel)
        self.horizontalLayout_pushButton.addStretch()
        self.horizontalLayout_pushButton.setContentsMargins(0, 0, 0, 0)

        self.label_func_list.setText("功能名称：")
        self.pushButton_ok.setText("确定")
        self.pushButton_cancel.setText("取消")

    def initWidget(self):
        self.comboBox_func_list.clear()
        available_func = list(SUPPORT_FUNC)
        for func_name in ["开始", "结束"]:
            available_func.remove(func_name)
        self.comboBox_func_list.addItems(available_func)

    def bindSignal(self):
        self.pushButton_ok.clicked.connect(self.sendFuncName)
        self.pushButton_cancel.clicked.connect(self.close)

    def sendFuncName(self):
        self.signal_send_func_name.emit(self.comboBox_func_list.currentText())
        self.close()
