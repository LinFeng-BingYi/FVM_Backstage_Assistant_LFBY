#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QWidget

from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.EndParam import Ui_EndParam

from AppImplement.GlobalValue.StaticValue import ROOT_PATH


class EndListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = EndParamWidget()

    def getFuncParam(self, get_for_json=False):
        return self.func_widget.getAllParam(get_for_json)


class EndParamWidget(Ui_EndParam, BaseParamWidget):
    def __init__(self):
        super(EndParamWidget, self).__init__()
        self.setupUi(self)

        self.cwd = ROOT_PATH                      # 程序当前工作目录

    def getAllParam(self, get_for_json=False):
        return None

    def checkInputValidity(self):
        return True
