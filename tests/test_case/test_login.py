import pytest

from api_automated_testing.api.login_api import LoginAPI
from api_automated_testing.api.register_api import RegisterAPI
from api_automated_testing.utils.excel_reader import ExcelReader
from src.config.logging_config import get_logger

reader = ExcelReader()
register_test_data = reader.get_sheet_data_as_dict("RegisterData")
login_test_data = reader.get_sheet_data_as_dict("LoginData")

class TestLogin:
    # 日志器
    logger = get_logger(
        log_name="TestLogin",  # 使用类名作为日志器名称
        filename='./log/api-automated-testing.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )


    def setup_class(self):
        self.register_api = RegisterAPI()
        self.login_api = LoginAPI()


    @pytest.mark.order(1)
    @pytest.mark.parametrize("register_data", register_test_data)
    def test_register(self, register_data):
        try:
            assert register_data["expectedResult"] in self.register_api.register(register_data).text

        except Exception as e:
            self.logger.error(f"注册测试用例异常: {e}")
            raise

    @pytest.mark.order(2)
    @pytest.mark.parametrize("login_data", login_test_data)
    def test_login(self, login_data):
        try:
            assert login_data["expectedResult"] in self.login_api.login(login_data).text

        except Exception as e:
            self.logger.error(f"登录测试用例异常: {e}")
            raise
