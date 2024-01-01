#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path

from PySide6.QtGui import QAction, QFont, QPixmap
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QMenu, QMessageBox, QWidget, QLabel, QLineEdit, QVBoxLayout
from PySide6.QtCore import Qt, Signal

from AppImplement.FlowFunction.StartListItem import StartListWidget
from AppImplement.FlowFunction.EndListItem import EndListWidget
from AppImplement.FlowFunction.LoopLevelListItem import LoopLevelListWidget
from AppImplement.FlowFunction.DailyAwardListItem import DailyAwardListWidget
from AppImplement.FlowFunction.UnionQuestListItem import UnionQuestListWidget
from AppImplement.FlowFunction.LoversQuestListItem import LoversQuestListWidget
from AppImplement.FlowFunction.VolcanicRelicListItem import VolcanicRelicListWidget
from AppImplement.FlowFunction.MagicTowerListItem import MagicTowerListWidget
from AppImplement.FlowFunction.CrossServiceListItem import CrossServiceListWidget
from AppImplement.FlowFunction.WantedListItem import WantedListWidget

from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH

# 若需要修改键名，BusinessBus类的run函数中也要做相应的修改
SUPPORT_FUNC = {
    "开始": StartListWidget,
    "结束": EndListWidget,
    "日常领取": DailyAwardListWidget,
    "刷指定关卡": LoopLevelListWidget,
    "公会任务": UnionQuestListWidget,
    "情侣任务": LoversQuestListWidget,
    "火山遗迹": VolcanicRelicListWidget,
    "魔塔蛋糕": MagicTowerListWidget,
    "跨服远征": CrossServiceListWidget,
    "悬赏三连": WantedListWidget
}


