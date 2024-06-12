# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SerialLevelParam.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SerialLevelParam(object):
    def setupUi(self, SerialLevelParam):
        if not SerialLevelParam.objectName():
            SerialLevelParam.setObjectName(u"SerialLevelParam")
        SerialLevelParam.resize(530, 340)
        self.verticalLayout_top = QVBoxLayout(SerialLevelParam)
        self.verticalLayout_top.setSpacing(2)
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.verticalLayout_top.setContentsMargins(3, 10, 3, 3)
        self.groupBox_select_players = QGroupBox(SerialLevelParam)
        self.groupBox_select_players.setObjectName(u"groupBox_select_players")
        self.horizontalLayout_select_player = QHBoxLayout(self.groupBox_select_players)
        self.horizontalLayout_select_player.setSpacing(5)
        self.horizontalLayout_select_player.setObjectName(u"horizontalLayout_select_player")
        self.horizontalLayout_select_player.setContentsMargins(-1, 0, -1, 5)
        self.label_select_1p = QLabel(self.groupBox_select_players)
        self.label_select_1p.setObjectName(u"label_select_1p")
        self.label_select_1p.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_select_player.addWidget(self.label_select_1p)

        self.comboBox_select_1p = QComboBox(self.groupBox_select_players)
        self.comboBox_select_1p.addItem("")
        self.comboBox_select_1p.addItem("")
        self.comboBox_select_1p.setObjectName(u"comboBox_select_1p")
        self.comboBox_select_1p.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_player.addWidget(self.comboBox_select_1p)

        self.label_select_2p = QLabel(self.groupBox_select_players)
        self.label_select_2p.setObjectName(u"label_select_2p")
        self.label_select_2p.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_select_player.addWidget(self.label_select_2p)

        self.comboBox_select_2p = QComboBox(self.groupBox_select_players)
        self.comboBox_select_2p.addItem("")
        self.comboBox_select_2p.addItem("")
        self.comboBox_select_2p.addItem("")
        self.comboBox_select_2p.setObjectName(u"comboBox_select_2p")
        self.comboBox_select_2p.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_player.addWidget(self.comboBox_select_2p)


        self.verticalLayout_top.addWidget(self.groupBox_select_players)

        self.groupBox_file_path = QGroupBox(SerialLevelParam)
        self.groupBox_file_path.setObjectName(u"groupBox_file_path")
        self.gridLayout_file_path = QGridLayout(self.groupBox_file_path)
        self.gridLayout_file_path.setSpacing(5)
        self.gridLayout_file_path.setObjectName(u"gridLayout_file_path")
        self.gridLayout_file_path.setContentsMargins(-1, 0, -1, 5)
        self.label_series_path = QLabel(self.groupBox_file_path)
        self.label_series_path.setObjectName(u"label_series_path")
        self.label_series_path.setMinimumSize(QSize(67, 0))
        self.label_series_path.setMaximumSize(QSize(67, 30))

        self.gridLayout_file_path.addWidget(self.label_series_path, 0, 0, 1, 1)

        self.lineEdit_series_path = QLineEdit(self.groupBox_file_path)
        self.lineEdit_series_path.setObjectName(u"lineEdit_series_path")
        self.lineEdit_series_path.setMinimumSize(QSize(0, 30))

        self.gridLayout_file_path.addWidget(self.lineEdit_series_path, 0, 1, 1, 1)

        self.pushButton_series_path = QPushButton(self.groupBox_file_path)
        self.pushButton_series_path.setObjectName(u"pushButton_series_path")
        self.pushButton_series_path.setMinimumSize(QSize(80, 30))
        self.pushButton_series_path.setMaximumSize(QSize(80, 30))

        self.gridLayout_file_path.addWidget(self.pushButton_series_path, 0, 2, 1, 1)

        self.label_plan_path_team = QLabel(self.groupBox_file_path)
        self.label_plan_path_team.setObjectName(u"label_plan_path_team")
        self.label_plan_path_team.setMinimumSize(QSize(67, 0))
        self.label_plan_path_team.setMaximumSize(QSize(67, 30))

        self.gridLayout_file_path.addWidget(self.label_plan_path_team, 0, 3, 1, 1)

        self.lineEdit_plan_path_team = QLineEdit(self.groupBox_file_path)
        self.lineEdit_plan_path_team.setObjectName(u"lineEdit_plan_path_team")
        self.lineEdit_plan_path_team.setMinimumSize(QSize(0, 30))

        self.gridLayout_file_path.addWidget(self.lineEdit_plan_path_team, 0, 4, 1, 1)

        self.pushButton_plan_path_team = QPushButton(self.groupBox_file_path)
        self.pushButton_plan_path_team.setObjectName(u"pushButton_plan_path_team")
        self.pushButton_plan_path_team.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_path_team.setMaximumSize(QSize(80, 30))

        self.gridLayout_file_path.addWidget(self.pushButton_plan_path_team, 0, 5, 1, 1)

        self.label_plan_path_1p = QLabel(self.groupBox_file_path)
        self.label_plan_path_1p.setObjectName(u"label_plan_path_1p")
        self.label_plan_path_1p.setMinimumSize(QSize(67, 0))
        self.label_plan_path_1p.setMaximumSize(QSize(67, 30))

        self.gridLayout_file_path.addWidget(self.label_plan_path_1p, 1, 0, 1, 1)

        self.lineEdit_plan_path_1p = QLineEdit(self.groupBox_file_path)
        self.lineEdit_plan_path_1p.setObjectName(u"lineEdit_plan_path_1p")
        self.lineEdit_plan_path_1p.setMinimumSize(QSize(0, 30))

        self.gridLayout_file_path.addWidget(self.lineEdit_plan_path_1p, 1, 1, 1, 1)

        self.pushButton_plan_path_1p = QPushButton(self.groupBox_file_path)
        self.pushButton_plan_path_1p.setObjectName(u"pushButton_plan_path_1p")
        self.pushButton_plan_path_1p.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_path_1p.setMaximumSize(QSize(80, 30))

        self.gridLayout_file_path.addWidget(self.pushButton_plan_path_1p, 1, 2, 1, 1)

        self.label_plan_path_2p = QLabel(self.groupBox_file_path)
        self.label_plan_path_2p.setObjectName(u"label_plan_path_2p")
        self.label_plan_path_2p.setMinimumSize(QSize(67, 0))
        self.label_plan_path_2p.setMaximumSize(QSize(67, 30))

        self.gridLayout_file_path.addWidget(self.label_plan_path_2p, 1, 3, 1, 1)

        self.lineEdit_plan_path_2p = QLineEdit(self.groupBox_file_path)
        self.lineEdit_plan_path_2p.setObjectName(u"lineEdit_plan_path_2p")
        self.lineEdit_plan_path_2p.setMinimumSize(QSize(0, 30))

        self.gridLayout_file_path.addWidget(self.lineEdit_plan_path_2p, 1, 4, 1, 1)

        self.pushButton_plan_path_2p = QPushButton(self.groupBox_file_path)
        self.pushButton_plan_path_2p.setObjectName(u"pushButton_plan_path_2p")
        self.pushButton_plan_path_2p.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_path_2p.setMaximumSize(QSize(80, 30))

        self.gridLayout_file_path.addWidget(self.pushButton_plan_path_2p, 1, 5, 1, 1)


        self.verticalLayout_top.addWidget(self.groupBox_file_path)

        self.groupBox_other_setting = QGroupBox(SerialLevelParam)
        self.groupBox_other_setting.setObjectName(u"groupBox_other_setting")
        self.horizontalLayout_other_setting = QHBoxLayout(self.groupBox_other_setting)
        self.horizontalLayout_other_setting.setSpacing(5)
        self.horizontalLayout_other_setting.setObjectName(u"horizontalLayout_other_setting")
        self.horizontalLayout_other_setting.setContentsMargins(-1, 0, -1, 5)
        self.label_flop_pos = QLabel(self.groupBox_other_setting)
        self.label_flop_pos.setObjectName(u"label_flop_pos")
        self.label_flop_pos.setMinimumSize(QSize(67, 0))
        self.label_flop_pos.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_other_setting.addWidget(self.label_flop_pos)

        self.lineEdit_flop_pos = QLineEdit(self.groupBox_other_setting)
        self.lineEdit_flop_pos.setObjectName(u"lineEdit_flop_pos")
        self.lineEdit_flop_pos.setMinimumSize(QSize(0, 30))
        self.lineEdit_flop_pos.setMaximumSize(QSize(178, 16777215))

        self.horizontalLayout_other_setting.addWidget(self.lineEdit_flop_pos)

        self.label_quest_panel = QLabel(self.groupBox_other_setting)
        self.label_quest_panel.setObjectName(u"label_quest_panel")
        self.label_quest_panel.setMinimumSize(QSize(67, 0))
        self.label_quest_panel.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_other_setting.addWidget(self.label_quest_panel)

        self.comboBox_quest_panel = QComboBox(self.groupBox_other_setting)
        self.comboBox_quest_panel.addItem("")
        self.comboBox_quest_panel.addItem("")
        self.comboBox_quest_panel.addItem("")
        self.comboBox_quest_panel.setObjectName(u"comboBox_quest_panel")
        self.comboBox_quest_panel.setMinimumSize(QSize(178, 30))

        self.horizontalLayout_other_setting.addWidget(self.comboBox_quest_panel)

        self.horizontalLayout_other_setting.setStretch(0, 2)
        self.horizontalLayout_other_setting.setStretch(1, 3)
        self.horizontalLayout_other_setting.setStretch(2, 2)
        self.horizontalLayout_other_setting.setStretch(3, 3)

        self.verticalLayout_top.addWidget(self.groupBox_other_setting)

        self.verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_top.addItem(self.verticalSpacer_top)

        self.verticalLayout_top.setStretch(0, 2)
        self.verticalLayout_top.setStretch(1, 4)
        self.verticalLayout_top.setStretch(2, 2)
        self.verticalLayout_top.setStretch(3, 3)

        self.retranslateUi(SerialLevelParam)

        QMetaObject.connectSlotsByName(SerialLevelParam)
    # setupUi

    def retranslateUi(self, SerialLevelParam):
        SerialLevelParam.setWindowTitle(QCoreApplication.translate("SerialLevelParam", u"Form", None))
        self.groupBox_select_players.setTitle(QCoreApplication.translate("SerialLevelParam", u"\u9009\u62e9\u8d26\u53f7", None))
        self.label_select_1p.setText(QCoreApplication.translate("SerialLevelParam", u"\u623f\u4e3b\uff1a", None))
        self.comboBox_select_1p.setItemText(0, QCoreApplication.translate("SerialLevelParam", u"1P", None))
        self.comboBox_select_1p.setItemText(1, QCoreApplication.translate("SerialLevelParam", u"2P", None))

        self.label_select_2p.setText(QCoreApplication.translate("SerialLevelParam", u"\u623f\u5ba2\uff1a", None))
        self.comboBox_select_2p.setItemText(0, QCoreApplication.translate("SerialLevelParam", u"\u65e0", None))
        self.comboBox_select_2p.setItemText(1, QCoreApplication.translate("SerialLevelParam", u"1P", None))
        self.comboBox_select_2p.setItemText(2, QCoreApplication.translate("SerialLevelParam", u"2P", None))

        self.groupBox_file_path.setTitle(QCoreApplication.translate("SerialLevelParam", u"\u6587\u4ef6\u8def\u5f84", None))
        self.label_series_path.setText(QCoreApplication.translate("SerialLevelParam", u"\u5e8f\u5217\u6587\u4ef6\uff1a", None))
        self.pushButton_series_path.setText(QCoreApplication.translate("SerialLevelParam", u"\u6d4f\u89c8", None))
        self.label_plan_path_team.setText(QCoreApplication.translate("SerialLevelParam", u"\u7ec4\u961f\u65b9\u6848\uff1a", None))
        self.pushButton_plan_path_team.setText(QCoreApplication.translate("SerialLevelParam", u"\u6d4f\u89c8", None))
        self.label_plan_path_1p.setText(QCoreApplication.translate("SerialLevelParam", u"\u623f\u4e3b\u65b9\u6848\uff1a", None))
        self.pushButton_plan_path_1p.setText(QCoreApplication.translate("SerialLevelParam", u"\u6d4f\u89c8", None))
        self.label_plan_path_2p.setText(QCoreApplication.translate("SerialLevelParam", u"\u623f\u5ba2\u65b9\u6848\uff1a", None))
        self.pushButton_plan_path_2p.setText(QCoreApplication.translate("SerialLevelParam", u"\u6d4f\u89c8", None))
        self.groupBox_other_setting.setTitle(QCoreApplication.translate("SerialLevelParam", u"\u901a\u5173\u8bbe\u7f6e", None))
        self.label_flop_pos.setText(QCoreApplication.translate("SerialLevelParam", u"\u7ffb\u724c\u4f4d\u7f6e\uff1a", None))
        self.lineEdit_flop_pos.setText(QCoreApplication.translate("SerialLevelParam", u"1;2", None))
        self.label_quest_panel.setText(QCoreApplication.translate("SerialLevelParam", u"\u4efb\u52a1\u754c\u9762\uff1a", None))
        self.comboBox_quest_panel.setItemText(0, QCoreApplication.translate("SerialLevelParam", u"\u65e0", None))
        self.comboBox_quest_panel.setItemText(1, QCoreApplication.translate("SerialLevelParam", u"\u7f8e\u98df\u5927\u8d5b", None))
        self.comboBox_quest_panel.setItemText(2, QCoreApplication.translate("SerialLevelParam", u"\u63a2\u9669\u8425\u5730", None))

    # retranslateUi

