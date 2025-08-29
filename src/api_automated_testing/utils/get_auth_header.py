from api_automated_testing.api.login_api import LoginAPI
from api_automated_testing.utils.excel_reader import ExcelReader
from src.config.logging_config import get_logger

reader = ExcelReader()
login_test_data = reader.get_sheet_data_as_dict("LoginData")

# 日志器
logger = get_logger(
    log_name="GetAuthHeader",  # 使用函数名作为日志器名称
    filename='./log/api-automated-testing.log',  # 所有类使用相同的日志文件
    level="INFO"  # 设置适当的日志级别
)

def get_auth_header():
    try:
        login_api = LoginAPI()
        response = login_api.login(login_test_data[0])
        token = response.json()["data"]
        return {"auth": token}
    except Exception as e:
        logger.error(f"获取token异常: {e}")
        raise