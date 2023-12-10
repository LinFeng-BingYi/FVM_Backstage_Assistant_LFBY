#!/usr/bin/env python3

import os
from configparser import ConfigParser, RawConfigParser, NoOptionError, NoSectionError


class INIProcessor:
    """处理ini文件的类

    Attributes:
        file_path: str 文件路径
        encoding: str 文件编码. 默认为 'utf-8'

    Exception:
        FileExistsError: 传入的ini文件不存在
        UnicodeDecodeError: 传入的ini文件不是utf-8格式
        MissingSectionHeaderError: 传入ini文件中，注释没有使用英文分号开头
    """
    def __init__(self, file_path, encoding='utf-8'):
        if not os.path.exists(file_path):
            raise FileExistsError("传入的ini文件不存在")
        self.file_path = file_path
        self.encoding = encoding

        self.config_p = RawConfigParser()
        # 设置ConfigParse处理键时，保持原大小写状态
        self.config_p.optionxform = lambda option: option
        self.config_p.read(file_path, encoding=encoding)

    def getAllSection(self):
        """获取ini文件所有section，以list形式返回

        Returns: list[str]
            list形式的所有section名称
        """
        return self.config_p.sections()

    def getAllKey(self, section):
        """获取ini文件所有section，以list形式返回

        Returns: list[str]
            list形式的所有key名称
        """
        return self.config_p.options(section)

    def getSpecificValue(self, section, key):
        """获取section下key对应的值

        Args:
            section: str
                指定的section名称
            key: str
                指定的key名称

        Returns: str | tuple[None, str['section' | 'key']]
            对应的值value。传入的section或key不存在时，返回一个两个元素的元组tuple[None, str['section' | 'key']]
            example:
            ...
        """
        try:
            value = self.config_p.get(section, key)
        except NoOptionError:
            value = None, "section"
        except NoSectionError:
            value = None, "key"
        return value

    def setSpecificValue(self, section, key, value):
        """在指定section中创建键值对 key=value。若section不存在，则先自动创建section

        Args:
            section: str
                指定的section名称
            key: str
                指定的key名称
            value: Any
                指定的值value
        """
        if not self.hasSection(section):
            self.config_p.add_section(section)
        self.config_p.set(section, key, value)
        print("写入：", key, value)
        self.saveIni()

    def setBatchValue(self, section, key_value_dict: dict):
        """在指定section中创建键值对 key=value。若section不存在，则先自动创建section

        Args:
            section: str
                指定的section名称
            key_value_dict: dict
                待创建的键值对
        """
        if not self.hasSection(section):
            self.config_p.add_section(section)
        for key, value in key_value_dict.items():
            self.config_p.set(section, key, value)
        self.saveIni()

    def deleteSectionOrValue(self, section, key=None):
        """删除section，或其下key对应的值。不存在section或key则没有动作

        Args:
            section: str
                指定的section名称
            key: str
                指定的key名称。不传值则删除整个section
        """
        if not self.hasSection(section):
            return
        if (key is None) or key == '':
            self.config_p.remove_section(section)
        else:
            self.config_p.remove_option(section, key)
        self.saveIni()

    def deleteBatchValue(self, section, key_list: list):
        """批量删除section，或其下key对应的值。不存在section或key则没有动作

        Args:
            section: str
                指定的section名称
            key_list: list[str]
                待删除的key名称列表
        """
        if not self.hasSection(section):
            return
        else:
            for key in key_list:
                self.config_p.remove_option(section, key)
        self.saveIni()

    def hasSection(self, section):
        return self.config_p.has_section(section)

    def hasKey(self, section, key):
        return self.config_p.has_option(section, key)

    def saveIni(self, file_path=None):
        if file_path is None:
            file_path = self.file_path

        fp = open(file_path, 'w', encoding=self.encoding)
        self.config_p.write(fp)
        fp.close()


if __name__ == '__main__':
    file_name = r"D:\Softwares\按键精灵\美食组队脚本\TeamConfig-V6.04-utf8.ini"
    ini_processor = INIProcessor(file_name)
    result = ini_processor.getSpecificValue("神殿1", "1P")
    print(result)
    ini_processor.setBatchValue("神殿1", {"1P卡1": "1", "hh": "海星"})
    ini_processor.deleteSectionOrValue("神殿1", "2")
    ini_processor.deleteBatchValue("神殿1", ["1P卡1", "hh"])
    ini_processor.deleteSectionOrValue("神殿1")
