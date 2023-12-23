#!/usr/bin/env python3

import os
from json import *


class JSONProcessor:
    """处理json文件的类

        Attributes:
            file_path: str 文件路径
            encoding: str 文件编码. 默认为 'utf-8'

        Exception:
            FileExistsError: 传入的json文件不存在
            UnicodeDecodeError: 传入的json文件不是utf-8格式
            MissingSectionHeaderError: 传入json文件中，注释没有使用英文分号开头
        """

    def __jsont__(self, file_path, encoding='utf-8'):
        if not os.path.exists(file_path):
            raise FileExistsError("传入的json文件不存在")
        self.file_path = file_path
        self.encoding = encoding

