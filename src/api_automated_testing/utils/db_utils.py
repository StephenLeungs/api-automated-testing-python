import pymysql

from config import config
from src.config.logging_config import get_logger


class DBUtils:
    # 日志器
    logger = get_logger(
        log_name="DBUtils",  # 使用类名作为日志器名称
        filename='./log/api-automated-testing.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )

    # 建立连接
    @classmethod
    def get_connect(cls):
        try:
            return pymysql.connect(user=config.DB_USER,
                                password=config.DB_PASSWORD,
                                host=config.DB_HOST,
                                database=config.DB_NAME,
                                port=config.DB_PORT,
                                charset=config.DB_CHARSET)
        except Exception as e:
            cls.logger.error(f"获取数据库连接异常: {e}")
            raise


    # 获取游标
    @classmethod
    def get_cursor(cls, connect):
        try:
            return connect.cursor()
        except Exception as e:
            cls.logger.error(f"获取数据库游标异常: {e}")
            raise

    # 关闭资源
    @classmethod
    def close_resource(cls, cursor, connect):
        try:
            if cursor:
                cursor.close()
            if connect:
                connect.close()
        except Exception as e:
            cls.logger.error(f"数据库资源关闭异常: {e}")
            raise