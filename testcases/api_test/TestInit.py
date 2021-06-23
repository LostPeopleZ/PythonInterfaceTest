#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 编写时间：2021/6/20 20:44
import os

import allure
from Tools.scripts.find_recursionlimit import test_init

from api.user_login import user
from common.YamlUtil import YamlUtil
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
data_file_path = os.path.join(BASE_PATH, "config", "env.yml")
api_root_url = YamlUtil().read_yaml(data_file_path).get('url')



class TestInit:
    """
    初始化接口 获取token，保存至token.yml
    """

    token_filepath = BASE_PATH + '/token.yml'

    @allure.story("story用例--初始化获取token")
    @allure.feature("feature用例--初始化获取token")
    @allure.story("story用例--初始化获取token")
    @allure.title("title用例--初始化获取token")
    @allure.description("该用例是初始化获取token的调用")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    def test_init(self):
        logger.info("*************** 初始化开始 ***************")

        yaml = YamlUtil().read_yaml(data_file_path)
        # if yaml.get("openId") is None :
        #     openId = ""
        if yaml.get("unionId") is None:
            unionId = ""
        # if yaml.get("mobileNo") is None :
        #     mobileNo = ""
        # if yaml.get("hospitalId") is None:
        #     hospitalId = ""
        json = {
            "openId": yaml.get("openId"),
            "unionId":  unionId,
            "mobileNo":  yaml.get("mobileNo"),
            "hospitalId":  yaml.get("hospitalId")
        }
        res = user.wechatAppletsLogin(json=json)
        logger.info("出参：" + res.text)
        token = res.json()['data']['token']
        if token is None:
            logger.error('===token值为NULL，请检查接口===')
            raise Exception('===token值为NULL，请检查接口===')
        if len(token) == 0:
            logger.error('===token值为空字符串，请检查接口===')
            raise Exception('===token值为空字符串，请检查接口===')
        else:
            YamlUtil().write_yaml(TestInit.token_filepath, {'token': res.json()['data']['token']})
            logger.info('===初始化获取token接口调用正常，写入token.yml文件成功===')
            logger.info("*************** 初始化结束 ***************")