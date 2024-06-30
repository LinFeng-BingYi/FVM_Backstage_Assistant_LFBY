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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_StartParam(object):
    def setupUi(self, StartParam):
        if not StartParam.objectName():
            StartParam.setObjectName(u"StartParam")
        StartParam.resize(530, 348)
        self.verticalLayout_general = QVBoxLayout(StartParam)
        self.verticalLayout_general.setSpacing(5)
        self.verticalLayout_general.setObjectName(u"verticalLayout_general")
        self.verticalLayout_general.setContentsMargins(0, 10, 0, 0)
        self.widget_other_setting = QWidget(StartParam)
        self.widget_other_setting.setObjectName(u"widget_other_setting")
        self.widget_other_setting.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_other_setting = QHBoxLayout(self.widget_other_setting)
        self.horizontalLayout_other_setting.setObjectName(u"horizontalLayout_other_setting")
        self.horizontalLayout_other_setting.setContentsMargins(-1, 0, -1, 0)
        self.checkBox_enable_2p = QCheckBox(self.widget_other_setting)
        self.checkBox_enable_2p.setObjectName(u"checkBox_enable_2p")
        self.checkBox_enable_2p.setMinimumSize(QSize(65, 0))
        self.checkBox_enable_2p.setChecked(True)

        self.horizontalLayout_other_setting.addWidget(self.checkBox_enable_2p)

        self.label_max_check_time = QLabel(self.widget_other_setting)
        self.label_max_check_time.setObjectName(u"label_max_check_time")
        self.label_max_check_time.setMinimumSize(QSize(97, 0))
        self.label_max_check_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_other_setting.addWidget(self.label_max_check_time)

        self.lineEdit_max_check_time = QLineEdit(self.widget_other_setting)
        self.lineEdit_max_check_time.setObjectName(u"lineEdit_max_check_time")
        self.lineEdit_max_check_time.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_other_setting.addWidget(self.lineEdit_max_check_time)

        self.horizontalSpacer = QSpacerItem(330, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_other_setting.addItem(self.horizontalSpacer)

        self.horizontalLayout_other_setting.setStretch(2, 2)
        self.horizontalLayout_other_setting.setStretch(3, 7)

        self.verticalLayout_general.addWidget(self.widget_other_setting)

        self.groupBox_player_setting = QGroupBox(StartParam)
        self.groupBox_player_setting.setObjectName(u"groupBox_player_setting")
        self.gridLayout_player_setting = QGridLayout(self.groupBox_player_setting)
        self.gridLayout_player_setting.setSpacing(5)
        self.gridLayout_player_setting.setObjectName(u"gridLayout_player_setting")
        self.gridLayout_player_setting.setContentsMargins(-1, 0, -1, 5)
        self.label_1p_hwnd = QLabel(self.groupBox_player_setting)
        self.label_1p_hwnd.setObjectName(u"label_1p_hwnd")
        self.label_1p_hwnd.setMinimumSize(QSize(65, 0))
        self.label_1p_hwnd.setMaximumSize(QSize(65, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_1p_hwnd, 0, 0, 1, 1)

        self.lineEdit_1p_hwnd = QLineEdit(self.groupBox_player_setting)
        self.lineEdit_1p_hwnd.setObjectName(u"lineEdit_1p_hwnd")
        self.lineEdit_1p_hwnd.setMinimumSize(QSize(0, 30))
        self.lineEdit_1p_hwnd.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_player_setting.addWidget(self.lineEdit_1p_hwnd, 0, 1, 1, 2)

        self.pushButton_1p_hwnd = QPushButton(self.groupBox_player_setting)
        self.pushButton_1p_hwnd.setObjectName(u"pushButton_1p_hwnd")
        self.pushButton_1p_hwnd.setMinimumSize(QSize(80, 30))
        self.pushButton_1p_hwnd.setMaximumSize(QSize(45, 30))

        self.gridLayout_player_setting.addWidget(self.pushButton_1p_hwnd, 0, 3, 1, 1)

        self.label_2p_hwnd = QLabel(self.groupBox_player_setting)
        self.label_2p_hwnd.setObjectName(u"label_2p_hwnd")
        self.label_2p_hwnd.setMinimumSize(QSize(65, 0))
        self.label_2p_hwnd.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_2p_hwnd, 0, 4, 1, 1)

        self.lineEdit_2p_hwnd = QLineEdit(self.groupBox_player_setting)
        self.lineEdit_2p_hwnd.setObjectName(u"lineEdit_2p_hwnd")
        self.lineEdit_2p_hwnd.setMinimumSize(QSize(0, 30))
        self.lineEdit_2p_hwnd.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_player_setting.addWidget(self.lineEdit_2p_hwnd, 0, 5, 1, 2)

        self.pushButton_2p_hwnd = QPushButton(self.groupBox_player_setting)
        self.pushButton_2p_hwnd.setObjectName(u"pushButton_2p_hwnd")
        self.pushButton_2p_hwnd.setMinimumSize(QSize(80, 30))
        self.pushButton_2p_hwnd.setMaximumSize(QSize(80, 30))

        self.gridLayout_player_setting.addWidget(self.pushButton_2p_hwnd, 0, 7, 1, 1)

        self.label_1p_zoom = QLabel(self.groupBox_player_setting)
        self.label_1p_zoom.setObjectName(u"label_1p_zoom")
        self.label_1p_zoom.setMinimumSize(QSize(65, 0))
        self.label_1p_zoom.setMaximumSize(QSize(65, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_1p_zoom, 1, 0, 1, 1)

        self.lineEdit_1p_zoom = QLineEdit(self.groupBox_player_setting)
        self.lineEdit_1p_zoom.setObjectName(u"lineEdit_1p_zoom")
        self.lineEdit_1p_zoom.setMinimumSize(QSize(40, 30))
        self.lineEdit_1p_zoom.setMaximumSize(QSize(40, 30))

        self.gridLayout_player_setting.addWidget(self.lineEdit_1p_zoom, 1, 1, 1, 1)

        self.label_1p_2nd_psw = QLabel(self.groupBox_player_setting)
        self.label_1p_2nd_psw.setObjectName(u"label_1p_2nd_psw")
        self.label_1p_2nd_psw.setMinimumSize(QSize(52, 0))
        self.label_1p_2nd_psw.setMaximumSize(QSize(52, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_1p_2nd_psw, 1, 2, 1, 1)

        self.lineEdit_1p_2nd_psw = QLineEdit(self.groupBox_player_setting)
        self.lineEdit_1p_2nd_psw.setObjectName(u"lineEdit_1p_2nd_psw")
        self.lineEdit_1p_2nd_psw.setMinimumSize(QSize(80, 30))
        self.lineEdit_1p_2nd_psw.setMaximumSize(QSize(65, 30))

        self.gridLayout_player_setting.addWidget(self.lineEdit_1p_2nd_psw, 1, 3, 1, 1)

        self.label_2p_zoom = QLabel(self.groupBox_player_setting)
        self.label_2p_zoom.setObjectName(u"label_2p_zoom")
        self.label_2p_zoom.setMinimumSize(QSize(65, 0))
        self.label_2p_zoom.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_2p_zoom, 1, 4, 1, 1)

        self.lineEdit_2p_zoom = QLineEdit(self.groupBox_player_setting)
        self.lineEdit_2p_zoom.setObjectName(u"lineEdit_2p_zoom")
        self.lineEdit_2p_zoom.setMinimumSize(QSize(40, 30))
        self.lineEdit_2p_zoom.setMaximumSize(QSize(40, 30))

        self.gridLayout_player_setting.addWidget(self.lineEdit_2p_zoom, 1, 5, 1, 1)

        self.label_2p_2nd_psw = QLabel(self.groupBox_player_setting)
        self.label_2p_2nd_psw.setObjectName(u"label_2p_2nd_psw")
        self.label_2p_2nd_psw.setMinimumSize(QSize(52, 0))
        self.label_2p_2nd_psw.setMaximumSize(QSize(52, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_2p_2nd_psw, 1, 6, 1, 1)

        self.lineEdit_2p_2nd_psw = QLineEdit(self.groupBox_player_setting)
        self.lineEdit_2p_2nd_psw.setObjectName(u"lineEdit_2p_2nd_psw")
        self.lineEdit_2p_2nd_psw.setMinimumSize(QSize(80, 30))
        self.lineEdit_2p_2nd_psw.setMaximumSize(QSize(80, 30))

        self.gridLayout_player_setting.addWidget(self.lineEdit_2p_2nd_psw, 1, 7, 1, 1)

        self.gridLayout_player_setting.setRowStretch(0, 1)
        self.gridLayout_player_setting.setRowStretch(1, 1)
        self.gridLayout_player_setting.setColumnStretch(0, 1)
        self.gridLayout_player_setting.setColumnStretch(1, 1)
        self.gridLayout_player_setting.setColumnStretch(2, 1)
        self.gridLayout_player_setting.setColumnStretch(3, 1)
        self.gridLayout_player_setting.setColumnStretch(4, 1)
        self.gridLayout_player_setting.setColumnStretch(5, 1)
        self.gridLayout_player_setting.setColumnStretch(6, 1)
        self.gridLayout_player_setting.setColumnStretch(7, 1)

        self.verticalLayout_general.addWidget(self.groupBox_player_setting)

        self.groupBox_necessity_pic = QGroupBox(StartParam)
        self.groupBox_necessity_pic.setObjectName(u"groupBox_necessity_pic")
        self.gridLayout_necessity_pic = QGridLayout(self.groupBox_necessity_pic)
        self.gridLayout_necessity_pic.setSpacing(5)
        self.gridLayout_necessity_pic.setObjectName(u"gridLayout_necessity_pic")
        self.gridLayout_necessity_pic.setContentsMargins(-1, 0, -1, 5)
        self.label_1p_name_pic = QLabel(self.groupBox_necessity_pic)
        self.label_1p_name_pic.setObjectName(u"label_1p_name_pic")
        self.label_1p_name_pic.setMinimumSize(QSize(65, 0))
        self.label_1p_name_pic.setMaximumSize(QSize(65, 16777215))

        self.gridLayout_necessity_pic.addWidget(self.label_1p_name_pic, 0, 0, 1, 1)

        self.lineEdit_1p_name_pic = QLineEdit(self.groupBox_necessity_pic)
        self.lineEdit_1p_name_pic.setObjectName(u"lineEdit_1p_name_pic")
        self.lineEdit_1p_name_pic.setMinimumSize(QSize(0, 30))

        self.gridLayout_necessity_pic.addWidget(self.lineEdit_1p_name_pic, 0, 1, 1, 1)

        self.pushButton_1p_name_pic = QPushButton(self.groupBox_necessity_pic)
        self.pushButton_1p_name_pic.setObjectName(u"pushButton_1p_name_pic")
        self.pushButton_1p_name_pic.setMinimumSize(QSize(80, 30))
        self.pushButton_1p_name_pic.setMaximumSize(QSize(40, 30))

        self.gridLayout_necessity_pic.addWidget(self.pushButton_1p_name_pic, 0, 2, 1, 1)

        self.label_2p_name_pic = QLabel(self.groupBox_necessity_pic)
        self.label_2p_name_pic.setObjectName(u"label_2p_name_pic")
        self.label_2p_name_pic.setMinimumSize(QSize(65, 0))
        self.label_2p_name_pic.setMaximumSize(QSize(65, 16777215))

        self.gridLayout_necessity_pic.addWidget(self.label_2p_name_pic, 0, 3, 1, 1)

        self.lineEdit_2p_name_pic = QLineEdit(self.groupBox_necessity_pic)
        self.lineEdit_2p_name_pic.setObjectName(u"lineEdit_2p_name_pic")
        self.lineEdit_2p_name_pic.setMinimumSize(QSize(0, 30))

        self.gridLayout_necessity_pic.addWidget(self.lineEdit_2p_name_pic, 0, 4, 1, 1)

        self.pushButton_2p_name_pic = QPushButton(self.groupBox_necessity_pic)
        self.pushButton_2p_name_pic.setObjectName(u"pushButton_2p_name_pic")
        self.pushButton_2p_name_pic.setMinimumSize(QSize(80, 30))
        self.pushButton_2p_name_pic.setMaximumSize(QSize(40, 30))

        self.gridLayout_necessity_pic.addWidget(self.pushButton_2p_name_pic, 0, 5, 1, 1)

        self.label_1p_cross_room_pic = QLabel(self.groupBox_necessity_pic)
        self.label_1p_cross_room_pic.setObjectName(u"label_1p_cross_room_pic")
        self.label_1p_cross_room_pic.setMinimumSize(QSize(65, 0))
        self.label_1p_cross_room_pic.setMaximumSize(QSize(65, 16777215))

        self.gridLayout_necessity_pic.addWidget(self.label_1p_cross_room_pic, 1, 0, 1, 1)

        self.lineEdit_1p_cross_room_pic = QLineEdit(self.groupBox_necessity_pic)
        self.lineEdit_1p_cross_room_pic.setObjectName(u"lineEdit_1p_cross_room_pic")
        self.lineEdit_1p_cross_room_pic.setMinimumSize(QSize(0, 30))

        self.gridLayout_necessity_pic.addWidget(self.lineEdit_1p_cross_room_pic, 1, 1, 1, 1)

        self.pushButton_1p_cross_room_pic = QPushButton(self.groupBox_necessity_pic)
        self.pushButton_1p_cross_room_pic.setObjectName(u"pushButton_1p_cross_room_pic")
        self.pushButton_1p_cross_room_pic.setMinimumSize(QSize(80, 30))
        self.pushButton_1p_cross_room_pic.setMaximumSize(QSize(40, 30))

        self.gridLayout_necessity_pic.addWidget(self.pushButton_1p_cross_room_pic, 1, 2, 1, 1)

        self.label_2p_cross_room_pic = QLabel(self.groupBox_necessity_pic)
        self.label_2p_cross_room_pic.setObjectName(u"label_2p_cross_room_pic")
        self.label_2p_cross_room_pic.setMinimumSize(QSize(65, 0))
        self.label_2p_cross_room_pic.setMaximumSize(QSize(65, 16777215))

        self.gridLayout_necessity_pic.addWidget(self.label_2p_cross_room_pic, 1, 3, 1, 1)

        self.lineEdit_2p_cross_room_pic = QLineEdit(self.groupBox_necessity_pic)
        self.lineEdit_2p_cross_room_pic.setObjectName(u"lineEdit_2p_cross_room_pic")
        self.lineEdit_2p_cross_room_pic.setMinimumSize(QSize(0, 30))

        self.gridLayout_necessity_pic.addWidget(self.lineEdit_2p_cross_room_pic, 1, 4, 1, 1)

        self.pushButton_2p_cross_room_pic = QPushButton(self.groupBox_necessity_pic)
        self.pushButton_2p_cross_room_pic.setObjectName(u"pushButton_2p_cross_room_pic")
        self.pushButton_2p_cross_room_pic.setMinimumSize(QSize(80, 30))
        self.pushButton_2p_cross_room_pic.setMaximumSize(QSize(40, 30))

        self.gridLayout_necessity_pic.addWidget(self.pushButton_2p_cross_room_pic, 1, 5, 1, 1)


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

        self.verticalLayout_general.setStretch(0, 2)
        self.verticalLayout_general.setStretch(1, 5)
        self.verticalLayout_general.setStretch(2, 5)
        self.verticalLayout_general.setStretch(3, 5)

        self.retranslateUi(StartParam)

        QMetaObject.connectSlotsByName(StartParam)
    # setupUi

    def retranslateUi(self, StartParam):
        StartParam.setWindowTitle(QCoreApplication.translate("StartParam", u"Form", None))
        self.checkBox_enable_2p.setText(QCoreApplication.translate("StartParam", u"\u542f\u75282P", None))
        self.label_max_check_time.setText(QCoreApplication.translate("StartParam", u"<html><head/><body><p style='line-height:0'>\u5bf9\u5c40\u591a\u5c11\u5206\u949f\u540e</p><p>\u5224\u5b9a\u4e3a\u901a\u5173\u5f02\u5e38</p></body></html>", None))
        self.lineEdit_max_check_time.setText(QCoreApplication.translate("StartParam", u"15", None))
        self.groupBox_player_setting.setTitle(QCoreApplication.translate("StartParam", u"\u8d26\u53f7\u8bbe\u7f6e", None))
        self.label_1p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u623f\u4e3b\u53e5\u67c4\uff1a", None))
        self.lineEdit_1p_hwnd.setText(QCoreApplication.translate("StartParam", u"0", None))
        self.pushButton_1p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u83b7\u53d6", None))
        self.label_2p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u623f\u5ba2\u53e5\u67c4\uff1a", None))
        self.lineEdit_2p_hwnd.setText(QCoreApplication.translate("StartParam", u"0", None))
        self.pushButton_2p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u83b7\u53d6", None))
        self.label_1p_zoom.setText(QCoreApplication.translate("StartParam", u"\u623f\u4e3b\u7f29\u653e\uff1a", None))
        self.lineEdit_1p_zoom.setText(QCoreApplication.translate("StartParam", u"1.25", None))
        self.label_1p_2nd_psw.setText(QCoreApplication.translate("StartParam", u"\u4e8c\u7ea7\u5bc6\u7801\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_1p_2nd_psw.setToolTip(QCoreApplication.translate("StartParam", u"\u4e3a\u7a7a\u65f6\u8868\u793a\u4e0d\u89e3\u9501", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_1p_2nd_psw.setText("")
        self.lineEdit_1p_2nd_psw.setPlaceholderText(QCoreApplication.translate("StartParam", u"\u7a7a\u8868\u793a\u4e0d\u89e3\u9501", None))
        self.label_2p_zoom.setText(QCoreApplication.translate("StartParam", u"\u623f\u5ba2\u7f29\u653e\uff1a", None))
        self.lineEdit_2p_zoom.setText(QCoreApplication.translate("StartParam", u"1.25", None))
        self.label_2p_2nd_psw.setText(QCoreApplication.translate("StartParam", u"\u4e8c\u7ea7\u5bc6\u7801\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2p_2nd_psw.setToolTip(QCoreApplication.translate("StartParam", u"\u4e3a\u7a7a\u65f6\u8868\u793a\u4e0d\u89e3\u9501", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2p_2nd_psw.setPlaceholderText(QCoreApplication.translate("StartParam", u"\u7a7a\u8868\u793a\u4e0d\u89e3\u9501", None))
        self.groupBox_necessity_pic.setTitle(QCoreApplication.translate("StartParam", u"\u5fc5\u8981\u56fe\u7247", None))
        self.label_1p_name_pic.setText(QCoreApplication.translate("StartParam", u"1P\u6635\u79f0\uff1a", None))
        self.pushButton_1p_name_pic.setText(QCoreApplication.translate("StartParam", u"\u6d4f\u89c8", None))
        self.label_2p_name_pic.setText(QCoreApplication.translate("StartParam", u"2P\u6635\u79f0\uff1a", None))
        self.pushButton_2p_name_pic.setText(QCoreApplication.translate("StartParam", u"\u6d4f\u89c8", None))
        self.label_1p_cross_room_pic.setText(QCoreApplication.translate("StartParam", u"1P\u8de8\u670d\u6635\u79f0\uff1a", None))
        self.pushButton_1p_cross_room_pic.setText(QCoreApplication.translate("StartParam", u"\u6d4f\u89c8", None))
        self.label_2p_cross_room_pic.setText(QCoreApplication.translate("StartParam", u"2P\u8de8\u670d\u6635\u79f0\uff1a", None))
        self.pushButton_2p_cross_room_pic.setText(QCoreApplication.translate("StartParam", u"\u6d4f\u89c8", None))
        self.groupBox_flow_file_path.setTitle(QCoreApplication.translate("StartParam", u"\u914d\u7f6e\u6587\u4ef6\u8def\u5f84", None))
        self.label_deck_file.setText(QCoreApplication.translate("StartParam", u"\u5361\u7247\u7ec4\uff1a", None))
        self.pushButton_deck_file.setText(QCoreApplication.translate("StartParam", u"\u6d4f\u89c8", None))
        self.label_plan_file.setText(QCoreApplication.translate("StartParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_plan_file.setText(QCoreApplication.translate("StartParam", u"\u6d4f\u89c8", None))
    # retranslateUi

