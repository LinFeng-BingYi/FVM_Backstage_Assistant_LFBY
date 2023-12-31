#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QMessageBox, QFileDialog
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Signal

from AppImplement.FormFiles.MyMainWindow import Ui_MyMainWindow
from AppImplement.FormFiles.EditPlacingPlanForm import WidgetEditPlacingPlan
from AppImplement.FormFiles.UpdateINIForm import WidgetUpdateINI
from AppImplement.FormFiles.SaveFlowListForm import WidgetSaveFlowList
from AppImplement.FormFiles.CustomWidgets.ListWidget import SUPPORT_FUNC
from AppImplement.FormFiles.CustomWidgets.Dialog import AddFuncFlowDialog

from AppImplement.Business.BusBusiness import BusinessBus
from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH, DEFAULT_FUNC_FLOW_JSON

from copy import deepcopy


class MainMyMainWindow(QMainWindow, Ui_MyMainWindow):
    signal_update_flow_func_status = Signal(int, str)

    def __init__(self):
        super(MainMyMainWindow, self).__init__()
        self.setupUi(self)
        # 补加控件
        self.verticalLayout_business_param_area = QVBoxLayout(self.widget_business_param_area)
        self.verticalLayout_business_param_area.setObjectName("verticalLayout_business_param_area")
        self.verticalLayout_business_param_area.setContentsMargins(5, 0, 0, 0)

        # 子窗口
        self.editPlacingPlanForm = None                     # 编辑放卡方案窗口
        self.updateIniForm = None                           # 升级放卡方案ini文件窗口
        self.add_func_flow_dialog = AddFuncFlowDialog()     # 添加功能到流程列表的内置对话框
        self.saveFlowListForm = WidgetSaveFlowList()        # 保存功能流程列表为json文件的窗口
        self.add_func_flow_dialog.signal_send_func_name.connect(self.addListWidget)
        # 内置消息框，用于提示信息
        self.tip_message_box = QMessageBox(
            QMessageBox.Icon.NoIcon,
            "提示",
            "信息",
            QMessageBox.StandardButton.Ok)
        self.tip_message_box.button(QMessageBox.StandardButton.Ok).setText("确定")

        # listWidget中的item列表
        self.flow_list = []

        # 内置主线程
        self.thread_business_bus = BusinessBus()

        self.bindSignal()
        self.initWidget()

    def initWidget(self):
        if ROOT_PATH is None or ROOT_PATH == "":
            self.tip_message_box.setWindowTitle("错误")
            self.tip_message_box.setText("未找到配置文件[AppGlobalSetting.ini]！\n请务必将其放在与exe同级目录下的config文件夹中，"
                                         "否则无法正常使用！\n\n完成以上操作后需要重启软件")
            self.tip_message_box.show()
        # 初始化时，加载指定的json文件，若未指定或指定的文件不存在，则向流程列表中添加”开始“、”结束“item
        if DEFAULT_FUNC_FLOW_JSON != "" and self.saveFlowListForm.setJsonToLineedit(DEFAULT_FUNC_FLOW_JSON):
            self.saveFlowListForm.readFlowListParam()
            self.saveFlowListForm.applyJsonFile()
        else:
            self.addListWidget("开始")
            self.addListWidget("结束")

    def bindSignal(self):
        # 菜单栏打开对应窗口
        self.action_edit_placing_plan.triggered.connect(self.displayEditPlacingPlanForm)
        self.action_ini_file_update.triggered.connect(self.displayUpdateIniForm)

        # 功能流程列表添加功能
        self.pushButton_add_flow.clicked.connect(self.showAddFuncFlowDialog)
        # 双击流程显示”功能参数“tab页
        self.listWidget_flow.signal_show_func_param_tab.connect(
            lambda: self.tabWidget_config_business.setCurrentIndex(1))
        # 保存功能流程参数
        self.pushButton_save_flow.clicked.connect(self.openSaveFlowList)
        # 应用功能流程参数
        self.pushButton_apply_flow.clicked.connect(self.openApplyFlowList)
        self.saveFlowListForm.signal_apply_flow_param.connect(self.applyFlowParam)

        # 启动/结束流程
        self.pushButton_start_flow.clicked.connect(self.startBusinessBus)
        self.pushButton_end_flow.clicked.connect(self.stopBusinessBus)

        # 线程业务消息打印在日志中
        self.thread_business_bus.signal_send_business_message.connect(self.printLog)
        # 线程业务错误通过提示框警告
        self.thread_business_bus.signal_send_business_error.connect(self.popupError)
        # 线程更新流程中功能的状态
        self.thread_business_bus.signal_send_func_status.connect(self.signal_update_flow_func_status)
        self.signal_update_flow_func_status.connect(self.listWidget_flow.updateFlowFuncStatus)
        # 完成流程后将所有状态置为“挂起”
        self.thread_business_bus.signal_flow_finished.connect(self.listWidget_flow.flowFinished)

        # 清除日志
        self.pushButton_clear_log.clicked.connect(self.plainTextEdit_log.clear)
        # 保存日志
        self.pushButton_save_log.clicked.connect(self.saveLog)

    def displayEditPlacingPlanForm(self):
        """响应菜单，打开'编辑放卡方案'窗口
        """
        self.editPlacingPlanForm = WidgetEditPlacingPlan()
        self.editPlacingPlanForm.show()

    def displayUpdateIniForm(self):
        """响应菜单，打开'升级ini文件'窗口
        """
        self.updateIniForm = WidgetUpdateINI()
        self.updateIniForm.show()

    def addListWidget(self, func_name):
        if func_name not in SUPPORT_FUNC:
            self.tip_message_box.setWindowTitle("错误")
            self.tip_message_box.setText("不支持的功能！！！")
            self.tip_message_box.show()
            return
        # 创建列表项控件
        func_widget = self.listWidget_flow.addListItem(func_name)
        # 将列表项控件关联的参数widget加入tab页
        self.verticalLayout_business_param_area.addWidget(func_widget)
        # 焦点设置到“功能参数配置”tab页
        if func_name not in ["开始", "结束"]:
            self.tabWidget_config_business.setCurrentIndex(1)

    def showAddFuncFlowDialog(self):
        self.add_func_flow_dialog.show()

    def startBusinessBus(self):
        if self.thread_business_bus.isRunning():
            self.tip_message_box.setWindowTitle("错误")
            self.tip_message_box.setText("当前还有流程正在执行！！！")
            self.tip_message_box.show()
            return
        flow_funcs_param = self.listWidget_flow.getFlowFuncsParam()
        if flow_funcs_param is None or len(flow_funcs_param) == 0:
            return
        print("获取到的界面参数：\n", flow_funcs_param)
        self.thread_business_bus.setFuncFlow(flow_funcs_param)
        self.thread_business_bus.start()

    def stopBusinessBus(self):
        if not self.thread_business_bus.isRunning():
            self.tip_message_box.setWindowTitle("错误")
            self.tip_message_box.setText("当前没有流程正在执行！！！")
            self.tip_message_box.show()
            return
        self.thread_business_bus.terminate()

    def printLog(self, message_str):
        self.plainTextEdit_log.setPlainText(
            self.plainTextEdit_log.toPlainText() + message_str
        )
        # 设置光标到文本末尾，方便查看最新消息
        self.plainTextEdit_log.moveCursor(QTextCursor.MoveOperation.End)

    def saveLog(self):
        if self.plainTextEdit_log.toPlainText() == "":
            self.tip_message_box.setWindowTitle("错误")
            self.tip_message_box.setText("日志输出区中没有信息！！！")
            self.tip_message_box.show()
            return
        first_line_str = self.plainTextEdit_log.document().findBlockByLineNumber(0).text()
        time_str = first_line_str[0:19]
        # print(time_str)
        pure_time_str = time_str.replace('/', '').replace(' ', '').replace(':', '')
        flow_file_path, _ = QFileDialog.getSaveFileName(
            self, "保存文件",
            ROOT_PATH + f"\\logs\\{pure_time_str}.log",
            "All Files(*);;LOG Files(*.log)"
        )
        f = open(flow_file_path, 'w', encoding='utf-8')
        f.write(self.plainTextEdit_log.toPlainText())
        f.close()

    def popupError(self, error_str):
        self.tip_message_box.setWindowTitle("错误")
        self.tip_message_box.setText(error_str)
        self.tip_message_box.show()

    def openSaveFlowList(self):
        flow_funcs_param = self.listWidget_flow.getFlowFuncsParam(False)
        if flow_funcs_param is None or len(flow_funcs_param) == 0:
            return
        # 流程中单个功能可以出现多次，使用dict存储会键冲突，改用list存储
        # print(flow_funcs_param)
        self.saveFlowListForm.setSaveMode()
        self.saveFlowListForm.setFlowParamList(flow_funcs_param)
        self.saveFlowListForm.show()

    def openApplyFlowList(self):
        self.saveFlowListForm.setApplyMode()
        self.saveFlowListForm.show()

    def applyFlowParam(self, flow_param_list):
        flow_param_list = deepcopy(flow_param_list)
        self.listWidget_flow.clearAllItem()
        for i in range(len(flow_param_list)):
            key = flow_param_list[i]["func_name"]
            del flow_param_list[i]["func_name"]
            value = flow_param_list[i]
            # print("本功能名称:", key)
            # print("本功能参数字典", value)
            self.addListWidget(key)
            self.listWidget_flow.item_widget_list[i].setFuncParam(value)
        self.addListWidget("结束")
