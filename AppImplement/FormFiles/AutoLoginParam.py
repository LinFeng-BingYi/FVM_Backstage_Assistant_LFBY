# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoLoginParam.ui'
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

class Ui_AutoLoginParam(object):
    def setupUi(self, AutoLoginParam):
        if not AutoLoginParam.objectName():
            AutoLoginParam.setObjectName(u"AutoLoginParam")
        AutoLoginParam.resize(530, 340)
        self.verticalLayout_general = QVBoxLayout(AutoLoginParam)
        self.verticalLayout_general.setSpacing(5)
        self.verticalLayout_general.setObjectName(u"verticalLayout_general")
        self.verticalLayout_general.setContentsMargins(0, 10, 0, 0)
        self.widget_dsc = QWidget(AutoLoginParam)
        self.widget_dsc.setObjectName(u"widget_dsc")
        self.verticalLayout_dsc = QVBoxLayout(self.widget_dsc)
        self.verticalLayout_dsc.setSpacing(5)
        self.verticalLayout_dsc.setObjectName(u"verticalLayout_dsc")
        self.verticalLayout_dsc.setContentsMargins(-1, 0, -1, 0)
        self.label_dsc = QLabel(self.widget_dsc)
        self.label_dsc.setObjectName(u"label_dsc")

        self.verticalLayout_dsc.addWidget(self.label_dsc)


        self.verticalLayout_general.addWidget(self.widget_dsc)

        self.widget_other_setting = QWidget(AutoLoginParam)
        self.widget_other_setting.setObjectName(u"widget_other_setting")
        self.widget_other_setting.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_other_setting = QHBoxLayout(self.widget_other_setting)
        self.horizontalLayout_other_setting.setSpacing(5)
        self.horizontalLayout_other_setting.setObjectName(u"horizontalLayout_other_setting")
        self.horizontalLayout_other_setting.setContentsMargins(-1, 0, -1, 0)
        self.label_start_delay = QLabel(self.widget_other_setting)
        self.label_start_delay.setObjectName(u"label_start_delay")
        self.label_start_delay.setMinimumSize(QSize(65, 0))
        self.label_start_delay.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_other_setting.addWidget(self.label_start_delay)

        self.lineEdit_start_delay = QLineEdit(self.widget_other_setting)
        self.lineEdit_start_delay.setObjectName(u"lineEdit_start_delay")
        self.lineEdit_start_delay.setMinimumSize(QSize(0, 30))
        self.lineEdit_start_delay.setMaximumSize(QSize(97, 16777215))

        self.horizontalLayout_other_setting.addWidget(self.lineEdit_start_delay)

        self.label_start_delay_unit = QLabel(self.widget_other_setting)
        self.label_start_delay_unit.setObjectName(u"label_start_delay_unit")

        self.horizontalLayout_other_setting.addWidget(self.label_start_delay_unit)

        self.horizontalSpacer_other_setting = QSpacerItem(308, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_other_setting.addItem(self.horizontalSpacer_other_setting)


        self.verticalLayout_general.addWidget(self.widget_other_setting)

        self.groupBox_player_setting = QGroupBox(AutoLoginParam)
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

        self.gridLayout_player_setting.addWidget(self.lineEdit_1p_hwnd, 0, 1, 1, 1)

        self.pushButton_1p_hwnd = QPushButton(self.groupBox_player_setting)
        self.pushButton_1p_hwnd.setObjectName(u"pushButton_1p_hwnd")
        self.pushButton_1p_hwnd.setMinimumSize(QSize(80, 30))
        self.pushButton_1p_hwnd.setMaximumSize(QSize(40, 30))

        self.gridLayout_player_setting.addWidget(self.pushButton_1p_hwnd, 0, 2, 1, 1)

        self.label_2p_hwnd = QLabel(self.groupBox_player_setting)
        self.label_2p_hwnd.setObjectName(u"label_2p_hwnd")
        self.label_2p_hwnd.setMinimumSize(QSize(65, 0))
        self.label_2p_hwnd.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_2p_hwnd, 0, 3, 1, 1)

        self.lineEdit_2p_hwnd = QLineEdit(self.groupBox_player_setting)
        self.lineEdit_2p_hwnd.setObjectName(u"lineEdit_2p_hwnd")
        self.lineEdit_2p_hwnd.setMinimumSize(QSize(0, 30))
        self.lineEdit_2p_hwnd.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_player_setting.addWidget(self.lineEdit_2p_hwnd, 0, 4, 1, 1)

        self.pushButton_2p_hwnd = QPushButton(self.groupBox_player_setting)
        self.pushButton_2p_hwnd.setObjectName(u"pushButton_2p_hwnd")
        self.pushButton_2p_hwnd.setMinimumSize(QSize(80, 30))
        self.pushButton_2p_hwnd.setMaximumSize(QSize(40, 30))

        self.gridLayout_player_setting.addWidget(self.pushButton_2p_hwnd, 0, 5, 1, 1)

        self.label_1p_login_way = QLabel(self.groupBox_player_setting)
        self.label_1p_login_way.setObjectName(u"label_1p_login_way")
        self.label_1p_login_way.setMinimumSize(QSize(65, 0))
        self.label_1p_login_way.setMaximumSize(QSize(65, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_1p_login_way, 1, 0, 1, 1)

        self.comboBox_1p_login_way = QComboBox(self.groupBox_player_setting)
        self.comboBox_1p_login_way.addItem("")
        self.comboBox_1p_login_way.addItem("")
        self.comboBox_1p_login_way.setObjectName(u"comboBox_1p_login_way")
        self.comboBox_1p_login_way.setMinimumSize(QSize(0, 30))
        self.comboBox_1p_login_way.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_player_setting.addWidget(self.comboBox_1p_login_way, 1, 1, 1, 2)

        self.label_2p_login_way = QLabel(self.groupBox_player_setting)
        self.label_2p_login_way.setObjectName(u"label_2p_login_way")
        self.label_2p_login_way.setMinimumSize(QSize(65, 0))
        self.label_2p_login_way.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_2p_login_way, 1, 3, 1, 1)

        self.comboBox_2p_login_way = QComboBox(self.groupBox_player_setting)
        self.comboBox_2p_login_way.addItem("")
        self.comboBox_2p_login_way.addItem("")
        self.comboBox_2p_login_way.setObjectName(u"comboBox_2p_login_way")
        self.comboBox_2p_login_way.setMinimumSize(QSize(0, 30))
        self.comboBox_2p_login_way.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_player_setting.addWidget(self.comboBox_2p_login_way, 1, 4, 1, 2)

        self.label_1p_server_no = QLabel(self.groupBox_player_setting)
        self.label_1p_server_no.setObjectName(u"label_1p_server_no")
        self.label_1p_server_no.setMinimumSize(QSize(65, 0))
        self.label_1p_server_no.setMaximumSize(QSize(65, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_1p_server_no, 2, 0, 1, 1)

        self.lineEdit_1p_server_no = QLineEdit(self.groupBox_player_setting)
        self.lineEdit_1p_server_no.setObjectName(u"lineEdit_1p_server_no")
        self.lineEdit_1p_server_no.setMinimumSize(QSize(0, 30))
        self.lineEdit_1p_server_no.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_player_setting.addWidget(self.lineEdit_1p_server_no, 2, 1, 1, 2)

        self.label_2p_server_no = QLabel(self.groupBox_player_setting)
        self.label_2p_server_no.setObjectName(u"label_2p_server_no")
        self.label_2p_server_no.setMinimumSize(QSize(65, 0))
        self.label_2p_server_no.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_player_setting.addWidget(self.label_2p_server_no, 2, 3, 1, 1)

        self.lineEdit_2p_server_no = QLineEdit(self.groupBox_player_setting)
        self.lineEdit_2p_server_no.setObjectName(u"lineEdit_2p_server_no")
        self.lineEdit_2p_server_no.setMinimumSize(QSize(0, 30))
        self.lineEdit_2p_server_no.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_player_setting.addWidget(self.lineEdit_2p_server_no, 2, 4, 1, 2)


        self.verticalLayout_general.addWidget(self.groupBox_player_setting)

        self.verticalSpacer_bottom = QSpacerItem(20, 179, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_general.addItem(self.verticalSpacer_bottom)


        self.retranslateUi(AutoLoginParam)

        QMetaObject.connectSlotsByName(AutoLoginParam)
    # setupUi

    def retranslateUi(self, AutoLoginParam):
        AutoLoginParam.setWindowTitle(QCoreApplication.translate("AutoLoginParam", u"Form", None))
        self.label_dsc.setText(QCoreApplication.translate("AutoLoginParam", u"<html><head/><body><p><span style=\" color:#00aa00;\">\u4f7f\u7528\u672c\u529f\u80fd\u65f6\uff0c\u52a1\u5fc5\u4f7f\u5b83\u7d27\u8ddf\u5728[\u5f00\u59cb]\u529f\u80fd\u540e\uff0c\u5426\u5219\u4e0d\u4f1a\u6267\u884c</span></p></body></html>", None))
        self.label_start_delay.setText(QCoreApplication.translate("AutoLoginParam", u"\u542f\u52a8\u5012\u8ba1\u65f6", None))
        self.lineEdit_start_delay.setText(QCoreApplication.translate("AutoLoginParam", u"60", None))
        self.label_start_delay_unit.setText(QCoreApplication.translate("AutoLoginParam", u"\u5206\u949f", None))
        self.groupBox_player_setting.setTitle(QCoreApplication.translate("AutoLoginParam", u"\u8d26\u53f7\u8bbe\u7f6e", None))
        self.label_1p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"\u623f\u4e3b\u53e5\u67c4\uff1a", None))
        self.lineEdit_1p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"0", None))
        self.pushButton_1p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"\u83b7\u53d6", None))
        self.label_2p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"\u623f\u5ba2\u53e5\u67c4\uff1a", None))
        self.lineEdit_2p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"0", None))
        self.pushButton_2p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"\u83b7\u53d6", None))
        self.label_1p_login_way.setText(QCoreApplication.translate("AutoLoginParam", u"\u767b\u5f55\u65b9\u5f0f\uff1a", None))
        self.comboBox_1p_login_way.setItemText(0, QCoreApplication.translate("AutoLoginParam", u"\u5fae\u7aef", None))
        self.comboBox_1p_login_way.setItemText(1, QCoreApplication.translate("AutoLoginParam", u"360\u6e38\u620f\u5927\u5385", None))

        self.label_2p_login_way.setText(QCoreApplication.translate("AutoLoginParam", u"\u767b\u5f55\u65b9\u5f0f\uff1a", None))
        self.comboBox_2p_login_way.setItemText(0, QCoreApplication.translate("AutoLoginParam", u"\u5fae\u7aef", None))
        self.comboBox_2p_login_way.setItemText(1, QCoreApplication.translate("AutoLoginParam", u"360\u6e38\u620f\u5927\u5385", None))

        self.label_1p_server_no.setText(QCoreApplication.translate("AutoLoginParam", u"\u623f\u4e3b\u533a\u670d\uff1a", None))
        self.lineEdit_1p_server_no.setText(QCoreApplication.translate("AutoLoginParam", u"4", None))
        self.label_2p_server_no.setText(QCoreApplication.translate("AutoLoginParam", u"\u623f\u5ba2\u533a\u670d\uff1a", None))
        self.lineEdit_2p_server_no.setText(QCoreApplication.translate("AutoLoginParam", u"4", None))
    # retranslateUi

