#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 编写时间：2021/6/20 13:06
import os

import allure
import pytest
import requests

from api.user import user
from common.YamlUtil import YamlUtil
from common.logger import logger
from core.rest_client import RestClient
from testcases.conftest import api_data, step_first, step_login, response_logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
data_file_path = os.path.join(BASE_PATH, "config", "env.yml")
api_root_url = YamlUtil().read_yaml(data_file_path).get('url')


class TestAuthorize:
    '''授权登录、个人中心模块'''

    token_filepath = BASE_PATH + '/token.yml'
    token = YamlUtil().read_yaml(token_filepath).get('token')

    # @allure.story("story用例--授权登录")
    # @allure.feature("feature用例--授权登录")
    # @allure.story("story用例--授权登录")
    # @allure.title("title用例--授权登录")
    # @allure.description("该用例是针对获取授权的测试")
    # @allure.issue("https://www.baidu.com", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.baidu.com", name="点击，跳转到对应用例的链接地址")
    # @pytest.mark.parametrize("openId, unionId, mobileNo, hospitalId",
    #                          api_data['test_get_token'])
    # def test_get_token(self, openId, unionId, mobileNo, hospitalId):
    #     logger.info("*************** 开始执行用例 ***************")
    #     #
    #     json = {
    #         "openId": openId,
    #         "unionId": unionId,
    #         "mobileNo": mobileNo,
    #         "hospitalId": hospitalId
    #     }
    #     res = user_login.wechatAppletsLogin(json=json)
    #     logger.info("出参：" + res.text)
    #     YamlUtil().write_yaml(TestAuthorize.token_filepath, {'token': res.json()['data']['token']})
    #     assert res.json()['code'] == 0
    #     logger.info("*************** 结束执行用例 ***************")

    @allure.story("story用例--就诊人列表")
    @allure.feature("feature用例--就诊人列表")
    @allure.story("story用例--就诊人列表")
    @allure.title("title用例--就诊人列表")
    @allure.description("该用例是获取就诊人列表数据的测试")
    @allure.issue("https://www.baidu.com", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.baidu.com", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.parametrize("accountId, withCard, hospitalId, status",
                             api_data['test_getVisitList'])
    def test_getVisitList(self, accountId, withCard, hospitalId, status):

        json ={
                "accountId": accountId,
                "withCard": withCard,
                # "isShowBlank": isShowBlank,
                "hospitalId": hospitalId
            }
        headers = {"token": TestAuthorize.token,
                   "hospitalId": "10010"
                   }
        res = user.PatientList(json=json,headers=headers)
        response_logger(res.text)
        assert res.json()['code'] == status

        logger.info("*************** 结束执行用例 ***************")
    #
    # def test_getGuahaoList(self):
    #     url = 'http://feetest.zhicall.cn/pay-web/mobile/guahao/app/list'


if __name__ == '__main__':
    # pytest.main(['-vs'])
    pytest.main()
    # print(api_root_url)
