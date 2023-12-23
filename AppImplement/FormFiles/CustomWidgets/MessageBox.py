#!/usr/bin/env python3

from PySide6.QtWidgets import QWidget, QPlainTextEdit, QPushButton, QVBoxLayout, QGridLayout, QHBoxLayout
from PySide6.QtCore import QSize, QMetaObject, Qt, QCoreApplication


class TipMessageBox(QWidget):
    def __init__(self, tittle, text, parent=None):
        super(TipMessageBox, self).__init__()
        self.setupUi()
        
        self.setParent(parent)
        self.setWindowTitle(tittle)
        self.plainTextEdit.setPlainText(text)

        self.pushButton_ok.clicked.connect(self.close)

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

    def setupUi(self):
        self.resize(250, 150)
        # 总widget
        self.widget_general = QWidget(self)
        self.widget_general.setObjectName(u"widget_general")
        self.widget_general.setMinimumSize(QSize(250, 150))
        
        self.plainTextEdit = QPlainTextEdit(self.widget_general)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.resize(200, 50)

        self.widget_bottom_button = QWidget(self.widget_general)
        self.widget_bottom_button.setObjectName(u"widget_bottom_button")
        
        self.pushButton_ok = QPushButton(self.widget_bottom_button)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setMinimumSize(QSize(80, 30))
        self.pushButton_ok.setMaximumSize(QSize(80, 30))

        # 布局
        self.gridLayout_top = QGridLayout(self)
        self.gridLayout_top.setSpacing(0)
        self.gridLayout_top.setObjectName(u"gridLayout_top")
        self.gridLayout_top.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_top.addWidget(self.widget_general, 0, 0, 1, 1)

        self.verticalLayout_general = QVBoxLayout(self.widget_general)
        self.verticalLayout_general.setObjectName(u"verticalLayout_general")
        self.verticalLayout_general.addWidget(self.plainTextEdit)
        self.verticalLayout_general.addWidget(self.widget_bottom_button)

        # 底部按钮
        self.horizontalLayout_bottom_button = QHBoxLayout(self.widget_bottom_button)
        self.horizontalLayout_bottom_button.setSpacing(10)
        self.horizontalLayout_bottom_button.setObjectName(u"horizontalLayout_bottom_button")
        self.horizontalLayout_bottom_button.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_bottom_button.addStretch()
        self.horizontalLayout_bottom_button.addWidget(self.pushButton_ok)
        self.horizontalLayout_bottom_button.addStretch()

        # 其他 ---------------------------------------------------------------------------------------
        self.pushButton_ok.setText(QCoreApplication.translate("UpdateINI", u"\u786E\u5B9A", None))
        QMetaObject.connectSlotsByName(self)
