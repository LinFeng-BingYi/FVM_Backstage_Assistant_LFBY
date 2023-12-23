# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QGroupBox,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
                               QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QTabWidget, QComboBox)


class Ui_UpdateINI(object):
    def setupUi(self, UpdateINI):
        if not UpdateINI.objectName():
            UpdateINI.setObjectName(u"UpdateINI")
        UpdateINI.resize(450, 250)

        # 控件 ---------------------------------------------------------------------------------------
        # 总widget
        self.widget_general = QWidget(UpdateINI)
        self.widget_general.setObjectName(u"widget_general")
        self.widget_general.setMinimumSize(QSize(450, 250))

        self.tabWidget = QTabWidget(self.widget_general)
        self.tabWidget.setObjectName("tabWidget")

        # tab页：<简易组队脚本>升级到V6.05 ----------------------------
        self.tab_v6_05 = QWidget(self.tabWidget)
        self.tab_v6_05.setObjectName("tab_v6_05")
        self.tabWidget.addTab(self.tab_v6_05, "升级至简易组队脚本V6.05")

        # 文件路径
        self.widget_file_path = QWidget(self.tab_v6_05)
        self.widget_file_path.setObjectName(u"widget_file_path")

        self.label_file_path = QLabel(self.widget_file_path)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setMinimumSize(QSize(70, 30))
        self.label_file_path.setMaximumSize(QSize(70, 30))

        self.lineEdit_file_path = QLineEdit(self.widget_file_path)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")
        self.lineEdit_file_path.setMinimumSize(QSize(0, 30))

        self.pushButton_file_path = QPushButton(self.widget_file_path)
        self.pushButton_file_path.setObjectName(u"pushButton_file_path")
        self.pushButton_file_path.setMinimumSize(QSize(80, 30))
        self.pushButton_file_path.setMaximumSize(QSize(80, 30))

        # 底部按键
        self.widget_bottom_button = QWidget(self.tab_v6_05)
        self.widget_bottom_button.setObjectName(u"widget_bottom_button")

        self.pushButton_execute = QPushButton(self.widget_bottom_button)
        self.pushButton_execute.setObjectName(u"pushButton_execute")
        self.pushButton_execute.setMinimumSize(QSize(80, 30))
        self.pushButton_execute.setMaximumSize(QSize(80, 30))

        # tab页：<一键日常助手>升级到V0.01 ----------------------------
        self.tab_new_v0_01 = QWidget(self.tabWidget)
        self.tab_new_v0_01.setObjectName("tab_new_v0_01")
        self.tabWidget.addTab(self.tab_new_v0_01, "升级至一键日常助手V0.01")

        # ini文件路径
        self.widget_file_path_new_v001 = QWidget(self.tab_new_v0_01)
        self.widget_file_path_new_v001.setObjectName(u"widget_file_path_new_v001")

        self.label_file_path_new_v001 = QLabel(self.widget_file_path_new_v001)
        self.label_file_path_new_v001.setObjectName(u"label_file_path_new_v001")
        self.label_file_path_new_v001.setMinimumSize(QSize(70, 30))
        self.label_file_path_new_v001.setMaximumSize(QSize(70, 30))

        self.lineEdit_file_path_new_v001 = QLineEdit(self.widget_file_path_new_v001)
        self.lineEdit_file_path_new_v001.setObjectName(u"lineEdit_file_path_new_v001")
        self.lineEdit_file_path_new_v001.setMinimumSize(QSize(0, 30))

        self.pushButton_file_path_new_v001 = QPushButton(self.widget_file_path_new_v001)
        self.pushButton_file_path_new_v001.setObjectName(u"pushButton_file_path_new_v001")
        self.pushButton_file_path_new_v001.setMinimumSize(QSize(80, 30))
        self.pushButton_file_path_new_v001.setMaximumSize(QSize(80, 30))

        # 卡片组文件路径
        self.widget_deck_path_new_v001 = QWidget(self.tab_new_v0_01)
        self.widget_deck_path_new_v001.setObjectName(u"widget_deck_path_new_v001")

        self.label_deck_path_new_v001 = QLabel(self.widget_deck_path_new_v001)
        self.label_deck_path_new_v001.setObjectName(u"label_deck_path_new_v001")
        self.label_deck_path_new_v001.setMinimumSize(QSize(70, 30))
        self.label_deck_path_new_v001.setMaximumSize(QSize(70, 30))

        self.lineEdit_deck_path_new_v001 = QLineEdit(self.widget_deck_path_new_v001)
        self.lineEdit_deck_path_new_v001.setObjectName(u"lineEdit_deck_path_new_v001")
        self.lineEdit_deck_path_new_v001.setMinimumSize(QSize(0, 30))

        self.pushButton_deck_path_new_v001 = QPushButton(self.widget_deck_path_new_v001)
        self.pushButton_deck_path_new_v001.setObjectName(u"pushButton_deck_path_new_v001")
        self.pushButton_deck_path_new_v001.setMinimumSize(QSize(80, 30))
        self.pushButton_deck_path_new_v001.setMaximumSize(QSize(80, 30))

        # 所用卡片组
        self.widget_deck_select_new_v001 = QWidget(self.tab_new_v0_01)
        self.widget_deck_select_new_v001.setObjectName(u"widget_deck_select_new_v001")

        self.label_deck_select_1p_new_v001 = QLabel(self.widget_deck_select_new_v001)
        self.label_deck_select_1p_new_v001.setObjectName(u"label_deck_select_1p_new_v001")
        self.label_deck_select_1p_new_v001.setMinimumSize(QSize(70, 30))
        self.label_deck_select_1p_new_v001.setMaximumSize(QSize(70, 30))

        self.comboBox_deck_select_1p_new_v001 = QComboBox(self.widget_deck_select_new_v001)
        self.comboBox_deck_select_1p_new_v001.setObjectName("comboBox_deck_select_1p_new_v001")
        self.comboBox_deck_select_1p_new_v001.setMinimumHeight(30)

        self.label_deck_select_2p_new_v001 = QLabel(self.widget_deck_select_new_v001)
        self.label_deck_select_2p_new_v001.setObjectName(u"label_deck_select_2p_new_v001")
        self.label_deck_select_2p_new_v001.setMinimumSize(QSize(70, 30))
        self.label_deck_select_2p_new_v001.setMaximumSize(QSize(70, 30))

        self.comboBox_deck_select_2p_new_v001 = QComboBox(self.widget_deck_select_new_v001)
        self.comboBox_deck_select_2p_new_v001.setObjectName("comboBox_deck_select_2p_new_v001")
        self.comboBox_deck_select_2p_new_v001.setMinimumHeight(30)

        # 底部按键
        self.widget_bottom_button_new_v001 = QWidget(self.tab_new_v0_01)
        self.widget_bottom_button_new_v001.setObjectName(u"widget_bottom_button_new_v001")

        self.pushButton_execute_new_v001 = QPushButton(self.widget_bottom_button)
        self.pushButton_execute_new_v001.setObjectName(u"pushButton_execute_new_v001")
        self.pushButton_execute_new_v001.setMinimumSize(QSize(80, 30))
        self.pushButton_execute_new_v001.setMaximumSize(QSize(80, 30))

        # 布局 ---------------------------------------------------------------------------------------
        # 总布局
        self.gridLayout_top = QGridLayout(UpdateINI)
        self.gridLayout_top.setSpacing(0)
        self.gridLayout_top.setObjectName(u"gridLayout_top")
        self.gridLayout_top.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_top.addWidget(self.widget_general, 0, 0, 1, 1)

        self.verticalLayout_general = QVBoxLayout(self.widget_general)
        self.verticalLayout_general.setObjectName(u"verticalLayout_general")
        self.gridLayout_top.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_general.addWidget(self.tabWidget)

        # tab[<简易组队脚本>升级到V6.05]的垂直布局 -----------------------
        self.verticalLayout_tab_v6_05 = QVBoxLayout(self.tab_v6_05)
        self.verticalLayout_tab_v6_05.setObjectName(u"verticalLayout_tab_v6_05")
        self.verticalLayout_tab_v6_05.addWidget(self.widget_file_path, 3)
        self.verticalLayout_tab_v6_05.addWidget(self.widget_bottom_button, 1)

        # 文件路径的水平布局
        self.horizontalLayout_file_path = QHBoxLayout(self.widget_file_path)
        self.horizontalLayout_file_path.setSpacing(10)
        self.horizontalLayout_file_path.setObjectName(u"horizontalLayout_file_path")
        self.horizontalLayout_file_path.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_file_path.addWidget(self.label_file_path)
        self.horizontalLayout_file_path.addWidget(self.lineEdit_file_path)
        self.horizontalLayout_file_path.addWidget(self.pushButton_file_path)

        # 底部按钮
        self.horizontalLayout_bottom_button = QHBoxLayout(self.widget_bottom_button)
        self.horizontalLayout_bottom_button.setSpacing(10)
        self.horizontalLayout_bottom_button.setObjectName(u"horizontalLayout_bottom_button")
        self.horizontalLayout_bottom_button.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_bottom_button.addStretch()
        self.horizontalLayout_bottom_button.addWidget(self.pushButton_execute)
        self.horizontalLayout_bottom_button.addStretch()

        # tab[<一键日常助手>升级到V0.01]的垂直布局 -----------------------
        self.verticalLayout_general_new_v001 = QVBoxLayout(self.tab_new_v0_01)
        self.verticalLayout_general_new_v001.setObjectName(u"verticalLayout_general_new_v001")
        self.verticalLayout_general_new_v001.addWidget(self.widget_deck_path_new_v001, 1)
        self.verticalLayout_general_new_v001.addWidget(self.widget_deck_select_new_v001, 1)
        self.verticalLayout_general_new_v001.addWidget(self.widget_file_path_new_v001, 1)
        self.verticalLayout_general_new_v001.addWidget(self.widget_bottom_button_new_v001, 1)

        # ini文件路径的水平布局
        self.horizontalLayout_file_path_new_v001 = QHBoxLayout(self.widget_file_path_new_v001)
        self.horizontalLayout_file_path_new_v001.setSpacing(10)
        self.horizontalLayout_file_path_new_v001.setObjectName(u"horizontalLayout_file_path_new_v001")
        self.horizontalLayout_file_path_new_v001.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_file_path_new_v001.addWidget(self.label_file_path_new_v001)
        self.horizontalLayout_file_path_new_v001.addWidget(self.lineEdit_file_path_new_v001)
        self.horizontalLayout_file_path_new_v001.addWidget(self.pushButton_file_path_new_v001)

        # 卡片组文件路径的水平布局
        self.horizontalLayout_deck_path_new_v001 = QHBoxLayout(self.widget_deck_path_new_v001)
        self.horizontalLayout_deck_path_new_v001.setSpacing(10)
        self.horizontalLayout_deck_path_new_v001.setObjectName(u"horizontalLayout_deck_path_new_v001")
        self.horizontalLayout_deck_path_new_v001.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_deck_path_new_v001.addWidget(self.label_deck_path_new_v001)
        self.horizontalLayout_deck_path_new_v001.addWidget(self.lineEdit_deck_path_new_v001)
        self.horizontalLayout_deck_path_new_v001.addWidget(self.pushButton_deck_path_new_v001)

        # 账号所用卡片组的水平布局
        self.horizontalLayout_deck_select_new_v001 = QHBoxLayout(self.widget_deck_select_new_v001)
        self.horizontalLayout_deck_select_new_v001.setSpacing(10)
        self.horizontalLayout_deck_select_new_v001.setObjectName(u"horizontalLayout_deck_select_new_v001")
        self.horizontalLayout_deck_select_new_v001.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_deck_select_new_v001.addWidget(self.label_deck_select_1p_new_v001)
        self.horizontalLayout_deck_select_new_v001.addWidget(self.comboBox_deck_select_1p_new_v001)
        self.horizontalLayout_deck_select_new_v001.addWidget(self.label_deck_select_2p_new_v001)
        self.horizontalLayout_deck_select_new_v001.addWidget(self.comboBox_deck_select_2p_new_v001)

        # 底部按钮
        self.horizontalLayout_bottom_button_new_v001 = QHBoxLayout(self.widget_bottom_button_new_v001)
        self.horizontalLayout_bottom_button_new_v001.setSpacing(10)
        self.horizontalLayout_bottom_button_new_v001.setObjectName(u"horizontalLayout_bottom_button_new_v001")
        self.horizontalLayout_bottom_button_new_v001.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_bottom_button_new_v001.addStretch()
        self.horizontalLayout_bottom_button_new_v001.addWidget(self.pushButton_execute_new_v001)
        self.horizontalLayout_bottom_button_new_v001.addStretch()

        # 其他 ---------------------------------------------------------------------------------------
        self.retranslateUi(UpdateINI)
        QMetaObject.connectSlotsByName(UpdateINI)

    def retranslateUi(self, UpdateINI):
        # 升级ini文件
        UpdateINI.setWindowTitle(QCoreApplication.translate("UpdateINI", u"\u5347\u7EA7ini\u6587\u4EF6", None))
        # <简易组队脚本>V6.05 ------------------------------------
        # 文件路径
        self.label_file_path.setText(QCoreApplication.translate("UpdateINI", u"\u6587\u4ef6\u8def\u5f84: ", None))
        # 浏览
        self.pushButton_file_path.setText(QCoreApplication.translate("UpdateINI", u"\u6d4f\u89c8", None))
        # 执行
        self.pushButton_execute.setText(QCoreApplication.translate("UpdateINI", u"\u6267\u884C", None))
        # <一键日常助手>V0.01 ------------------------------------
        # 卡片组文件路径
        self.label_deck_path_new_v001.setText(QCoreApplication.translate("UpdateINI", u"卡片组\u8def\u5f84: ", None))
        # 浏览
        self.pushButton_deck_path_new_v001.setText(QCoreApplication.translate("UpdateINI", u"\u6d4f\u89c8", None))
        # 1P所用卡组
        self.label_deck_select_1p_new_v001.setText(QCoreApplication.translate("UpdateINI", u"1P所用卡组: ", None))
        # 2P所用卡组
        self.label_deck_select_2p_new_v001.setText(QCoreApplication.translate("UpdateINI", u"2P所用卡组: ", None))
        # ini文件路径
        self.label_file_path_new_v001.setText(QCoreApplication.translate("UpdateINI", u"ini\u6587\u4ef6\u8def\u5f84: ", None))
        # 浏览
        self.pushButton_file_path_new_v001.setText(QCoreApplication.translate("UpdateINI", u"\u6d4f\u89c8", None))
        # 执行
        self.pushButton_execute_new_v001.setText(QCoreApplication.translate("UpdateINI", u"\u6267\u884C", None))
