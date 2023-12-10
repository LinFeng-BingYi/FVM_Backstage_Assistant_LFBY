# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartParam.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_StartParam(object):
    def setupUi(self, StartParam):
        if not StartParam.objectName():
            StartParam.setObjectName(u"StartParam")
        StartParam.resize(523, 364)
        self.verticalLayout_general = QVBoxLayout(StartParam)
        self.verticalLayout_general.setSpacing(10)
        self.verticalLayout_general.setObjectName(u"verticalLayout_general")
        self.verticalLayout_general.setContentsMargins(0, 10, 0, 0)
        self.label_dsc = QLabel(StartParam)
        self.label_dsc.setObjectName(u"label_dsc")
        self.label_dsc.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_general.addWidget(self.label_dsc)

        self.groupBox_player_hwnd = QGroupBox(StartParam)
        self.groupBox_player_hwnd.setObjectName(u"groupBox_player_hwnd")
        self.groupBox_player_hwnd.setMaximumSize(QSize(16777215, 60))
        self.groupBox_player_hwnd.setFlat(False)
        self.horizontalLayout_player_hwnd = QHBoxLayout(self.groupBox_player_hwnd)
        self.horizontalLayout_player_hwnd.setSpacing(5)
        self.horizontalLayout_player_hwnd.setObjectName(u"horizontalLayout_player_hwnd")
        self.horizontalLayout_player_hwnd.setContentsMargins(9, 0, 9, 5)
        self.label_1p_hwnd = QLabel(self.groupBox_player_hwnd)
        self.label_1p_hwnd.setObjectName(u"label_1p_hwnd")
        self.label_1p_hwnd.setMinimumSize(QSize(65, 0))
        self.label_1p_hwnd.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_player_hwnd.addWidget(self.label_1p_hwnd)

        self.lineEdit_1p_hwnd = QLineEdit(self.groupBox_player_hwnd)
        self.lineEdit_1p_hwnd.setObjectName(u"lineEdit_1p_hwnd")
        self.lineEdit_1p_hwnd.setMinimumSize(QSize(0, 30))
        self.lineEdit_1p_hwnd.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_player_hwnd.addWidget(self.lineEdit_1p_hwnd)

        self.pushButton_1p_hwnd = QPushButton(self.groupBox_player_hwnd)
        self.pushButton_1p_hwnd.setObjectName(u"pushButton_1p_hwnd")
        self.pushButton_1p_hwnd.setMinimumSize(QSize(80, 30))
        self.pushButton_1p_hwnd.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_player_hwnd.addWidget(self.pushButton_1p_hwnd)

        self.label_2p_hwnd = QLabel(self.groupBox_player_hwnd)
        self.label_2p_hwnd.setObjectName(u"label_2p_hwnd")
        self.label_2p_hwnd.setMinimumSize(QSize(65, 0))
        self.label_2p_hwnd.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_player_hwnd.addWidget(self.label_2p_hwnd)

        self.lineEdit_2p_hwnd = QLineEdit(self.groupBox_player_hwnd)
        self.lineEdit_2p_hwnd.setObjectName(u"lineEdit_2p_hwnd")
        self.lineEdit_2p_hwnd.setMinimumSize(QSize(0, 30))
        self.lineEdit_2p_hwnd.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_player_hwnd.addWidget(self.lineEdit_2p_hwnd)

        self.pushButton_2p_hwnd = QPushButton(self.groupBox_player_hwnd)
        self.pushButton_2p_hwnd.setObjectName(u"pushButton_2p_hwnd")
        self.pushButton_2p_hwnd.setMinimumSize(QSize(80, 30))
        self.pushButton_2p_hwnd.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_player_hwnd.addWidget(self.pushButton_2p_hwnd)


        self.verticalLayout_general.addWidget(self.groupBox_player_hwnd)

        self.groupBox_necessity_pic = QGroupBox(StartParam)
        self.groupBox_necessity_pic.setObjectName(u"groupBox_necessity_pic")
        self.groupBox_necessity_pic.setMinimumSize(QSize(0, 50))
        self.groupBox_necessity_pic.setMaximumSize(QSize(16777215, 60))
        self.groupBox_necessity_pic.setFlat(False)
        self.horizontalLayout_necessity_pic = QHBoxLayout(self.groupBox_necessity_pic)
        self.horizontalLayout_necessity_pic.setSpacing(5)
        self.horizontalLayout_necessity_pic.setObjectName(u"horizontalLayout_necessity_pic")
        self.horizontalLayout_necessity_pic.setContentsMargins(9, 0, 9, 5)
        self.label_2p_name_pic = QLabel(self.groupBox_necessity_pic)
        self.label_2p_name_pic.setObjectName(u"label_2p_name_pic")
        self.label_2p_name_pic.setMinimumSize(QSize(65, 0))
        self.label_2p_name_pic.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_necessity_pic.addWidget(self.label_2p_name_pic)

        self.lineEdit_2p_name_pic = QLineEdit(self.groupBox_necessity_pic)
        self.lineEdit_2p_name_pic.setObjectName(u"lineEdit_2p_name_pic")
        self.lineEdit_2p_name_pic.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_necessity_pic.addWidget(self.lineEdit_2p_name_pic)

        self.pushButton_2p_name_pic = QPushButton(self.groupBox_necessity_pic)
        self.pushButton_2p_name_pic.setObjectName(u"pushButton_2p_name_pic")
        self.pushButton_2p_name_pic.setMinimumSize(QSize(80, 30))
        self.pushButton_2p_name_pic.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_necessity_pic.addWidget(self.pushButton_2p_name_pic)


        self.verticalLayout_general.addWidget(self.groupBox_necessity_pic)

        self.groupBox_flow_file_path = QGroupBox(StartParam)
        self.groupBox_flow_file_path.setObjectName(u"groupBox_flow_file_path")
        self.groupBox_flow_file_path.setMinimumSize(QSize(0, 90))
        self.gridLayout_flow_file_path = QGridLayout(self.groupBox_flow_file_path)
        self.gridLayout_flow_file_path.setSpacing(5)
        self.gridLayout_flow_file_path.setObjectName(u"gridLayout_flow_file_path")
        self.gridLayout_flow_file_path.setContentsMargins(-1, 0, -1, 0)
        self.label_deck_file = QLabel(self.groupBox_flow_file_path)
        self.label_deck_file.setObjectName(u"label_deck_file")
        self.label_deck_file.setMinimumSize(QSize(65, 0))

        self.gridLayout_flow_file_path.addWidget(self.label_deck_file, 0, 0, 1, 1)

        self.lineEdit_deck_file = QLineEdit(self.groupBox_flow_file_path)
        self.lineEdit_deck_file.setObjectName(u"lineEdit_deck_file")
        self.lineEdit_deck_file.setMinimumSize(QSize(0, 30))

        self.gridLayout_flow_file_path.addWidget(self.lineEdit_deck_file, 0, 1, 1, 1)

        self.pushButton_deck_file = QPushButton(self.groupBox_flow_file_path)
        self.pushButton_deck_file.setObjectName(u"pushButton_deck_file")
        self.pushButton_deck_file.setMinimumSize(QSize(80, 30))
        self.pushButton_deck_file.setMaximumSize(QSize(40, 30))

        self.gridLayout_flow_file_path.addWidget(self.pushButton_deck_file, 0, 2, 1, 1)

        self.label_plan_file = QLabel(self.groupBox_flow_file_path)
        self.label_plan_file.setObjectName(u"label_plan_file")
        self.label_plan_file.setMinimumSize(QSize(65, 0))

        self.gridLayout_flow_file_path.addWidget(self.label_plan_file, 1, 0, 1, 1)

        self.lineEdit_plan_file = QLineEdit(self.groupBox_flow_file_path)
        self.lineEdit_plan_file.setObjectName(u"lineEdit_plan_file")
        self.lineEdit_plan_file.setMinimumSize(QSize(0, 30))

        self.gridLayout_flow_file_path.addWidget(self.lineEdit_plan_file, 1, 1, 1, 1)

        self.pushButton_plan_file = QPushButton(self.groupBox_flow_file_path)
        self.pushButton_plan_file.setObjectName(u"pushButton_plan_file")
        self.pushButton_plan_file.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_file.setMaximumSize(QSize(40, 30))

        self.gridLayout_flow_file_path.addWidget(self.pushButton_plan_file, 1, 2, 1, 1)


        self.verticalLayout_general.addWidget(self.groupBox_flow_file_path)

        self.widget_other_setting = QWidget(StartParam)
        self.widget_other_setting.setObjectName(u"widget_other_setting")
        self.widget_other_setting.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_other_setting = QHBoxLayout(self.widget_other_setting)
        self.horizontalLayout_other_setting.setObjectName(u"horizontalLayout_other_setting")
        self.horizontalLayout_other_setting.setContentsMargins(-1, 0, -1, 0)
        self.label_max_check_time = QLabel(self.widget_other_setting)
        self.label_max_check_time.setObjectName(u"label_max_check_time")
        self.label_max_check_time.setMinimumSize(QSize(65, 0))
        self.label_max_check_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_other_setting.addWidget(self.label_max_check_time)

        self.lineEdit_max_check_time = QLineEdit(self.widget_other_setting)
        self.lineEdit_max_check_time.setObjectName(u"lineEdit_max_check_time")
        self.lineEdit_max_check_time.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_other_setting.addWidget(self.lineEdit_max_check_time)

        self.horizontalSpacer = QSpacerItem(330, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_other_setting.addItem(self.horizontalSpacer)

        self.horizontalLayout_other_setting.setStretch(1, 2)
        self.horizontalLayout_other_setting.setStretch(2, 7)

        self.verticalLayout_general.addWidget(self.widget_other_setting)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_general.addItem(self.verticalSpacer_bottom)


        self.retranslateUi(StartParam)

        QMetaObject.connectSlotsByName(StartParam)
    # setupUi

    def retranslateUi(self, StartParam):
        StartParam.setWindowTitle(QCoreApplication.translate("StartParam", u"Form", None))
        self.label_dsc.setText(QCoreApplication.translate("StartParam", u"  \u8bbe\u7f6e\u6574\u4e2a\u6d41\u7a0b\u4e2d\u6240\u9700\u7684\u5168\u5c40\u4fe1\u606f", None))
        self.groupBox_player_hwnd.setTitle(QCoreApplication.translate("StartParam", u"\u8d26\u53f7\u53e5\u67c4", None))
        self.label_1p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u623f\u4e3b\u53e5\u67c4\uff1a", None))
        self.lineEdit_1p_hwnd.setText(QCoreApplication.translate("StartParam", u"0", None))
        self.pushButton_1p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u83b7\u53d6", None))
        self.label_2p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u623f\u5ba2\u53e5\u67c4\uff1a", None))
        self.lineEdit_2p_hwnd.setText(QCoreApplication.translate("StartParam", u"0", None))
        self.pushButton_2p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u83b7\u53d6", None))
        self.groupBox_necessity_pic.setTitle(QCoreApplication.translate("StartParam", u"\u5fc5\u8981\u56fe\u7247", None))
        self.label_2p_name_pic.setText(QCoreApplication.translate("StartParam", u"2P\u6635\u79f0\uff1a", None))
        self.pushButton_2p_name_pic.setText(QCoreApplication.translate("StartParam", u"\u6d4f\u89c8", None))
        self.groupBox_flow_file_path.setTitle(QCoreApplication.translate("StartParam", u"\u914d\u7f6e\u6587\u4ef6\u8def\u5f84", None))
        self.label_deck_file.setText(QCoreApplication.translate("StartParam", u"\u5361\u7247\u7ec4\uff1a", None))
        self.pushButton_deck_file.setText(QCoreApplication.translate("StartParam", u"\u6d4f\u89c8", None))
        self.label_plan_file.setText(QCoreApplication.translate("StartParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_plan_file.setText(QCoreApplication.translate("StartParam", u"\u6d4f\u89c8", None))
        self.label_max_check_time.setText(QCoreApplication.translate("StartParam", u"<html><head/><body><p style='line-height:0'>\u591a\u4e45\u63d0\u9192\u5bf9</p><p>\u5c40\u65f6\u95f4\u8fc7\u957f</p></body></html>", None))
        self.lineEdit_max_check_time.setText(QCoreApplication.translate("StartParam", u"15", None))
    # retranslateUi