class FuncFlowListWidget(QListWidget):
    signal_show_func_param_tab = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        # 设置双击item使它对应的 func_widget 控件可见
        self.itemDoubleClicked.connect(self.showSelectedFuncWidget)

        # 列表中 所有的 item_widget
        self.item_widget_list = []
        # 列表中 有效的 item_widget
        self.active_item_widget_list = []

    def showContextMenu(self, pos):
        """添加右键菜单
        """
        list_item = self.itemAt(pos)
        index = self.row(list_item)
        if list_item is None or index == 0:
            # 没有item时 以及 开始item 不支持右键菜单
            return
        if self.itemWidget(list_item).getFuncName() == "结束":
            # “结束”item不支持右键菜单
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
        # 创建 重置所有功能状态 动作
        action_reset_all_status = QAction("重置所有功能状态", self)
        action_reset_all_status.triggered.connect(self.resetAllFuncStatus)
        # 加入菜单
        list_widget_menu = QMenu(self)
        list_widget_menu.addAction(action_delete)
        list_widget_menu.addAction(action_ban)
        list_widget_menu.addAction(action_lift_ban)
        list_widget_menu.addAction(action_reset_all_status)
        list_widget_menu.exec(self.mapToGlobal(pos))

    def showSelectedFuncWidget(self, list_item):
        # 先将所有控件设置为不可见
        for item_widget in self.item_widget_list:
            item_widget.getFuncWidget().setVisible(False)
        # 在将对应的控件设为可见
        item_widget = self.itemWidget(list_item)
        item_widget.getFuncWidget().setVisible(True)
        self.signal_show_func_param_tab.emit()

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
        if func_name == "开始":
            # 如果是“开始”功能，则设置该item不可拖拽
            listWidgetItem.setFlags(listWidgetItem.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
        # 添加列表项并关联控件
        self.addItem(listWidgetItem)
        self.setItemWidget(listWidgetItem, list_item_widget)

        # 先将其他控件设置为不可见
        for item_widget in self.item_widget_list:
            item_widget.getFuncWidget().setVisible(False)
        # 将列表项控件加入属性
        self.item_widget_list.append(list_item_widget)
        # 将焦点放在新创建的item上
        self.setCurrentItem(listWidgetItem)
        # 将需要加入tab页的 列表项控件关联的参数widget 返回
        return list_item_widget.getFuncWidget()

    def deleteItem(self, list_item):
        item_widget = self.itemWidget(list_item)
        item_widget.getFuncWidget().deleteLater()
        self.takeItem(self.row(list_item))

        self.item_widget_list.remove(item_widget)
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

    def clearAllItem(self):
        for list_item in [self.item(i) for i in range(self.count())]:
            self.deleteItem(list_item)

    def resetAllFuncStatus(self):
        for i in range(self.count()):
            list_item = self.item(i)
            item_widget = self.itemWidget(list_item)
            # 对于“结束”item之前的所有状态不是“挂起”的功能，重置它的状态
            if item_widget.getFuncName() == "结束":
                break
            if item_widget.getStatus() != "hanging":
                item_widget.changeStatus("hanging")

    def checkFuncOrderValidity(self):
        if self.item_widget_list[0].getFuncName() != "开始":
            return False
        if self.item_widget_list[-1:][0].getFuncName() != "结束":
            tip_message_box = QMessageBox(
                QMessageBox.Icon.NoIcon,
                "提示",
                "[结束]功能之后还有其他功能，这些功能将不被执行，是否继续",
                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
            )
            tip_message_box.setButtonText(QMessageBox.StandardButton.Ok, "确定")
            tip_message_box.setButtonText(QMessageBox.StandardButton.Cancel, "取消")
            result = tip_message_box.exec()
            if result == QMessageBox.StandardButton.Cancel:
                return False
        return True

    def checkActiveFuncParamValidity(self):
        # 避免使用list.clear()方法，这会导致原地址中的数据被清除
        self.active_item_widget_list = []
        # print("当前列表中功能数", self.count())
        for i in range(self.count()):
            list_item = self.item(i)
            item_widget = self.itemWidget(list_item)
            # 对于“结束”item之前的所有状态为“挂起”的功能，检查其界面参数合法性
            if item_widget.getFuncName() == "结束":
                break
            if item_widget.getStatus() != "hanging":
                continue
            # 若检测正常，则加入 有效功能list中
            func_check_result = item_widget.getFuncWidget().checkInputValidity()
            if isinstance(func_check_result, bool):
                self.active_item_widget_list.append(item_widget)
            else:
                # 否则，提示错误
                tip_message_box = QMessageBox(
                    QMessageBox.Icon.NoIcon,
                    "错误",
                    f"[{item_widget.getFuncName()}]功能的界面参数不合法！\n\n{func_check_result[1]}",
                    QMessageBox.StandardButton.Ok
                )
                tip_message_box.setButtonText(QMessageBox.StandardButton.Ok, "确定")
                tip_message_box.exec()
                return False
        return True

    def getFlowFuncsParam(self, change_status=True):
        if not self.checkFuncOrderValidity():
            return None
        if not self.checkActiveFuncParamValidity():
            return None
        flow_funcs_param = []
        for item_widget in self.active_item_widget_list:
            func_widget_param = item_widget.getFuncParam()
            func_widget_param["func_name"] = item_widget.getFuncName()
            flow_funcs_param.append(func_widget_param)
            # print("功能参数", func_widget_param)
            if change_status:
                item_widget.changeStatus("waiting")
        return flow_funcs_param

    def updateFlowFuncStatus(self, func_no, status):
        self.active_item_widget_list[func_no].changeStatus(status)

    def flowFinished(self):
        for item_widget in self.active_item_widget_list:
            if item_widget.getStatus() != "wrong":
                item_widget.changeStatus("hanging")

    def dropEvent(self, event):
        # 设置其他item不能排在“开始”item之前
        # print(event.pos())
        old_no = self.currentRow()
        if event.pos().y() < self.item(0).sizeHint().height() / 2:
            event.ignore()
        else:
            super().dropEvent(event)
            new_no = self.currentRow()

            old_item_widget = self.item_widget_list.pop(old_no)
            self.item_widget_list.insert(new_no, old_item_widget)


class PlayerDeckListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, pos):
        """添加右键菜单
        """
        list_item = self.itemAt(pos)
        # 创建 添加 动作
        action_add = QAction("添加", self)
        action_add.triggered.connect(lambda: self.addListItem(None, None))
        # 创建 删除 动作
        action_delete = QAction("删除", self)
        action_delete.triggered.connect(lambda: self.deleteItem(list_item))
        # 加入菜单
        list_widget_menu = QMenu(self)
        list_widget_menu.addAction(action_add)
        list_widget_menu.addAction(action_delete)
        list_widget_menu.exec(self.mapToGlobal(pos))

    def addListItem(self, card_info: list = None, card_pic_path: str = None):
        # print(card_info)
        # 创建列表项控件
        card_item_widget = PlayerDeckListWidget.DeckListItem(self)
        if card_pic_path is None or not os.path.exists(card_pic_path):
            card_pic_path = ROOT_PATH + r"\resources\images\application\其他图片\默认卡片图片.bmp"
        if card_info is not None:
            card_item_widget.setCardInfo(card_info)
        card_item_widget.setCardPic(card_pic_path)
        # 创建列表项
        listWidgetItem = QListWidgetItem(self)
        listWidgetItem.setSizeHint(card_item_widget.size())
        # 添加列表项并关联控件
        self.addItem(listWidgetItem)
        self.setItemWidget(listWidgetItem, card_item_widget)

    def deleteItem(self, list_item):
        item_widget = self.itemWidget(list_item)
        self.takeItem(self.row(list_item))
        item_widget.deleteLater()

    class DeckListItem(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setupUi()

        def setupUi(self):
            # 整个widget的设置
            self.setFixedSize(50, 90)
            # 卡片图片
            self.label_card_pic = QLabel(self)
            self.label_card_pic.setObjectName("label_card_pic")
            # self.label_card_pic.setFixedSize(40, 40)
            # self.label_card_pic.setPixmap("card_pic.png")
            # self.label_card_pic.setScaledContents(True)
            # 卡片名称
            self.lineEdit_card_name = QLineEdit(self)
            self.lineEdit_card_name.setObjectName("lineEdit_card_name")
            self.lineEdit_card_name.setMinimumHeight(30)
            font_card_name = QFont()
            font_card_name.setBold(True)
            font_card_name.setPointSize(10)
            self.lineEdit_card_name.setFont(font_card_name)
            # 卡槽位置
            self.lineEdit_card_slot = QLineEdit(self)
            self.lineEdit_card_slot.setObjectName("lineEdit_card_slot")
            self.lineEdit_card_slot.setMinimumHeight(20)

            # 布局
            self.verticalLayout = QVBoxLayout(self)
            self.verticalLayout.setObjectName("verticalLayout")
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout.setSpacing(0)
            self.verticalLayout.addWidget(self.label_card_pic)
            self.verticalLayout.addWidget(self.lineEdit_card_name)
            self.verticalLayout.addWidget(self.lineEdit_card_slot)

        def setCardInfo(self, card_info):
            self.lineEdit_card_name.setText(card_info[0])
            self.lineEdit_card_slot.setText(str(card_info[1]))

        def setCardPic(self, pic_path):
            self.label_card_pic.setPixmap(QPixmap(pic_path))
