import pymysql
from pymysql import Connection
from pymysql.cursors import Cursor

from config import config
from src.config.logging_config import get_logger


class DBUtils:
    """
    数据库管理工具类

    提供获取数据库连接等数据库管理相关的工具方法
    """

    # 日志器
    logger = get_logger(
        log_name="DBUtils",  # 使用类名作为日志器名称
        filename='./log/api-automated-testing.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )

    @classmethod
    def get_connect(cls) -> Connection[Cursor]:
        """
        获取数据库连接

        读取.env配置文件中的数据库账号密码等数据库连接信息，获取数据库连接

        Returns:
            Connection[Cursor]: 数据库连接实例
        """
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

    @classmethod
    def get_cursor(cls, connect: Connection[Cursor]) -> Cursor:
        """
        获取游标

        传入数据库连接实例，获取游标

        Args:
            connect: 数据库连接实例

        Returns:
            Cursor: 数据库游标实例
        """
        try:
            return connect.cursor()
        except Exception as e:
            cls.logger.error(f"获取数据库游标异常: {e}")
            raise

    @classmethod
    def close_resource(cls, cursor: Cursor, connect: Connection[Cursor]) -> None:
        """
        关闭资源

        关闭数据库游标和数据库连接

        Args:
            cursor: 数据库游标实例
            connect: 数据库连接实例
        """
        try:
            if cursor:
                cursor.close()
            if connect:
                connect.close()
        except Exception as e:
            cls.logger.error(f"数据库资源关闭异常: {e}")
            raise
