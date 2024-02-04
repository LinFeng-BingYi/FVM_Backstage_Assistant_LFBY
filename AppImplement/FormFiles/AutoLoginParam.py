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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTimeEdit, QVBoxLayout, QWidget)

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

        self.groupBox_start_way = QGroupBox(AutoLoginParam)
        self.groupBox_start_way.setObjectName(u"groupBox_start_way")
        self.groupBox_start_way.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_start_way = QHBoxLayout(self.groupBox_start_way)
        self.horizontalLayout_start_way.setSpacing(5)
        self.horizontalLayout_start_way.setObjectName(u"horizontalLayout_start_way")
        self.horizontalLayout_start_way.setContentsMargins(-1, 0, -1, 5)
        self.radioButton_start_time = QRadioButton(self.groupBox_start_way)
        self.radioButton_start_time.setObjectName(u"radioButton_start_time")
        self.radioButton_start_time.setMinimumSize(QSize(65, 0))
        self.radioButton_start_time.setMaximumSize(QSize(65, 16777215))
        self.radioButton_start_time.setChecked(True)

        self.horizontalLayout_start_way.addWidget(self.radioButton_start_time)

        self.timeEdit_start_time = QTimeEdit(self.groupBox_start_way)
        self.timeEdit_start_time.setObjectName(u"timeEdit_start_time")
        self.timeEdit_start_time.setMinimumSize(QSize(0, 30))
        self.timeEdit_start_time.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 1, 0)))
        self.timeEdit_start_time.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_start_way.addWidget(self.timeEdit_start_time)

        self.radioButton_start_delay = QRadioButton(self.groupBox_start_way)
        self.radioButton_start_delay.setObjectName(u"radioButton_start_delay")
        self.radioButton_start_delay.setMinimumSize(QSize(65, 0))
        self.radioButton_start_delay.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_start_way.addWidget(self.radioButton_start_delay)

        self.doubleSpinBox_start_delay = QDoubleSpinBox(self.groupBox_start_way)
        self.doubleSpinBox_start_delay.setObjectName(u"doubleSpinBox_start_delay")
        self.doubleSpinBox_start_delay.setMinimumSize(QSize(0, 30))
        self.doubleSpinBox_start_delay.setDecimals(1)
        self.doubleSpinBox_start_delay.setValue(60.000000000000000)

        self.horizontalLayout_start_way.addWidget(self.doubleSpinBox_start_delay)


        self.verticalLayout_general.addWidget(self.groupBox_start_way)

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
        self.groupBox_start_way.setTitle(QCoreApplication.translate("AutoLoginParam", u"\u542f\u52a8\u65b9\u5f0f", None))
        self.radioButton_start_time.setText(QCoreApplication.translate("AutoLoginParam", u"\u65f6\u95f4\u70b9", None))
        self.timeEdit_start_time.setDisplayFormat(QCoreApplication.translate("AutoLoginParam", u"HH:mm:ss", None))
        self.radioButton_start_delay.setText(QCoreApplication.translate("AutoLoginParam", u"\u5012\u8ba1\u65f6", None))
        self.doubleSpinBox_start_delay.setSuffix(QCoreApplication.translate("AutoLoginParam", u"min", None))
        self.groupBox_player_setting.setTitle(QCoreApplication.translate("AutoLoginParam", u"\u8d26\u53f7\u8bbe\u7f6e", None))
        self.label_1p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"\u623f\u4e3b\u53e5\u67c4\uff1a", None))
        self.lineEdit_1p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"0", None))
        self.pushButton_1p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"\u83b7\u53d6", None))
        self.label_2p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"\u623f\u5ba2\u53e5\u67c4\uff1a", None))
        self.lineEdit_2p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"0", None))
        self.pushButton_2p_hwnd.setText(QCoreApplication.translate("AutoLoginParam", u"\u83b7\u53d6", None))
        self.label_1p_login_way.setText(QCoreApplication.translate("AutoLoginParam", u"\u767b\u5f55\u65b9\u5f0f\uff1a", None))
        self.comboBox_1p_login_way.setItemText(0, QCoreApplication.translate("AutoLoginParam", u"\u5fae\u7aef", None))
        self.comboBox_1p_login_way.setItemText(1, QCoreApplication.translate("AutoLoginParam", u"360\u6e38\u620f\u5927\u5385-4399\u670d", None))
        self.comboBox_1p_login_way.setItemText(2, QCoreApplication.translate("AutoLoginParam", u"360\u6e38\u620f\u5927\u5385-\u7a7a\u95f43366\u670d", None))

        self.label_2p_login_way.setText(QCoreApplication.translate("AutoLoginParam", u"\u767b\u5f55\u65b9\u5f0f\uff1a", None))
        self.comboBox_2p_login_way.setItemText(0, QCoreApplication.translate("AutoLoginParam", u"\u5fae\u7aef", None))
        self.comboBox_2p_login_way.setItemText(1, QCoreApplication.translate("AutoLoginParam", u"360\u6e38\u620f\u5927\u5385-4399\u670d", None))
        self.comboBox_2p_login_way.setItemText(2, QCoreApplication.translate("AutoLoginParam", u"360\u6e38\u620f\u5927\u5385-\u7a7a\u95f43366\u670d", None))

        self.label_1p_server_no.setText(QCoreApplication.translate("AutoLoginParam", u"\u623f\u4e3b\u533a\u670d\uff1a", None))
        self.lineEdit_1p_server_no.setText(QCoreApplication.translate("AutoLoginParam", u"4", None))
        self.label_2p_server_no.setText(QCoreApplication.translate("AutoLoginParam", u"\u623f\u5ba2\u533a\u670d\uff1a", None))
        self.lineEdit_2p_server_no.setText(QCoreApplication.translate("AutoLoginParam", u"4", None))
    # retranslateUi

