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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

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

        self.groupBox_select_players = QGroupBox(UnionQuestParam)
        self.groupBox_select_players.setObjectName(u"groupBox_select_players")
        self.horizontalLayout_select_players = QHBoxLayout(self.groupBox_select_players)
        self.horizontalLayout_select_players.setSpacing(5)
        self.horizontalLayout_select_players.setObjectName(u"horizontalLayout_select_players")
        self.horizontalLayout_select_players.setContentsMargins(-1, 0, -1, 5)
        self.label_select_1p = QLabel(self.groupBox_select_players)
        self.label_select_1p.setObjectName(u"label_select_1p")
        self.label_select_1p.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_select_players.addWidget(self.label_select_1p)

        self.comboBox_select_1p = QComboBox(self.groupBox_select_players)
        self.comboBox_select_1p.addItem("")
        self.comboBox_select_1p.addItem("")
        self.comboBox_select_1p.setObjectName(u"comboBox_select_1p")
        self.comboBox_select_1p.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_players.addWidget(self.comboBox_select_1p)

        self.label_select_2p = QLabel(self.groupBox_select_players)
        self.label_select_2p.setObjectName(u"label_select_2p")
        self.label_select_2p.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_select_players.addWidget(self.label_select_2p)

        self.comboBox_select_2p = QComboBox(self.groupBox_select_players)
        self.comboBox_select_2p.addItem("")
        self.comboBox_select_2p.addItem("")
        self.comboBox_select_2p.addItem("")
        self.comboBox_select_2p.setObjectName(u"comboBox_select_2p")
        self.comboBox_select_2p.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_players.addWidget(self.comboBox_select_2p)


        self.verticalLayout_top.addWidget(self.groupBox_select_players)

        self.groupBox_file_path = QGroupBox(UnionQuestParam)
        self.groupBox_file_path.setObjectName(u"groupBox_file_path")
        self.horizontalLayout_file_path = QHBoxLayout(self.groupBox_file_path)
        self.horizontalLayout_file_path.setSpacing(5)
        self.horizontalLayout_file_path.setObjectName(u"horizontalLayout_file_path")
        self.horizontalLayout_file_path.setContentsMargins(-1, 0, -1, 5)
        self.label_file_path = QLabel(self.groupBox_file_path)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setMinimumSize(QSize(80, 0))
        self.label_file_path.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_file_path.addWidget(self.label_file_path)

        self.lineEdit_file_path = QLineEdit(self.groupBox_file_path)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")
        self.lineEdit_file_path.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_file_path.addWidget(self.lineEdit_file_path)

        self.pushButton_file_path = QPushButton(self.groupBox_file_path)
        self.pushButton_file_path.setObjectName(u"pushButton_file_path")
        self.pushButton_file_path.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_file_path.addWidget(self.pushButton_file_path)


        self.verticalLayout_top.addWidget(self.groupBox_file_path)

        self.groupBox_roam_quest = QGroupBox(UnionQuestParam)
        self.groupBox_roam_quest.setObjectName(u"groupBox_roam_quest")
        self.horizontalLayout = QHBoxLayout(self.groupBox_roam_quest)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 5)
        self.label_roam_file_path = QLabel(self.groupBox_roam_quest)
        self.label_roam_file_path.setObjectName(u"label_roam_file_path")
        self.label_roam_file_path.setMinimumSize(QSize(80, 0))
        self.label_roam_file_path.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.label_roam_file_path)

        self.lineEdit_roam_file_path = QLineEdit(self.groupBox_roam_quest)
        self.lineEdit_roam_file_path.setObjectName(u"lineEdit_roam_file_path")
        self.lineEdit_roam_file_path.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.lineEdit_roam_file_path)

        self.pushButton_roam_file_path = QPushButton(self.groupBox_roam_quest)
        self.pushButton_roam_file_path.setObjectName(u"pushButton_roam_file_path")
        self.pushButton_roam_file_path.setMinimumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.pushButton_roam_file_path)

        self.label_roam_type = QLabel(self.groupBox_roam_quest)
        self.label_roam_type.setObjectName(u"label_roam_type")
        self.label_roam_type.setMinimumSize(QSize(80, 0))
        self.label_roam_type.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.label_roam_type)

        self.comboBox_roam_type = QComboBox(self.groupBox_roam_quest)
        self.comboBox_roam_type.setObjectName(u"comboBox_roam_type")
        self.comboBox_roam_type.setMinimumSize(QSize(83, 30))

        self.horizontalLayout.addWidget(self.comboBox_roam_type)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 2)

        self.verticalLayout_top.addWidget(self.groupBox_roam_quest)

        self.groupBox_select_quest = QGroupBox(UnionQuestParam)
        self.groupBox_select_quest.setObjectName(u"groupBox_select_quest")
        self.groupBox_select_quest.setMinimumSize(QSize(0, 52))
        self.horizontalLayout_select_quest = QHBoxLayout(self.groupBox_select_quest)
        self.horizontalLayout_select_quest.setSpacing(5)
        self.horizontalLayout_select_quest.setObjectName(u"horizontalLayout_select_quest")
        self.horizontalLayout_select_quest.setContentsMargins(-1, 0, -1, 5)
        self.label_quest_no = QLabel(self.groupBox_select_quest)
        self.label_quest_no.setObjectName(u"label_quest_no")
        self.label_quest_no.setMinimumSize(QSize(80, 0))
        self.label_quest_no.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_select_quest.addWidget(self.label_quest_no)

        self.lineEdit_quest_no = QLineEdit(self.groupBox_select_quest)
        self.lineEdit_quest_no.setObjectName(u"lineEdit_quest_no")
        self.lineEdit_quest_no.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_quest.addWidget(self.lineEdit_quest_no)

        self.horizontalSpacer_select_quest = QSpacerItem(252, 14, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_select_quest.addItem(self.horizontalSpacer_select_quest)


        self.verticalLayout_top.addWidget(self.groupBox_select_quest)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_top.addItem(self.verticalSpacer)

        self.verticalLayout_top.setStretch(0, 7)
        self.verticalLayout_top.setStretch(1, 2)
        self.verticalLayout_top.setStretch(2, 2)

        self.retranslateUi(UnionQuestParam)

        QMetaObject.connectSlotsByName(UnionQuestParam)
    # setupUi

    def retranslateUi(self, UnionQuestParam):
        UnionQuestParam.setWindowTitle(QCoreApplication.translate("UnionQuestParam", u"Form", None))
        self.label_dsc.setText(QCoreApplication.translate("UnionQuestParam", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u516c\u4f1a\u4efb\u52a1\u622a\u56fe\u6587\u4ef6\u7684\u540d\u79f0\u683c\u5f0f\uff1a\u7565\u3010\u8be6\u89c1\u9996\u9875\u4f7f\u7528\u6559\u7a0b\u5728\u7ebf\u6587\u6863\u3011</span></p></body></html>", None))
        self.groupBox_select_players.setTitle(QCoreApplication.translate("UnionQuestParam", u"\u9009\u62e9\u8d26\u53f7", None))
        self.label_select_1p.setText(QCoreApplication.translate("UnionQuestParam", u"\u623f\u4e3b\uff1a", None))
        self.comboBox_select_1p.setItemText(0, QCoreApplication.translate("UnionQuestParam", u"1P", None))
        self.comboBox_select_1p.setItemText(1, QCoreApplication.translate("UnionQuestParam", u"2P", None))

        self.label_select_2p.setText(QCoreApplication.translate("UnionQuestParam", u"\u623f\u5ba2\uff1a", None))
        self.comboBox_select_2p.setItemText(0, QCoreApplication.translate("UnionQuestParam", u"\u65e0", None))
        self.comboBox_select_2p.setItemText(1, QCoreApplication.translate("UnionQuestParam", u"1P", None))
        self.comboBox_select_2p.setItemText(2, QCoreApplication.translate("UnionQuestParam", u"2P", None))

        self.groupBox_file_path.setTitle(QCoreApplication.translate("UnionQuestParam", u"\u5176\u4ed6\u4efb\u52a1\u65b9\u6848", None))
        self.label_file_path.setText(QCoreApplication.translate("UnionQuestParam", u"\u653e\u5361\u65b9\u6848\u8def\u5f84\uff1a", None))
        self.pushButton_file_path.setText(QCoreApplication.translate("UnionQuestParam", u"\u6d4f\u89c8", None))
        self.groupBox_roam_quest.setTitle(QCoreApplication.translate("UnionQuestParam", u"\u6f2b\u6e38\u4efb\u52a1\u65b9\u6848", None))
        self.label_roam_file_path.setText(QCoreApplication.translate("UnionQuestParam", u"\u6f2b\u6e38\u65b9\u6848\u8def\u5f84\uff1a", None))
        self.pushButton_roam_file_path.setText(QCoreApplication.translate("UnionQuestParam", u"\u6d4f\u89c8", None))
        self.label_roam_type.setText(QCoreApplication.translate("UnionQuestParam", u"\u6f2b\u6e38\u7c7b\u578b\uff1a", None))
        self.groupBox_select_quest.setTitle(QCoreApplication.translate("UnionQuestParam", u"\u9009\u62e9\u4efb\u52a1", None))
        self.label_quest_no.setText(QCoreApplication.translate("UnionQuestParam", u"\u4efb\u52a1\u7f16\u53f7\uff1a", None))
        self.lineEdit_quest_no.setText(QCoreApplication.translate("UnionQuestParam", u"1;2;3", None))
    # retranslateUi

