# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DailyAwardParam.ui'
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

class Ui_DailyAwardParam(object):
    def setupUi(self, DailyAwardParam):
        if not DailyAwardParam.objectName():
            DailyAwardParam.setObjectName(u"DailyAwardParam")
        DailyAwardParam.resize(530, 340)
        DailyAwardParam.setMaximumSize(QSize(530, 16777215))
        self.verticalLayout_top = QVBoxLayout(DailyAwardParam)
        self.verticalLayout_top.setSpacing(5)
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.verticalLayout_top.setContentsMargins(0, 5, 0, 0)
        self.widget_select_player = QWidget(DailyAwardParam)
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


        self.verticalLayout_top.addWidget(self.widget_select_player)

        self.groupBox_common = QGroupBox(DailyAwardParam)
        self.groupBox_common.setObjectName(u"groupBox_common")
        self.horizontalLayout_common = QHBoxLayout(self.groupBox_common)
        self.horizontalLayout_common.setSpacing(5)
        self.horizontalLayout_common.setObjectName(u"horizontalLayout_common")
        self.horizontalLayout_common.setContentsMargins(-1, 0, -1, 0)
        self.checkBox_vip_signin = QCheckBox(self.groupBox_common)
        self.checkBox_vip_signin.setObjectName(u"checkBox_vip_signin")
        self.checkBox_vip_signin.setMinimumSize(QSize(70, 30))
        self.checkBox_vip_signin.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_vip_signin)

        self.checkBox_daily_signin = QCheckBox(self.groupBox_common)
        self.checkBox_daily_signin.setObjectName(u"checkBox_daily_signin")
        self.checkBox_daily_signin.setMinimumSize(QSize(70, 30))
        self.checkBox_daily_signin.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_daily_signin)

        self.checkBox_free_wish = QCheckBox(self.groupBox_common)
        self.checkBox_free_wish.setObjectName(u"checkBox_free_wish")
        self.checkBox_free_wish.setMinimumSize(QSize(70, 30))
        self.checkBox_free_wish.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_free_wish)

        self.checkBox_bottom_quest = QCheckBox(self.groupBox_common)
        self.checkBox_bottom_quest.setObjectName(u"checkBox_bottom_quest")
        self.checkBox_bottom_quest.setMinimumSize(QSize(70, 30))
        self.checkBox_bottom_quest.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_bottom_quest)

        self.checkBox_tarot_treasure = QCheckBox(self.groupBox_common)
        self.checkBox_tarot_treasure.setObjectName(u"checkBox_tarot_treasure")
        self.checkBox_tarot_treasure.setMinimumSize(QSize(70, 30))
        self.checkBox_tarot_treasure.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_tarot_treasure)

        self.checkBox_campsite_key = QCheckBox(self.groupBox_common)
        self.checkBox_campsite_key.setObjectName(u"checkBox_campsite_key")
        self.checkBox_campsite_key.setMinimumSize(QSize(70, 30))
        self.checkBox_campsite_key.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_campsite_key)

        self.checkBox_monthly_card = QCheckBox(self.groupBox_common)
        self.checkBox_monthly_card.setObjectName(u"checkBox_monthly_card")

        self.horizontalLayout_common.addWidget(self.checkBox_monthly_card)


        self.verticalLayout_top.addWidget(self.groupBox_common)

        self.groupBox_cycle = QGroupBox(DailyAwardParam)
        self.groupBox_cycle.setObjectName(u"groupBox_cycle")
        self.groupBox_cycle.setMaximumSize(QSize(530, 16777215))
        self.gridLayout_cycle = QGridLayout(self.groupBox_cycle)
        self.gridLayout_cycle.setObjectName(u"gridLayout_cycle")
        self.gridLayout_cycle.setHorizontalSpacing(4)
        self.gridLayout_cycle.setContentsMargins(-1, 0, -1, 0)
        self.comboBox_use_coupon_times = QComboBox(self.groupBox_cycle)
        self.comboBox_use_coupon_times.addItem("")
        self.comboBox_use_coupon_times.addItem("")
        self.comboBox_use_coupon_times.addItem("")
        self.comboBox_use_coupon_times.addItem("")
        self.comboBox_use_coupon_times.addItem("")
        self.comboBox_use_coupon_times.addItem("")
        self.comboBox_use_coupon_times.addItem("")
        self.comboBox_use_coupon_times.addItem("")
        self.comboBox_use_coupon_times.addItem("")
        self.comboBox_use_coupon_times.addItem("")
        self.comboBox_use_coupon_times.setObjectName(u"comboBox_use_coupon_times")
        self.comboBox_use_coupon_times.setMinimumSize(QSize(60, 30))

        self.gridLayout_cycle.addWidget(self.comboBox_use_coupon_times, 4, 8, 1, 1)

        self.checkBox_pharaoh_treasure = QCheckBox(self.groupBox_cycle)
        self.checkBox_pharaoh_treasure.setObjectName(u"checkBox_pharaoh_treasure")
        self.checkBox_pharaoh_treasure.setMinimumSize(QSize(70, 30))
        self.checkBox_pharaoh_treasure.setChecked(True)

        self.gridLayout_cycle.addWidget(self.checkBox_pharaoh_treasure, 0, 0, 1, 1)

        self.label_flowers_receiver = QLabel(self.groupBox_cycle)
        self.label_flowers_receiver.setObjectName(u"label_flowers_receiver")
        self.label_flowers_receiver.setMinimumSize(QSize(60, 30))

        self.gridLayout_cycle.addWidget(self.label_flowers_receiver, 4, 1, 1, 1)

        self.lineEdit_fertilize_date = QLineEdit(self.groupBox_cycle)
        self.lineEdit_fertilize_date.setObjectName(u"lineEdit_fertilize_date")
        self.lineEdit_fertilize_date.setMinimumSize(QSize(0, 30))

        self.gridLayout_cycle.addWidget(self.lineEdit_fertilize_date, 1, 6, 1, 3)

        self.label_use_coupon_times = QLabel(self.groupBox_cycle)
        self.label_use_coupon_times.setObjectName(u"label_use_coupon_times")
        self.label_use_coupon_times.setMinimumSize(QSize(60, 30))

        self.gridLayout_cycle.addWidget(self.label_use_coupon_times, 4, 7, 1, 1)

        self.checkBox_use_gift_coupon = QCheckBox(self.groupBox_cycle)
        self.checkBox_use_gift_coupon.setObjectName(u"checkBox_use_gift_coupon")
        self.checkBox_use_gift_coupon.setMinimumSize(QSize(70, 30))

        self.gridLayout_cycle.addWidget(self.checkBox_use_gift_coupon, 4, 6, 1, 1)

        self.checkBox_force_destiny_tree = QCheckBox(self.groupBox_cycle)
        self.checkBox_force_destiny_tree.setObjectName(u"checkBox_force_destiny_tree")
        self.checkBox_force_destiny_tree.setMinimumSize(QSize(70, 30))

        self.gridLayout_cycle.addWidget(self.checkBox_force_destiny_tree, 3, 7, 1, 2)

        self.label_pharaoh_flop_pos = QLabel(self.groupBox_cycle)
        self.label_pharaoh_flop_pos.setObjectName(u"label_pharaoh_flop_pos")
        self.label_pharaoh_flop_pos.setMinimumSize(QSize(60, 30))

        self.gridLayout_cycle.addWidget(self.label_pharaoh_flop_pos, 0, 1, 1, 1)

        self.checkBox_give_flowers = QCheckBox(self.groupBox_cycle)
        self.checkBox_give_flowers.setObjectName(u"checkBox_give_flowers")
        self.checkBox_give_flowers.setMinimumSize(QSize(70, 30))
        self.checkBox_give_flowers.setChecked(True)

        self.gridLayout_cycle.addWidget(self.checkBox_give_flowers, 4, 0, 1, 1)

        self.label_fertilize_date = QLabel(self.groupBox_cycle)
        self.label_fertilize_date.setObjectName(u"label_fertilize_date")

        self.gridLayout_cycle.addWidget(self.label_fertilize_date, 1, 5, 1, 1)

        self.comboBox_pharaoh_flop_pos = QComboBox(self.groupBox_cycle)
        self.comboBox_pharaoh_flop_pos.addItem("")
        self.comboBox_pharaoh_flop_pos.addItem("")
        self.comboBox_pharaoh_flop_pos.addItem("")
        self.comboBox_pharaoh_flop_pos.addItem("")
        self.comboBox_pharaoh_flop_pos.addItem("")
        self.comboBox_pharaoh_flop_pos.addItem("")
        self.comboBox_pharaoh_flop_pos.addItem("")
        self.comboBox_pharaoh_flop_pos.addItem("")
        self.comboBox_pharaoh_flop_pos.setObjectName(u"comboBox_pharaoh_flop_pos")
        self.comboBox_pharaoh_flop_pos.setMinimumSize(QSize(60, 30))

        self.gridLayout_cycle.addWidget(self.comboBox_pharaoh_flop_pos, 0, 2, 1, 2)

        self.pushButton_flowers_receiver = QPushButton(self.groupBox_cycle)
        self.pushButton_flowers_receiver.setObjectName(u"pushButton_flowers_receiver")
        self.pushButton_flowers_receiver.setMinimumSize(QSize(50, 30))

        self.gridLayout_cycle.addWidget(self.pushButton_flowers_receiver, 4, 5, 1, 1)

        self.checkBox_destiny_tree = QCheckBox(self.groupBox_cycle)
        self.checkBox_destiny_tree.setObjectName(u"checkBox_destiny_tree")
        self.checkBox_destiny_tree.setMinimumSize(QSize(70, 30))
        self.checkBox_destiny_tree.setChecked(True)

        self.gridLayout_cycle.addWidget(self.checkBox_destiny_tree, 3, 5, 1, 2)

        self.line_cycle = QFrame(self.groupBox_cycle)
        self.line_cycle.setObjectName(u"line_cycle")
        self.line_cycle.setFrameShape(QFrame.VLine)
        self.line_cycle.setFrameShadow(QFrame.Sunken)

        self.gridLayout_cycle.addWidget(self.line_cycle, 0, 4, 4, 1)

        self.label_plant_type = QLabel(self.groupBox_cycle)
        self.label_plant_type.setObjectName(u"label_plant_type")
        self.label_plant_type.setMinimumSize(QSize(60, 30))

        self.gridLayout_cycle.addWidget(self.label_plant_type, 1, 1, 1, 1)

        self.checkBox_union_garden = QCheckBox(self.groupBox_cycle)
        self.checkBox_union_garden.setObjectName(u"checkBox_union_garden")
        self.checkBox_union_garden.setMinimumSize(QSize(70, 30))
        self.checkBox_union_garden.setChecked(True)

        self.gridLayout_cycle.addWidget(self.checkBox_union_garden, 1, 0, 1, 1)

        self.comboBox_garden_plant_type = QComboBox(self.groupBox_cycle)
        self.comboBox_garden_plant_type.addItem("")
        self.comboBox_garden_plant_type.addItem("")
        self.comboBox_garden_plant_type.addItem("")
        self.comboBox_garden_plant_type.addItem("")
        self.comboBox_garden_plant_type.setObjectName(u"comboBox_garden_plant_type")
        self.comboBox_garden_plant_type.setMinimumSize(QSize(60, 30))

        self.gridLayout_cycle.addWidget(self.comboBox_garden_plant_type, 1, 2, 1, 2)

        self.checkBox_release_quest = QCheckBox(self.groupBox_cycle)
        self.checkBox_release_quest.setObjectName(u"checkBox_release_quest")
        self.checkBox_release_quest.setMinimumSize(QSize(70, 30))

        self.gridLayout_cycle.addWidget(self.checkBox_release_quest, 0, 7, 1, 2)

        self.checkBox_union_quest = QCheckBox(self.groupBox_cycle)
        self.checkBox_union_quest.setObjectName(u"checkBox_union_quest")
        self.checkBox_union_quest.setMinimumSize(QSize(70, 30))
        self.checkBox_union_quest.setChecked(True)

        self.gridLayout_cycle.addWidget(self.checkBox_union_quest, 0, 5, 1, 2)

        self.lineEdit_flowers_receiver = QLineEdit(self.groupBox_cycle)
        self.lineEdit_flowers_receiver.setObjectName(u"lineEdit_flowers_receiver")
        self.lineEdit_flowers_receiver.setMinimumSize(QSize(60, 30))

        self.gridLayout_cycle.addWidget(self.lineEdit_flowers_receiver, 4, 2, 1, 2)

        self.checkBox_force_team_magic_tower = QCheckBox(self.groupBox_cycle)
        self.checkBox_force_team_magic_tower.setObjectName(u"checkBox_force_team_magic_tower")
        self.checkBox_force_team_magic_tower.setMinimumSize(QSize(70, 30))

        self.gridLayout_cycle.addWidget(self.checkBox_force_team_magic_tower, 2, 7, 1, 2)

        self.checkBox_open_food_contest = QCheckBox(self.groupBox_cycle)
        self.checkBox_open_food_contest.setObjectName(u"checkBox_open_food_contest")
        self.checkBox_open_food_contest.setMinimumSize(QSize(70, 30))
        self.checkBox_open_food_contest.setChecked(True)

        self.gridLayout_cycle.addWidget(self.checkBox_open_food_contest, 2, 0, 1, 2)

        self.checkBox_team_magic_tower = QCheckBox(self.groupBox_cycle)
        self.checkBox_team_magic_tower.setObjectName(u"checkBox_team_magic_tower")
        self.checkBox_team_magic_tower.setMinimumSize(QSize(70, 30))
        self.checkBox_team_magic_tower.setChecked(True)

        self.gridLayout_cycle.addWidget(self.checkBox_team_magic_tower, 2, 5, 1, 2)

        self.checkBox_open_backpack = QCheckBox(self.groupBox_cycle)
        self.checkBox_open_backpack.setObjectName(u"checkBox_open_backpack")
        self.checkBox_open_backpack.setMinimumSize(QSize(70, 30))
        self.checkBox_open_backpack.setChecked(True)

        self.gridLayout_cycle.addWidget(self.checkBox_open_backpack, 3, 0, 1, 2)

        self.gridLayout_cycle.setRowStretch(0, 1)
        self.gridLayout_cycle.setRowStretch(1, 1)
        self.gridLayout_cycle.setRowStretch(2, 1)
        self.gridLayout_cycle.setRowStretch(3, 1)
        self.gridLayout_cycle.setRowStretch(4, 1)
        self.gridLayout_cycle.setColumnStretch(0, 3)
        self.gridLayout_cycle.setColumnStretch(1, 2)
        self.gridLayout_cycle.setColumnStretch(2, 3)
        self.gridLayout_cycle.setColumnStretch(3, 2)
        self.gridLayout_cycle.setColumnStretch(5, 3)
        self.gridLayout_cycle.setColumnStretch(6, 2)
        self.gridLayout_cycle.setColumnStretch(7, 3)
        self.gridLayout_cycle.setColumnStretch(8, 2)

        self.verticalLayout_top.addWidget(self.groupBox_cycle)


        self.retranslateUi(DailyAwardParam)

        QMetaObject.connectSlotsByName(DailyAwardParam)
    # setupUi

    def retranslateUi(self, DailyAwardParam):
        DailyAwardParam.setWindowTitle(QCoreApplication.translate("DailyAwardParam", u"Form", None))
        self.label_select_player.setText(QCoreApplication.translate("DailyAwardParam", u"\u9009\u62e9\u8d26\u53f7\uff1a", None))
        self.comboBox_select_player.setItemText(0, QCoreApplication.translate("DailyAwardParam", u"1P", None))
        self.comboBox_select_player.setItemText(1, QCoreApplication.translate("DailyAwardParam", u"2P", None))

        self.groupBox_common.setTitle(QCoreApplication.translate("DailyAwardParam", u"\u4e00\u822c\u7c7b\u522b", None))
        self.checkBox_vip_signin.setText(QCoreApplication.translate("DailyAwardParam", u"VIP\u7b7e\u5230", None))
        self.checkBox_daily_signin.setText(QCoreApplication.translate("DailyAwardParam", u"\u6bcf\u65e5\u7b7e\u5230", None))
        self.checkBox_free_wish.setText(QCoreApplication.translate("DailyAwardParam", u"\u514d\u8d39\u8bb8\u613f", None))
