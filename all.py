#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 编写时间：2021/6/20 14:57
import os

import pytest

from testcases.api_test.TestInit import TestInit

if __name__ == '__main__':

    TestInit().test_init()

    pytest.main()
    os.system("allure generate report --clean -o AllureReports")
