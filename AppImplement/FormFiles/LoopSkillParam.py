# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoopSkillParam.ui'
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

class Ui_LoopSkillParam(object):
    def setupUi(self, LoopSkillParam):
        if not LoopSkillParam.objectName():
            LoopSkillParam.setObjectName(u"LoopSkillParam")
        LoopSkillParam.resize(530, 340)
        self.verticalLayout_top = QVBoxLayout(LoopSkillParam)
        self.verticalLayout_top.setSpacing(5)
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.verticalLayout_top.setContentsMargins(3, 10, 3, 3)
        self.widget_select_player = QWidget(LoopSkillParam)
        self.widget_select_player.setObjectName(u"widget_select_player")
        self.widget_select_player.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_select_player = QHBoxLayout(self.widget_select_player)
        self.horizontalLayout_select_player.setSpacing(5)
        self.horizontalLayout_select_player.setObjectName(u"horizontalLayout_select_player")
        self.horizontalLayout_select_player.setContentsMargins(-1, 0, -1, 0)
        self.label_select_player = QLabel(self.widget_select_player)
        self.label_select_player.setObjectName(u"label_select_player")
        self.label_select_player.setMinimumSize(QSize(67, 0))

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

        self.groupBox_select_level = QGroupBox(LoopSkillParam)
        self.groupBox_select_level.setObjectName(u"groupBox_select_level")
        self.horizontalLayout_select_level = QHBoxLayout(self.groupBox_select_level)
        self.horizontalLayout_select_level.setSpacing(5)
        self.horizontalLayout_select_level.setObjectName(u"horizontalLayout_select_level")
        self.horizontalLayout_select_level.setContentsMargins(9, 0, -1, 5)
        self.label_zone = QLabel(self.groupBox_select_level)
        self.label_zone.setObjectName(u"label_zone")
        self.label_zone.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_select_level.addWidget(self.label_zone)

        self.comboBox_zone = QComboBox(self.groupBox_select_level)
        self.comboBox_zone.setObjectName(u"comboBox_zone")
        self.comboBox_zone.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_select_level.addWidget(self.comboBox_zone)

        self.label_level = QLabel(self.groupBox_select_level)
        self.label_level.setObjectName(u"label_level")
        self.label_level.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_select_level.addWidget(self.label_level)

        self.comboBox_level = QComboBox(self.groupBox_select_level)
        self.comboBox_level.setObjectName(u"comboBox_level")
        self.comboBox_level.setMinimumSize(QSize(0, 30))
        self.comboBox_level.setEditable(True)

        self.horizontalLayout_select_level.addWidget(self.comboBox_level)

        self.horizontalLayout_select_level.setStretch(0, 1)
        self.horizontalLayout_select_level.setStretch(1, 2)
        self.horizontalLayout_select_level.setStretch(2, 1)
        self.horizontalLayout_select_level.setStretch(3, 2)

        self.verticalLayout_top.addWidget(self.groupBox_select_level)

        self.groupBox_select_plan = QGroupBox(LoopSkillParam)
        self.groupBox_select_plan.setObjectName(u"groupBox_select_plan")
        self.gridLayout_select_plan = QGridLayout(self.groupBox_select_plan)
        self.gridLayout_select_plan.setSpacing(5)
        self.gridLayout_select_plan.setObjectName(u"gridLayout_select_plan")
        self.gridLayout_select_plan.setContentsMargins(-1, 0, -1, 5)
        self.label_plan_path = QLabel(self.groupBox_select_plan)
        self.label_plan_path.setObjectName(u"label_plan_path")
        self.label_plan_path.setMinimumSize(QSize(67, 0))
        self.label_plan_path.setMaximumSize(QSize(67, 30))

        self.gridLayout_select_plan.addWidget(self.label_plan_path, 0, 0, 1, 1)

        self.lineEdit_plan_path = QLineEdit(self.groupBox_select_plan)
        self.lineEdit_plan_path.setObjectName(u"lineEdit_plan_path")
        self.lineEdit_plan_path.setMinimumSize(QSize(0, 30))

        self.gridLayout_select_plan.addWidget(self.lineEdit_plan_path, 0, 1, 1, 1)

        self.pushButton_plan_path = QPushButton(self.groupBox_select_plan)
        self.pushButton_plan_path.setObjectName(u"pushButton_plan_path")
        self.pushButton_plan_path.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_path.setMaximumSize(QSize(80, 30))

        self.gridLayout_select_plan.addWidget(self.pushButton_plan_path, 0, 2, 1, 1)

        self.label_1p_plan = QLabel(self.groupBox_select_plan)
        self.label_1p_plan.setObjectName(u"label_1p_plan")
        self.label_1p_plan.setMaximumSize(QSize(67, 30))

        self.gridLayout_select_plan.addWidget(self.label_1p_plan, 1, 0, 1, 1)

        self.comboBox_1p_plan = QComboBox(self.groupBox_select_plan)
        self.comboBox_1p_plan.setObjectName(u"comboBox_1p_plan")
        self.comboBox_1p_plan.setMinimumSize(QSize(0, 30))

        self.gridLayout_select_plan.addWidget(self.comboBox_1p_plan, 1, 1, 1, 1)

        self.pushButton_view_plan = QPushButton(self.groupBox_select_plan)
        self.pushButton_view_plan.setObjectName(u"pushButton_view_plan")
        self.pushButton_view_plan.setMinimumSize(QSize(80, 30))
        self.pushButton_view_plan.setMaximumSize(QSize(80, 30))

        self.gridLayout_select_plan.addWidget(self.pushButton_view_plan, 1, 2, 1, 1)


        self.verticalLayout_top.addWidget(self.groupBox_select_plan)

        self.groupBox_other_setting = QGroupBox(LoopSkillParam)
        self.groupBox_other_setting.setObjectName(u"groupBox_other_setting")
        self.horizontalLayout_other_setting = QHBoxLayout(self.groupBox_other_setting)
        self.horizontalLayout_other_setting.setSpacing(5)
        self.horizontalLayout_other_setting.setObjectName(u"horizontalLayout_other_setting")
        self.horizontalLayout_other_setting.setContentsMargins(-1, 0, -1, 5)
        self.label_loop_count = QLabel(self.groupBox_other_setting)
        self.label_loop_count.setObjectName(u"label_loop_count")
        self.label_loop_count.setMinimumSize(QSize(67, 0))
        self.label_loop_count.setMaximumSize(QSize(67, 16777215))

        self.horizontalLayout_other_setting.addWidget(self.label_loop_count)

        self.lineEdit_loop_count = QLineEdit(self.groupBox_other_setting)
        self.lineEdit_loop_count.setObjectName(u"lineEdit_loop_count")
        self.lineEdit_loop_count.setMinimumSize(QSize(0, 30))
        self.lineEdit_loop_count.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_other_setting.addWidget(self.lineEdit_loop_count)

        self.label_exit_delay = QLabel(self.groupBox_other_setting)
        self.label_exit_delay.setObjectName(u"label_exit_delay")

        self.horizontalLayout_other_setting.addWidget(self.label_exit_delay)

        self.lineEdit_exit_delay = QLineEdit(self.groupBox_other_setting)
        self.lineEdit_exit_delay.setObjectName(u"lineEdit_exit_delay")
        self.lineEdit_exit_delay.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_other_setting.addWidget(self.lineEdit_exit_delay)


        self.verticalLayout_top.addWidget(self.groupBox_other_setting)

        self.widget_instruction = QWidget(LoopSkillParam)
        self.widget_instruction.setObjectName(u"widget_instruction")
        self.verticalLayout_instruction = QVBoxLayout(self.widget_instruction)
        self.verticalLayout_instruction.setSpacing(5)
        self.verticalLayout_instruction.setObjectName(u"verticalLayout_instruction")
        self.verticalLayout_instruction.setContentsMargins(-1, 0, -1, 0)
        self.label_instruction = QLabel(self.widget_instruction)
        self.label_instruction.setObjectName(u"label_instruction")

        self.verticalLayout_instruction.addWidget(self.label_instruction)


        self.verticalLayout_top.addWidget(self.widget_instruction)

        self.verticalLayout_top.setStretch(0, 2)
        self.verticalLayout_top.setStretch(1, 2)
        self.verticalLayout_top.setStretch(2, 3)
        self.verticalLayout_top.setStretch(3, 2)
        self.verticalLayout_top.setStretch(4, 3)

        self.retranslateUi(LoopSkillParam)

        QMetaObject.connectSlotsByName(LoopSkillParam)
    # setupUi

    def retranslateUi(self, LoopSkillParam):
        LoopSkillParam.setWindowTitle(QCoreApplication.translate("LoopSkillParam", u"Form", None))
        self.label_select_player.setText(QCoreApplication.translate("LoopSkillParam", u"\u9009\u62e9\u8d26\u53f7\uff1a", None))
        self.comboBox_select_player.setItemText(0, QCoreApplication.translate("LoopSkillParam", u"1P", None))
        self.comboBox_select_player.setItemText(1, QCoreApplication.translate("LoopSkillParam", u"2P", None))

        self.groupBox_select_level.setTitle(QCoreApplication.translate("LoopSkillParam", u"\u9009\u62e9\u5173\u5361", None))
        self.label_zone.setText(QCoreApplication.translate("LoopSkillParam", u"\u5730\u56fe\uff1a", None))
        self.label_level.setText(QCoreApplication.translate("LoopSkillParam", u"\u5173\u5361\uff1a", None))
        self.groupBox_select_plan.setTitle(QCoreApplication.translate("LoopSkillParam", u"\u9009\u62e9\u65b9\u6848", None))
        self.label_plan_path.setText(QCoreApplication.translate("LoopSkillParam", u"\u65b9\u6848\u8def\u5f84\uff1a", None))
        self.pushButton_plan_path.setText(QCoreApplication.translate("LoopSkillParam", u"\u6d4f\u89c8", None))
        self.label_1p_plan.setText(QCoreApplication.translate("LoopSkillParam", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_view_plan.setText(QCoreApplication.translate("LoopSkillParam", u"\u67e5\u770b\u65b9\u6848", None))
        self.groupBox_other_setting.setTitle(QCoreApplication.translate("LoopSkillParam", u"\u5176\u4ed6\u8bbe\u7f6e", None))
        self.label_loop_count.setText(QCoreApplication.translate("LoopSkillParam", u"\u5faa\u73af\u6b21\u6570\uff1a", None))
        self.lineEdit_loop_count.setText(QCoreApplication.translate("LoopSkillParam", u"1000", None))
        self.label_exit_delay.setText(QCoreApplication.translate("LoopSkillParam", u"\u591a\u4e45\u9000\u51fa\u5173\u5361(\u6beb\u79d2)\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_exit_delay.setToolTip(QCoreApplication.translate("LoopSkillParam", u"\u51b0\u6dc7\u6dcb\u586b2500, \u51b0\u6c99\u586b4500, \u5426\u5219\u586b500", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_exit_delay.setText("")
        self.lineEdit_exit_delay.setPlaceholderText(QCoreApplication.translate("LoopSkillParam", u"\u51b0\u6dc7\u6dcb\u586b2500, \u51b0\u6c99\u586b4500, \u5426\u5219\u586b500", None))
        self.label_instruction.setText(QCoreApplication.translate("LoopSkillParam", u"<html><head/><body><p style = \"line-height:50%\"><span style=\" color:#00aa00;\">\u5faa\u73af\u6b21\u6570 = (\u76ee\u6807\u719f\u7ec3\u5ea6 - \u5f53\u524d\u719f\u7ec3\u5ea6) / (1 + \u719f\u7ec3\u5ea6\u52a0\u6210)</span></p><p style = \"line-height:50%\"><span style=\" color:#00aa00;\">\u9000\u51fa\u5173\u5361\u65f6\u957f\u9ed8\u8ba4\u4e3a500(\u6beb\u79d2)\uff0c\u4f7f\u7528\u51b0\u6dc7\u6dcb\u65f6\u8bf7\u586b\u51992500\uff0c\u4f7f\u7528\u51b0\u6c99\u5219\u586b\u51994500</span></p><p style = \"line-height:50%\"><span style=\" color:#00aa00;\">\u53ef\u4ee5\u642d\u914d\u529f\u80fd[\u4f7f\u7528\u7269\u54c1]\uff0c\u4e2d\u9014\u4f7f\u7528\u9ad8\u7ea7/\u7ec8\u6781/\u7a76\u6781\u6280\u80fd\u4e66\uff0c\u4e00\u6b21\u6027\u81ea\u52a8\u5237\u5b8c</span></p></body></html>", None))
    # retranslateUi

