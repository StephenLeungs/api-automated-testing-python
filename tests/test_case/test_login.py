from typing import Dict

import pytest

from api_automated_testing.api.login_api import LoginAPI
from api_automated_testing.api.register_api import RegisterAPI
from api_automated_testing.utils.token_manager import TokenManager
from api_automated_testing.utils.excel_reader import ExcelReader
from src.config.logging_config import get_logger

reader = ExcelReader()
register_test_data = reader.get_sheet_data_as_dict("RegisterData")
login_test_data = reader.get_sheet_data_as_dict("LoginData")


class TestLogin:
    """
    注册登录模块测试类

    应包含所有注册登录模块的测试用例
    """
    # 日志器
    logger = get_logger(
        log_name="TestLogin",  # 使用类名作为日志器名称
        filename='./log/api-automated-testing.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )

    def setup_class(self) -> None:
        """
        setup_class特殊方法

        当前测试类执行前会执行一次，用于实例化注册和登录接口类对象
        """
        # 实例化注册和登录接口类对象
        self.register_api = RegisterAPI()
        self.login_api = LoginAPI()

    @pytest.mark.order(1)
    @pytest.mark.parametrize("register_data", register_test_data)
    def test_register(self, register_data: Dict[str, str]) -> None:
        """
        注册接口测试用例

        用于测试注册接口

        Args:
            register_data:通过@pytest.mark.parametrize装饰器参数化，读取Excel文件获得的存放注册接口测试数据的字典
        """
        try:
            # 调用注册接口类的实例方法register()发起请求，并对响应文本进行断言
            response = self.register_api.register(register_data)
            assert register_data["expectedResult"] in response.text
        except Exception as e:
            self.logger.error(f"注册测试用例异常: {e}")
            raise

    @pytest.mark.order(2)
    @pytest.mark.parametrize("login_data", login_test_data)
    def test_login(self, login_data: Dict[str, str]) -> None:
        """
        登录接口测试用例

        用于测试登录接口

        Args:
            login_data: 通过@pytest.mark.parametrize装饰器参数化，读取Excel文件获得的存放登录接口测试数据的字典
        """
        try:
            # 调用登录接口类的实例方法login()发起请求，并对响应文本进行断言
            response = self.login_api.login(login_data)
            assert login_data["expectedResult"] in response.text

            # 断言通过（登录成功）后，调用TokenManager类添加token的工具方法，把当前账号的token添加到存放各个账号token的字典里
            username = login_data["username"]
            token = response.json()["data"]
            TokenManager.add_token_to_dict(username, token)

        except Exception as e:
            self.logger.error(f"登录测试用例异常: {e}")
            raise
