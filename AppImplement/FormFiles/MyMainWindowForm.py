from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QMessageBox
from PySide6.QtGui import QTextCursor

from AppImplement.FormFiles.MyMainWindow import Ui_MyMainWindow
from AppImplement.FormFiles.EditPlacingPlanForm import WidgetEditPlacingPlan
from AppImplement.FormFiles.CustomWidgets.ListWidget import SUPPORT_FUNC
from AppImplement.FormFiles.CustomWidgets.Dialog import AddFuncFlowDialog

from AppImplement.Business.BaseBusiness import BusinessBus


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
        self.editAccountBookForm = None
        self.visualizeAccountBookForm = None
        self.add_func_flow_dialog = AddFuncFlowDialog()     # 添加功能到流程列表的内置对话框
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

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        # 初始化时，向流程列表中添加”开始“、”结束“item
        self.addListWidget("开始")
        self.addListWidget("结束")

    def bindSignal(self):
        # 菜单栏打开对应窗口
        self.action_edit_placing_plan.triggered.connect(self.displayEditPlacingPlanForm)
        # 功能流程列表添加功能
        self.pushButton_add_flow.clicked.connect(self.showAddFuncFlowDialog)
        # 启动/结束流程
        self.pushButton_start_flow.clicked.connect(self.startBusinessBus)
        self.pushButton_end_flow.clicked.connect(self.stopBusinessBus)
        # 双击流程显示”功能参数“tab页
        self.listWidget_flow.signal_show_func_param_tab.connect(
            lambda: self.tabWidget_config_business.setCurrentIndex(1))
        # 线程业务消息打印在日志中
        self.thread_business_bus.signal_send_business_message.connect(self.printLog)
        # 线程更新流程中功能的状态
        self.thread_business_bus.signal_send_func_status.connect(self.signal_update_flow_func_status)
        self.signal_update_flow_func_status.connect(self.listWidget_flow.updateFlowFuncStatus)
        # 清除日志
        self.pushButton_clear_log.clicked.connect(self.plainTextEdit_log.clear)

    def displayEditPlacingPlanForm(self):
        """响应菜单，打开'编辑放卡方案'窗口
        """
        self.editAccountBookForm = WidgetEditPlacingPlan()
        self.editAccountBookForm.show()

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
