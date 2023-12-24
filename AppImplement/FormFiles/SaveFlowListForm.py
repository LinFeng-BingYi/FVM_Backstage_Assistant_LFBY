#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : SaveFlowListForm.py
# @Time    : 2023/12/24 22:19
# @Dsc     : 保存功能流程列表的参数

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt, Signal

import os
import json

from AppImplement.FormFiles.CustomWidgets.MessageBox import TipMessageBox
from AppImplement.FormFiles.SaveFlowList import Ui_SaveFlowList
from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH


class WidgetSaveFlowList(QWidget, Ui_SaveFlowList):
    signal_apply_flow_param = Signal(dict)

    def __init__(self):
        super(WidgetSaveFlowList, self).__init__()
        self.setupUi(self)

        self.file_processor = None    # json文件读写器
        self.flow_param_dict = dict()
        self.json_file_dict = dict()
        self.cwd = ROOT_PATH + r"\config\功能流程列表参数"     # 程序当前工作目录
        self.tip_dialog = None

        self.bindSignal()

        self.setWindowModality(Qt.WindowModality.WindowModal)

    def bindSignal(self):
        self.pushButton_flow_file.clicked.connect(self.chooseJsonFile)
        self.pushButton_save.clicked.connect(self.writeFlowListParam)
        self.pushButton_apply.clicked.connect(self.applyJsonFile)

    def chooseJsonFile(self):
        chosen_file, file_type = QFileDialog.getOpenFileName(self, "选择文件",
                                                             self.cwd,
                                                             "All Files(*);;JSON Files(*.ini)")
        # chosen_file = QFileDialog.getExistingDirectory(self, "选择文件夹", self.cwd)
        norm_file_path = os.path.normpath(chosen_file)
        # if norm_file_path == '.' or norm_file_path[-4:] != "json":
        #     print("未选择正确的文件！！")
        #     return
        self.lineEdit_flow_file.setText(norm_file_path)
        self.readFlowListParam()

    def setFlowParamDict(self, flow_param_dict):
        self.flow_param_dict = flow_param_dict

    def setApplyMode(self):
        self.pushButton_apply.setEnabled(True)
        self.pushButton_save.setEnabled(False)

    def setSaveMode(self):
        self.pushButton_save.setEnabled(True)
        self.pushButton_apply.setEnabled(False)
        self.lineEdit_flow_file.setText(self.cwd)

    def readFlowListParam(self):
        flow_file_path = self.lineEdit_flow_file.text()
        if flow_file_path[-4:] != "json":
            self.tip_dialog = TipMessageBox("错误", "未选择正确的文件！！")
            self.tip_dialog.show()
            return
        json_file = open(flow_file_path, 'r', encoding='utf-8')
        json_file_dict = json.load(json_file)
        try:
            flow_dsc = json_file_dict["流程描述"]
            self.flow_param_dict = json_file_dict["流程参数"]
            self.plainTextEdit.setPlainText(flow_dsc)
            # print(self.flow_param_dict["开始"]["2p_name_pic_path"])
        except KeyError as keyError:
            self.tip_dialog = TipMessageBox(
                "错误",
                f"该json文件格式不正确！")
            self.tip_dialog.show()
        finally:
            json_file.close()

    def writeFlowListParam(self):
        self.json_file_dict["流程描述"] = self.plainTextEdit.toPlainText()
        self.json_file_dict["流程参数"] = self.flow_param_dict
        flow_file_path = self.lineEdit_flow_file.text()
        if flow_file_path[-4:] != "json":
            self.tip_dialog = TipMessageBox("错误", f"请先在”文件路径“输入框中填写正确的json文件名称\n\n文件不存在时将自动新建，否则会覆盖原文件")
            self.tip_dialog.show()
            return
        # if not os.path.exists(flow_file_path):
        #     os.mknod(flow_file_path)
        json_file = open(flow_file_path, 'w', encoding='utf-8')
        json.dump(self.json_file_dict, json_file, indent=4, ensure_ascii=False)
        json_file.close()
        self.tip_dialog = TipMessageBox("提示", "文件保存成功！！")
        self.tip_dialog.show()

    def applyJsonFile(self):
        print(self.flow_param_dict)
        if self.flow_param_dict is None or len(self.flow_param_dict) == 0:
            self.tip_dialog = TipMessageBox(
                "错误",
                f"还未解析json文件！")
            self.tip_dialog.show()
            return
        self.signal_apply_flow_param.emit(self.flow_param_dict)
