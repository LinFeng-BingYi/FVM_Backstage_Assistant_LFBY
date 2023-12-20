# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CrossServiceParam.ui'
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

class Ui_CrossServiceParam(object):
    def setupUi(self, CrossServiceParam):
        if not CrossServiceParam.objectName():
            CrossServiceParam.setObjectName(u"CrossServiceParam")
        CrossServiceParam.resize(530, 340)
        self.verticalLayout_top = QVBoxLayout(CrossServiceParam)
        self.verticalLayout_top.setSpacing(0)
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.verticalLayout_top.setContentsMargins(3, 10, 3, 3)
        self.groupBox_select_level = QGroupBox(CrossServiceParam)
        self.groupBox_select_level.setObjectName(u"groupBox_select_level")
        self.groupBox_select_level.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_select_level = QHBoxLayout(self.groupBox_select_level)
        self.horizontalLayout_select_level.setSpacing(5)
        self.horizontalLayout_select_level.setObjectName(u"horizontalLayout_select_level")
        self.horizontalLayout_select_level.setContentsMargins(9, 0, -1, 5)
        self.label_level_type = QLabel(self.groupBox_select_level)
        self.label_level_type.setObjectName(u"label_level_type")
        self.label_level_type.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_select_level.addWidget(self.label_level_type)

        self.comboBox_level_type = QComboBox(self.groupBox_select_level)
        self.comboBox_level_type.addItem("")
        self.comboBox_level_type.addItem("")
        self.comboBox_level_type.addItem("")
        self.comboBox_level_type.addItem("")
        self.comboBox_level_type.addItem("")
        self.comboBox_level_type.addItem("")
        self.comboBox_level_type.setObjectName(u"comboBox_level_type")
        self.comboBox_level_type.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_level.addWidget(self.comboBox_level_type)

        self.label_level_num = QLabel(self.groupBox_select_level)
        self.label_level_num.setObjectName(u"label_level_num")
        self.label_level_num.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_select_level.addWidget(self.label_level_num)

        self.comboBox_level_num = QComboBox(self.groupBox_select_level)
        self.comboBox_level_num.addItem("")
        self.comboBox_level_num.addItem("")
        self.comboBox_level_num.addItem("")
        self.comboBox_level_num.addItem("")
        self.comboBox_level_num.addItem("")
        self.comboBox_level_num.addItem("")
        self.comboBox_level_num.addItem("")
        self.comboBox_level_num.addItem("")
        self.comboBox_level_num.setObjectName(u"comboBox_level_num")
        self.comboBox_level_num.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_level.addWidget(self.comboBox_level_num)


        self.verticalLayout_top.addWidget(self.groupBox_select_level)

        self.groupBox_1p_deck = QGroupBox(CrossServiceParam)
        self.groupBox_1p_deck.setObjectName(u"groupBox_1p_deck")
        self.groupBox_1p_deck.setMinimumSize(QSize(0, 90))
        self.gridLayout_1p_deck = QGridLayout(self.groupBox_1p_deck)
        self.gridLayout_1p_deck.setObjectName(u"gridLayout_1p_deck")
        self.gridLayout_1p_deck.setHorizontalSpacing(5)
        self.gridLayout_1p_deck.setVerticalSpacing(7)
        self.gridLayout_1p_deck.setContentsMargins(-1, 0, -1, 5)
        self.label_1p_plan = QLabel(self.groupBox_1p_deck)
        self.label_1p_plan.setObjectName(u"label_1p_plan")
        self.label_1p_plan.setMinimumSize(QSize(67, 0))

        self.gridLayout_1p_deck.addWidget(self.label_1p_plan, 0, 0, 1, 1)

        self.comboBox_1p_plan = QComboBox(self.groupBox_1p_deck)
        self.comboBox_1p_plan.setObjectName(u"comboBox_1p_plan")
        self.comboBox_1p_plan.setMinimumSize(QSize(0, 30))

        self.gridLayout_1p_deck.addWidget(self.comboBox_1p_plan, 0, 1, 1, 1)

        self.pushButton_view_plan = QPushButton(self.groupBox_1p_deck)
        self.pushButton_view_plan.setObjectName(u"pushButton_view_plan")
        self.pushButton_view_plan.setMinimumSize(QSize(80, 30))
        self.pushButton_view_plan.setMaximumSize(QSize(80, 30))

        self.gridLayout_1p_deck.addWidget(self.pushButton_view_plan, 0, 2, 1, 1)

        self.label_1p_room_name_path = QLabel(self.groupBox_1p_deck)
        self.label_1p_room_name_path.setObjectName(u"label_1p_room_name_path")
        self.label_1p_room_name_path.setMinimumSize(QSize(67, 0))

        self.gridLayout_1p_deck.addWidget(self.label_1p_room_name_path, 1, 0, 1, 1)

        self.lineEdit_1p_room_name_path = QLineEdit(self.groupBox_1p_deck)
        self.lineEdit_1p_room_name_path.setObjectName(u"lineEdit_1p_room_name_path")
        self.lineEdit_1p_room_name_path.setMinimumSize(QSize(0, 30))

        self.gridLayout_1p_deck.addWidget(self.lineEdit_1p_room_name_path, 1, 1, 1, 1)

        self.pushButton_1p_room_name_path = QPushButton(self.groupBox_1p_deck)
        self.pushButton_1p_room_name_path.setObjectName(u"pushButton_1p_room_name_path")
        self.pushButton_1p_room_name_path.setMinimumSize(QSize(80, 30))
        self.pushButton_1p_room_name_path.setMaximumSize(QSize(80, 30))

        self.gridLayout_1p_deck.addWidget(self.pushButton_1p_room_name_path, 1, 2, 1, 1)


        self.verticalLayout_top.addWidget(self.groupBox_1p_deck)

        self.groupBox_level_setting = QGroupBox(CrossServiceParam)
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

        self.verticalSpacer = QSpacerItem(20, 115, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_top.addItem(self.verticalSpacer)

        self.verticalLayout_top.setStretch(0, 1)
        self.verticalLayout_top.setStretch(1, 1)
        self.verticalLayout_top.setStretch(2, 1)
        self.verticalLayout_top.setStretch(3, 2)

        self.retranslateUi(CrossServiceParam)

        self.comboBox_level_type.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CrossServiceParam)
    # setupUi

    def retranslateUi(self, CrossServiceParam):
        CrossServiceParam.setWindowTitle(QCoreApplication.translate("CrossServiceParam", u"Form", None))
        self.groupBox_select_level.setTitle(QCoreApplication.translate("CrossServiceParam", u"\u9009\u62e9\u5173\u5361", None))
        self.label_level_type.setText(QCoreApplication.translate("CrossServiceParam", u"\u5173\u5361\u7c7b\u578b\uff1a", None))
        self.comboBox_level_type.setItemText(0, QCoreApplication.translate("CrossServiceParam", u"\u6df1\u6e0a\u53e4\u5821", None))
        self.comboBox_level_type.setItemText(1, QCoreApplication.translate("CrossServiceParam", u"\u68a6\u9b47\u5929\u7a7a", None))
        self.comboBox_level_type.setItemText(2, QCoreApplication.translate("CrossServiceParam", u"\u707c\u70ed\u5730\u72f1", None))
        self.comboBox_level_type.setItemText(3, QCoreApplication.translate("CrossServiceParam", u"\u6c34\u706b\u4e4b\u95f4", None))
        self.comboBox_level_type.setItemText(4, QCoreApplication.translate("CrossServiceParam", u"\u5deb\u6bd2\u7814\u7a76\u6240", None))
        self.comboBox_level_type.setItemText(5, QCoreApplication.translate("CrossServiceParam", u"\u51b0\u5c01\u9057\u8ff9", None))

        self.label_level_num.setText(QCoreApplication.translate("CrossServiceParam", u"\u5173\u5361\u96be\u5ea6\uff1a", None))
        self.comboBox_level_num.setItemText(0, QCoreApplication.translate("CrossServiceParam", u"8\u661f", None))
        self.comboBox_level_num.setItemText(1, QCoreApplication.translate("CrossServiceParam", u"9\u661f", None))
        self.comboBox_level_num.setItemText(2, QCoreApplication.translate("CrossServiceParam", u"10\u661f", None))
        self.comboBox_level_num.setItemText(3, QCoreApplication.translate("CrossServiceParam", u"11\u661f", None))
        self.comboBox_level_num.setItemText(4, QCoreApplication.translate("CrossServiceParam", u"12\u661f", None))
        self.comboBox_level_num.setItemText(5, QCoreApplication.translate("CrossServiceParam", u"13\u661f", None))
        self.comboBox_level_num.setItemText(6, QCoreApplication.translate("CrossServiceParam", u"14\u661f", None))
        self.comboBox_level_num.setItemText(7, QCoreApplication.translate("CrossServiceParam", u"15\u661f", None))

        self.groupBox_1p_deck.setTitle(QCoreApplication.translate("CrossServiceParam", u"\u4fe1\u606f\u914d\u7f6e", None))
        self.label_1p_plan.setText(QCoreApplication.translate("CrossServiceParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_view_plan.setText(QCoreApplication.translate("CrossServiceParam", u"\u67e5\u770b\u65b9\u6848", None))
#if QT_CONFIG(tooltip)
        self.label_1p_room_name_path.setToolTip(QCoreApplication.translate("CrossServiceParam", u"\u8de8\u670d\u623f\u95f4\u5217\u8868\u4e2d\u7684\u623f\u4e3b\u6635\u79f0\u622a\u56fe", None))
#endif // QT_CONFIG(tooltip)
        self.label_1p_room_name_path.setText(QCoreApplication.translate("CrossServiceParam", u"\u623f\u4e3b\u6635\u79f0\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_1p_room_name_path.setToolTip(QCoreApplication.translate("CrossServiceParam", u"\u8de8\u670d\u623f\u95f4\u5217\u8868\u4e2d\u7684\u623f\u4e3b\u6635\u79f0\u622a\u56fe", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_1p_room_name_path.setToolTip(QCoreApplication.translate("CrossServiceParam", u"\u8de8\u670d\u623f\u95f4\u5217\u8868\u4e2d\u7684\u623f\u4e3b\u6635\u79f0\u622a\u56fe", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_1p_room_name_path.setText(QCoreApplication.translate("CrossServiceParam", u"\u6d4f\u89c8", None))
        self.groupBox_level_setting.setTitle(QCoreApplication.translate("CrossServiceParam", u"\u901a\u5173\u8bbe\u7f6e", None))
        self.label_loop_count.setText(QCoreApplication.translate("CrossServiceParam", u"\u5faa\u73af\u6b21\u6570\uff1a", None))
        self.lineEdit_loop_count.setText(QCoreApplication.translate("CrossServiceParam", u"10", None))
        self.label_flop_pos.setText(QCoreApplication.translate("CrossServiceParam", u"\u7ffb\u724c\u4f4d\u7f6e\uff1a", None))
        self.lineEdit_flop_pos.setText(QCoreApplication.translate("CrossServiceParam", u"1;2", None))
    # retranslateUi

