# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoversQuestParam.ui'
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

class Ui_LoversQuestParam(object):
    def setupUi(self, LoversQuestParam):
        if not LoversQuestParam.objectName():
            LoversQuestParam.setObjectName(u"LoversQuestParam")
        LoversQuestParam.resize(530, 340)
        self.verticalLayout = QVBoxLayout(LoversQuestParam)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.widget_dcs = QWidget(LoversQuestParam)
        self.widget_dcs.setObjectName(u"widget_dcs")
        self.verticalLayout_dsc = QVBoxLayout(self.widget_dcs)
        self.verticalLayout_dsc.setSpacing(5)
        self.verticalLayout_dsc.setObjectName(u"verticalLayout_dsc")
        self.verticalLayout_dsc.setContentsMargins(-1, 0, -1, 10)
        self.label_dsc = QLabel(self.widget_dcs)
        self.label_dsc.setObjectName(u"label_dsc")
        self.label_dsc.setWordWrap(True)

        self.verticalLayout_dsc.addWidget(self.label_dsc)


        self.verticalLayout.addWidget(self.widget_dcs)

        self.groupBox_select_players = QGroupBox(LoversQuestParam)
        self.groupBox_select_players.setObjectName(u"groupBox_select_players")
        self.horizontalLayout_select_players = QHBoxLayout(self.groupBox_select_players)
        self.horizontalLayout_select_players.setSpacing(5)
        self.horizontalLayout_select_players.setObjectName(u"horizontalLayout_select_players")
        self.horizontalLayout_select_players.setContentsMargins(-1, 0, -1, 5)
        self.label_select_1p = QLabel(self.groupBox_select_players)
        self.label_select_1p.setObjectName(u"label_select_1p")
        self.label_select_1p.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_select_players.addWidget(self.label_select_1p)

        self.comboBox_select_1p = QComboBox(self.groupBox_select_players)
        self.comboBox_select_1p.addItem("")
        self.comboBox_select_1p.addItem("")
        self.comboBox_select_1p.setObjectName(u"comboBox_select_1p")
        self.comboBox_select_1p.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_players.addWidget(self.comboBox_select_1p)

        self.label_select_2p = QLabel(self.groupBox_select_players)
        self.label_select_2p.setObjectName(u"label_select_2p")
        self.label_select_2p.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_select_players.addWidget(self.label_select_2p)

        self.comboBox_select_2p = QComboBox(self.groupBox_select_players)
        self.comboBox_select_2p.addItem("")
        self.comboBox_select_2p.addItem("")
        self.comboBox_select_2p.addItem("")
        self.comboBox_select_2p.setObjectName(u"comboBox_select_2p")
        self.comboBox_select_2p.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_players.addWidget(self.comboBox_select_2p)


        self.verticalLayout.addWidget(self.groupBox_select_players)

        self.groupBox_file_path = QGroupBox(LoversQuestParam)
        self.groupBox_file_path.setObjectName(u"groupBox_file_path")
        self.horizontalLayout_file_path = QHBoxLayout(self.groupBox_file_path)
        self.horizontalLayout_file_path.setSpacing(5)
        self.horizontalLayout_file_path.setObjectName(u"horizontalLayout_file_path")
        self.horizontalLayout_file_path.setContentsMargins(-1, 0, -1, 5)
        self.label_file_path = QLabel(self.groupBox_file_path)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setMinimumSize(QSize(80, 0))
        self.label_file_path.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_file_path.addWidget(self.label_file_path)

        self.lineEdit_file_path = QLineEdit(self.groupBox_file_path)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")
        self.lineEdit_file_path.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_file_path.addWidget(self.lineEdit_file_path)

        self.pushButton_file_path = QPushButton(self.groupBox_file_path)
        self.pushButton_file_path.setObjectName(u"pushButton_file_path")
        self.pushButton_file_path.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_file_path.addWidget(self.pushButton_file_path)


        self.verticalLayout.addWidget(self.groupBox_file_path)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)

        self.retranslateUi(LoversQuestParam)

        QMetaObject.connectSlotsByName(LoversQuestParam)
    # setupUi

    def retranslateUi(self, LoversQuestParam):
        LoversQuestParam.setWindowTitle(QCoreApplication.translate("LoversQuestParam", u"Form", None))
        self.label_dsc.setText(QCoreApplication.translate("LoversQuestParam", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u60c5\u4fa3\u4efb\u52a1\u622a\u56fe\u6587\u4ef6\u7684\u540d\u79f0\u683c\u5f0f\uff1a\u5730\u56fe\u533a\u57df-\u5173\u5361\u540d\u79f0-\u901a\u5173\u7b56\u7565-\u653e\u5361\u65b9\u6848</span></p><p><span style=\" color:#00aa00;\">&lt;\u5730\u56fe\u533a\u57df&gt;\u8868\u793a\u201c\u4e16\u754c\u5730\u56fe\u201d\u4e0a\u663e\u793a\u7684\u533a\u57df\u540d\u79f0\uff1b</span></p><p><span style=\" color:#00aa00;\">&lt;\u5173\u5361\u540d\u79f0&gt;\u8868\u793a\u5404\u5730\u56fe\u533a\u57df\u4e2d\u663e\u793a\u7684\u5173\u5361\u540d\u79f0\uff0c\u5fc5\u987b\u4e25\u683c\u5bf9\u5e94\u754c\u9762\u4e0a\u6240\u663e\u793a\u7684\u540d\u79f0\u3002\u540d\u79f0\u91cd\u590d\u7684\u5173\u5361\u52a0\u4e0a\u201c\u65e5/\u591c\u201d\u3001\u201c\u6c34/\u9646\u201d\u5355\u4e2a\u5b57\uff0c\u4e0d\u8981\u62ec\u53f7\uff1b</span></p><p><span style=\" color:#00aa00;\">&lt;\u901a\u5173\u7b56\u7565&gt;\u586b\u5199\u201c\u65e0\u4e8c\u9636\u6bb5\u201d\u3001\u201c\u7ee7\u7eed\u6311\u6218\u201d\u3001"
                        "\u201c\u9886\u53d6\u5956\u52b1\u201d\u3001\u201c\u8df3\u8fc7\u201d\u4e4b\u4e2d\u7684\u4e00\u4e2a\uff1b</span></p><p><span style=\" color:#00aa00;\">&lt;\u653e\u5361\u65b9\u6848&gt;\u586b\u5199ini\u6587\u4ef6\u4e2d\u8be5\u4efb\u52a1\u6240\u7528\u7684\u653e\u5361\u65b9\u6848\u540d\u79f0\uff0c\u82e5\u4e0d\u586b\u5199\uff0c\u5219\u9ed8\u8ba4\u4f7f\u7528\u4e0e&lt;\u5173\u5361\u540d\u79f0&gt;\u76f8\u540c\u7684\u65b9\u6848</span></p></body></html>", None))
        self.groupBox_select_players.setTitle(QCoreApplication.translate("LoversQuestParam", u"\u9009\u62e9\u8d26\u53f7", None))
        self.label_select_1p.setText(QCoreApplication.translate("LoversQuestParam", u"\u623f\u4e3b\uff1a", None))
        self.comboBox_select_1p.setItemText(0, QCoreApplication.translate("LoversQuestParam", u"1P", None))
        self.comboBox_select_1p.setItemText(1, QCoreApplication.translate("LoversQuestParam", u"2P", None))

        self.label_select_2p.setText(QCoreApplication.translate("LoversQuestParam", u"\u623f\u5ba2\uff1a", None))
        self.comboBox_select_2p.setItemText(0, QCoreApplication.translate("LoversQuestParam", u"\u65e0", None))
        self.comboBox_select_2p.setItemText(1, QCoreApplication.translate("LoversQuestParam", u"1P", None))
        self.comboBox_select_2p.setItemText(2, QCoreApplication.translate("LoversQuestParam", u"2P", None))

        self.groupBox_file_path.setTitle(QCoreApplication.translate("LoversQuestParam", u"\u9009\u62e9\u65b9\u6848", None))
        self.label_file_path.setText(QCoreApplication.translate("LoversQuestParam", u"\u653e\u5361\u65b9\u6848\u8def\u5f84\uff1a", None))
        self.pushButton_file_path.setText(QCoreApplication.translate("LoversQuestParam", u"\u6d4f\u89c8", None))
    # retranslateUi

