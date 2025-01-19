# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WantedParam.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_WantedParam(object):
    def setupUi(self, WantedParam):
        if not WantedParam.objectName():
            WantedParam.setObjectName(u"WantedParam")
        WantedParam.resize(522, 345)
        self.verticalLayout_top = QVBoxLayout(WantedParam)
        self.verticalLayout_top.setSpacing(5)
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.verticalLayout_top.setContentsMargins(3, 5, 3, 3)
        self.groupBox_select_players = QGroupBox(WantedParam)
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

        self.groupBox_select_plan = QGroupBox(WantedParam)
        self.groupBox_select_plan.setObjectName(u"groupBox_select_plan")
        self.gridLayout_select_plan = QGridLayout(self.groupBox_select_plan)
        self.gridLayout_select_plan.setSpacing(5)
        self.gridLayout_select_plan.setObjectName(u"gridLayout_select_plan")
        self.gridLayout_select_plan.setContentsMargins(-1, 0, -1, 5)
        self.lineEdit_plan_path = QLineEdit(self.groupBox_select_plan)
        self.lineEdit_plan_path.setObjectName(u"lineEdit_plan_path")
        self.lineEdit_plan_path.setMinimumSize(QSize(0, 30))

        self.gridLayout_select_plan.addWidget(self.lineEdit_plan_path, 0, 1, 1, 1)

        self.label_plan_path = QLabel(self.groupBox_select_plan)
        self.label_plan_path.setObjectName(u"label_plan_path")
        self.label_plan_path.setMinimumSize(QSize(67, 0))
        self.label_plan_path.setMaximumSize(QSize(67, 30))

        self.gridLayout_select_plan.addWidget(self.label_plan_path, 0, 0, 1, 1)

        self.pushButton_plan_path = QPushButton(self.groupBox_select_plan)
        self.pushButton_plan_path.setObjectName(u"pushButton_plan_path")
        self.pushButton_plan_path.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_path.setMaximumSize(QSize(80, 30))

        self.gridLayout_select_plan.addWidget(self.pushButton_plan_path, 0, 2, 1, 1)


        self.verticalLayout_top.addWidget(self.groupBox_select_plan)

        self.widget_plan_enable = QWidget(WantedParam)
        self.widget_plan_enable.setObjectName(u"widget_plan_enable")
        self.widget_plan_enable.setMaximumSize(QSize(530, 16777215))
        self.gridLayout_plan_enable = QGridLayout(self.widget_plan_enable)
        self.gridLayout_plan_enable.setSpacing(0)
        self.gridLayout_plan_enable.setObjectName(u"gridLayout_plan_enable")
        self.gridLayout_plan_enable.setContentsMargins(0, 0, 0, 0)
        self.groupBox_mwd = QGroupBox(self.widget_plan_enable)
        self.groupBox_mwd.setObjectName(u"groupBox_mwd")
        self.horizontalLayout_mwd = QHBoxLayout(self.groupBox_mwd)
        self.horizontalLayout_mwd.setSpacing(5)
        self.horizontalLayout_mwd.setObjectName(u"horizontalLayout_mwd")
        self.horizontalLayout_mwd.setContentsMargins(-1, 0, -1, 5)
        self.checkBox_enable_mwd = QCheckBox(self.groupBox_mwd)
        self.checkBox_enable_mwd.setObjectName(u"checkBox_enable_mwd")
        self.checkBox_enable_mwd.setMinimumSize(QSize(45, 0))
        self.checkBox_enable_mwd.setMaximumSize(QSize(45, 16777215))
        self.checkBox_enable_mwd.setChecked(True)

        self.horizontalLayout_mwd.addWidget(self.checkBox_enable_mwd)

        self.label_plan_mwd = QLabel(self.groupBox_mwd)
        self.label_plan_mwd.setObjectName(u"label_plan_mwd")
        self.label_plan_mwd.setMinimumSize(QSize(55, 0))
        self.label_plan_mwd.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_mwd.addWidget(self.label_plan_mwd)

        self.comboBox_plan_mwd = QComboBox(self.groupBox_mwd)
        self.comboBox_plan_mwd.setObjectName(u"comboBox_plan_mwd")
        self.comboBox_plan_mwd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_mwd.addWidget(self.comboBox_plan_mwd)

        self.pushButton_plan_mwd = QPushButton(self.groupBox_mwd)
        self.pushButton_plan_mwd.setObjectName(u"pushButton_plan_mwd")
        self.pushButton_plan_mwd.setMinimumSize(QSize(55, 30))
        self.pushButton_plan_mwd.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_mwd.addWidget(self.pushButton_plan_mwd)


        self.gridLayout_plan_enable.addWidget(self.groupBox_mwd, 0, 0, 1, 1)

        self.groupBox_hsd = QGroupBox(self.widget_plan_enable)
        self.groupBox_hsd.setObjectName(u"groupBox_hsd")
        self.horizontalLayout_hsd = QHBoxLayout(self.groupBox_hsd)
        self.horizontalLayout_hsd.setSpacing(5)
        self.horizontalLayout_hsd.setObjectName(u"horizontalLayout_hsd")
        self.horizontalLayout_hsd.setContentsMargins(-1, 0, -1, 5)
        self.checkBox_enable_hsd = QCheckBox(self.groupBox_hsd)
        self.checkBox_enable_hsd.setObjectName(u"checkBox_enable_hsd")
        self.checkBox_enable_hsd.setMinimumSize(QSize(45, 0))
        self.checkBox_enable_hsd.setMaximumSize(QSize(45, 16777215))
        self.checkBox_enable_hsd.setChecked(True)

        self.horizontalLayout_hsd.addWidget(self.checkBox_enable_hsd)

        self.label_plan_hsd = QLabel(self.groupBox_hsd)
        self.label_plan_hsd.setObjectName(u"label_plan_hsd")
        self.label_plan_hsd.setMinimumSize(QSize(55, 0))
        self.label_plan_hsd.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_hsd.addWidget(self.label_plan_hsd)

        self.comboBox_plan_hsd = QComboBox(self.groupBox_hsd)
        self.comboBox_plan_hsd.setObjectName(u"comboBox_plan_hsd")
        self.comboBox_plan_hsd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_hsd.addWidget(self.comboBox_plan_hsd)

        self.pushButton_plan_hsd = QPushButton(self.groupBox_hsd)
        self.pushButton_plan_hsd.setObjectName(u"pushButton_plan_hsd")
        self.pushButton_plan_hsd.setMinimumSize(QSize(55, 30))
        self.pushButton_plan_hsd.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_hsd.addWidget(self.pushButton_plan_hsd)


        self.gridLayout_plan_enable.addWidget(self.groupBox_hsd, 0, 1, 1, 1)

        self.groupBox_fkd = QGroupBox(self.widget_plan_enable)
        self.groupBox_fkd.setObjectName(u"groupBox_fkd")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_fkd)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 5)
        self.checkBox_enable_fkd = QCheckBox(self.groupBox_fkd)
        self.checkBox_enable_fkd.setObjectName(u"checkBox_enable_fkd")
        self.checkBox_enable_fkd.setMinimumSize(QSize(45, 0))
        self.checkBox_enable_fkd.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_3.addWidget(self.checkBox_enable_fkd)

        self.label_plan_fkd = QLabel(self.groupBox_fkd)
        self.label_plan_fkd.setObjectName(u"label_plan_fkd")
        self.label_plan_fkd.setMinimumSize(QSize(55, 0))
        self.label_plan_fkd.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_3.addWidget(self.label_plan_fkd)

        self.comboBox_plan_fkd = QComboBox(self.groupBox_fkd)
        self.comboBox_plan_fkd.setObjectName(u"comboBox_plan_fkd")
        self.comboBox_plan_fkd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.comboBox_plan_fkd)

        self.pushButton_plan_fkd = QPushButton(self.groupBox_fkd)
        self.pushButton_plan_fkd.setObjectName(u"pushButton_plan_fkd")
        self.pushButton_plan_fkd.setMinimumSize(QSize(55, 30))
        self.pushButton_plan_fkd.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_plan_fkd)


        self.gridLayout_plan_enable.addWidget(self.groupBox_fkd, 1, 0, 1, 1)

        self.groupBox_xjcy = QGroupBox(self.widget_plan_enable)
        self.groupBox_xjcy.setObjectName(u"groupBox_xjcy")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_xjcy)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 5)
        self.checkBox_enable_xjcy = QCheckBox(self.groupBox_xjcy)
        self.checkBox_enable_xjcy.setObjectName(u"checkBox_enable_xjcy")
        self.checkBox_enable_xjcy.setMinimumSize(QSize(45, 0))
        self.checkBox_enable_xjcy.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_4.addWidget(self.checkBox_enable_xjcy)

        self.label_plan_xjcy = QLabel(self.groupBox_xjcy)
        self.label_plan_xjcy.setObjectName(u"label_plan_xjcy")
        self.label_plan_xjcy.setMinimumSize(QSize(55, 0))
        self.label_plan_xjcy.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_4.addWidget(self.label_plan_xjcy)

        self.comboBox_plan_xjcy = QComboBox(self.groupBox_xjcy)
        self.comboBox_plan_xjcy.setObjectName(u"comboBox_plan_xjcy")
        self.comboBox_plan_xjcy.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.comboBox_plan_xjcy)

        self.pushButton_plan_xjcy = QPushButton(self.groupBox_xjcy)
        self.pushButton_plan_xjcy.setObjectName(u"pushButton_plan_xjcy")
        self.pushButton_plan_xjcy.setMinimumSize(QSize(55, 30))
        self.pushButton_plan_xjcy.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_plan_xjcy)


        self.gridLayout_plan_enable.addWidget(self.groupBox_xjcy, 1, 1, 1, 1)


        self.verticalLayout_top.addWidget(self.widget_plan_enable)

        self.groupBox_level_setting = QGroupBox(WantedParam)
        self.groupBox_level_setting.setObjectName(u"groupBox_level_setting")
        self.groupBox_level_setting.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout = QHBoxLayout(self.groupBox_level_setting)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 5)
        self.label_flop_pos = QLabel(self.groupBox_level_setting)
        self.label_flop_pos.setObjectName(u"label_flop_pos")
        self.label_flop_pos.setMinimumSize(QSize(67, 0))

        self.horizontalLayout.addWidget(self.label_flop_pos)

        self.lineEdit_flop_pos = QLineEdit(self.groupBox_level_setting)
        self.lineEdit_flop_pos.setObjectName(u"lineEdit_flop_pos")
        self.lineEdit_flop_pos.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.lineEdit_flop_pos)


        self.verticalLayout_top.addWidget(self.groupBox_level_setting)

        self.verticalLayout_top.setStretch(0, 2)
        self.verticalLayout_top.setStretch(1, 2)
        self.verticalLayout_top.setStretch(2, 5)
        self.verticalLayout_top.setStretch(3, 2)

        self.retranslateUi(WantedParam)

        QMetaObject.connectSlotsByName(WantedParam)
    # setupUi

    def retranslateUi(self, WantedParam):
        WantedParam.setWindowTitle(QCoreApplication.translate("WantedParam", u"Form", None))
        self.groupBox_select_players.setTitle(QCoreApplication.translate("WantedParam", u"\u9009\u62e9\u8d26\u53f7", None))
        self.label_select_1p.setText(QCoreApplication.translate("WantedParam", u"\u623f\u4e3b\uff1a", None))
        self.comboBox_select_1p.setItemText(0, QCoreApplication.translate("WantedParam", u"1P", None))
        self.comboBox_select_1p.setItemText(1, QCoreApplication.translate("WantedParam", u"2P", None))

        self.label_select_2p.setText(QCoreApplication.translate("WantedParam", u"\u623f\u5ba2\uff1a", None))
        self.comboBox_select_2p.setItemText(0, QCoreApplication.translate("WantedParam", u"\u65e0", None))
        self.comboBox_select_2p.setItemText(1, QCoreApplication.translate("WantedParam", u"1P", None))
        self.comboBox_select_2p.setItemText(2, QCoreApplication.translate("WantedParam", u"2P", None))

        self.groupBox_select_plan.setTitle(QCoreApplication.translate("WantedParam", u"\u9009\u62e9\u65b9\u6848", None))
        self.label_plan_path.setText(QCoreApplication.translate("WantedParam", u"\u65b9\u6848\u8def\u5f84\uff1a", None))
        self.pushButton_plan_path.setText(QCoreApplication.translate("WantedParam", u"\u6d4f\u89c8", None))
        self.groupBox_mwd.setTitle(QCoreApplication.translate("WantedParam", u"\u7f8e\u5473\u5c9b", None))
        self.checkBox_enable_mwd.setText(QCoreApplication.translate("WantedParam", u"\u542f\u7528", None))
        self.label_plan_mwd.setText(QCoreApplication.translate("WantedParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_plan_mwd.setText(QCoreApplication.translate("WantedParam", u"\u67e5\u770b\u65b9\u6848", None))
        self.groupBox_hsd.setTitle(QCoreApplication.translate("WantedParam", u"\u706b\u5c71\u5c9b", None))
        self.checkBox_enable_hsd.setText(QCoreApplication.translate("WantedParam", u"\u542f\u7528", None))
        self.label_plan_hsd.setText(QCoreApplication.translate("WantedParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_plan_hsd.setText(QCoreApplication.translate("WantedParam", u"\u67e5\u770b\u65b9\u6848", None))
        self.groupBox_fkd.setTitle(QCoreApplication.translate("WantedParam", u"\u6d6e\u7a7a\u5c9b", None))
        self.checkBox_enable_fkd.setText(QCoreApplication.translate("WantedParam", u"\u542f\u7528", None))
        self.label_plan_fkd.setText(QCoreApplication.translate("WantedParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_plan_fkd.setText(QCoreApplication.translate("WantedParam", u"\u67e5\u770b\u65b9\u6848", None))
        self.groupBox_xjcy.setTitle(QCoreApplication.translate("WantedParam", u"\u661f\u9645\u7a7f\u8d8a", None))
        self.checkBox_enable_xjcy.setText(QCoreApplication.translate("WantedParam", u"\u542f\u7528", None))
        self.label_plan_xjcy.setText(QCoreApplication.translate("WantedParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_plan_xjcy.setText(QCoreApplication.translate("WantedParam", u"\u67e5\u770b\u65b9\u6848", None))
        self.groupBox_level_setting.setTitle(QCoreApplication.translate("WantedParam", u"\u901a\u5173\u8bbe\u7f6e", None))
        self.label_flop_pos.setText(QCoreApplication.translate("WantedParam", u"\u7ffb\u724c\u4f4d\u7f6e\uff1a", None))
        self.lineEdit_flop_pos.setText(QCoreApplication.translate("WantedParam", u"1;2", None))
    # retranslateUi

