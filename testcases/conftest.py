import pytest
import os
import allure
from api.user_login import user
from common.YamlUtil import YamlUtil
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = YamlUtil().read_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


api_data = get_data("api_test_data.yml")


@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> *************")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@allure.step("前置步骤 ==>> 用户登录")
def step_login(username, password):
    logger.info("前置步骤 ==>> 用户 {} 登录".format(username, password))


@pytest.fixture(scope="session", autouse=True)
def login_token():
    YamlUtil().clear_yaml(BASE_PATH + '/token.yml')


def response_logger(response):
    logger.info("接口出参：" + response)
