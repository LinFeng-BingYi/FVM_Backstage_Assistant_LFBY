from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QListWidgetItem, QMessageBox

from src.AppImplement.FormFiles.MyMainWindow import Ui_MyMainWindow
from src.AppImplement.FormFiles.EditPlacingPlanForm import WidgetEditPlacingPlan

from src.AppImplement.FormFiles.CustomWidgets.ListWidget import SUPPORT_FUNC


class MainMyMainWindow(QMainWindow, Ui_MyMainWindow):
    def __init__(self):
        super(MainMyMainWindow, self).__init__()
        self.setupUi(self)
        # 补加控件
        self.verticalLayout_business_param_area = QVBoxLayout(self.widget_business_param_area)
        self.verticalLayout_business_param_area.setObjectName("verticalLayout_business_param_area")
        self.verticalLayout_business_param_area.setContentsMargins(5, 0, 0, 0)

        # 子页面
        self.editAccountBookForm = None
        self.visualizeAccountBookForm = None
        # 内置消息框，用于提示信息
        self.tip_message_box = QMessageBox(
            QMessageBox.Icon.NoIcon,
            "提示",
            "信息",
            QMessageBox.StandardButton.Ok)
        self.tip_message_box.button(QMessageBox.StandardButton.Ok).setText("确定")

        # listWidget中的item列表
        self.flow_list = []

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        # 初始化时，向流程列表中添加”开始“、”结束“item
        self.addListWidget("开始")
        self.addListWidget("开始")
        # self.addListWidget("开始")
        # self.addListWidget("开始")

    def bindSignal(self):
        # 菜单栏打开对应窗口
        self.action_edit_placing_plan.triggered.connect(self.displayEditPlacingPlanForm)

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
