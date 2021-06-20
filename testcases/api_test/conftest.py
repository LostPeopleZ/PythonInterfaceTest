import pytest
import os

from common.YamlUtil import YamlUtil
from testcases.conftest import api_data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture(scope="session", autouse=True)
def login_token():
    YamlUtil().clear_yaml(os.getcwd() + '/token.yml')

@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return api_data.get(testcase_name)