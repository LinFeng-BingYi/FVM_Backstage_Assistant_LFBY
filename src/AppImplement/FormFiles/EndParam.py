# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EndParam.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_EndParam(object):
    def setupUi(self, EndParam):
        if not EndParam.objectName():
            EndParam.setObjectName(u"EndParam")
        EndParam.resize(400, 300)
        self.gridLayout = QGridLayout(EndParam)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_func_dsc = QLabel(EndParam)
        self.label_func_dsc.setObjectName(u"label_func_dsc")
        self.label_func_dsc.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_func_dsc, 0, 0, 1, 1)


        self.retranslateUi(EndParam)

        QMetaObject.connectSlotsByName(EndParam)
    # setupUi

    def retranslateUi(self, EndParam):
        EndParam.setWindowTitle(QCoreApplication.translate("EndParam", u"\u7ed3\u675f", None))
        self.label_func_dsc.setText(QCoreApplication.translate("EndParam", u"\u8868\u793a\u6d41\u7a0b\u7684\u7ed3\u675f\uff0c\u5176\u540e\u7684\u529f\u80fd\u4e0d\u4f1a\u88ab\u6267\u884c", None))
    # retranslateUi

