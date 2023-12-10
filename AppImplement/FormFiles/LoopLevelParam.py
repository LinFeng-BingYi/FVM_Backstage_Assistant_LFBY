# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoopLevelParam.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_LoopLevelParam(object):
    def setupUi(self, LoopLevelParam):
        if not LoopLevelParam.objectName():
            LoopLevelParam.setObjectName(u"LoopLevelParam")
        LoopLevelParam.resize(496, 360)
        self.verticalLayout_top = QVBoxLayout(LoopLevelParam)
        self.verticalLayout_top.setSpacing(0)
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.verticalLayout_top.setContentsMargins(3, 10, 3, 3)
        self.groupBox_select_level = QGroupBox(LoopLevelParam)
        self.groupBox_select_level.setObjectName(u"groupBox_select_level")
        self.groupBox_select_level.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_select_level = QHBoxLayout(self.groupBox_select_level)
        self.horizontalLayout_select_level.setSpacing(5)
        self.horizontalLayout_select_level.setObjectName(u"horizontalLayout_select_level")
        self.horizontalLayout_select_level.setContentsMargins(9, 0, -1, 5)
        self.label_zone = QLabel(self.groupBox_select_level)
        self.label_zone.setObjectName(u"label_zone")
        self.label_zone.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_select_level.addWidget(self.label_zone)

        self.comboBox_zone = QComboBox(self.groupBox_select_level)
        self.comboBox_zone.setObjectName(u"comboBox_zone")
        self.comboBox_zone.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_level.addWidget(self.comboBox_zone)

        self.label_level = QLabel(self.groupBox_select_level)
        self.label_level.setObjectName(u"label_level")
        self.label_level.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_select_level.addWidget(self.label_level)

        self.comboBox_level = QComboBox(self.groupBox_select_level)
        self.comboBox_level.setObjectName(u"comboBox_level")
        self.comboBox_level.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_level.addWidget(self.comboBox_level)

        self.horizontalLayout_select_level.setStretch(0, 1)
        self.horizontalLayout_select_level.setStretch(1, 2)
        self.horizontalLayout_select_level.setStretch(2, 1)
        self.horizontalLayout_select_level.setStretch(3, 2)

        self.verticalLayout_top.addWidget(self.groupBox_select_level)

        self.groupBox_1p_deck = QGroupBox(LoopLevelParam)
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

        self.verticalLayout_top.addWidget(self.groupBox_1p_deck)

        self.groupBox_level_setting = QGroupBox(LoopLevelParam)
        self.groupBox_level_setting.setObjectName(u"groupBox_level_setting")
        self.groupBox_level_setting.setMaximumSize(QSize(16777215, 90))
        self.gridLayout_level_setting = QGridLayout(self.groupBox_level_setting)
        self.gridLayout_level_setting.setSpacing(5)
        self.gridLayout_level_setting.setObjectName(u"gridLayout_level_setting")
        self.gridLayout_level_setting.setContentsMargins(-1, 0, -1, 5)
        self.label_loop_count = QLabel(self.groupBox_level_setting)
        self.label_loop_count.setObjectName(u"label_loop_count")

        self.gridLayout_level_setting.addWidget(self.label_loop_count, 0, 0, 1, 1)

        self.lineEdit_loop_count = QLineEdit(self.groupBox_level_setting)
        self.lineEdit_loop_count.setObjectName(u"lineEdit_loop_count")
        self.lineEdit_loop_count.setMinimumSize(QSize(0, 30))

        self.gridLayout_level_setting.addWidget(self.lineEdit_loop_count, 0, 1, 1, 1)

        self.label_flop_pos = QLabel(self.groupBox_level_setting)
        self.label_flop_pos.setObjectName(u"label_flop_pos")

        self.gridLayout_level_setting.addWidget(self.label_flop_pos, 0, 2, 1, 1)

        self.lineEdit_flop_pos = QLineEdit(self.groupBox_level_setting)
        self.lineEdit_flop_pos.setObjectName(u"lineEdit_flop_pos")
        self.lineEdit_flop_pos.setMinimumSize(QSize(0, 30))

        self.gridLayout_level_setting.addWidget(self.lineEdit_flop_pos, 0, 3, 1, 1)

        self.checkBox_has_stage2 = QCheckBox(self.groupBox_level_setting)
        self.checkBox_has_stage2.setObjectName(u"checkBox_has_stage2")
        self.checkBox_has_stage2.setMaximumSize(QSize(67, 16777215))
        self.checkBox_has_stage2.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_has_stage2.setChecked(True)

        self.gridLayout_level_setting.addWidget(self.checkBox_has_stage2, 1, 0, 1, 1)

        self.checkBox_continue = QCheckBox(self.groupBox_level_setting)
        self.checkBox_continue.setObjectName(u"checkBox_continue")
        self.checkBox_continue.setMaximumSize(QSize(67, 16777215))
        self.checkBox_continue.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_continue.setChecked(True)

        self.gridLayout_level_setting.addWidget(self.checkBox_continue, 1, 2, 1, 1)

        self.gridLayout_level_setting.setRowStretch(0, 1)
        self.gridLayout_level_setting.setRowStretch(1, 1)
        self.gridLayout_level_setting.setColumnStretch(0, 1)
        self.gridLayout_level_setting.setColumnStretch(1, 1)
        self.gridLayout_level_setting.setColumnStretch(2, 1)
        self.gridLayout_level_setting.setColumnStretch(3, 1)

        self.verticalLayout_top.addWidget(self.groupBox_level_setting)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_top.addItem(self.verticalSpacer)

        self.verticalLayout_top.setStretch(1, 3)
        self.verticalLayout_top.setStretch(2, 5)

        self.retranslateUi(LoopLevelParam)

        QMetaObject.connectSlotsByName(LoopLevelParam)
    # setupUi

    def retranslateUi(self, LoopLevelParam):
        LoopLevelParam.setWindowTitle(QCoreApplication.translate("LoopLevelParam", u"Form", None))
        self.groupBox_select_level.setTitle(QCoreApplication.translate("LoopLevelParam", u"\u9009\u62e9\u5173\u5361", None))
        self.label_zone.setText(QCoreApplication.translate("LoopLevelParam", u"\u5730\u56fe\uff1a", None))
        self.label_level.setText(QCoreApplication.translate("LoopLevelParam", u"\u5173\u5361\uff1a", None))
        self.groupBox_1p_deck.setTitle(QCoreApplication.translate("LoopLevelParam", u"\u623f\u4e3b\u5361\u7ec4\u914d\u7f6e", None))
        self.label_1p_plan.setText(QCoreApplication.translate("LoopLevelParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_view_plan.setText(QCoreApplication.translate("LoopLevelParam", u"\u67e5\u770b\u65b9\u6848", None))
        self.groupBox_level_setting.setTitle(QCoreApplication.translate("LoopLevelParam", u"\u901a\u5173\u8bbe\u7f6e", None))
        self.label_loop_count.setText(QCoreApplication.translate("LoopLevelParam", u"\u5faa\u73af\u6b21\u6570\uff1a", None))
        self.lineEdit_loop_count.setText(QCoreApplication.translate("LoopLevelParam", u"1", None))
        self.label_flop_pos.setText(QCoreApplication.translate("LoopLevelParam", u"\u7ffb\u724c\u4f4d\u7f6e\uff1a", None))
        self.lineEdit_flop_pos.setText(QCoreApplication.translate("LoopLevelParam", u"1;2", None))
        self.checkBox_has_stage2.setText(QCoreApplication.translate("LoopLevelParam", u"\u6709\u4e8c\u9636\u6bb5", None))
        self.checkBox_continue.setText(QCoreApplication.translate("LoopLevelParam", u"\u7ee7\u7eed\u6311\u6218", None))
    # retranslateUi

