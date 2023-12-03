#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Linfeng_Bingyi
# @Contact : linfengbingyi@qq.com
# @File    : CustomException.py
# @Time    : 2023/12/3 1:06
# @Dsc     : 自定义异常

from builtins import Exception


class BusinessError(Exception):
    """业务处理时抛出

    Attributes:
        error_info: str 异常信息
    """
    def __init__(self, error_info: str):
        super().__init__()
        self.error_info = error_info

    def __str__(self):
        return self.error_info
