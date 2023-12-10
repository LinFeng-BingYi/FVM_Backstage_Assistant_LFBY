# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QToolBar, QVBoxLayout, QWidget)

from AppImplement.FormFiles.CustomWidgets.ListWidget import FuncFlowListWidget

class Ui_MyMainWindow(object):
    def setupUi(self, MyMainWindow):
        if not MyMainWindow.objectName():
            MyMainWindow.setObjectName(u"MyMainWindow")
        MyMainWindow.resize(900, 600)
        MyMainWindow.setMinimumSize(QSize(900, 600))
        MyMainWindow.setMaximumSize(QSize(900, 600))
        MyMainWindow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.action_edit_placing_plan = QAction(MyMainWindow)
        self.action_edit_placing_plan.setObjectName(u"action_edit_placing_plan")
        self.action_edit_player_deck = QAction(MyMainWindow)
        self.action_edit_player_deck.setObjectName(u"action_edit_player_deck")
        self.action_style = QAction(MyMainWindow)
        self.action_style.setObjectName(u"action_style")
        self.action_global_config = QAction(MyMainWindow)
        self.action_global_config.setObjectName(u"action_global_config")
        self.action_tutorial = QAction(MyMainWindow)
        self.action_tutorial.setObjectName(u"action_tutorial")
        self.action_about = QAction(MyMainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(MyMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_central_widget = QVBoxLayout(self.centralwidget)
        self.verticalLayout_central_widget.setSpacing(5)
        self.verticalLayout_central_widget.setObjectName(u"verticalLayout_central_widget")
        self.verticalLayout_central_widget.setContentsMargins(7, 7, 7, 10)
        self.widget_main_tittle = QWidget(self.centralwidget)
        self.widget_main_tittle.setObjectName(u"widget_main_tittle")
        self.widget_main_tittle.setMaximumSize(QSize(16777215, 30))
        self.verticalLayout_main_tittle = QVBoxLayout(self.widget_main_tittle)
        self.verticalLayout_main_tittle.setSpacing(5)
        self.verticalLayout_main_tittle.setObjectName(u"verticalLayout_main_tittle")
        self.verticalLayout_main_tittle.setContentsMargins(0, 0, 0, 0)
        self.label_main_tittle = QLabel(self.widget_main_tittle)
        self.label_main_tittle.setObjectName(u"label_main_tittle")
        self.label_main_tittle.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"\u5e7c\u5706"])
        font.setPointSize(17)
        self.label_main_tittle.setFont(font)
        self.label_main_tittle.setFrameShape(QFrame.StyledPanel)
        self.label_main_tittle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_main_tittle.addWidget(self.label_main_tittle)

        self.verticalLayout_main_tittle.setStretch(0, 3)

        self.verticalLayout_central_widget.addWidget(self.widget_main_tittle)

        self.widget_business_flow = QWidget(self.centralwidget)
        self.widget_business_flow.setObjectName(u"widget_business_flow")
        self.horizontalLayout_business_flow = QHBoxLayout(self.widget_business_flow)
        self.horizontalLayout_business_flow.setSpacing(5)
        self.horizontalLayout_business_flow.setObjectName(u"horizontalLayout_business_flow")
        self.horizontalLayout_business_flow.setContentsMargins(0, 0, 0, 0)
        self.widget_edit_flow = QWidget(self.widget_business_flow)
        self.widget_edit_flow.setObjectName(u"widget_edit_flow")
        self.verticalLayout_edit_flow = QVBoxLayout(self.widget_edit_flow)
        self.verticalLayout_edit_flow.setObjectName(u"verticalLayout_edit_flow")
        self.verticalLayout_edit_flow.setContentsMargins(0, 0, 0, 3)
        self.label_edit_flow = QLabel(self.widget_edit_flow)
        self.label_edit_flow.setObjectName(u"label_edit_flow")
        self.label_edit_flow.setMinimumSize(QSize(0, 19))
        self.label_edit_flow.setMaximumSize(QSize(16777215, 19))

        self.verticalLayout_edit_flow.addWidget(self.label_edit_flow)

        self.listWidget_flow = FuncFlowListWidget(self.widget_edit_flow)
        self.listWidget_flow.setObjectName(u"listWidget_flow")
        self.listWidget_flow.setDragEnabled(True)
        self.listWidget_flow.setDragDropMode(QAbstractItemView.InternalMove)

        self.verticalLayout_edit_flow.addWidget(self.listWidget_flow)

        self.pushButton_add_flow = QPushButton(self.widget_edit_flow)
        self.pushButton_add_flow.setObjectName(u"pushButton_add_flow")
        self.pushButton_add_flow.setMinimumSize(QSize(0, 30))
        self.pushButton_add_flow.setMaximumSize(QSize(174, 16777215))

        self.verticalLayout_edit_flow.addWidget(self.pushButton_add_flow)


        self.horizontalLayout_business_flow.addWidget(self.widget_edit_flow)

        self.tabWidget_config_business = QTabWidget(self.widget_business_flow)
        self.tabWidget_config_business.setObjectName(u"tabWidget_config_business")
        self.tabWidget_config_business.setTabShape(QTabWidget.Rounded)
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"tab_home")
        self.verticalLayout_home = QVBoxLayout(self.tab_home)
        self.verticalLayout_home.setSpacing(6)
        self.verticalLayout_home.setObjectName(u"verticalLayout_home")
        self.verticalLayout_home.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_changelog = QPlainTextEdit(self.tab_home)
        self.plainTextEdit_changelog.setObjectName(u"plainTextEdit_changelog")

        self.verticalLayout_home.addWidget(self.plainTextEdit_changelog)

        self.progressBar = QProgressBar(self.tab_home)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        self.progressBar.setValue(0)

        self.verticalLayout_home.addWidget(self.progressBar)

        self.tabWidget_config_business.addTab(self.tab_home, "")
        self.tab_config_business = QWidget()
        self.tab_config_business.setObjectName(u"tab_config_business")
        self.verticalLayout_config_business = QVBoxLayout(self.tab_config_business)
        self.verticalLayout_config_business.setSpacing(6)
        self.verticalLayout_config_business.setObjectName(u"verticalLayout_config_business")
        self.verticalLayout_config_business.setContentsMargins(0, 0, 0, 0)
        self.widget_business_config = QWidget(self.tab_config_business)
        self.widget_business_config.setObjectName(u"widget_business_config")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_business_config)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_business_param_area = QWidget(self.widget_business_config)
        self.widget_business_param_area.setObjectName(u"widget_business_param_area")

        self.horizontalLayout_2.addWidget(self.widget_business_param_area)

        self.widget_business_button_area = QWidget(self.widget_business_config)
        self.widget_business_button_area.setObjectName(u"widget_business_button_area")
        self.widget_business_button_area.setMaximumSize(QSize(30, 16777215))
        self.verticalLayout_business_button_area = QVBoxLayout(self.widget_business_button_area)
        self.verticalLayout_business_button_area.setSpacing(5)
        self.verticalLayout_business_button_area.setObjectName(u"verticalLayout_business_button_area")
        self.verticalLayout_business_button_area.setContentsMargins(0, 0, 0, 0)
        self.pushButton_save_business = QPushButton(self.widget_business_button_area)
        self.pushButton_save_business.setObjectName(u"pushButton_save_business")
        self.pushButton_save_business.setMinimumSize(QSize(30, 0))
        self.pushButton_save_business.setMaximumSize(QSize(30, 16777215))

        self.verticalLayout_business_button_area.addWidget(self.pushButton_save_business)

        self.pushButton_apply_business = QPushButton(self.widget_business_button_area)
        self.pushButton_apply_business.setObjectName(u"pushButton_apply_business")
        self.pushButton_apply_business.setMinimumSize(QSize(30, 0))
        self.pushButton_apply_business.setMaximumSize(QSize(30, 16777215))

        self.verticalLayout_business_button_area.addWidget(self.pushButton_apply_business)


        self.horizontalLayout_2.addWidget(self.widget_business_button_area)


        self.verticalLayout_config_business.addWidget(self.widget_business_config)

        self.widget_business_config_file = QWidget(self.tab_config_business)
        self.widget_business_config_file.setObjectName(u"widget_business_config_file")
        self.widget_business_config_file.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.widget_business_config_file)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_business_config_file = QLabel(self.widget_business_config_file)
        self.label_business_config_file.setObjectName(u"label_business_config_file")
        self.label_business_config_file.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.label_business_config_file)

        self.lineEdit_business_config_file = QLineEdit(self.widget_business_config_file)
        self.lineEdit_business_config_file.setObjectName(u"lineEdit_business_config_file")
        self.lineEdit_business_config_file.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.lineEdit_business_config_file)

        self.pushButton_browser_business_config_file = QPushButton(self.widget_business_config_file)
        self.pushButton_browser_business_config_file.setObjectName(u"pushButton_browser_business_config_file")
        self.pushButton_browser_business_config_file.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.pushButton_browser_business_config_file)


        self.verticalLayout_config_business.addWidget(self.widget_business_config_file)

        self.tabWidget_config_business.addTab(self.tab_config_business, "")

        self.horizontalLayout_business_flow.addWidget(self.tabWidget_config_business)

        self.widget_log = QWidget(self.widget_business_flow)
        self.widget_log.setObjectName(u"widget_log")
        self.verticalLayout_log = QVBoxLayout(self.widget_log)
        self.verticalLayout_log.setSpacing(6)
        self.verticalLayout_log.setObjectName(u"verticalLayout_log")
        self.verticalLayout_log.setContentsMargins(0, 0, 0, 3)
        self.label_log = QLabel(self.widget_log)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setMinimumSize(QSize(0, 19))
        self.label_log.setMaximumSize(QSize(16777215, 19))

        self.verticalLayout_log.addWidget(self.label_log)

        self.plainTextEdit_log = QPlainTextEdit(self.widget_log)
        self.plainTextEdit_log.setObjectName(u"plainTextEdit_log")
        self.plainTextEdit_log.setReadOnly(True)

        self.verticalLayout_log.addWidget(self.plainTextEdit_log)

        self.widget_log_action = QWidget(self.widget_log)
        self.widget_log_action.setObjectName(u"widget_log_action")
        self.horizontalLayout_log_action = QHBoxLayout(self.widget_log_action)
        self.horizontalLayout_log_action.setSpacing(6)
        self.horizontalLayout_log_action.setObjectName(u"horizontalLayout_log_action")
        self.horizontalLayout_log_action.setContentsMargins(0, 0, 0, 0)
        self.pushButton_save_log = QPushButton(self.widget_log_action)
        self.pushButton_save_log.setObjectName(u"pushButton_save_log")
        self.pushButton_save_log.setMinimumSize(QSize(84, 30))
        self.pushButton_save_log.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_log_action.addWidget(self.pushButton_save_log)

        self.pushButton_clear_log = QPushButton(self.widget_log_action)
        self.pushButton_clear_log.setObjectName(u"pushButton_clear_log")
        self.pushButton_clear_log.setMinimumSize(QSize(84, 30))
        self.pushButton_clear_log.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_log_action.addWidget(self.pushButton_clear_log)


        self.verticalLayout_log.addWidget(self.widget_log_action)


        self.horizontalLayout_business_flow.addWidget(self.widget_log)

        self.horizontalLayout_business_flow.setStretch(0, 2)
        self.horizontalLayout_business_flow.setStretch(1, 6)
        self.horizontalLayout_business_flow.setStretch(2, 2)

        self.verticalLayout_central_widget.addWidget(self.widget_business_flow)

        self.widget_flow_control = QWidget(self.centralwidget)
        self.widget_flow_control.setObjectName(u"widget_flow_control")
        self.widget_flow_control.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_flow_control = QHBoxLayout(self.widget_flow_control)
        self.horizontalLayout_flow_control.setObjectName(u"horizontalLayout_flow_control")
        self.horizontalLayout_flow_control.setContentsMargins(0, 0, 0, 0)
        self.pushButton_save_flow = QPushButton(self.widget_flow_control)
        self.pushButton_save_flow.setObjectName(u"pushButton_save_flow")
        self.pushButton_save_flow.setMinimumSize(QSize(84, 30))

        self.horizontalLayout_flow_control.addWidget(self.pushButton_save_flow)

        self.pushButton_apply_flow = QPushButton(self.widget_flow_control)
        self.pushButton_apply_flow.setObjectName(u"pushButton_apply_flow")
        self.pushButton_apply_flow.setMinimumSize(QSize(84, 30))

        self.horizontalLayout_flow_control.addWidget(self.pushButton_apply_flow)

        self.widget_flow_setting = QWidget(self.widget_flow_control)
        self.widget_flow_setting.setObjectName(u"widget_flow_setting")
        self.widget_flow_setting.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_flow_setting = QHBoxLayout(self.widget_flow_setting)
        self.horizontalLayout_flow_setting.setObjectName(u"horizontalLayout_flow_setting")
        self.horizontalLayout_flow_setting.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_flow_setting_left = QSpacerItem(201, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_flow_setting.addItem(self.horizontalSpacer_flow_setting_left)

        self.checkBox_remaind_stop = QCheckBox(self.widget_flow_setting)
        self.checkBox_remaind_stop.setObjectName(u"checkBox_remaind_stop")
        self.checkBox_remaind_stop.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_flow_setting.addWidget(self.checkBox_remaind_stop)

        self.horizontalSpacer_flow_setting_right = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_flow_setting.addItem(self.horizontalSpacer_flow_setting_right)


        self.horizontalLayout_flow_control.addWidget(self.widget_flow_setting)

        self.pushButton_start_flow = QPushButton(self.widget_flow_control)
        self.pushButton_start_flow.setObjectName(u"pushButton_start_flow")
        self.pushButton_start_flow.setMinimumSize(QSize(84, 30))

        self.horizontalLayout_flow_control.addWidget(self.pushButton_start_flow)

        self.pushButton_end_flow = QPushButton(self.widget_flow_control)
        self.pushButton_end_flow.setObjectName(u"pushButton_end_flow")
        self.pushButton_end_flow.setMinimumSize(QSize(84, 30))

        self.horizontalLayout_flow_control.addWidget(self.pushButton_end_flow)


        self.verticalLayout_central_widget.addWidget(self.widget_flow_control)

        self.verticalLayout_central_widget.setStretch(0, 1)
        self.verticalLayout_central_widget.setStretch(1, 8)
        self.verticalLayout_central_widget.setStretch(2, 2)
        MyMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MyMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menu_function = QMenu(self.menubar)
        self.menu_function.setObjectName(u"menu_function")
        self.menu_function.setMinimumSize(QSize(120, 0))
        self.menu_setting = QMenu(self.menubar)
        self.menu_setting.setObjectName(u"menu_setting")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MyMainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MyMainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MyMainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_function.menuAction())
        self.menubar.addAction(self.menu_setting.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_function.addAction(self.action_edit_placing_plan)
        self.menu_function.addAction(self.action_edit_player_deck)
        self.menu_setting.addAction(self.action_style)
        self.menu_setting.addAction(self.action_global_config)
        self.menu_help.addAction(self.action_tutorial)
        self.menu_help.addAction(self.action_about)
        self.toolBar.addAction(self.action_edit_placing_plan)
        self.toolBar.addAction(self.action_edit_player_deck)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_style)
        self.toolBar.addAction(self.action_global_config)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_tutorial)
        self.toolBar.addAction(self.action_about)

        self.retranslateUi(MyMainWindow)

        self.tabWidget_config_business.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MyMainWindow)
    # setupUi

    def retranslateUi(self, MyMainWindow):
        MyMainWindow.setWindowTitle(QCoreApplication.translate("MyMainWindow", u"FVM\u4e00\u952e\u65e5\u5e38\u52a9\u624b - \u6797\u98ce\u51b0\u7ffc", None))
        self.action_edit_placing_plan.setText(QCoreApplication.translate("MyMainWindow", u"\u7f16\u8f91\u653e\u5361\u65b9\u6848", None))
        self.action_edit_player_deck.setText(QCoreApplication.translate("MyMainWindow", u"\u7f16\u8f91\u8d26\u53f7\u5361\u7ec4", None))
        self.action_style.setText(QCoreApplication.translate("MyMainWindow", u"\u7a97\u53e3\u98ce\u683c", None))
        self.action_global_config.setText(QCoreApplication.translate("MyMainWindow", u"\u5168\u5c40\u914d\u7f6e", None))
        self.action_tutorial.setText(QCoreApplication.translate("MyMainWindow", u"\u4f7f\u7528\u6559\u7a0b", None))
        self.action_about.setText(QCoreApplication.translate("MyMainWindow", u"\u5173\u4e8e", None))
        self.label_main_tittle.setText(QCoreApplication.translate("MyMainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#55aaff;\">\u6b22\u8fce\u4f7f\u7528\u3010FVM\u4e00\u952e\u65e5\u5e38\u52a9\u624b\u3011\uff01</span><span style=\" font-size:10pt;\">\u95ee\u9898\u53cd\u9988Q\u7fa4\uff1a51865331 B\u7ad9\u89c6\u9891\u6559\u7a0b\uff1a\u6797\u98ce\u51b0\u7ffc</span></p></body></html>", None))
        self.label_edit_flow.setText(QCoreApplication.translate("MyMainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\u6d41\u7a0b\u7f16\u8f91\u533a</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.listWidget_flow.setToolTip(QCoreApplication.translate("MyMainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u529f\u80fd\u6d41\u7a0b\u5217\u8868</span></p><p>\u53cc\u51fb\u9009\u4e2d\uff0c\u53f3\u4fa7\u663e\u793a\u53c2\u6570\u754c\u9762</p><p>\u53f3\u952e\u53ef\u5220\u9664\u3001\u7981\u7528\u3001\u89e3\u7981</p><p>\u6d41\u7a0b\u72b6\u6001\uff1a</p><p><span style=\" font-size:12pt; color:#5f9ea0;\">\u25cf</span>\u6302\u8d77</p><p><span style=\" font-size:12pt; color:green;\">\u25cf</span>\u7b49\u5f85</p><p><span style=\" font-size:12pt; color:blue;\">\u25cf</span><span style=\" font-size:12pt;\"/>\u6267\u884c</p><p><span style=\" font-size:12pt; color:yellow;\">\u25cf</span><span style=\" font-size:12pt;\"/>\u5b8c\u6210</p><p><span style=\" font-size:12pt; color:red;\">\u25cf</span><span style=\" font-size:12pt;\"/>\u9519\u8bef</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_add_flow.setToolTip(QCoreApplication.translate("MyMainWindow", u"\u5411\u6d41\u7a0b\u5217\u8868\u4e2d\u6dfb\u52a0\u529f\u80fd", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_add_flow.setText(QCoreApplication.translate("MyMainWindow", u"\u6dfb\u52a0\u529f\u80fd", None))
        self.tabWidget_config_business.setTabText(self.tabWidget_config_business.indexOf(self.tab_home), QCoreApplication.translate("MyMainWindow", u"\u9996\u9875", None))
        self.pushButton_save_business.setText(QCoreApplication.translate("MyMainWindow", u"\u4fdd\n"
"\u5b58\n"
"\u529f\n"
"\u80fd\n"
"\u53c2\n"
"\u6570", None))
        self.pushButton_apply_business.setText(QCoreApplication.translate("MyMainWindow", u"\u5e94\n"
"\u7528\n"
"\u529f\n"
"\u80fd\n"
"\u53c2\n"
"\u6570", None))
        self.label_business_config_file.setText(QCoreApplication.translate("MyMainWindow", u"\u529f\u80fd\u914d\u7f6e\u6587\u4ef6\uff1a", None))
        self.pushButton_browser_business_config_file.setText(QCoreApplication.translate("MyMainWindow", u"\u6d4f\u89c8", None))
        self.tabWidget_config_business.setTabText(self.tabWidget_config_business.indexOf(self.tab_config_business), QCoreApplication.translate("MyMainWindow", u"\u529f\u80fd\u53c2\u6570\u914d\u7f6e", None))
        self.label_log.setText(QCoreApplication.translate("MyMainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\u65e5\u5fd7\u8f93\u51fa\u533a</span></p></body></html>", None))
        self.pushButton_save_log.setText(QCoreApplication.translate("MyMainWindow", u"\u4fdd\u5b58\u65e5\u5fd7", None))
        self.pushButton_clear_log.setText(QCoreApplication.translate("MyMainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
#if QT_CONFIG(tooltip)
        self.pushButton_save_flow.setToolTip(QCoreApplication.translate("MyMainWindow", u"\u5c06\u5217\u8868\u4e2d\u7684\u529f\u80fd\u6d41\u7a0b\u4fdd\u5b58\u81f3JSON\u6587\u4ef6\uff0c\u4ee5\u4fbf\u4ee5\u540e\u5feb\u901f\u5e94\u7528", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_save_flow.setText(QCoreApplication.translate("MyMainWindow", u"\u4fdd\u5b58\u6d41\u7a0b", None))
#if QT_CONFIG(tooltip)
        self.pushButton_apply_flow.setToolTip(QCoreApplication.translate("MyMainWindow", u"\u4ece\u4fdd\u5b58\u7684JSON\u6587\u4ef6\u4e2d\u5e94\u7528\u529f\u80fd\u6d41\u7a0b", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_apply_flow.setText(QCoreApplication.translate("MyMainWindow", u"\u5e94\u7528\u6d41\u7a0b", None))
        self.checkBox_remaind_stop.setText(QCoreApplication.translate("MyMainWindow", u"\u7ed3\u675f\u65f6\u5f39\u7a97\u63d0\u9192", None))
        self.pushButton_start_flow.setText(QCoreApplication.translate("MyMainWindow", u"\u5f00\u59cb\u6d41\u7a0b", None))
        self.pushButton_end_flow.setText(QCoreApplication.translate("MyMainWindow", u"\u7ed3\u675f\u6d41\u7a0b", None))
        self.menu_function.setTitle(QCoreApplication.translate("MyMainWindow", u"\u529f\u80fd", None))
        self.menu_setting.setTitle(QCoreApplication.translate("MyMainWindow", u"\u8bbe\u7f6e", None))
        self.menu_help.setTitle(QCoreApplication.translate("MyMainWindow", u"\u5e2e\u52a9", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MyMainWindow", u"toolBar", None))
    # retranslateUi

