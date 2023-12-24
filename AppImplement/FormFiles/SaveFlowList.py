# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SaveFlowList.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SaveFlowList(object):
    def setupUi(self, SaveFlowList):
        if not SaveFlowList.objectName():
            SaveFlowList.setObjectName(u"SaveFlowList")
        SaveFlowList.resize(386, 199)
        self.gridLayout_top = QGridLayout(SaveFlowList)
        self.gridLayout_top.setSpacing(5)
        self.gridLayout_top.setObjectName(u"gridLayout_top")
        self.gridLayout_top.setContentsMargins(0, 0, 0, 0)
        self.widget_general = QWidget(SaveFlowList)
        self.widget_general.setObjectName(u"widget_general")
        self.verticalLayout_general = QVBoxLayout(self.widget_general)
        self.verticalLayout_general.setSpacing(5)
        self.verticalLayout_general.setObjectName(u"verticalLayout_general")
        self.verticalLayout_general.setContentsMargins(0, 5, 0, 5)
        self.widget_file_path = QWidget(self.widget_general)
        self.widget_file_path.setObjectName(u"widget_file_path")
        self.horizontalLayout_file_path = QHBoxLayout(self.widget_file_path)
        self.horizontalLayout_file_path.setSpacing(5)
        self.horizontalLayout_file_path.setObjectName(u"horizontalLayout_file_path")
        self.horizontalLayout_file_path.setContentsMargins(-1, 0, -1, 0)
        self.label_flow_file = QLabel(self.widget_file_path)
        self.label_flow_file.setObjectName(u"label_flow_file")
        self.label_flow_file.setMinimumSize(QSize(65, 0))

        self.horizontalLayout_file_path.addWidget(self.label_flow_file)

        self.lineEdit_flow_file = QLineEdit(self.widget_file_path)
        self.lineEdit_flow_file.setObjectName(u"lineEdit_flow_file")
        self.lineEdit_flow_file.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_file_path.addWidget(self.lineEdit_flow_file)

        self.pushButton_flow_file = QPushButton(self.widget_file_path)
        self.pushButton_flow_file.setObjectName(u"pushButton_flow_file")
        self.pushButton_flow_file.setMinimumSize(QSize(80, 30))
        self.pushButton_flow_file.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_file_path.addWidget(self.pushButton_flow_file)


        self.verticalLayout_general.addWidget(self.widget_file_path)

        self.groupBox_file_dsc = QGroupBox(self.widget_general)
        self.groupBox_file_dsc.setObjectName(u"groupBox_file_dsc")
        self.verticalLayout_file_dsc = QVBoxLayout(self.groupBox_file_dsc)
        self.verticalLayout_file_dsc.setSpacing(5)
        self.verticalLayout_file_dsc.setObjectName(u"verticalLayout_file_dsc")
        self.verticalLayout_file_dsc.setContentsMargins(-1, 0, -1, 5)
        self.plainTextEdit = QPlainTextEdit(self.groupBox_file_dsc)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_file_dsc.addWidget(self.plainTextEdit)


        self.verticalLayout_general.addWidget(self.groupBox_file_dsc)

        self.widget_button = QWidget(self.widget_general)
        self.widget_button.setObjectName(u"widget_button")
        self.horizontalLayout_button = QHBoxLayout(self.widget_button)
        self.horizontalLayout_button.setSpacing(5)
        self.horizontalLayout_button.setObjectName(u"horizontalLayout_button")
        self.horizontalLayout_button.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_button_1 = QSpacerItem(66, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_button.addItem(self.horizontalSpacer_button_1)

        self.pushButton_apply = QPushButton(self.widget_button)
        self.pushButton_apply.setObjectName(u"pushButton_apply")
        self.pushButton_apply.setMinimumSize(QSize(80, 30))
        self.pushButton_apply.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_button.addWidget(self.pushButton_apply)

        self.horizontalSpacer_button_2 = QSpacerItem(65, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_button.addItem(self.horizontalSpacer_button_2)

        self.pushButton_save = QPushButton(self.widget_button)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(80, 30))
        self.pushButton_save.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_button.addWidget(self.pushButton_save)

        self.horizontalSpacer_button_3 = QSpacerItem(66, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_button.addItem(self.horizontalSpacer_button_3)


        self.verticalLayout_general.addWidget(self.widget_button)


        self.gridLayout_top.addWidget(self.widget_general, 0, 0, 1, 1)


        self.retranslateUi(SaveFlowList)

        QMetaObject.connectSlotsByName(SaveFlowList)
    # setupUi

    def retranslateUi(self, SaveFlowList):
        SaveFlowList.setWindowTitle(QCoreApplication.translate("SaveFlowList", u"\u4fdd\u5b58\u529f\u80fd\u6d41\u7a0b\u5217\u8868\u53c2\u6570", None))
        self.label_flow_file.setText(QCoreApplication.translate("SaveFlowList", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.pushButton_flow_file.setText(QCoreApplication.translate("SaveFlowList", u"\u6d4f\u89c8", None))
        self.groupBox_file_dsc.setTitle(QCoreApplication.translate("SaveFlowList", u"\u6d41\u7a0b\u63cf\u8ff0", None))
        self.pushButton_apply.setText(QCoreApplication.translate("SaveFlowList", u"\u5e94\u7528", None))
        self.pushButton_save.setText(QCoreApplication.translate("SaveFlowList", u"\u4fdd\u5b58", None))
    # retranslateUi