#if QT_CONFIG(tooltip)
        self.checkBox_bottom_quest.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u9886\u53d6\u5e95\u90e8\u4efb\u52a1\u4e2d\u7684\u65e5\u5e38\u4efb\u52a1\u3002\u4f1a\u81ea\u52a8\u6536\u8d77\u524d\u4e09\u79cd\u4efb\u52a1\u7c7b\u522b", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_bottom_quest.setText(QCoreApplication.translate("DailyAwardParam", u"\u5e95\u90e8\u4efb\u52a1", None))
#if QT_CONFIG(tooltip)
        self.checkBox_tarot_treasure.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u6ca1\u6709\u514d\u8d39\u6b21\u6570\u65f6\u4e0d\u4f1a\u7ffb\u724c", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_tarot_treasure.setText(QCoreApplication.translate("DailyAwardParam", u"\u5854\u7f57\u5bfb\u5b9d", None))
        self.checkBox_campsite_key.setText(QCoreApplication.translate("DailyAwardParam", u"\u8425\u5730\u94a5\u5319", None))
        self.checkBox_monthly_card.setText(QCoreApplication.translate("DailyAwardParam", u"\u6708\u5361\u798f\u5229", None))
        self.groupBox_cycle.setTitle(QCoreApplication.translate("DailyAwardParam", u"\u5468\u671f\u7c7b\u522b", None))
        self.comboBox_use_coupon_times.setItemText(0, QCoreApplication.translate("DailyAwardParam", u"1", None))
        self.comboBox_use_coupon_times.setItemText(1, QCoreApplication.translate("DailyAwardParam", u"2", None))
        self.comboBox_use_coupon_times.setItemText(2, QCoreApplication.translate("DailyAwardParam", u"3", None))
        self.comboBox_use_coupon_times.setItemText(3, QCoreApplication.translate("DailyAwardParam", u"4", None))
        self.comboBox_use_coupon_times.setItemText(4, QCoreApplication.translate("DailyAwardParam", u"5", None))
        self.comboBox_use_coupon_times.setItemText(5, QCoreApplication.translate("DailyAwardParam", u"6", None))
        self.comboBox_use_coupon_times.setItemText(6, QCoreApplication.translate("DailyAwardParam", u"7", None))
        self.comboBox_use_coupon_times.setItemText(7, QCoreApplication.translate("DailyAwardParam", u"8", None))
        self.comboBox_use_coupon_times.setItemText(8, QCoreApplication.translate("DailyAwardParam", u"9", None))
        self.comboBox_use_coupon_times.setItemText(9, QCoreApplication.translate("DailyAwardParam", u"10", None))

