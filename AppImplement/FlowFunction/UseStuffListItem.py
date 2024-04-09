#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFileDialog, QHeaderView, QWidget, QLineEdit, QPushButton, QHBoxLayout, QComboBox, \
    QTableWidgetItem
from AppImplement.FlowFunction.BaseListItem import BaseListWidget, BaseParamWidget
from AppImplement.FormFiles.UseStuffParam import Ui_UseStuffParam

import os
from re import match

from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH
from AppImplement.Business.UseStuffBusiness import USE_STUFF_SUB_FUNCTION_DICT


class UseStuffListWidget(BaseListWidget):
    def __init__(self, func_name, parent=None):
        super().__init__(func_name, parent)

        self.func_widget = UseStuffParamWidget()

    def getFuncParam(self, get_for_json=False):
        return self.func_widget.getAllParam(get_for_json)


class UseStuffParamWidget(Ui_UseStuffParam, BaseParamWidget):
    def __init__(self):
        super(UseStuffParamWidget, self).__init__()
        self.setupUi(self)
        self.tableWidget_stuff_list.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

        self.initWidget()
        self.bindSignal()

    def initWidget(self):
        pass

    def bindSignal(self):
        self.pushButton_insert_row.clicked.connect(self.insertTableRow)
        self.pushButton_delete_row.clicked.connect(self.deleteTableRow)

    def insertTableRow(self):
        def responsePanelComboBox(comboBox_opt):
            comboBox_opt.clear()
            comboBox_opt.addItems(list(USE_STUFF_SUB_FUNCTION_DICT[comboBox_panel.currentText()]))
        tableWidget = self.tableWidget_stuff_list
        cur_row = tableWidget.currentRow()
        if cur_row == -1:
            new_row = tableWidget.rowCount()
        else:
            new_row = cur_row + 1
        tableWidget.insertRow(new_row)

        # 定制每列单元格控件
        # “图片路径”列
        tableWidget.setCellWidget(new_row, 0, self.lineEditForChooseFile())
        # “交互界面”列
        comboBox_panel = QComboBox()
        comboBox_panel.addItems(list(USE_STUFF_SUB_FUNCTION_DICT))
        tableWidget.setCellWidget(new_row, 1, comboBox_panel)
        # “执行操作”列
        comboBox_operation = QComboBox()
        comboBox_operation.addItems(list(USE_STUFF_SUB_FUNCTION_DICT[comboBox_panel.currentText()]))
        tableWidget.setCellWidget(new_row, 2, comboBox_operation)
        # “执行次数”列
        tableWidget.setItem(new_row, 3, QTableWidgetItem(""))

        comboBox_panel.currentIndexChanged.connect(lambda: responsePanelComboBox(comboBox_operation))

    def lineEditForChooseFile(self):
        widget = QWidget()
        lineEdit = QLineEdit(widget)
        lineEdit.setMinimumHeight(30)
        # 放大按钮
        file_btn = QPushButton('浏览')
        file_btn.setFixedSize(30, 30)
        file_btn.clicked.connect(lambda: self.chooseFile(lineEdit))

        hLayout = QHBoxLayout(widget)
        hLayout.addWidget(lineEdit)
        hLayout.addWidget(file_btn)
        hLayout.setContentsMargins(0, 0, 0, 0)
        hLayout.setSpacing(2)
        return widget

    def deleteTableRow(self):
        cur_row = self.tableWidget_stuff_list.currentRow()
        if cur_row == -1:
            return
        self.tableWidget_stuff_list.removeRow(cur_row)

    def setTableRow(self, row_no, stuff_info):
        tableWidget = self.tableWidget_stuff_list

        tableWidget.cellWidget(row_no, 0).findChild(QLineEdit).setText(stuff_info["pic_path"])
        tableWidget.cellWidget(row_no, 1).setCurrentText(stuff_info["panel"])
        tableWidget.cellWidget(row_no, 2).setCurrentText(stuff_info["operation"])
        tableWidget.item(row_no, 3).setText(str(stuff_info["opt_times"]))

    def chooseFile(self, lineedit):
        chosen_file, file_type = QFileDialog.getOpenFileName(
            self, "选择文件",
            ROOT_PATH + "\\userdata\\用户图片\\交互物品截图\\",
            "All Files(*);;BMP Files(*.bmp)")
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.':
            print("未选择正确的文件！！")
            return
        lineedit.setText(norm_file_path)

    def getAllParam(self, get_for_json=False):
        stuff_list = []
        tableWidget = self.tableWidget_stuff_list
        for row in range(tableWidget.rowCount()):
            stuff_list.append({
                "pic_path": tableWidget.cellWidget(row, 0).findChild(QLineEdit).text(),
                "panel": tableWidget.cellWidget(row, 1).currentText(),
                "operation": tableWidget.cellWidget(row, 2).currentText(),
                "opt_times": int(tableWidget.item(row, 3).text())
            })
        return {
            "player": self.comboBox_select_player.currentIndex(),
            "count_chest_stuff": self.checkBox_count_chest_stuff.isChecked(),
            "stuff_list": stuff_list
        }

    def setAllParam(self, param_dict):
        flag_set_success = True
        error_msg_list = []
        self.comboBox_select_player.setCurrentIndex(param_dict["player"])
        if "count_chest_stuff" in param_dict:
            self.checkBox_count_chest_stuff.setChecked(param_dict["count_chest_stuff"])
        row_no = 0
        for stuff_info in param_dict["stuff_list"]:
            self.insertTableRow()
            self.setTableRow(row_no, stuff_info)
            if not os.path.exists(stuff_info["pic_path"]):
                flag_set_success = False
                error_msg_list.append(f"未找到第{row_no + 1}行物品截图或文件夹！")
            row_no += 1
        if not flag_set_success:
            return False, "\n".join(error_msg_list)
        return True

    def checkInputValidity(self):
        tableWidget = self.tableWidget_stuff_list
        for row in range(tableWidget.rowCount()):
            if not os.path.exists(tableWidget.cellWidget(row, 0).findChild(QLineEdit).text()):
                return False, f"未找到第{row + 1}行物品截图或文件夹！"
            if not match("-?[0-9]+", tableWidget.item(row, 3).text()):
                return False, f"第{row + 1}行物品执行次数必须为整数！(-1代表一直执行直到消耗完)"
        return True
