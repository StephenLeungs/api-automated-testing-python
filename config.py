import os
from dotenv import load_dotenv

# 加载 .env 文件中的变量到环境变量
load_dotenv()

class Config:
    """从环境变量中读取配置"""
    BASE_URL = os.getenv("BASE_URL") # 基准路径
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 3306)) # 端口号，注意类型转换
    DB_NAME = os.getenv("DB_NAME")  # 数据库名称
    DB_USER = os.getenv("DB_USER")  # 数据库账号
    DB_PASSWORD = os.getenv("DB_PASSWORD")  # 数据库密码
    DB_CHARSET = os.getenv("DB_CHARSET")    # 数据库字符集

# 创建一个配置实例供其他地方导入
config = Config()