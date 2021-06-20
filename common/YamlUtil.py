#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 编写时间：2021/6/20 13:15
import yaml
from common.logger import logger


class YamlUtil:

    # 读取yaml文件内容
    @staticmethod
    def read_yaml(filepath):
        logger.info("加载 {} 文件......".format(filepath))
        with open(filepath, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)  # 加载yaml所有内容
        logger.info("读到数据 ==>>  {} ".format(value))
        return value

    # 写入yaml文件内容
    @staticmethod
    def write_yaml(filepath, data):
        logger.info("加载 {} 文件......".format(filepath))
        with open(filepath, mode='w', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f)
        logger.info("写入 {} 文件......".format(filepath) + '成功')

    # 清除yaml文件内容
    @staticmethod
    def clear_yaml(filepath):
        logger.info("加载 {} 文件......".format(filepath))
        with open(filepath, mode='w', encoding='utf-8') as f:
            f.truncate()
        logger.info("清除 {} 文件......".format(filepath) + '成功')

    @staticmethod
    def read_testcase_yaml(filepath, yaml_name):
        logger.info("加载 {} 文件......".format(yaml_name))
        with open(filepath, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)  # 加载yaml所有内容
        logger.info("读到{}测试数据 ==>>  {} ".format(yaml_name, value))
        return value
