# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MagicTowerParam.ui'
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

class Ui_MagicTowerParam(object):
    def setupUi(self, MagicTowerParam):
        if not MagicTowerParam.objectName():
            MagicTowerParam.setObjectName(u"MagicTowerParam")
        MagicTowerParam.resize(530, 340)
        self.verticalLayout = QVBoxLayout(MagicTowerParam)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 10, 3, 3)
        self.groupBox_select_level = QGroupBox(MagicTowerParam)
        self.groupBox_select_level.setObjectName(u"groupBox_select_level")
        self.groupBox_select_level.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_select_level = QHBoxLayout(self.groupBox_select_level)
        self.horizontalLayout_select_level.setSpacing(5)
        self.horizontalLayout_select_level.setObjectName(u"horizontalLayout_select_level")
        self.horizontalLayout_select_level.setContentsMargins(9, 0, -1, 5)
        self.label_level_num = QLabel(self.groupBox_select_level)
        self.label_level_num.setObjectName(u"label_level_num")
        self.label_level_num.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_select_level.addWidget(self.label_level_num)

        self.lineEdit_level_num = QLineEdit(self.groupBox_select_level)
        self.lineEdit_level_num.setObjectName(u"lineEdit_level_num")
        self.lineEdit_level_num.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_level.addWidget(self.lineEdit_level_num)

        self.horizontalSpacer = QSpacerItem(85, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_select_level.addItem(self.horizontalSpacer)

        self.horizontalLayout_select_level.setStretch(0, 1)
        self.horizontalLayout_select_level.setStretch(1, 2)

        self.verticalLayout.addWidget(self.groupBox_select_level)

        self.groupBox_1p_deck = QGroupBox(MagicTowerParam)
        self.groupBox_1p_deck.setObjectName(u"groupBox_1p_deck")
        self.groupBox_1p_deck.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_1p_deck = QHBoxLayout(self.groupBox_1p_deck)
        self.horizontalLayout_1p_deck.setSpacing(5)
        self.horizontalLayout_1p_deck.setObjectName(u"horizontalLayout_1p_deck")
        self.horizontalLayout_1p_deck.setContentsMargins(-1, 0, -1, 5)
        self.label_1p_plan = QLabel(self.groupBox_1p_deck)
        self.label_1p_plan.setObjectName(u"label_1p_plan")
        self.label_1p_plan.setMaximumSize(QSize(67, 30))

        self.horizontalLayout_1p_deck.addWidget(self.label_1p_plan)

        self.comboBox_1p_plan = QComboBox(self.groupBox_1p_deck)
        self.comboBox_1p_plan.setObjectName(u"comboBox_1p_plan")
        self.comboBox_1p_plan.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_1p_deck.addWidget(self.comboBox_1p_plan)

        self.pushButton_view_plan = QPushButton(self.groupBox_1p_deck)
        self.pushButton_view_plan.setObjectName(u"pushButton_view_plan")
        self.pushButton_view_plan.setMinimumSize(QSize(80, 30))
        self.pushButton_view_plan.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_1p_deck.addWidget(self.pushButton_view_plan)

        self.horizontalLayout_1p_deck.setStretch(0, 1)
        self.horizontalLayout_1p_deck.setStretch(1, 2)

        self.verticalLayout.addWidget(self.groupBox_1p_deck)

        self.groupBox_level_setting = QGroupBox(MagicTowerParam)
        self.groupBox_level_setting.setObjectName(u"groupBox_level_setting")
        self.groupBox_level_setting.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout = QHBoxLayout(self.groupBox_level_setting)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 5)
        self.label_loop_count = QLabel(self.groupBox_level_setting)
        self.label_loop_count.setObjectName(u"label_loop_count")

        self.horizontalLayout.addWidget(self.label_loop_count)

        self.lineEdit_loop_count = QLineEdit(self.groupBox_level_setting)
        self.lineEdit_loop_count.setObjectName(u"lineEdit_loop_count")
        self.lineEdit_loop_count.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.lineEdit_loop_count)

        self.label_flop_pos = QLabel(self.groupBox_level_setting)
        self.label_flop_pos.setObjectName(u"label_flop_pos")

        self.horizontalLayout.addWidget(self.label_flop_pos)

        self.lineEdit_flop_pos = QLineEdit(self.groupBox_level_setting)
        self.lineEdit_flop_pos.setObjectName(u"lineEdit_flop_pos")
        self.lineEdit_flop_pos.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.lineEdit_flop_pos)


        self.verticalLayout.addWidget(self.groupBox_level_setting)

        self.verticalSpacer = QSpacerItem(20, 135, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)

        self.retranslateUi(MagicTowerParam)

        QMetaObject.connectSlotsByName(MagicTowerParam)
    # setupUi

    def retranslateUi(self, MagicTowerParam):
        MagicTowerParam.setWindowTitle(QCoreApplication.translate("MagicTowerParam", u"Form", None))
        self.groupBox_select_level.setTitle(QCoreApplication.translate("MagicTowerParam", u"\u9009\u62e9\u5173\u5361", None))
        self.label_level_num.setText(QCoreApplication.translate("MagicTowerParam", u"\u5c42\u6570\uff1a", None))
        self.lineEdit_level_num.setText(QCoreApplication.translate("MagicTowerParam", u"99", None))
        self.groupBox_1p_deck.setTitle(QCoreApplication.translate("MagicTowerParam", u"\u4fe1\u606f\u914d\u7f6e", None))
        self.label_1p_plan.setText(QCoreApplication.translate("MagicTowerParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_view_plan.setText(QCoreApplication.translate("MagicTowerParam", u"\u67e5\u770b\u65b9\u6848", None))
        self.groupBox_level_setting.setTitle(QCoreApplication.translate("MagicTowerParam", u"\u901a\u5173\u8bbe\u7f6e", None))
        self.label_loop_count.setText(QCoreApplication.translate("MagicTowerParam", u"\u5faa\u73af\u6b21\u6570\uff1a", None))
        self.lineEdit_loop_count.setText(QCoreApplication.translate("MagicTowerParam", u"5", None))
        self.label_flop_pos.setText(QCoreApplication.translate("MagicTowerParam", u"\u7ffb\u724c\u4f4d\u7f6e\uff1a", None))
        self.lineEdit_flop_pos.setText(QCoreApplication.translate("MagicTowerParam", u"1;2;3;4;5;6", None))
    # retranslateUi

