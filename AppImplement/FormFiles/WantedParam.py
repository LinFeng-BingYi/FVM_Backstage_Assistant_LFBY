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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_WantedParam(object):
    def setupUi(self, WantedParam):
        if not WantedParam.objectName():
            WantedParam.setObjectName(u"WantedParam")
        WantedParam.resize(522, 340)
        self.verticalLayout_top = QVBoxLayout(WantedParam)
        self.verticalLayout_top.setSpacing(0)
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.verticalLayout_top.setContentsMargins(3, 10, 3, 3)
        self.groupBox_mwd = QGroupBox(WantedParam)
        self.groupBox_mwd.setObjectName(u"groupBox_mwd")
        self.horizontalLayout_mwd = QHBoxLayout(self.groupBox_mwd)
        self.horizontalLayout_mwd.setSpacing(5)
        self.horizontalLayout_mwd.setObjectName(u"horizontalLayout_mwd")
        self.horizontalLayout_mwd.setContentsMargins(-1, 0, -1, 5)
        self.checkBox_enable_mwd = QCheckBox(self.groupBox_mwd)
        self.checkBox_enable_mwd.setObjectName(u"checkBox_enable_mwd")
        self.checkBox_enable_mwd.setMinimumSize(QSize(60, 0))
        self.checkBox_enable_mwd.setMaximumSize(QSize(60, 16777215))
        self.checkBox_enable_mwd.setChecked(True)

        self.horizontalLayout_mwd.addWidget(self.checkBox_enable_mwd)

        self.label_plan_mwd = QLabel(self.groupBox_mwd)
        self.label_plan_mwd.setObjectName(u"label_plan_mwd")
        self.label_plan_mwd.setMinimumSize(QSize(60, 0))
        self.label_plan_mwd.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_mwd.addWidget(self.label_plan_mwd)

        self.comboBox_plan_mwd = QComboBox(self.groupBox_mwd)
        self.comboBox_plan_mwd.setObjectName(u"comboBox_plan_mwd")
        self.comboBox_plan_mwd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_mwd.addWidget(self.comboBox_plan_mwd)

        self.pushButton_plan_mwd = QPushButton(self.groupBox_mwd)
        self.pushButton_plan_mwd.setObjectName(u"pushButton_plan_mwd")
        self.pushButton_plan_mwd.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_mwd.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_mwd.addWidget(self.pushButton_plan_mwd)


        self.verticalLayout_top.addWidget(self.groupBox_mwd)

        self.groupBox_hsd = QGroupBox(WantedParam)
        self.groupBox_hsd.setObjectName(u"groupBox_hsd")
        self.horizontalLayout_hsd = QHBoxLayout(self.groupBox_hsd)
        self.horizontalLayout_hsd.setSpacing(5)
        self.horizontalLayout_hsd.setObjectName(u"horizontalLayout_hsd")
        self.horizontalLayout_hsd.setContentsMargins(-1, 0, -1, 5)
        self.checkBox_enable_hsd = QCheckBox(self.groupBox_hsd)
        self.checkBox_enable_hsd.setObjectName(u"checkBox_enable_hsd")
        self.checkBox_enable_hsd.setMinimumSize(QSize(60, 0))
        self.checkBox_enable_hsd.setMaximumSize(QSize(60, 16777215))
        self.checkBox_enable_hsd.setChecked(True)

        self.horizontalLayout_hsd.addWidget(self.checkBox_enable_hsd)

        self.label_plan_hsd = QLabel(self.groupBox_hsd)
        self.label_plan_hsd.setObjectName(u"label_plan_hsd")
        self.label_plan_hsd.setMinimumSize(QSize(60, 0))
        self.label_plan_hsd.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_hsd.addWidget(self.label_plan_hsd)

        self.comboBox_plan_hsd = QComboBox(self.groupBox_hsd)
        self.comboBox_plan_hsd.setObjectName(u"comboBox_plan_hsd")
        self.comboBox_plan_hsd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_hsd.addWidget(self.comboBox_plan_hsd)

        self.pushButton_plan_hsd = QPushButton(self.groupBox_hsd)
        self.pushButton_plan_hsd.setObjectName(u"pushButton_plan_hsd")
        self.pushButton_plan_hsd.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_hsd.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_hsd.addWidget(self.pushButton_plan_hsd)


        self.verticalLayout_top.addWidget(self.groupBox_hsd)

        self.groupBox_fkd = QGroupBox(WantedParam)
        self.groupBox_fkd.setObjectName(u"groupBox_fkd")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_fkd)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 5)
        self.checkBox_enable_fkd = QCheckBox(self.groupBox_fkd)
        self.checkBox_enable_fkd.setObjectName(u"checkBox_enable_fkd")
        self.checkBox_enable_fkd.setMinimumSize(QSize(60, 0))
        self.checkBox_enable_fkd.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.checkBox_enable_fkd)

        self.label_plan_fkd = QLabel(self.groupBox_fkd)
        self.label_plan_fkd.setObjectName(u"label_plan_fkd")
        self.label_plan_fkd.setMinimumSize(QSize(60, 0))
        self.label_plan_fkd.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.label_plan_fkd)

        self.comboBox_plan_fkd = QComboBox(self.groupBox_fkd)
        self.comboBox_plan_fkd.setObjectName(u"comboBox_plan_fkd")
        self.comboBox_plan_fkd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.comboBox_plan_fkd)

        self.pushButton_plan_fkd = QPushButton(self.groupBox_fkd)
        self.pushButton_plan_fkd.setObjectName(u"pushButton_plan_fkd")
        self.pushButton_plan_fkd.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_fkd.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_plan_fkd)


        self.verticalLayout_top.addWidget(self.groupBox_fkd)

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

        self.verticalSpacer = QSpacerItem(20, 86, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_top.addItem(self.verticalSpacer)

        self.verticalLayout_top.setStretch(0, 2)
        self.verticalLayout_top.setStretch(1, 2)
        self.verticalLayout_top.setStretch(2, 2)
        self.verticalLayout_top.setStretch(3, 2)
        self.verticalLayout_top.setStretch(4, 3)

        self.retranslateUi(WantedParam)

        QMetaObject.connectSlotsByName(WantedParam)
    # setupUi

    def retranslateUi(self, WantedParam):
        WantedParam.setWindowTitle(QCoreApplication.translate("WantedParam", u"Form", None))
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
        self.groupBox_level_setting.setTitle(QCoreApplication.translate("WantedParam", u"\u901a\u5173\u8bbe\u7f6e", None))
        self.label_flop_pos.setText(QCoreApplication.translate("WantedParam", u"\u7ffb\u724c\u4f4d\u7f6e\uff1a", None))
        self.lineEdit_flop_pos.setText(QCoreApplication.translate("WantedParam", u"1;2", None))
    # retranslateUi