#if QT_CONFIG(tooltip)
        self.comboBox_use_coupon_times.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u4f7f\u7528\u793c\u5238\u8d60\u9001\u9c9c\u82b1\u7684\u6b21\u6570", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_pharaoh_treasure.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u6ca1\u6709\u514d\u8d39\u6b21\u6570\u65f6\u4e0d\u4f1a\u7ffb\u724c", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_pharaoh_treasure.setText(QCoreApplication.translate("DailyAwardParam", u"\u6cd5\u8001\u5b9d\u85cf", None))
#if QT_CONFIG(tooltip)
        self.label_flowers_receiver.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u9009\u62e9\u8d60\u9001\u5bf9\u8c61\u6635\u79f0\u622a\u56fe\u3002\u8be5\u622a\u56fe\u4e0e\u623f\u95f4\u5185\u7ec4\u961f\u9080\u8bf7\u622a\u56fe\u901a\u7528", None))
#endif // QT_CONFIG(tooltip)
        self.label_flowers_receiver.setText(QCoreApplication.translate("DailyAwardParam", u"\u8d60\u9001\u5bf9\u8c61\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_fertilize_date.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u5728\u6240\u586b\u65e5\u671f\u8303\u56f4\u5185\u81ea\u52a8\u65bd\u80a5(\u95ed\u533a\u95f4)", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_fertilize_date.setText(QCoreApplication.translate("DailyAwardParam", u"2024/01/01-2024/01/03", None))
        self.label_use_coupon_times.setText(QCoreApplication.translate("DailyAwardParam", u"\u793c\u5238\u6b21\u6570\uff1a", None))
        self.checkBox_use_gift_coupon.setText(QCoreApplication.translate("DailyAwardParam", u"\u4f7f\u7528\u793c\u5238", None))
#if QT_CONFIG(tooltip)
        self.checkBox_force_destiny_tree.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u52fe\u9009\u540e\uff0c\u975e\u5468\u4e00\u4e5f\u4f1a\u6267\u884c", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_force_destiny_tree.setText(QCoreApplication.translate("DailyAwardParam", u"\u5176\u4ed6\u65e5\u671f\u5f3a\u5236\u9886\u53d6", None))
        self.label_pharaoh_flop_pos.setText(QCoreApplication.translate("DailyAwardParam", u"\u7ffb\u724c\u4f4d\u7f6e\uff1a", None))
        self.checkBox_give_flowers.setText(QCoreApplication.translate("DailyAwardParam", u"\u8d60\u9001\u9c9c\u82b1", None))
        self.label_fertilize_date.setText(QCoreApplication.translate("DailyAwardParam", u"\u65bd\u80a5\u65e5\u671f\uff1a", None))
        self.comboBox_pharaoh_flop_pos.setItemText(0, QCoreApplication.translate("DailyAwardParam", u"1", None))
        self.comboBox_pharaoh_flop_pos.setItemText(1, QCoreApplication.translate("DailyAwardParam", u"2", None))
        self.comboBox_pharaoh_flop_pos.setItemText(2, QCoreApplication.translate("DailyAwardParam", u"3", None))
        self.comboBox_pharaoh_flop_pos.setItemText(3, QCoreApplication.translate("DailyAwardParam", u"4", None))
        self.comboBox_pharaoh_flop_pos.setItemText(4, QCoreApplication.translate("DailyAwardParam", u"5", None))
        self.comboBox_pharaoh_flop_pos.setItemText(5, QCoreApplication.translate("DailyAwardParam", u"6", None))
        self.comboBox_pharaoh_flop_pos.setItemText(6, QCoreApplication.translate("DailyAwardParam", u"7", None))
        self.comboBox_pharaoh_flop_pos.setItemText(7, QCoreApplication.translate("DailyAwardParam", u"8", None))

#if QT_CONFIG(tooltip)
        self.comboBox_pharaoh_flop_pos.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u4ece\u5de6\u5f80\u53f3\u3001\u4ece\u4e0a\u5f80\u4e0b\u7684\u987a\u5e8f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_flowers_receiver.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u9009\u62e9\u8d60\u9001\u5bf9\u8c61\u6635\u79f0\u622a\u56fe\u3002\u8be5\u622a\u56fe\u4e0e\u623f\u95f4\u5185\u7ec4\u961f\u9080\u8bf7\u622a\u56fe\u901a\u7528", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_flowers_receiver.setText(QCoreApplication.translate("DailyAwardParam", u"\u6d4f\u89c8", None))
        self.checkBox_destiny_tree.setText(QCoreApplication.translate("DailyAwardParam", u"\u6bcf\u5468\u4e00\u7f18\u5206\u6811\u5956\u52b1", None))
#if QT_CONFIG(tooltip)
        self.label_plant_type.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u5f53\u672c\u516c\u4f1a\u7684\u516c\u4f1a\u6811\u9700\u8981\u79cd\u690d\u65f6\u751f\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.label_plant_type.setText(QCoreApplication.translate("DailyAwardParam", u"\u6811\u82d7\u7b49\u7ea7\uff1a", None))
        self.checkBox_union_garden.setText(QCoreApplication.translate("DailyAwardParam", u"\u516c\u4f1a\u82b1\u56ed", None))
        self.comboBox_garden_plant_type.setItemText(0, QCoreApplication.translate("DailyAwardParam", u"\u65e0\u6743\u9650", None))
        self.comboBox_garden_plant_type.setItemText(1, QCoreApplication.translate("DailyAwardParam", u"\u521d\u7ea7\u516c\u4f1a\u6811", None))
        self.comboBox_garden_plant_type.setItemText(2, QCoreApplication.translate("DailyAwardParam", u"\u4e2d\u7ea7\u516c\u4f1a\u6811", None))
        self.comboBox_garden_plant_type.setItemText(3, QCoreApplication.translate("DailyAwardParam", u"\u9ad8\u7ea7\u516c\u4f1a\u6811", None))

#if QT_CONFIG(tooltip)
        self.comboBox_garden_plant_type.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u65e0\u79cd\u690d\u6743\u9650\u65f6\u4e0d\u8981\u9009\u62e9\u5176\u4ed6\uff0c\u5426\u5219\u53ef\u80fd\u9020\u6210\u4e0d\u786e\u5b9a\u7684\u5f71\u54cd", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_release_quest.setText(QCoreApplication.translate("DailyAwardParam", u"\u6709\u6743\u53d1\u5e03\u4f1a\u957f\u4efb\u52a1", None))
        self.checkBox_union_quest.setText(QCoreApplication.translate("DailyAwardParam", u"\u516c\u4f1a\u4efb\u52a1", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_flowers_receiver.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u9009\u62e9\u8d60\u9001\u5bf9\u8c61\u6635\u79f0\u622a\u56fe\u3002\u8be5\u622a\u56fe\u4e0e\u623f\u95f4\u5185\u7ec4\u961f\u9080\u8bf7\u622a\u56fe\u901a\u7528", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_force_team_magic_tower.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u52fe\u9009\u540e\uff0c\u975e\u5468\u4e00\u4e5f\u4f1a\u6267\u884c", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_force_team_magic_tower.setText(QCoreApplication.translate("DailyAwardParam", u"\u5176\u4ed6\u65e5\u671f\u5f3a\u5236\u9886\u53d6", None))
#if QT_CONFIG(tooltip)
        self.checkBox_open_food_contest.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u6253\u5f00\u7f8e\u98df\u5927\u8d5b\u754c\u9762\uff0c\u4ee5\u5b8c\u6210\u7d2f\u8ba1\u767b\u5f5520\u5929\u7684\u4efb\u52a1\u3002\u6ca1\u627e\u5230\u65f6\u81ea\u52a8\u8df3\u8fc7", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_open_food_contest.setText(QCoreApplication.translate("DailyAwardParam", u"\u6253\u5f00\u7f8e\u98df\u5927\u8d5b\u754c\u9762", None))
        self.checkBox_team_magic_tower.setText(QCoreApplication.translate("DailyAwardParam", u"\u6bcf\u5468\u4e00\u53cc\u4eba\u9b54\u5854\u5956\u52b1", None))
#if QT_CONFIG(tooltip)
        self.checkBox_open_backpack.setToolTip(QCoreApplication.translate("DailyAwardParam", u"\u4e0a\u7ebf\u540e\uff0c\u9700\u8981\u6253\u5f00\u80cc\u5305\u624d\u80fd\u6fc0\u6d3b\u60c5\u4fa3\u4efb\u52a1", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_open_backpack.setText(QCoreApplication.translate("DailyAwardParam", u"\u6253\u5f00\u80cc\u5305", None))
    # retranslateUi

