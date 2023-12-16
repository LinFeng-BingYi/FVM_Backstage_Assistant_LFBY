# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UnionQuestParam.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_UnionQuestParam(object):
    def setupUi(self, UnionQuestParam):
        if not UnionQuestParam.objectName():
            UnionQuestParam.setObjectName(u"UnionQuestParam")
        UnionQuestParam.resize(530, 340)
        self.verticalLayout_top = QVBoxLayout(UnionQuestParam)
        self.verticalLayout_top.setSpacing(5)
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.verticalLayout_top.setContentsMargins(0, 5, 0, 0)
        self.widget_dsc = QWidget(UnionQuestParam)
        self.widget_dsc.setObjectName(u"widget_dsc")
        self.verticalLayout_dsc = QVBoxLayout(self.widget_dsc)
        self.verticalLayout_dsc.setSpacing(5)
        self.verticalLayout_dsc.setObjectName(u"verticalLayout_dsc")
        self.verticalLayout_dsc.setContentsMargins(-1, 0, -1, 10)
        self.label_dsc = QLabel(self.widget_dsc)
        self.label_dsc.setObjectName(u"label_dsc")
        self.label_dsc.setWordWrap(True)

        self.verticalLayout_dsc.addWidget(self.label_dsc)


        self.verticalLayout_top.addWidget(self.widget_dsc)

        self.widget_file_path = QWidget(UnionQuestParam)
        self.widget_file_path.setObjectName(u"widget_file_path")
        self.horizontalLayout_file_path = QHBoxLayout(self.widget_file_path)
        self.horizontalLayout_file_path.setSpacing(5)
        self.horizontalLayout_file_path.setObjectName(u"horizontalLayout_file_path")
        self.horizontalLayout_file_path.setContentsMargins(-1, 0, -1, 0)
        self.label_file_path = QLabel(self.widget_file_path)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_file_path.addWidget(self.label_file_path)

        self.lineEdit_file_path = QLineEdit(self.widget_file_path)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")
        self.lineEdit_file_path.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_file_path.addWidget(self.lineEdit_file_path)

        self.pushButton_file_path = QPushButton(self.widget_file_path)
        self.pushButton_file_path.setObjectName(u"pushButton_file_path")
        self.pushButton_file_path.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_file_path.addWidget(self.pushButton_file_path)


        self.verticalLayout_top.addWidget(self.widget_file_path)

        self.verticalSpacer = QSpacerItem(20, 158, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_top.addItem(self.verticalSpacer)


        self.retranslateUi(UnionQuestParam)

        QMetaObject.connectSlotsByName(UnionQuestParam)
    # setupUi

    def retranslateUi(self, UnionQuestParam):
        UnionQuestParam.setWindowTitle(QCoreApplication.translate("UnionQuestParam", u"Form", None))
        self.label_dsc.setText(QCoreApplication.translate("UnionQuestParam", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u516c\u4f1a\u4efb\u52a1\u622a\u56fe\u6587\u4ef6\u7684\u540d\u79f0\u683c\u5f0f\uff1a\u5730\u56fe\u533a\u57df-\u5173\u5361\u540d\u79f0-\u901a\u5173\u7b56\u7565</span></p><p>\u5176\u4e2d\uff1a&lt;\u5730\u56fe\u533a\u57df&gt;\u8868\u793a\u201c\u4e16\u754c\u5730\u56fe\u201d\u4e0a\u663e\u793a\u7684\u533a\u57df\u540d\u79f0\uff0c&lt;\u5173\u5361\u540d\u79f0&gt;\u8868\u793a\u5404\u5730\u56fe\u533a\u57df\u4e2d\u663e\u793a\u7684\u5173\u5361\u540d\u79f0\uff0c\u5fc5\u987b\u4e25\u683c\u5bf9\u5e94\u754c\u9762\u4e0a\u6240\u663e\u793a\u7684\u540d\u79f0\u3002\u540d\u79f0\u91cd\u590d\u7684\u5173\u5361\u52a0\u4e0a\u201c\u65e5/\u591c\u201d\u3001\u201c\u6c34/\u9646\u201d\u5355\u4e2a\u5b57\uff0c\u4e0d\u8981\u62ec\u53f7\u3002&lt;\u901a\u5173\u7b56\u7565&gt;\u586b\u5199\u201c\u65e0\u4e8c\u9636\u6bb5\u201d\u3001\u201c\u7ee7\u7eed\u6311\u6218\u201d\u3001\u201c\u9886\u53d6\u5956\u52b1\u201d\u3001\u201c\u8df3\u8fc7\u201d\u4e4b\u4e2d\u7684\u4e00\u4e2a</p><p>\u6ce8\u610f\uff1a\u901a\u5173"
                        "\u6240\u7528\u7684\u653e\u5361\u65b9\u6848\u9700\u8981\u5728\u8be5\u754c\u9762\u9009\u62e9\u7684\u653e\u5361\u65b9\u6848\u6587\u4ef6\u4e2d\u5b58\u5728\uff0c\u4e14\u5176\u540d\u79f0\u9700\u8981\u4e0e\u5173\u5361\u540d\u79f0\u4fdd\u6301\u4e00\u81f4</p></body></html>", None))
        self.label_file_path.setText(QCoreApplication.translate("UnionQuestParam", u"\u653e\u5361\u65b9\u6848\u8def\u5f84\uff1a", None))
        self.pushButton_file_path.setText(QCoreApplication.translate("UnionQuestParam", u"\u6d4f\u89c8", None))
    # retranslateUi

