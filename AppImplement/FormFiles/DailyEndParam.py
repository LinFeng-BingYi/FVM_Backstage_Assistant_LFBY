# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DailyEndParam.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DailyEndParam(object):
    def setupUi(self, DailyEndParam):
        if not DailyEndParam.objectName():
            DailyEndParam.setObjectName(u"DailyEndParam")
        DailyEndParam.resize(530, 340)
        self.verticalLayout = QVBoxLayout(DailyEndParam)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.widget_select_player = QWidget(DailyEndParam)
        self.widget_select_player.setObjectName(u"widget_select_player")
        self.horizontalLayout_select_player = QHBoxLayout(self.widget_select_player)
        self.horizontalLayout_select_player.setSpacing(5)
        self.horizontalLayout_select_player.setObjectName(u"horizontalLayout_select_player")
        self.horizontalLayout_select_player.setContentsMargins(-1, 0, -1, 0)
        self.label_select_player = QLabel(self.widget_select_player)
        self.label_select_player.setObjectName(u"label_select_player")

        self.horizontalLayout_select_player.addWidget(self.label_select_player)

        self.comboBox_select_player = QComboBox(self.widget_select_player)
        self.comboBox_select_player.addItem("")
        self.comboBox_select_player.addItem("")
        self.comboBox_select_player.setObjectName(u"comboBox_select_player")
        self.comboBox_select_player.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_select_player.addWidget(self.comboBox_select_player)

        self.horizontalSpacer_select_player = QSpacerItem(398, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_select_player.addItem(self.horizontalSpacer_select_player)


        self.verticalLayout.addWidget(self.widget_select_player)

        self.groupBox_common = QGroupBox(DailyEndParam)
        self.groupBox_common.setObjectName(u"groupBox_common")
        self.horizontalLayout_common = QHBoxLayout(self.groupBox_common)
        self.horizontalLayout_common.setSpacing(5)
        self.horizontalLayout_common.setObjectName(u"horizontalLayout_common")
        self.horizontalLayout_common.setContentsMargins(-1, 0, -1, 0)
        self.checkBox_bottom_quest = QCheckBox(self.groupBox_common)
        self.checkBox_bottom_quest.setObjectName(u"checkBox_bottom_quest")
        self.checkBox_bottom_quest.setMinimumSize(QSize(70, 30))
        self.checkBox_bottom_quest.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_bottom_quest)

        self.checkBox_union_quest = QCheckBox(self.groupBox_common)
        self.checkBox_union_quest.setObjectName(u"checkBox_union_quest")
        self.checkBox_union_quest.setMinimumSize(QSize(70, 30))
        self.checkBox_union_quest.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_union_quest)

        self.checkBox_lover_quest = QCheckBox(self.groupBox_common)
        self.checkBox_lover_quest.setObjectName(u"checkBox_lover_quest")
        self.checkBox_lover_quest.setMinimumSize(QSize(70, 30))
        self.checkBox_lover_quest.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_lover_quest)

        self.checkBox_wanted = QCheckBox(self.groupBox_common)
        self.checkBox_wanted.setObjectName(u"checkBox_wanted")
        self.checkBox_wanted.setMinimumSize(QSize(70, 30))
        self.checkBox_wanted.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_wanted)

        self.horizontalSpacer_common = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_common.addItem(self.horizontalSpacer_common)


        self.verticalLayout.addWidget(self.groupBox_common)

        self.groupBox_other = QGroupBox(DailyEndParam)
        self.groupBox_other.setObjectName(u"groupBox_other")
        self.groupBox_other.setMaximumSize(QSize(530, 16777215))
        self.gridLayout_cycle = QGridLayout(self.groupBox_other)
        self.gridLayout_cycle.setObjectName(u"gridLayout_cycle")
        self.gridLayout_cycle.setHorizontalSpacing(4)
        self.gridLayout_cycle.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_backpack_item_pic = QPushButton(self.groupBox_other)
        self.pushButton_backpack_item_pic.setObjectName(u"pushButton_backpack_item_pic")
        self.pushButton_backpack_item_pic.setMinimumSize(QSize(60, 30))

        self.gridLayout_cycle.addWidget(self.pushButton_backpack_item_pic, 1, 3, 1, 1)

        self.lineEdit_backpack_item_pic = QLineEdit(self.groupBox_other)
        self.lineEdit_backpack_item_pic.setObjectName(u"lineEdit_backpack_item_pic")
        self.lineEdit_backpack_item_pic.setMinimumSize(QSize(60, 30))

        self.gridLayout_cycle.addWidget(self.lineEdit_backpack_item_pic, 1, 2, 1, 1)

        self.label_backpack_item_pic = QLabel(self.groupBox_other)
        self.label_backpack_item_pic.setObjectName(u"label_backpack_item_pic")
        self.label_backpack_item_pic.setMinimumSize(QSize(60, 30))
        self.label_backpack_item_pic.setFrameShape(QFrame.NoFrame)

        self.gridLayout_cycle.addWidget(self.label_backpack_item_pic, 1, 1, 1, 1)

        self.checkBox_backpack_exchange = QCheckBox(self.groupBox_other)
        self.checkBox_backpack_exchange.setObjectName(u"checkBox_backpack_exchange")
        self.checkBox_backpack_exchange.setMinimumSize(QSize(70, 30))

        self.gridLayout_cycle.addWidget(self.checkBox_backpack_exchange, 1, 0, 1, 1)

        self.checkBox_monopoly = QCheckBox(self.groupBox_other)
        self.checkBox_monopoly.setObjectName(u"checkBox_monopoly")
        self.checkBox_monopoly.setMinimumSize(QSize(70, 30))
        self.checkBox_monopoly.setChecked(True)

        self.gridLayout_cycle.addWidget(self.checkBox_monopoly, 0, 0, 1, 1)

        self.checkBox_monopoly_use_dice = QCheckBox(self.groupBox_other)
        self.checkBox_monopoly_use_dice.setObjectName(u"checkBox_monopoly_use_dice")
        self.checkBox_monopoly_use_dice.setMinimumSize(QSize(70, 30))

        self.gridLayout_cycle.addWidget(self.checkBox_monopoly_use_dice, 0, 1, 1, 1)

        self.gridLayout_cycle.setRowStretch(0, 1)
        self.gridLayout_cycle.setColumnStretch(0, 1)
        self.gridLayout_cycle.setColumnStretch(1, 1)
        self.gridLayout_cycle.setColumnStretch(2, 3)
        self.gridLayout_cycle.setColumnStretch(3, 1)

        self.verticalLayout.addWidget(self.groupBox_other)


        self.retranslateUi(DailyEndParam)

        QMetaObject.connectSlotsByName(DailyEndParam)
    # setupUi

    def retranslateUi(self, DailyEndParam):
        DailyEndParam.setWindowTitle(QCoreApplication.translate("DailyEndParam", u"Form", None))
        self.label_select_player.setText(QCoreApplication.translate("DailyEndParam", u"\u9009\u62e9\u8d26\u53f7\uff1a", None))
        self.comboBox_select_player.setItemText(0, QCoreApplication.translate("DailyEndParam", u"1P", None))
        self.comboBox_select_player.setItemText(1, QCoreApplication.translate("DailyEndParam", u"2P", None))

        self.groupBox_common.setTitle(QCoreApplication.translate("DailyEndParam", u"\u4e00\u822c\u7c7b\u522b", None))
