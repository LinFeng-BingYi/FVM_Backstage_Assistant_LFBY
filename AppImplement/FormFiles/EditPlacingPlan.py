# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditPlacingPlan.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_EditPlacingPlan(object):
    def setupUi(self, EditPlacingPlan):
        if not EditPlacingPlan.objectName():
            EditPlacingPlan.setObjectName(u"EditPlacingPlan")
        EditPlacingPlan.resize(850, 600)
        self.gridLayout_top = QGridLayout(EditPlacingPlan)
        self.gridLayout_top.setSpacing(0)
        self.gridLayout_top.setObjectName(u"gridLayout_top")
        self.gridLayout_top.setContentsMargins(0, 10, 0, 0)
        self.widget_general = QWidget(EditPlacingPlan)
        self.widget_general.setObjectName(u"widget_general")
        self.verticalLayout_general = QVBoxLayout(self.widget_general)
        self.verticalLayout_general.setSpacing(5)
        self.verticalLayout_general.setObjectName(u"verticalLayout_general")
        self.verticalLayout_general.setContentsMargins(0, 0, 0, 5)
        self.groupBox_file_path = QGroupBox(self.widget_general)
        self.groupBox_file_path.setObjectName(u"groupBox_file_path")
        self.groupBox_file_path.setMinimumSize(QSize(0, 90))
        self.gridLayout_file_path = QGridLayout(self.groupBox_file_path)
        self.gridLayout_file_path.setSpacing(5)
        self.gridLayout_file_path.setObjectName(u"gridLayout_file_path")
        self.gridLayout_file_path.setContentsMargins(-1, 0, -1, 5)
        self.label_deck_path = QLabel(self.groupBox_file_path)
        self.label_deck_path.setObjectName(u"label_deck_path")
        self.label_deck_path.setMinimumSize(QSize(70, 30))
        self.label_deck_path.setMaximumSize(QSize(70, 30))

        self.gridLayout_file_path.addWidget(self.label_deck_path, 0, 0, 1, 1)

        self.lineEdit_deck_path = QLineEdit(self.groupBox_file_path)
        self.lineEdit_deck_path.setObjectName(u"lineEdit_deck_path")
        self.lineEdit_deck_path.setMinimumSize(QSize(0, 30))

        self.gridLayout_file_path.addWidget(self.lineEdit_deck_path, 0, 1, 1, 1)

        self.pushButton_deck_path = QPushButton(self.groupBox_file_path)
        self.pushButton_deck_path.setObjectName(u"pushButton_deck_path")
        self.pushButton_deck_path.setMinimumSize(QSize(80, 30))
        self.pushButton_deck_path.setMaximumSize(QSize(80, 30))

        self.gridLayout_file_path.addWidget(self.pushButton_deck_path, 0, 2, 1, 1)

        self.label_plan_path = QLabel(self.groupBox_file_path)
        self.label_plan_path.setObjectName(u"label_plan_path")
        self.label_plan_path.setMinimumSize(QSize(70, 30))
        self.label_plan_path.setMaximumSize(QSize(70, 30))

        self.gridLayout_file_path.addWidget(self.label_plan_path, 1, 0, 1, 1)

        self.lineEdit_plan_path = QLineEdit(self.groupBox_file_path)
        self.lineEdit_plan_path.setObjectName(u"lineEdit_plan_path")
        self.lineEdit_plan_path.setMinimumSize(QSize(0, 30))

        self.gridLayout_file_path.addWidget(self.lineEdit_plan_path, 1, 1, 1, 1)

        self.pushButton_plan_path = QPushButton(self.groupBox_file_path)
        self.pushButton_plan_path.setObjectName(u"pushButton_plan_path")
        self.pushButton_plan_path.setMinimumSize(QSize(80, 30))
        self.pushButton_plan_path.setMaximumSize(QSize(80, 30))

        self.gridLayout_file_path.addWidget(self.pushButton_plan_path, 1, 2, 1, 1)


        self.verticalLayout_general.addWidget(self.groupBox_file_path)

        self.groupBox_common = QGroupBox(self.widget_general)
        self.groupBox_common.setObjectName(u"groupBox_common")
        self.horizontalLayout_common = QHBoxLayout(self.groupBox_common)
        self.horizontalLayout_common.setSpacing(5)
        self.horizontalLayout_common.setObjectName(u"horizontalLayout_common")
        self.horizontalLayout_common.setContentsMargins(-1, 0, 9, 5)
        self.checkBox_is_team_mode = QCheckBox(self.groupBox_common)
        self.checkBox_is_team_mode.setObjectName(u"checkBox_is_team_mode")
        self.checkBox_is_team_mode.setMinimumSize(QSize(135, 30))
        self.checkBox_is_team_mode.setMaximumSize(QSize(135, 30))
        self.checkBox_is_team_mode.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_is_team_mode)

        self.label_choose_section = QLabel(self.groupBox_common)
        self.label_choose_section.setObjectName(u"label_choose_section")
        self.label_choose_section.setMinimumSize(QSize(60, 0))
        self.label_choose_section.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_common.addWidget(self.label_choose_section)

        self.comboBox_choose_section = QComboBox(self.groupBox_common)
        self.comboBox_choose_section.setObjectName(u"comboBox_choose_section")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.comboBox_choose_section.sizePolicy().hasHeightForWidth())
        self.comboBox_choose_section.setSizePolicy(sizePolicy)
        self.comboBox_choose_section.setMinimumSize(QSize(180, 30))
        self.comboBox_choose_section.setMaximumSize(QSize(180, 30))

        self.horizontalLayout_common.addWidget(self.comboBox_choose_section)

        self.horizontalSpacer_common = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_common.addItem(self.horizontalSpacer_common)

        self.pushButton_save_plan = QPushButton(self.groupBox_common)
        self.pushButton_save_plan.setObjectName(u"pushButton_save_plan")
        self.pushButton_save_plan.setMinimumSize(QSize(80, 30))
        self.pushButton_save_plan.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_common.addWidget(self.pushButton_save_plan)

        self.pushButton_new_plan = QPushButton(self.groupBox_common)
        self.pushButton_new_plan.setObjectName(u"pushButton_new_plan")
        self.pushButton_new_plan.setMinimumSize(QSize(80, 30))
        self.pushButton_new_plan.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_common.addWidget(self.pushButton_new_plan)

        self.pushButton_delete_plan = QPushButton(self.groupBox_common)
        self.pushButton_delete_plan.setObjectName(u"pushButton_delete_plan")
        self.pushButton_delete_plan.setMinimumSize(QSize(80, 30))
        self.pushButton_delete_plan.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_common.addWidget(self.pushButton_delete_plan)


        self.verticalLayout_general.addWidget(self.groupBox_common)

        self.tabWidget_placing_config = QTabWidget(self.widget_general)
        self.tabWidget_placing_config.setObjectName(u"tabWidget_placing_config")
        self.tab_1p_placing_config = QWidget()
        self.tab_1p_placing_config.setObjectName(u"tab_1p_placing_config")
        self.verticalLayout_1p_placing_config = QVBoxLayout(self.tab_1p_placing_config)
        self.verticalLayout_1p_placing_config.setSpacing(10)
        self.verticalLayout_1p_placing_config.setObjectName(u"verticalLayout_1p_placing_config")
        self.verticalLayout_1p_placing_config.setContentsMargins(7, 10, 7, 10)
        self.widget_1p_setting = QWidget(self.tab_1p_placing_config)
        self.widget_1p_setting.setObjectName(u"widget_1p_setting")
        self.horizontalLayout_1p_setting = QHBoxLayout(self.widget_1p_setting)
        self.horizontalLayout_1p_setting.setSpacing(5)
        self.horizontalLayout_1p_setting.setObjectName(u"horizontalLayout_1p_setting")
        self.horizontalLayout_1p_setting.setContentsMargins(0, 0, 0, 0)
        self.label_1p_pos = QLabel(self.widget_1p_setting)
        self.label_1p_pos.setObjectName(u"label_1p_pos")
        self.label_1p_pos.setMinimumSize(QSize(70, 30))
        self.label_1p_pos.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_1p_setting.addWidget(self.label_1p_pos)

        self.lineEdit_1p_pos = QLineEdit(self.widget_1p_setting)
        self.lineEdit_1p_pos.setObjectName(u"lineEdit_1p_pos")
        self.lineEdit_1p_pos.setMinimumSize(QSize(60, 30))
        self.lineEdit_1p_pos.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_1p_setting.addWidget(self.lineEdit_1p_pos)

        self.label_1p_deck = QLabel(self.widget_1p_setting)
        self.label_1p_deck.setObjectName(u"label_1p_deck")
        self.label_1p_deck.setMinimumSize(QSize(60, 0))
        self.label_1p_deck.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_1p_setting.addWidget(self.label_1p_deck)

        self.comboBox_1p_deck = QComboBox(self.widget_1p_setting)
        self.comboBox_1p_deck.setObjectName(u"comboBox_1p_deck")
        self.comboBox_1p_deck.setMinimumSize(QSize(180, 30))
        self.comboBox_1p_deck.setMaximumSize(QSize(180, 30))

        self.horizontalLayout_1p_setting.addWidget(self.comboBox_1p_deck)

        self.horizontalSpacer_1p_setting = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_1p_setting.addItem(self.horizontalSpacer_1p_setting)

        self.pushButton_1p_save_deck = QPushButton(self.widget_1p_setting)
        self.pushButton_1p_save_deck.setObjectName(u"pushButton_1p_save_deck")
        self.pushButton_1p_save_deck.setMinimumSize(QSize(80, 30))
        self.pushButton_1p_save_deck.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_1p_setting.addWidget(self.pushButton_1p_save_deck)

        self.pushButton_1p_new_deck = QPushButton(self.widget_1p_setting)
        self.pushButton_1p_new_deck.setObjectName(u"pushButton_1p_new_deck")
        self.pushButton_1p_new_deck.setMinimumSize(QSize(80, 30))
        self.pushButton_1p_new_deck.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_1p_setting.addWidget(self.pushButton_1p_new_deck)

        self.pushButton_1p_delete_deck = QPushButton(self.widget_1p_setting)
        self.pushButton_1p_delete_deck.setObjectName(u"pushButton_1p_delete_deck")
        self.pushButton_1p_delete_deck.setMinimumSize(QSize(80, 30))
        self.pushButton_1p_delete_deck.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_1p_setting.addWidget(self.pushButton_1p_delete_deck)


        self.verticalLayout_1p_placing_config.addWidget(self.widget_1p_setting)

        self.listWidget_1p_deck = QListWidget(self.tab_1p_placing_config)
        self.listWidget_1p_deck.setObjectName(u"listWidget_1p_deck")
        self.listWidget_1p_deck.setFlow(QListView.LeftToRight)

        self.verticalLayout_1p_placing_config.addWidget(self.listWidget_1p_deck)

        self.groupBox_1p_placing_table = QGroupBox(self.tab_1p_placing_config)
        self.groupBox_1p_placing_table.setObjectName(u"groupBox_1p_placing_table")
        self.groupBox_1p_placing_table.setFlat(True)
        self.groupBox_1p_placing_table.setCheckable(True)
        self.verticalLayout_1p_placing_table = QVBoxLayout(self.groupBox_1p_placing_table)
        self.verticalLayout_1p_placing_table.setSpacing(5)
        self.verticalLayout_1p_placing_table.setObjectName(u"verticalLayout_1p_placing_table")
        self.verticalLayout_1p_placing_table.setContentsMargins(0, 5, 0, 0)
        self.tableWidget_1p_placing_table = QTableWidget(self.groupBox_1p_placing_table)
        if (self.tableWidget_1p_placing_table.columnCount() < 6):
            self.tableWidget_1p_placing_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_1p_placing_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_1p_placing_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_1p_placing_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_1p_placing_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_1p_placing_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_1p_placing_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_1p_placing_table.setObjectName(u"tableWidget_1p_placing_table")
        self.tableWidget_1p_placing_table.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableWidget_1p_placing_table.setAlternatingRowColors(True)
        self.tableWidget_1p_placing_table.horizontalHeader().setMinimumSectionSize(100)

        self.verticalLayout_1p_placing_table.addWidget(self.tableWidget_1p_placing_table)


        self.verticalLayout_1p_placing_config.addWidget(self.groupBox_1p_placing_table)

        self.verticalLayout_1p_placing_config.setStretch(0, 1)
        self.verticalLayout_1p_placing_config.setStretch(1, 2)
        self.verticalLayout_1p_placing_config.setStretch(2, 10)
        self.tabWidget_placing_config.addTab(self.tab_1p_placing_config, "")
        self.tab_2p_placing_config = QWidget()
        self.tab_2p_placing_config.setObjectName(u"tab_2p_placing_config")
        self.verticalLayout_2p_placing_config = QVBoxLayout(self.tab_2p_placing_config)
        self.verticalLayout_2p_placing_config.setSpacing(10)
        self.verticalLayout_2p_placing_config.setObjectName(u"verticalLayout_2p_placing_config")
        self.verticalLayout_2p_placing_config.setContentsMargins(7, 10, 7, 10)
        self.widget_2p_setting = QWidget(self.tab_2p_placing_config)
        self.widget_2p_setting.setObjectName(u"widget_2p_setting")
        self.horizontalLayout_2p_setting = QHBoxLayout(self.widget_2p_setting)
        self.horizontalLayout_2p_setting.setSpacing(5)
        self.horizontalLayout_2p_setting.setObjectName(u"horizontalLayout_2p_setting")
        self.horizontalLayout_2p_setting.setContentsMargins(0, 0, 0, 0)
        self.label_2p_pos = QLabel(self.widget_2p_setting)
        self.label_2p_pos.setObjectName(u"label_2p_pos")
        self.label_2p_pos.setMinimumSize(QSize(70, 30))
        self.label_2p_pos.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2p_setting.addWidget(self.label_2p_pos)

        self.lineEdit_2p_pos = QLineEdit(self.widget_2p_setting)
        self.lineEdit_2p_pos.setObjectName(u"lineEdit_2p_pos")
        self.lineEdit_2p_pos.setMinimumSize(QSize(60, 30))
        self.lineEdit_2p_pos.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2p_setting.addWidget(self.lineEdit_2p_pos)

        self.label_2p_deck = QLabel(self.widget_2p_setting)
        self.label_2p_deck.setObjectName(u"label_2p_deck")
        self.label_2p_deck.setMinimumSize(QSize(60, 0))
        self.label_2p_deck.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2p_setting.addWidget(self.label_2p_deck)

        self.comboBox_2p_deck = QComboBox(self.widget_2p_setting)
        self.comboBox_2p_deck.setObjectName(u"comboBox_2p_deck")
        self.comboBox_2p_deck.setMinimumSize(QSize(180, 30))
        self.comboBox_2p_deck.setMaximumSize(QSize(180, 30))

        self.horizontalLayout_2p_setting.addWidget(self.comboBox_2p_deck)

        self.horizontalSpacer_2p_setting = QSpacerItem(567, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2p_setting.addItem(self.horizontalSpacer_2p_setting)

        self.pushButton_2p_save_deck = QPushButton(self.widget_2p_setting)
        self.pushButton_2p_save_deck.setObjectName(u"pushButton_2p_save_deck")
        self.pushButton_2p_save_deck.setMinimumSize(QSize(80, 30))
        self.pushButton_2p_save_deck.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2p_setting.addWidget(self.pushButton_2p_save_deck)

        self.pushButton_2p_new_deck = QPushButton(self.widget_2p_setting)
        self.pushButton_2p_new_deck.setObjectName(u"pushButton_2p_new_deck")
        self.pushButton_2p_new_deck.setMinimumSize(QSize(80, 30))
        self.pushButton_2p_new_deck.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2p_setting.addWidget(self.pushButton_2p_new_deck)

        self.pushButton_2p_delete_deck = QPushButton(self.widget_2p_setting)
        self.pushButton_2p_delete_deck.setObjectName(u"pushButton_2p_delete_deck")
        self.pushButton_2p_delete_deck.setMinimumSize(QSize(80, 30))
        self.pushButton_2p_delete_deck.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2p_setting.addWidget(self.pushButton_2p_delete_deck)


        self.verticalLayout_2p_placing_config.addWidget(self.widget_2p_setting)

        self.listWidget_2p_deck = QListWidget(self.tab_2p_placing_config)
        self.listWidget_2p_deck.setObjectName(u"listWidget_2p_deck")
        self.listWidget_2p_deck.setFlow(QListView.LeftToRight)

        self.verticalLayout_2p_placing_config.addWidget(self.listWidget_2p_deck)

        self.groupBox_2p_placing_table = QGroupBox(self.tab_2p_placing_config)
        self.groupBox_2p_placing_table.setObjectName(u"groupBox_2p_placing_table")
        self.groupBox_2p_placing_table.setFlat(True)
        self.groupBox_2p_placing_table.setCheckable(True)
        self.verticalLayout_2p_placing_table = QVBoxLayout(self.groupBox_2p_placing_table)
        self.verticalLayout_2p_placing_table.setSpacing(5)
        self.verticalLayout_2p_placing_table.setObjectName(u"verticalLayout_2p_placing_table")
        self.verticalLayout_2p_placing_table.setContentsMargins(0, 5, 0, 0)
        self.tableWidget_2p_placing_table = QTableWidget(self.groupBox_2p_placing_table)
        if (self.tableWidget_2p_placing_table.columnCount() < 6):
            self.tableWidget_2p_placing_table.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tableWidget_2p_placing_table.setObjectName(u"tableWidget_2p_placing_table")
        self.tableWidget_2p_placing_table.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableWidget_2p_placing_table.setAlternatingRowColors(True)

        self.verticalLayout_2p_placing_table.addWidget(self.tableWidget_2p_placing_table)


        self.verticalLayout_2p_placing_config.addWidget(self.groupBox_2p_placing_table)

        self.verticalLayout_2p_placing_config.setStretch(0, 1)
        self.verticalLayout_2p_placing_config.setStretch(1, 2)
        self.verticalLayout_2p_placing_config.setStretch(2, 10)
        self.tabWidget_placing_config.addTab(self.tab_2p_placing_config, "")

        self.verticalLayout_general.addWidget(self.tabWidget_placing_config)

        self.widget_other_edit_way = QWidget(self.widget_general)
        self.widget_other_edit_way.setObjectName(u"widget_other_edit_way")
        self.widget_other_edit_way.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_other_edit_way = QHBoxLayout(self.widget_other_edit_way)
        self.horizontalLayout_other_edit_way.setSpacing(5)
        self.horizontalLayout_other_edit_way.setObjectName(u"horizontalLayout_other_edit_way")
        self.horizontalLayout_other_edit_way.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_other_edit_way_1 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_other_edit_way.addItem(self.horizontalSpacer_other_edit_way_1)

        self.pushButton_plan_timeline = QPushButton(self.widget_other_edit_way)
        self.pushButton_plan_timeline.setObjectName(u"pushButton_plan_timeline")
        self.pushButton_plan_timeline.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_other_edit_way.addWidget(self.pushButton_plan_timeline)

        self.horizontalSpacer_other_edit_way_2 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_other_edit_way.addItem(self.horizontalSpacer_other_edit_way_2)

        self.pushButton_plan_visualize = QPushButton(self.widget_other_edit_way)
        self.pushButton_plan_visualize.setObjectName(u"pushButton_plan_visualize")
        self.pushButton_plan_visualize.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_other_edit_way.addWidget(self.pushButton_plan_visualize)

        self.horizontalSpacer_other_edit_way_3 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_other_edit_way.addItem(self.horizontalSpacer_other_edit_way_3)


        self.verticalLayout_general.addWidget(self.widget_other_edit_way)


        self.gridLayout_top.addWidget(self.widget_general, 0, 0, 1, 1)


        self.retranslateUi(EditPlacingPlan)

        self.tabWidget_placing_config.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EditPlacingPlan)
    # setupUi

    def retranslateUi(self, EditPlacingPlan):
        EditPlacingPlan.setWindowTitle(QCoreApplication.translate("EditPlacingPlan", u"\u5361\u7247\u653e\u7f6e\u65b9\u6848\u7f16\u8f91", None))
        self.groupBox_file_path.setTitle(QCoreApplication.translate("EditPlacingPlan", u"\u6587\u4ef6\u8def\u5f84", None))
        self.label_deck_path.setText(QCoreApplication.translate("EditPlacingPlan", u"\u5361\u7247\u7ec4\uff1a", None))
        self.pushButton_deck_path.setText(QCoreApplication.translate("EditPlacingPlan", u"\u6d4f\u89c8", None))
        self.label_plan_path.setText(QCoreApplication.translate("EditPlacingPlan", u"\u653e\u5361\u65b9\u6848\uff1a", None))
        self.pushButton_plan_path.setText(QCoreApplication.translate("EditPlacingPlan", u"\u6d4f\u89c8", None))
        self.groupBox_common.setTitle(QCoreApplication.translate("EditPlacingPlan", u"\u8bbe\u7f6e", None))
        self.checkBox_is_team_mode.setText(QCoreApplication.translate("EditPlacingPlan", u"\u7ec4\u961f\u653e\u5361\u65b9\u6848\u6a21\u5f0f", None))
        self.label_choose_section.setText(QCoreApplication.translate("EditPlacingPlan", u"\u9009\u62e9\u65b9\u6848\uff1a", None))
        self.pushButton_save_plan.setText(QCoreApplication.translate("EditPlacingPlan", u"\u4fdd\u5b58\u65b9\u6848", None))
        self.pushButton_new_plan.setText(QCoreApplication.translate("EditPlacingPlan", u"\u65b0\u5efa\u65b9\u6848", None))
        self.pushButton_delete_plan.setText(QCoreApplication.translate("EditPlacingPlan", u"\u5220\u9664\u65b9\u6848", None))
        self.label_1p_pos.setText(QCoreApplication.translate("EditPlacingPlan", u"\u623f\u4e3b\u4f4d\u7f6e\uff1a", None))
        self.label_1p_deck.setText(QCoreApplication.translate("EditPlacingPlan", u"\u9009\u62e9\u5361\u7ec4\uff1a", None))
        self.pushButton_1p_save_deck.setText(QCoreApplication.translate("EditPlacingPlan", u"\u4fdd\u5b58\u5361\u7247\u7ec4", None))
        self.pushButton_1p_new_deck.setText(QCoreApplication.translate("EditPlacingPlan", u"\u65b0\u5efa\u5361\u7247\u7ec4", None))
        self.pushButton_1p_delete_deck.setText(QCoreApplication.translate("EditPlacingPlan", u"\u5220\u9664\u5361\u7247\u7ec4", None))
        self.groupBox_1p_placing_table.setTitle(QCoreApplication.translate("EditPlacingPlan", u"\u623f\u4e3b\u5361\u7247\u653e\u7f6e\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tableWidget_1p_placing_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EditPlacingPlan", u"\u5361\u7247\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget_1p_placing_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EditPlacingPlan", u"\u5361\u69fd\u4f4d\u7f6e", None));
        ___qtablewidgetitem2 = self.tableWidget_1p_placing_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EditPlacingPlan", u"\u653e\u7f6e\u4f4d\u7f6e", None));
        ___qtablewidgetitem3 = self.tableWidget_1p_placing_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EditPlacingPlan", u"\u8865\u5361\u4f4d\u7f6e", None));
        ___qtablewidgetitem4 = self.tableWidget_1p_placing_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EditPlacingPlan", u"\u9ed8\u8ba4CD", None));
        ___qtablewidgetitem5 = self.tableWidget_1p_placing_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EditPlacingPlan", u"\u64cd\u4f5c", None));
        self.tabWidget_placing_config.setTabText(self.tabWidget_placing_config.indexOf(self.tab_1p_placing_config), QCoreApplication.translate("EditPlacingPlan", u"\u623f\u4e3b\u5361\u7247\u653e\u7f6e\u65b9\u6848", None))
        self.label_2p_pos.setText(QCoreApplication.translate("EditPlacingPlan", u"\u623f\u5ba2\u4f4d\u7f6e\uff1a", None))
        self.label_2p_deck.setText(QCoreApplication.translate("EditPlacingPlan", u"\u9009\u62e9\u5361\u7ec4\uff1a", None))
        self.pushButton_2p_save_deck.setText(QCoreApplication.translate("EditPlacingPlan", u"\u4fdd\u5b58\u5361\u7247\u7ec4", None))
        self.pushButton_2p_new_deck.setText(QCoreApplication.translate("EditPlacingPlan", u"\u65b0\u5efa\u5361\u7247\u7ec4", None))
        self.pushButton_2p_delete_deck.setText(QCoreApplication.translate("EditPlacingPlan", u"\u5220\u9664\u5361\u7247\u7ec4", None))
        self.groupBox_2p_placing_table.setTitle(QCoreApplication.translate("EditPlacingPlan", u"\u623f\u5ba2\u5361\u7247\u653e\u7f6e\u4fe1\u606f", None))
        ___qtablewidgetitem6 = self.tableWidget_2p_placing_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("EditPlacingPlan", u"\u5361\u7247\u540d\u79f0", None));
        ___qtablewidgetitem7 = self.tableWidget_2p_placing_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("EditPlacingPlan", u"\u5361\u69fd\u4f4d\u7f6e", None));
        ___qtablewidgetitem8 = self.tableWidget_2p_placing_table.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("EditPlacingPlan", u"\u653e\u7f6e\u4f4d\u7f6e", None));
        ___qtablewidgetitem9 = self.tableWidget_2p_placing_table.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("EditPlacingPlan", u"\u8865\u5361\u4f4d\u7f6e", None));
        ___qtablewidgetitem10 = self.tableWidget_2p_placing_table.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("EditPlacingPlan", u"\u9ed8\u8ba4CD", None));
        ___qtablewidgetitem11 = self.tableWidget_2p_placing_table.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("EditPlacingPlan", u"\u64cd\u4f5c", None));
        self.tabWidget_placing_config.setTabText(self.tabWidget_placing_config.indexOf(self.tab_2p_placing_config), QCoreApplication.translate("EditPlacingPlan", u"\u623f\u5ba2\u5361\u7247\u653e\u7f6e\u65b9\u6848", None))
        self.pushButton_plan_timeline.setText(QCoreApplication.translate("EditPlacingPlan", u"\u653e\u5361\u65b9\u6848\u65f6\u95f4\u7ebf", None))
        self.pushButton_plan_visualize.setText(QCoreApplication.translate("EditPlacingPlan", u"\u653e\u5361\u9635\u5bb9\u53ef\u89c6\u5316", None))
    # retranslateUi

