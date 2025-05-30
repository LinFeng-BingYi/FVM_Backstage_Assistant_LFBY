#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : SaveFlowListForm.py
# @Time    : 2023/12/24 22:19
# @Dsc     : 保存功能流程列表的参数
from collections import OrderedDict

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt, Signal

import os
import json

from AppImplement.FormFiles.CustomWidgets.MessageBox import TipMessageBox
from AppImplement.FormFiles.SaveFlowList import Ui_SaveFlowList
from AppImplement.GlobalValue.ConfigFilePath import ROOT_PATH


class WidgetSaveFlowList(QWidget, Ui_SaveFlowList):
    signal_apply_flow_param = Signal(list)

    def __init__(self):
        super(WidgetSaveFlowList, self).__init__()
        self.setupUi(self)

        self.flag_save_mode = False
        self.flow_param_list = list()
        self.json_file_dict = dict()
        self.cwd = ROOT_PATH + r"\userdata\功能流程列表参数"     # 程序当前工作目录
        self.tip_dialog = None

        self.bindSignal()

        self.setWindowModality(Qt.WindowModality.WindowModal)

    def bindSignal(self):
        self.pushButton_flow_file.clicked.connect(self.chooseJsonFile)
        self.pushButton_save.clicked.connect(self.writeFlowListParam)
        self.pushButton_apply.clicked.connect(self.applyJsonFile)

    def chooseJsonFile(self):
        if not self.flag_save_mode:
            chosen_file, file_type = QFileDialog.getOpenFileName(self, "选择文件",
                                                                 self.cwd,
                                                                 "All Files(*);;JSON Files(*.json)")
        else:
            chosen_file, _ = QFileDialog.getSaveFileName(
                self, "保存文件",
                self.cwd,
                "All Files(*);;JSON Files(*.json)"
            )
        norm_file_path = os.path.normpath(chosen_file)
        if norm_file_path == '.' or norm_file_path[-4:] != "json":
            print("未选择正确的文件！！")
            return
        self.lineEdit_flow_file.setText(norm_file_path)
        # 若当前是保存模式，则在”浏览“文件后不要更新窗口存储的流程参数list self.flow_param_list
        # 因为在”保存“模式下，该参数list是主窗口送过来的，若在点击”浏览“按钮后再点击”更新“，则会将内容保存为”浏览“所选择的文件内容
        if not self.flag_save_mode:
            self.readFlowListParam()

    def setFlowParamList(self, flow_param_list):
        self.flow_param_list = flow_param_list

    def setApplyMode(self):
        self.flag_save_mode = False
        self.pushButton_apply.setEnabled(True)
        self.pushButton_save.setEnabled(False)

    def setSaveMode(self):
        self.flag_save_mode = True
        self.pushButton_save.setEnabled(True)
        self.pushButton_apply.setEnabled(False)
        # self.lineEdit_flow_file.setText(self.cwd)

    def setJsonToLineedit(self, json_file_path):
        """给主界面初始化时自动加载指定的json调用
        """
        if os.path.exists(json_file_path):
            self.lineEdit_flow_file.setText(json_file_path)
            return True
        else:
            return False

    def readFlowListParam(self):
        flow_file_path = self.lineEdit_flow_file.text()
        # print(flow_file_path)
        if flow_file_path[-4:] != "json":
            self.tip_dialog = TipMessageBox("错误", "未选择正确的文件！！")
            self.tip_dialog.show()
            return
        json_file = open(flow_file_path, 'r', encoding='utf-8')
        json_file_dict = json.load(json_file, object_pairs_hook=OrderedDict)
        try:
            flow_dsc = json_file_dict["流程描述"]
            self.flow_param_list = json_file_dict["流程参数"]
            self.plainTextEdit.setPlainText(flow_dsc)
            # print(self.flow_param_list[0]["2p_name_pic_path"])
        except KeyError as keyError:
            self.tip_dialog = TipMessageBox(
                "错误",
                f"该json文件格式不正确！\n{keyError.args}")
            self.tip_dialog.show()
        finally:
            json_file.close()

    def writeFlowListParam(self):
        flow_file_path = self.lineEdit_flow_file.text()
        if flow_file_path[-4:] != "json":
            self.tip_dialog = TipMessageBox("错误", f"请选择正确的json文件名称\n\n文件不存在时将自动新建，否则会覆盖原文件")
            self.tip_dialog.show()
            return
        self.json_file_dict["流程描述"] = self.plainTextEdit.toPlainText()
        self.json_file_dict["流程参数"] = self.flow_param_list
        json_file = open(flow_file_path, 'w', encoding='utf-8')
        json.dump(self.json_file_dict, json_file, indent=4, ensure_ascii=False)
        json_file.close()
        self.tip_dialog = TipMessageBox("提示", "文件保存成功！！")
        self.tip_dialog.show()

    def applyJsonFile(self):
        # print("应用的流程参数：\n", self.flow_param_list)
        if len(self.flow_param_list) == 0:
            self.tip_dialog = TipMessageBox(
                "错误",
                f"还未解析json文件！或该文件的流程中没有任何功能！")
            self.tip_dialog.show()
            return
        self.signal_apply_flow_param.emit(self.flow_param_list)
