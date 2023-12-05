#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QMenu
from PySide6.QtCore import Qt

from src.AppImplement.FlowFunction.StartListItem import StartListWidget

SUPPORT_FUNC = {"开始": StartListWidget}


class FuncFlowListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        self.flow_list = []

    def addListItem(self, func_name):
        """向 listWidget 中添加对应功能的 item_widget，并返回它关联的 func_widget，以便加入主界面的"功能参数配置"tab页

        Args:
            func_name: str["开始", "结束"]
                功能名称
        """
        # 创建列表项控件
        list_item_widget = SUPPORT_FUNC[func_name](func_name)
        # 创建列表项
        listWidgetItem = QListWidgetItem(self)
        listWidgetItem.setSizeHint(list_item_widget.sizeHint())
        # 添加列表项并关联控件
        self.addItem(listWidgetItem)
        self.setItemWidget(listWidgetItem, list_item_widget)

        # 将列表项控件加入属性
        self.flow_list.append(list_item_widget)
        # 将需要加入tab页的 列表项控件关联的参数widget 返回
        return list_item_widget.getFuncWidget()

    def showContextMenu(self, pos):
        """添加右键菜单
        """
        list_item = self.itemAt(pos)
        index = self.row(list_item)
        if list_item is None or index == 0 or index == len(self.flow_list) - 1:
            return
        # 创建 删除 动作
        action_delete = QAction("删除", self)
        action_delete.triggered.connect(lambda: self.deleteItem(list_item))
        # 创建 禁用 动作
        action_ban = QAction("禁用", self)
        action_ban.triggered.connect(lambda: self.banItem(list_item))
        # 创建 解禁 动作
        action_lift_ban = QAction("解禁", self)
        action_lift_ban.triggered.connect(lambda: self.liftBanItem(list_item))
        # 加入菜单
        list_widget_menu = QMenu(self)
        list_widget_menu.addAction(action_delete)
        list_widget_menu.addAction(action_ban)
        list_widget_menu.addAction(action_lift_ban)
        list_widget_menu.exec(self.mapToGlobal(pos))

    def deleteItem(self, list_item):
        item_widget = self.itemWidget(list_item)
        item_widget.getFuncWidget().deleteLater()
        self.takeItem(self.row(list_item))

        self.flow_list.remove(item_widget)
        item_widget.deleteLater()

    def banItem(self, list_item):
        item_widget = self.itemWidget(list_item)
        if item_widget.getStatus() == "banned":
            return
        item_widget.getFuncWidget().setEnabled(False)
        item_widget.changeStatus("banned")

    def liftBanItem(self, list_item):
        item_widget = self.itemWidget(list_item)
        if item_widget.getStatus() != "banned":
            return
        item_widget.getFuncWidget().setEnabled(True)
        item_widget.changeStatus("hanging")
