import pytest

from api_automated_testing.api.check_username_api import CheckUsernameAPI
from api_automated_testing.utils.excel_reader import ExcelReader
from api_automated_testing.utils.get_auth_header import get_auth_header
from src.config.logging_config import get_logger


class TestUser:
    # 日志器
    logger = get_logger(
        log_name="TestUser",  # 使用类名作为日志器名称
        filename='./log/api-automated-testing.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )

    reader = ExcelReader()
    check_username_test_data = reader.get_sheet_data_as_dict("CheckUsernameData")

    def setup_class(self):
        self.check_username_api = CheckUsernameAPI()


    @pytest.mark.order(3)

    @pytest.mark.parametrize("check_username_data", check_username_test_data)
    def test_check_username(self, check_username_data):
        try:
            headers = get_auth_header()
            assert check_username_data["expectedResult"] in self.check_username_api.check_username(headers=headers).text

        except Exception as e:
            self.logger.error(f"查询账号测试用例异常: {e}")
            raise



