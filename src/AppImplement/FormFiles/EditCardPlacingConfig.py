# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditCardPlacingConfig.ui'
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

class Ui_EditCardPlacingConfig(object):
    def setupUi(self, EditCardPlacingConfig):
        if not EditCardPlacingConfig.objectName():
            EditCardPlacingConfig.setObjectName(u"EditCardPlacingConfig")
        EditCardPlacingConfig.resize(753, 450)
        self.gridLayout_top = QGridLayout(EditCardPlacingConfig)
        self.gridLayout_top.setSpacing(0)
        self.gridLayout_top.setObjectName(u"gridLayout_top")
        self.gridLayout_top.setContentsMargins(0, 0, 0, 0)
        self.widget_general = QWidget(EditCardPlacingConfig)
        self.widget_general.setObjectName(u"widget_general")
        self.verticalLayout_general = QVBoxLayout(self.widget_general)
        self.verticalLayout_general.setSpacing(10)
        self.verticalLayout_general.setObjectName(u"verticalLayout_general")
        self.verticalLayout_general.setContentsMargins(0, 0, 0, 0)
        self.widget_file_path = QWidget(self.widget_general)
        self.widget_file_path.setObjectName(u"widget_file_path")
        self.horizontalLayout_file_path = QHBoxLayout(self.widget_file_path)
        self.horizontalLayout_file_path.setSpacing(9)
        self.horizontalLayout_file_path.setObjectName(u"horizontalLayout_file_path")
        self.horizontalLayout_file_path.setContentsMargins(10, 10, 10, 0)
        self.label_file_path = QLabel(self.widget_file_path)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setMinimumSize(QSize(70, 30))
        self.label_file_path.setMaximumSize(QSize(70, 30))

        self.horizontalLayout_file_path.addWidget(self.label_file_path)

        self.lineEdit_file_path = QLineEdit(self.widget_file_path)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")
        self.lineEdit_file_path.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_file_path.addWidget(self.lineEdit_file_path)

        self.pushButton_file_path = QPushButton(self.widget_file_path)
        self.pushButton_file_path.setObjectName(u"pushButton_file_path")
        self.pushButton_file_path.setMinimumSize(QSize(80, 30))
        self.pushButton_file_path.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_file_path.addWidget(self.pushButton_file_path)


        self.verticalLayout_general.addWidget(self.widget_file_path)

        self.widget_common = QWidget(self.widget_general)
        self.widget_common.setObjectName(u"widget_common")
        self.horizontalLayout_common = QHBoxLayout(self.widget_common)
        self.horizontalLayout_common.setSpacing(9)
        self.horizontalLayout_common.setObjectName(u"horizontalLayout_common")
        self.horizontalLayout_common.setContentsMargins(10, 0, 10, 0)
        self.checkBox_is_team_mode = QCheckBox(self.widget_common)
        self.checkBox_is_team_mode.setObjectName(u"checkBox_is_team_mode")
        self.checkBox_is_team_mode.setMinimumSize(QSize(70, 30))
        self.checkBox_is_team_mode.setMaximumSize(QSize(70, 30))
        self.checkBox_is_team_mode.setChecked(True)

        self.horizontalLayout_common.addWidget(self.checkBox_is_team_mode)

        self.label_choose_section = QLabel(self.widget_common)
        self.label_choose_section.setObjectName(u"label_choose_section")
        self.label_choose_section.setMinimumSize(QSize(60, 0))
        self.label_choose_section.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_common.addWidget(self.label_choose_section)

        self.comboBox_choose_section = QComboBox(self.widget_common)
        self.comboBox_choose_section.setObjectName(u"comboBox_choose_section")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.comboBox_choose_section.sizePolicy().hasHeightForWidth())
        self.comboBox_choose_section.setSizePolicy(sizePolicy)
        self.comboBox_choose_section.setMinimumSize(QSize(120, 30))
        self.comboBox_choose_section.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_common.addWidget(self.comboBox_choose_section)

        self.horizontalSpacer_common = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_common.addItem(self.horizontalSpacer_common)

        self.pushButton_new_config = QPushButton(self.widget_common)
        self.pushButton_new_config.setObjectName(u"pushButton_new_config")
        self.pushButton_new_config.setMinimumSize(QSize(80, 30))
        self.pushButton_new_config.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_common.addWidget(self.pushButton_new_config)

        self.pushButton_modify_config = QPushButton(self.widget_common)
        self.pushButton_modify_config.setObjectName(u"pushButton_modify_config")
        self.pushButton_modify_config.setMinimumSize(QSize(80, 30))
        self.pushButton_modify_config.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_common.addWidget(self.pushButton_modify_config)

        self.pushButton_delete_config = QPushButton(self.widget_common)
        self.pushButton_delete_config.setObjectName(u"pushButton_delete_config")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_delete_config.sizePolicy().hasHeightForWidth())
        self.pushButton_delete_config.setSizePolicy(sizePolicy1)
        self.pushButton_delete_config.setMinimumSize(QSize(80, 30))
        self.pushButton_delete_config.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_common.addWidget(self.pushButton_delete_config)


        self.verticalLayout_general.addWidget(self.widget_common)

        self.tabWidget_placing_config = QTabWidget(self.widget_general)
        self.tabWidget_placing_config.setObjectName(u"tabWidget_placing_config")
        self.tab_1p_placing_config = QWidget()
        self.tab_1p_placing_config.setObjectName(u"tab_1p_placing_config")
        self.verticalLayout_1p_placing_config = QVBoxLayout(self.tab_1p_placing_config)
        self.verticalLayout_1p_placing_config.setSpacing(10)
        self.verticalLayout_1p_placing_config.setObjectName(u"verticalLayout_1p_placing_config")
        self.verticalLayout_1p_placing_config.setContentsMargins(10, 10, 10, 10)
        self.widget_1p_setting = QWidget(self.tab_1p_placing_config)
        self.widget_1p_setting.setObjectName(u"widget_1p_setting")
        self.horizontalLayout_1p_setting = QHBoxLayout(self.widget_1p_setting)
        self.horizontalLayout_1p_setting.setSpacing(9)
        self.horizontalLayout_1p_setting.setObjectName(u"horizontalLayout_1p_setting")
        self.horizontalLayout_1p_setting.setContentsMargins(0, 0, -1, 0)
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
        self.comboBox_1p_deck.setMinimumSize(QSize(120, 30))
        self.comboBox_1p_deck.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_1p_setting.addWidget(self.comboBox_1p_deck)

        self.horizontalSpacer_1p_setting = QSpacerItem(576, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_1p_setting.addItem(self.horizontalSpacer_1p_setting)


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
        if (self.tableWidget_1p_placing_table.columnCount() < 5):
            self.tableWidget_1p_placing_table.setColumnCount(5)
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
        self.tableWidget_1p_placing_table.setObjectName(u"tableWidget_1p_placing_table")
        self.tableWidget_1p_placing_table.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableWidget_1p_placing_table.setAlternatingRowColors(True)

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
        self.verticalLayout_2p_placing_config.setContentsMargins(10, 10, 10, 10)
        self.widget_2p_setting = QWidget(self.tab_2p_placing_config)
        self.widget_2p_setting.setObjectName(u"widget_2p_setting")
        self.horizontalLayout_2p_setting = QHBoxLayout(self.widget_2p_setting)
        self.horizontalLayout_2p_setting.setSpacing(9)
        self.horizontalLayout_2p_setting.setObjectName(u"horizontalLayout_2p_setting")
        self.horizontalLayout_2p_setting.setContentsMargins(0, 0, -1, 0)
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
        self.comboBox_2p_deck.setMinimumSize(QSize(120, 30))
        self.comboBox_2p_deck.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_2p_setting.addWidget(self.comboBox_2p_deck)

        self.horizontalSpacer_2p_setting = QSpacerItem(567, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2p_setting.addItem(self.horizontalSpacer_2p_setting)


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
        if (self.tableWidget_2p_placing_table.columnCount() < 5):
            self.tableWidget_2p_placing_table.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2p_placing_table.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_2p_placing_table.setObjectName(u"tableWidget_2p_placing_table")
        self.tableWidget_2p_placing_table.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableWidget_2p_placing_table.setAlternatingRowColors(True)

        self.verticalLayout_2p_placing_table.addWidget(self.tableWidget_2p_placing_table)


        self.verticalLayout_2p_placing_config.addWidget(self.groupBox_2p_placing_table)

        self.verticalLayout_2p_placing_config.setStretch(1, 1)
        self.verticalLayout_2p_placing_config.setStretch(2, 5)
        self.tabWidget_placing_config.addTab(self.tab_2p_placing_config, "")

        self.verticalLayout_general.addWidget(self.tabWidget_placing_config)


        self.gridLayout_top.addWidget(self.widget_general, 0, 0, 1, 1)


        self.retranslateUi(EditCardPlacingConfig)

        self.tabWidget_placing_config.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EditCardPlacingConfig)
    # setupUi

    def retranslateUi(self, EditCardPlacingConfig):
        EditCardPlacingConfig.setWindowTitle(QCoreApplication.translate("EditCardPlacingConfig", u"\u5361\u7247\u653e\u7f6e\u65b9\u6848\u7f16\u8f91", None))
        self.label_file_path.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.pushButton_file_path.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u6d4f\u89c8", None))
        self.checkBox_is_team_mode.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u7ec4\u961f\u6a21\u5f0f", None))
        self.label_choose_section.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u9009\u62e9\u65b9\u6848\uff1a", None))
        self.pushButton_new_config.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u65b0\u5efa\u65b9\u6848", None))
        self.pushButton_modify_config.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u4fee\u6539\u65b9\u6848", None))
        self.pushButton_delete_config.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u5220\u9664\u65b9\u6848", None))
        self.label_1p_pos.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u623f\u4e3b\u653e\u7f6e\u4f4d\u7f6e", None))
        self.label_1p_deck.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u9009\u62e9\u5361\u7ec4\uff1a", None))
        self.groupBox_1p_placing_table.setTitle(QCoreApplication.translate("EditCardPlacingConfig", u"\u623f\u4e3b\u5361\u7247\u653e\u7f6e\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tableWidget_1p_placing_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u5361\u7247\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget_1p_placing_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u5361\u69fd\u4f4d\u7f6e", None));
        ___qtablewidgetitem2 = self.tableWidget_1p_placing_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u653e\u7f6e\u4f4d\u7f6e", None));
        ___qtablewidgetitem3 = self.tableWidget_1p_placing_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u9ed8\u8ba4CD", None));
        ___qtablewidgetitem4 = self.tableWidget_1p_placing_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u64cd\u4f5c", None));
        self.tabWidget_placing_config.setTabText(self.tabWidget_placing_config.indexOf(self.tab_1p_placing_config), QCoreApplication.translate("EditCardPlacingConfig", u"\u623f\u4e3b\u5361\u7247\u653e\u7f6e\u65b9\u6848", None))
        self.label_2p_pos.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u623f\u5ba2\u653e\u7f6e\u4f4d\u7f6e", None))
        self.label_2p_deck.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u9009\u62e9\u5361\u7ec4\uff1a", None))
        self.groupBox_2p_placing_table.setTitle(QCoreApplication.translate("EditCardPlacingConfig", u"\u623f\u5ba2\u5361\u7247\u653e\u7f6e\u4fe1\u606f", None))
        ___qtablewidgetitem5 = self.tableWidget_2p_placing_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u5361\u7247\u540d\u79f0", None));
        ___qtablewidgetitem6 = self.tableWidget_2p_placing_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u5361\u69fd\u4f4d\u7f6e", None));
        ___qtablewidgetitem7 = self.tableWidget_2p_placing_table.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u653e\u7f6e\u4f4d\u7f6e", None));
        ___qtablewidgetitem8 = self.tableWidget_2p_placing_table.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u9ed8\u8ba4CD", None));
        ___qtablewidgetitem9 = self.tableWidget_2p_placing_table.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("EditCardPlacingConfig", u"\u64cd\u4f5c", None));
        self.tabWidget_placing_config.setTabText(self.tabWidget_placing_config.indexOf(self.tab_2p_placing_config), QCoreApplication.translate("EditCardPlacingConfig", u"\u623f\u5ba2\u5361\u7247\u653e\u7f6e\u65b9\u6848", None))
    # retranslateUi

