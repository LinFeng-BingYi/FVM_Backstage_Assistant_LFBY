#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QWidget, QComboBox, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QPlainTextEdit, QLineEdit
from PySide6.QtCore import Qt, Signal

from AppImplement.FormFiles.CustomWidgets.ListWidget import SUPPORT_FUNC


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


class EditCardPosDialog(QDialog):
    signal_send_card_pos_str = Signal(str)

    def __init__(self, card_pos_str, parent=None):
        super().__init__(parent)
        self.setupUi()

        self.bindSignal()

        self.plainTextEdit_card_pos.setPlainText(card_pos_str)

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

    def setupUi(self):
        # 设置 自身属性
        self.setWindowTitle("编辑位置")
        self.setMinimumSize(550, 300)

        # 编辑位置
        self.widget_card_pos = QWidget(self)
        self.widget_card_pos.setObjectName("widget_card_pos")

        self.label_card_pos = QLabel(self.widget_card_pos)
        self.label_card_pos.setObjectName("label_card_pos")

        self.plainTextEdit_card_pos = QPlainTextEdit(self.widget_card_pos)
        self.plainTextEdit_card_pos.setObjectName("plainTextEdit_card_pos")
        self.plainTextEdit_card_pos.setMinimumHeight(90)
        font_card_pos = QFont()
        font_card_pos.setBold(True)
        font_card_pos.setPointSize(12)
        font_card_pos.setFamily("Times New Roman")
        self.plainTextEdit_card_pos.setFont(font_card_pos)

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
        self.verticalLayout_top.addWidget(self.widget_card_pos)
        self.verticalLayout_top.addWidget(self.widget_pushButton)
        self.verticalLayout_top.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout_card_pos = QVBoxLayout(self.widget_card_pos)
        self.verticalLayout_card_pos.setObjectName("verticalLayout_card_pos")
        self.verticalLayout_card_pos.addWidget(self.label_card_pos)
        self.verticalLayout_card_pos.addWidget(self.plainTextEdit_card_pos)
        self.verticalLayout_card_pos.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_card_pos.setStretch(0, 1)
        self.verticalLayout_card_pos.setStretch(1, 3)

        self.horizontalLayout_pushButton = QHBoxLayout(self.widget_pushButton)
        self.horizontalLayout_pushButton.setObjectName("horizontalLayout_pushButton")
        self.horizontalLayout_pushButton.addStretch()
        self.horizontalLayout_pushButton.addWidget(self.pushButton_ok)
        self.horizontalLayout_pushButton.addStretch()
        self.horizontalLayout_pushButton.addWidget(self.pushButton_cancel)
        self.horizontalLayout_pushButton.addStretch()
        self.horizontalLayout_pushButton.setContentsMargins(0, 0, 0, 0)

        self.label_card_pos.setText("""卡片的放置位置，格式如下：
1,7,1000;2,7;-;3,7;1;4,7;10;5,7,500
每个坐标元组 (x, y, t) 以英文分号“;”分隔，元组内的三个元素以英文逗号“,”分隔。
其中x表示本次放卡坐标从上往下数第几行；y表示从左往右数第几列；t表示距离上一次放
卡后隔多少时长再放本次卡片，单位毫秒，是可选填的，不填写则默认使用输入框中的“该卡CD”。
每种卡片第一个坐标元组的t代表开局多久放置第一张卡""")
        self.pushButton_ok.setText("确定")
        self.pushButton_cancel.setText("取消")

    def bindSignal(self):
        self.pushButton_ok.clicked.connect(self.sendFuncName)
        self.pushButton_cancel.clicked.connect(self.close)

    def sendFuncName(self):
        self.signal_send_card_pos_str.emit(self.plainTextEdit_card_pos.toPlainText().replace('\n', ''))
        self.close()


class NewPlacePlanDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

        self.plan_name = ''

        self.pushButton_ok.clicked.connect(self.sendPlanName)
        self.pushButton_cancel.clicked.connect(self.close)

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

    def setupUi(self):
        # 设置 自身属性
        self.setWindowTitle("新建方案")
        self.resize(250, 150)

        # 方案名称widget
        self.widget_plan_name = QWidget(self)
        self.widget_plan_name.setObjectName(u"widget_plan_name")
        
        self.label_plan_name = QLabel(self.widget_plan_name)
        self.label_plan_name.setObjectName("label_plan_name")

        self.lineEdit_plan_name = QLineEdit(self.widget_plan_name)
        self.lineEdit_plan_name.setObjectName("lineEdit_plan_name")
        self.lineEdit_plan_name.setMinimumHeight(30)

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
        self.verticalLayout_top.addWidget(self.widget_plan_name)
        self.verticalLayout_top.addWidget(self.widget_pushButton)
        self.verticalLayout_top.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_func_list = QHBoxLayout(self.widget_plan_name)
        self.horizontalLayout_func_list.setObjectName("horizontalLayout_func_list")
        self.horizontalLayout_func_list.addWidget(self.label_plan_name)
        self.horizontalLayout_func_list.addWidget(self.lineEdit_plan_name)
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

        self.label_plan_name.setText("方案名称：")
        self.pushButton_ok.setText("确定")
        self.pushButton_cancel.setText("取消")

    def sendPlanName(self):
        self.plan_name = self.lineEdit_plan_name.text()
        self.accept()
