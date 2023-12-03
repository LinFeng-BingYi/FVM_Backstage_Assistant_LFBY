from PySide6.QtWidgets import QMainWindow

from src.AppImplement.FormFiles.MyMainWindow import Ui_MyMainWindow
from src.AppImplement.FormFiles.EditPlacingPlanForm import WidgetEditPlacingPlan


class MainMyMainWindow(QMainWindow, Ui_MyMainWindow):
    def __init__(self):
        super(MainMyMainWindow, self).__init__()
        self.setupUi(self)

        self.editAccountBookForm = None
        self.visualizeAccountBookForm = None

        self.bindSignal()

    def bindSignal(self):
        self.action_edit_placing_plan.triggered.connect(self.displayEditAccountBookForm)

    def displayEditAccountBookForm(self):
        self.editAccountBookForm = WidgetEditPlacingPlan()
        self.editAccountBookForm.show()