#if QT_CONFIG(tooltip)
        self.checkBox_bottom_quest.setToolTip(QCoreApplication.translate("DailyEndParam", u"\u9886\u53d6\u5e95\u90e8\u4efb\u52a1\u4e2d\u7684\u65e5\u5e38\u4efb\u52a1\u3002\u4f1a\u81ea\u52a8\u6536\u8d77\u524d\u4e09\u79cd\u4efb\u52a1\u7c7b\u522b", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_bottom_quest.setText(QCoreApplication.translate("DailyEndParam", u"\u5e95\u90e8\u4efb\u52a1", None))
        self.checkBox_union_quest.setText(QCoreApplication.translate("DailyEndParam", u"\u516c\u4f1a\u4efb\u52a1", None))
        self.checkBox_lover_quest.setText(QCoreApplication.translate("DailyEndParam", u"\u60c5\u4fa3\u4efb\u52a1", None))
        self.checkBox_wanted.setText(QCoreApplication.translate("DailyEndParam", u"\u60ac\u8d4f\u6d3b\u52a8", None))
        self.groupBox_other.setTitle(QCoreApplication.translate("DailyEndParam", u"\u5176\u4ed6\u7c7b\u522b", None))
        self.pushButton_backpack_item_pic.setText(QCoreApplication.translate("DailyEndParam", u"\u6d4f\u89c8", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_backpack_item_pic.setToolTip(QCoreApplication.translate("DailyEndParam", u"\u9009\u62e9\u8d60\u9001\u5bf9\u8c61\u6635\u79f0\u622a\u56fe\u3002\u8be5\u622a\u56fe\u4e0e\u623f\u95f4\u5185\u7ec4\u961f\u9080\u8bf7\u622a\u56fe\u901a\u7528", None))
#endif // QT_CONFIG(tooltip)
        self.label_backpack_item_pic.setText(QCoreApplication.translate("DailyEndParam", u"\u6761\u76ee\u622a\u56fe\uff1a", None))
#if QT_CONFIG(tooltip)
        self.checkBox_backpack_exchange.setToolTip(QCoreApplication.translate("DailyEndParam", u"\u6ca1\u6709\u514d\u8d39\u6b21\u6570\u65f6\u4e0d\u4f1a\u7ffb\u724c", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_backpack_exchange.setText(QCoreApplication.translate("DailyEndParam", u"\u529f\u80fd\u5f85\u5b9a", None))
        self.checkBox_monopoly.setText(QCoreApplication.translate("DailyEndParam", u"\u5927\u5bcc\u7fc1", None))
        self.checkBox_monopoly_use_dice.setText(QCoreApplication.translate("DailyEndParam", u"\u4f7f\u7528\u9ab0\u5b50", None))
    # retranslateUi

