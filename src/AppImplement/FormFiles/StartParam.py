# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartParam.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_StartParam(object):
    def setupUi(self, StartParam):
        if not StartParam.objectName():
            StartParam.setObjectName(u"StartParam")
        StartParam.resize(400, 300)
        self.verticalLayout_general = QVBoxLayout(StartParam)
        self.verticalLayout_general.setSpacing(10)
        self.verticalLayout_general.setObjectName(u"verticalLayout_general")
        self.verticalLayout_general.setContentsMargins(0, 10, 0, 0)
        self.label_dsc = QLabel(StartParam)
        self.label_dsc.setObjectName(u"label_dsc")
        self.label_dsc.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_general.addWidget(self.label_dsc)

        self.groupBox_player_hwnd = QGroupBox(StartParam)
        self.groupBox_player_hwnd.setObjectName(u"groupBox_player_hwnd")
        self.groupBox_player_hwnd.setMaximumSize(QSize(16777215, 60))
        self.groupBox_player_hwnd.setFlat(True)
        self.horizontalLayout_player_hwnd = QHBoxLayout(self.groupBox_player_hwnd)
        self.horizontalLayout_player_hwnd.setSpacing(5)
        self.horizontalLayout_player_hwnd.setObjectName(u"horizontalLayout_player_hwnd")
        self.horizontalLayout_player_hwnd.setContentsMargins(0, 0, 0, 0)
        self.label_1p_hwnd = QLabel(self.groupBox_player_hwnd)
        self.label_1p_hwnd.setObjectName(u"label_1p_hwnd")
        self.label_1p_hwnd.setMinimumSize(QSize(65, 0))
        self.label_1p_hwnd.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_player_hwnd.addWidget(self.label_1p_hwnd)

        self.lineEdit_1p_hwnd = QLineEdit(self.groupBox_player_hwnd)
        self.lineEdit_1p_hwnd.setObjectName(u"lineEdit_1p_hwnd")
        self.lineEdit_1p_hwnd.setMinimumSize(QSize(0, 30))
        self.lineEdit_1p_hwnd.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_player_hwnd.addWidget(self.lineEdit_1p_hwnd)

        self.pushButton_1p_hwnd = QPushButton(self.groupBox_player_hwnd)
        self.pushButton_1p_hwnd.setObjectName(u"pushButton_1p_hwnd")
        self.pushButton_1p_hwnd.setMinimumSize(QSize(40, 30))
        self.pushButton_1p_hwnd.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_player_hwnd.addWidget(self.pushButton_1p_hwnd)

        self.label_2p_hwnd = QLabel(self.groupBox_player_hwnd)
        self.label_2p_hwnd.setObjectName(u"label_2p_hwnd")
        self.label_2p_hwnd.setMinimumSize(QSize(65, 0))
        self.label_2p_hwnd.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_player_hwnd.addWidget(self.label_2p_hwnd)

        self.lineEdit_2p_hwnd = QLineEdit(self.groupBox_player_hwnd)
        self.lineEdit_2p_hwnd.setObjectName(u"lineEdit_2p_hwnd")
        self.lineEdit_2p_hwnd.setMinimumSize(QSize(0, 30))
        self.lineEdit_2p_hwnd.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_player_hwnd.addWidget(self.lineEdit_2p_hwnd)

        self.pushButton_2p_hwnd = QPushButton(self.groupBox_player_hwnd)
        self.pushButton_2p_hwnd.setObjectName(u"pushButton_2p_hwnd")
        self.pushButton_2p_hwnd.setMinimumSize(QSize(40, 30))
        self.pushButton_2p_hwnd.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_player_hwnd.addWidget(self.pushButton_2p_hwnd)


        self.verticalLayout_general.addWidget(self.groupBox_player_hwnd)

        self.groupBox_necessity_pic = QGroupBox(StartParam)
        self.groupBox_necessity_pic.setObjectName(u"groupBox_necessity_pic")
        self.groupBox_necessity_pic.setMaximumSize(QSize(16777215, 60))
        self.groupBox_necessity_pic.setFlat(True)
        self.horizontalLayout_necessity_pic = QHBoxLayout(self.groupBox_necessity_pic)
        self.horizontalLayout_necessity_pic.setSpacing(5)
        self.horizontalLayout_necessity_pic.setObjectName(u"horizontalLayout_necessity_pic")
        self.horizontalLayout_necessity_pic.setContentsMargins(0, 0, 0, 0)
        self.label_2p_name_pic = QLabel(self.groupBox_necessity_pic)
        self.label_2p_name_pic.setObjectName(u"label_2p_name_pic")
        self.label_2p_name_pic.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_necessity_pic.addWidget(self.label_2p_name_pic)

        self.lineEdit_2p_name_pic = QLineEdit(self.groupBox_necessity_pic)
        self.lineEdit_2p_name_pic.setObjectName(u"lineEdit_2p_name_pic")
        self.lineEdit_2p_name_pic.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_necessity_pic.addWidget(self.lineEdit_2p_name_pic)

        self.pushButton_2p_name_pic = QPushButton(self.groupBox_necessity_pic)
        self.pushButton_2p_name_pic.setObjectName(u"pushButton_2p_name_pic")
        self.pushButton_2p_name_pic.setMinimumSize(QSize(40, 30))
        self.pushButton_2p_name_pic.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_necessity_pic.addWidget(self.pushButton_2p_name_pic)


        self.verticalLayout_general.addWidget(self.groupBox_necessity_pic)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_general.addItem(self.verticalSpacer_bottom)


        self.retranslateUi(StartParam)

        QMetaObject.connectSlotsByName(StartParam)
    # setupUi

    def retranslateUi(self, StartParam):
        StartParam.setWindowTitle(QCoreApplication.translate("StartParam", u"Form", None))
        self.label_dsc.setText(QCoreApplication.translate("StartParam", u"\u8bbe\u7f6e\u6574\u4e2a\u6d41\u7a0b\u4e2d\u6240\u9700\u7684\u5168\u5c40\u4fe1\u606f", None))
        self.groupBox_player_hwnd.setTitle(QCoreApplication.translate("StartParam", u"\u8d26\u53f7\u53e5\u67c4", None))
        self.label_1p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u623f\u4e3b\u53e5\u67c4\uff1a", None))
        self.pushButton_1p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u83b7\u53d6", None))
        self.label_2p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u623f\u5ba2\u53e5\u67c4\uff1a", None))
        self.pushButton_2p_hwnd.setText(QCoreApplication.translate("StartParam", u"\u83b7\u53d6", None))
        self.groupBox_necessity_pic.setTitle(QCoreApplication.translate("StartParam", u"\u5fc5\u8981\u56fe\u7247", None))
        self.label_2p_name_pic.setText(QCoreApplication.translate("StartParam", u"2P\u6635\u79f0\u8def\u5f84", None))
        self.pushButton_2p_name_pic.setText(QCoreApplication.translate("StartParam", u"\u6d4f\u89c8", None))
    # retranslateUi

