from typing import Dict

import pytest

from api_automated_testing.api.check_username_api import CheckUsernameAPI
from api_automated_testing.utils.token_manager import TokenManager
from api_automated_testing.utils.excel_reader import ExcelReader
from src.config.logging_config import get_logger


class TestUser:
    """
    用户模块测试类

    应包含所有用户模块的测试用例
    """
    # 日志器
    logger = get_logger(
        log_name="TestUser",  # 使用类名作为日志器名称
        filename='./log/api-automated-testing.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )

    reader = ExcelReader()
    check_username_test_data = reader.get_sheet_data_as_dict("CheckUsernameData")

    def setup_class(self) -> None:
        """
        setup_class特殊方法

        当前测试类执行前会执行一次，用于实例化查询当前账号接口类对象
        """
        self.check_username_api = CheckUsernameAPI()


    @pytest.mark.order(3)
    @pytest.mark.parametrize("check_username_data", check_username_test_data)
    def test_check_username(self, check_username_data: Dict[str, str]) -> None:
        """
        查询当前账号接口测试用例

        用于测试查询当前账号接口

        Args:
            check_username_data: 通过@pytest.mark.parametrize装饰器参数化，读取Excel文件获得的存放查询当前账号接口测试数据的字典
        """
        try:
            username = check_username_data["username"]
            headers = TokenManager.get_token_from_dict(username)
            assert check_username_data["expectedResult"] in self.check_username_api.check_username(headers=headers).text

        except Exception as e:
            self.logger.error(f"查询账号测试用例异常: {e}")
            raise



