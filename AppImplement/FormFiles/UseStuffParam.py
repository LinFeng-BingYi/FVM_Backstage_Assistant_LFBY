# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UseStuffParam.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_UseStuffParam(object):
    def setupUi(self, UseStuffParam):
        if not UseStuffParam.objectName():
            UseStuffParam.setObjectName(u"UseStuffParam")
        UseStuffParam.resize(530, 340)
        self.verticalLayout_top = QVBoxLayout(UseStuffParam)
        self.verticalLayout_top.setSpacing(5)
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.verticalLayout_top.setContentsMargins(0, 5, 0, 10)
        self.widget_select_player = QWidget(UseStuffParam)
        self.widget_select_player.setObjectName(u"widget_select_player")
        self.horizontalLayout_select_player = QHBoxLayout(self.widget_select_player)
        self.horizontalLayout_select_player.setSpacing(5)
        self.horizontalLayout_select_player.setObjectName(u"horizontalLayout_select_player")
        self.horizontalLayout_select_player.setContentsMargins(-1, 0, -1, 0)
        self.label_select_player = QLabel(self.widget_select_player)
        self.label_select_player.setObjectName(u"label_select_player")

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

        self.widget_stuff_list = QWidget(UseStuffParam)
        self.widget_stuff_list.setObjectName(u"widget_stuff_list")
        self.verticalLayout_stuff_list = QVBoxLayout(self.widget_stuff_list)
        self.verticalLayout_stuff_list.setSpacing(5)
        self.verticalLayout_stuff_list.setObjectName(u"verticalLayout_stuff_list")
        self.verticalLayout_stuff_list.setContentsMargins(-1, 0, -1, 0)
        self.tableWidget_stuff_list = QTableWidget(self.widget_stuff_list)
        if (self.tableWidget_stuff_list.columnCount() < 4):
            self.tableWidget_stuff_list.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_stuff_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_stuff_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_stuff_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_stuff_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_stuff_list.setObjectName(u"tableWidget_stuff_list")
        self.tableWidget_stuff_list.setFrameShape(QFrame.Box)
        self.tableWidget_stuff_list.setFrameShadow(QFrame.Plain)
        self.tableWidget_stuff_list.setLineWidth(1)
        self.tableWidget_stuff_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_stuff_list.addWidget(self.tableWidget_stuff_list)

        self.widget_edit_btn = QWidget(self.widget_stuff_list)
        self.widget_edit_btn.setObjectName(u"widget_edit_btn")
        self.horizontalLayout_edit_btn = QHBoxLayout(self.widget_edit_btn)
        self.horizontalLayout_edit_btn.setSpacing(5)
        self.horizontalLayout_edit_btn.setObjectName(u"horizontalLayout_edit_btn")
        self.horizontalLayout_edit_btn.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_edit_btn_1 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_edit_btn.addItem(self.horizontalSpacer_edit_btn_1)

        self.pushButton_insert_row = QPushButton(self.widget_edit_btn)
        self.pushButton_insert_row.setObjectName(u"pushButton_insert_row")
        self.pushButton_insert_row.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_edit_btn.addWidget(self.pushButton_insert_row)

        self.horizontalSpacer_edit_btn_2 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_edit_btn.addItem(self.horizontalSpacer_edit_btn_2)

        self.pushButton_delete_row = QPushButton(self.widget_edit_btn)
        self.pushButton_delete_row.setObjectName(u"pushButton_delete_row")
        self.pushButton_delete_row.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_edit_btn.addWidget(self.pushButton_delete_row)

        self.horizontalSpacer_edit_btn_3 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_edit_btn.addItem(self.horizontalSpacer_edit_btn_3)


        self.verticalLayout_stuff_list.addWidget(self.widget_edit_btn)


        self.verticalLayout_top.addWidget(self.widget_stuff_list)


        self.retranslateUi(UseStuffParam)

        QMetaObject.connectSlotsByName(UseStuffParam)
    # setupUi

    def retranslateUi(self, UseStuffParam):
        UseStuffParam.setWindowTitle(QCoreApplication.translate("UseStuffParam", u"Form", None))
        self.label_select_player.setText(QCoreApplication.translate("UseStuffParam", u"\u9009\u62e9\u8d26\u53f7\uff1a", None))
        self.comboBox_select_player.setItemText(0, QCoreApplication.translate("UseStuffParam", u"1P", None))
        self.comboBox_select_player.setItemText(1, QCoreApplication.translate("UseStuffParam", u"2P", None))

        ___qtablewidgetitem = self.tableWidget_stuff_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UseStuffParam", u"\u622a\u56fe\u8def\u5f84", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem.setToolTip(QCoreApplication.translate("UseStuffParam", u"\u9009\u62e9\u5f85\u4f7f\u7528\u7269\u54c1\u7684\u622a\u56fe\u8def\u5f84\u3002\u5f53\u9009\u62e9\u6587\u4ef6\u5939\u65f6\uff0c\u8868\u793a\u5bf9\u8be5\u6587\u4ef6\u5939\u4e0b\u6240\u6709\u7269\u54c1\u6267\u884c\u64cd\u4f5c", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem1 = self.tableWidget_stuff_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UseStuffParam", u"\u4ea4\u4e92\u754c\u9762", None));
        ___qtablewidgetitem2 = self.tableWidget_stuff_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("UseStuffParam", u"\u6267\u884c\u64cd\u4f5c", None));
        ___qtablewidgetitem3 = self.tableWidget_stuff_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("UseStuffParam", u"\u6267\u884c\u6b21\u6570", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem3.setToolTip(QCoreApplication.translate("UseStuffParam", u"\u5f53\u586b\u5165-1\u65f6\uff0c\u8868\u793a\u6267\u884c\u64cd\u4f5c\u76f4\u5230\u6d88\u8017\u5b8c", None));
#endif // QT_CONFIG(tooltip)
        self.pushButton_insert_row.setText(QCoreApplication.translate("UseStuffParam", u"\u4e0b\u65b9\u63d2\u5165\u884c", None))
        self.pushButton_delete_row.setText(QCoreApplication.translate("UseStuffParam", u"\u5220\u9664\u5f53\u524d\u884c", None))
    # retranslateUi

