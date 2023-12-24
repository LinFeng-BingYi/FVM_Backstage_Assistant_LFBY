# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VolcanicRelicParam.ui'
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

class Ui_VolcanicRelicParam(object):
    def setupUi(self, VolcanicRelicParam):
        if not VolcanicRelicParam.objectName():
            VolcanicRelicParam.setObjectName(u"VolcanicRelicParam")
        VolcanicRelicParam.resize(530, 340)
        self.verticalLayout_top = QVBoxLayout(VolcanicRelicParam)
        self.verticalLayout_top.setSpacing(5)
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.verticalLayout_top.setContentsMargins(3, 10, 3, 3)
        self.groupBox_select_players = QGroupBox(VolcanicRelicParam)
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

        self.groupBox_select_level = QGroupBox(VolcanicRelicParam)
        self.groupBox_select_level.setObjectName(u"groupBox_select_level")
        self.groupBox_select_level.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_select_level = QHBoxLayout(self.groupBox_select_level)
        self.horizontalLayout_select_level.setSpacing(5)
        self.horizontalLayout_select_level.setObjectName(u"horizontalLayout_select_level")
        self.horizontalLayout_select_level.setContentsMargins(9, 0, -1, 5)
        self.label_level = QLabel(self.groupBox_select_level)
        self.label_level.setObjectName(u"label_level")
        self.label_level.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_select_level.addWidget(self.label_level)

        self.comboBox_level = QComboBox(self.groupBox_select_level)
        self.comboBox_level.addItem("")
        self.comboBox_level.addItem("")
        self.comboBox_level.addItem("")
        self.comboBox_level.addItem("")
        self.comboBox_level.addItem("")
        self.comboBox_level.addItem("")
        self.comboBox_level.setObjectName(u"comboBox_level")
        self.comboBox_level.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_level.addWidget(self.comboBox_level)

        self.horizontalSpacer = QSpacerItem(85, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_select_level.addItem(self.horizontalSpacer)

        self.horizontalLayout_select_level.setStretch(0, 1)
        self.horizontalLayout_select_level.setStretch(1, 2)

        self.verticalLayout_top.addWidget(self.groupBox_select_level)

        self.groupBox_select_plan = QGroupBox(VolcanicRelicParam)
        self.groupBox_select_plan.setObjectName(u"groupBox_select_plan")
        self.gridLayout_select_plan = QGridLayout(self.groupBox_select_plan)
        self.gridLayout_select_plan.setSpacing(5)
        self.gridLayout_select_plan.setObjectName(u"gridLayout_select_plan")
        self.gridLayout_select_plan.setContentsMargins(-1, 0, -1, 5)
        self.label_plan_path = QLabel(self.groupBox_select_plan)
        self.label_plan_path.setObjectName(u"label_plan_path")
        self.label_plan_path.setMinimumSize(QSize(67, 0))
        self.label_plan_path.setMaximumSize(QSize(67, 30))

        self.gridLayout_select_plan.addWidget(self.label_plan_path, 0, 0, 1, 1)

        self.lineEdit_plan_path = QLineEdit(self.groupBox_select_plan)
        self.lineEdit_plan_path.setObjectName(u"lineEdit_plan_path")
        self.lineEdit_plan_path.setMinimumSize(QSize(0, 30))

        self.gridLayout_select_plan.addWidget(self.lineEdit_plan_path, 0, 1, 1, 1)

        self.pushButton_plan_path = QPushButton(self.groupBox_select_plan)
        self.pushButton_plan_path.setObjectName(u"pushButton_plan_path")
        self.pushButton_plan_path.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_path.setMaximumSize(QSize(80, 30))

        self.gridLayout_select_plan.addWidget(self.pushButton_plan_path, 0, 2, 1, 1)

        self.label_1p_plan = QLabel(self.groupBox_select_plan)
        self.label_1p_plan.setObjectName(u"label_1p_plan")
        self.label_1p_plan.setMaximumSize(QSize(67, 30))

        self.gridLayout_select_plan.addWidget(self.label_1p_plan, 1, 0, 1, 1)

        self.comboBox_1p_plan = QComboBox(self.groupBox_select_plan)
        self.comboBox_1p_plan.setObjectName(u"comboBox_1p_plan")
        self.comboBox_1p_plan.setMinimumSize(QSize(0, 30))

        self.gridLayout_select_plan.addWidget(self.comboBox_1p_plan, 1, 1, 1, 1)

        self.pushButton_view_plan = QPushButton(self.groupBox_select_plan)
        self.pushButton_view_plan.setObjectName(u"pushButton_view_plan")
        self.pushButton_view_plan.setMinimumSize(QSize(80, 30))
        self.pushButton_view_plan.setMaximumSize(QSize(80, 30))

        self.gridLayout_select_plan.addWidget(self.pushButton_view_plan, 1, 2, 1, 1)


        self.verticalLayout_top.addWidget(self.groupBox_select_plan)

        self.groupBox_level_setting = QGroupBox(VolcanicRelicParam)
        self.groupBox_level_setting.setObjectName(u"groupBox_level_setting")
        self.groupBox_level_setting.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout = QHBoxLayout(self.groupBox_level_setting)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 5)
        self.label_loop_count = QLabel(self.groupBox_level_setting)
        self.label_loop_count.setObjectName(u"label_loop_count")
        self.label_loop_count.setMinimumSize(QSize(67, 0))

        self.horizontalLayout.addWidget(self.label_loop_count)

        self.lineEdit_loop_count = QLineEdit(self.groupBox_level_setting)
        self.lineEdit_loop_count.setObjectName(u"lineEdit_loop_count")
        self.lineEdit_loop_count.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.lineEdit_loop_count)

        self.label_flop_pos = QLabel(self.groupBox_level_setting)
        self.label_flop_pos.setObjectName(u"label_flop_pos")
        self.label_flop_pos.setMinimumSize(QSize(67, 0))

        self.horizontalLayout.addWidget(self.label_flop_pos)

        self.lineEdit_flop_pos = QLineEdit(self.groupBox_level_setting)
        self.lineEdit_flop_pos.setObjectName(u"lineEdit_flop_pos")
        self.lineEdit_flop_pos.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.lineEdit_flop_pos)


        self.verticalLayout_top.addWidget(self.groupBox_level_setting)

        self.verticalSpacer = QSpacerItem(20, 135, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_top.addItem(self.verticalSpacer)


        self.retranslateUi(VolcanicRelicParam)

        self.comboBox_level.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(VolcanicRelicParam)
    # setupUi

    def retranslateUi(self, VolcanicRelicParam):
        VolcanicRelicParam.setWindowTitle(QCoreApplication.translate("VolcanicRelicParam", u"Form", None))
        self.groupBox_select_players.setTitle(QCoreApplication.translate("VolcanicRelicParam", u"\u9009\u62e9\u8d26\u53f7", None))
        self.label_select_1p.setText(QCoreApplication.translate("VolcanicRelicParam", u"\u623f\u4e3b\uff1a", None))
        self.comboBox_select_1p.setItemText(0, QCoreApplication.translate("VolcanicRelicParam", u"1P", None))
        self.comboBox_select_1p.setItemText(1, QCoreApplication.translate("VolcanicRelicParam", u"2P", None))

        self.label_select_2p.setText(QCoreApplication.translate("VolcanicRelicParam", u"\u623f\u5ba2\uff1a", None))
        self.comboBox_select_2p.setItemText(0, QCoreApplication.translate("VolcanicRelicParam", u"\u65e0", None))
        self.comboBox_select_2p.setItemText(1, QCoreApplication.translate("VolcanicRelicParam", u"1P", None))
        self.comboBox_select_2p.setItemText(2, QCoreApplication.translate("VolcanicRelicParam", u"2P", None))

        self.groupBox_select_level.setTitle(QCoreApplication.translate("VolcanicRelicParam", u"\u9009\u62e9\u5173\u5361", None))
        self.label_level.setText(QCoreApplication.translate("VolcanicRelicParam", u"\u5173\u5361\uff1a", None))
        self.comboBox_level.setItemText(0, QCoreApplication.translate("VolcanicRelicParam", u"\u679c\u4ec1\u7011\u5e03", None))
        self.comboBox_level.setItemText(1, QCoreApplication.translate("VolcanicRelicParam", u"\u699b\u5b50\u7011\u5e03", None))
        self.comboBox_level.setItemText(2, QCoreApplication.translate("VolcanicRelicParam", u"\u84dd\u8393\u4e1b\u6797", None))
        self.comboBox_level.setItemText(3, QCoreApplication.translate("VolcanicRelicParam", u"\u9ed1\u63d0\u4e1b\u6797", None))
        self.comboBox_level.setItemText(4, QCoreApplication.translate("VolcanicRelicParam", u"\u5976\u6614\u57fa\u5730", None))
        self.comboBox_level.setItemText(5, QCoreApplication.translate("VolcanicRelicParam", u"\u5723\u4ee3\u57fa\u5730", None))

        self.groupBox_select_plan.setTitle(QCoreApplication.translate("VolcanicRelicParam", u"\u9009\u62e9\u65b9\u6848", None))
        self.label_plan_path.setText(QCoreApplication.translate("VolcanicRelicParam", u"\u65b9\u6848\u8def\u5f84\uff1a", None))
        self.pushButton_plan_path.setText(QCoreApplication.translate("VolcanicRelicParam", u"\u6d4f\u89c8", None))
        self.label_1p_plan.setText(QCoreApplication.translate("VolcanicRelicParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_view_plan.setText(QCoreApplication.translate("VolcanicRelicParam", u"\u67e5\u770b\u65b9\u6848", None))
        self.groupBox_level_setting.setTitle(QCoreApplication.translate("VolcanicRelicParam", u"\u901a\u5173\u8bbe\u7f6e", None))
        self.label_loop_count.setText(QCoreApplication.translate("VolcanicRelicParam", u"\u5faa\u73af\u6b21\u6570\uff1a", None))
        self.lineEdit_loop_count.setText(QCoreApplication.translate("VolcanicRelicParam", u"5", None))
        self.label_flop_pos.setText(QCoreApplication.translate("VolcanicRelicParam", u"\u7ffb\u724c\u4f4d\u7f6e\uff1a", None))
        self.lineEdit_flop_pos.setText(QCoreApplication.translate("VolcanicRelicParam", u"1;2;3;4", None))
    # retranslateUi

