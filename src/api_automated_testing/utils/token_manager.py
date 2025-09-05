from typing import Dict, Any

from src.config.logging_config import get_logger


class TokenManager:
    """
    数据库管理工具类

    提供添加和获取各个用户token的工具方法
    """
    # 初始化user_token作为存放各个账号token的字典
    user_token = {}

    # 日志器
    logger = get_logger(
        log_name="TokenManager",  # 使用类名作为日志器名称
        filename='./log/api-automated-testing.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )

    @classmethod
    def add_token_to_dict(cls, username: str, token: str) -> None:
        """
        添加token

        添加token的工具方法，往存放各个账号token的字典里添加一个元素：{ 账号，该账号的token值 }
        建议每次登录成功后都添加一个token，方便后续获取和使用

        Args:
            username: token所属的账号
            token: 该账号的token值
        """
        try:
            cls.user_token[username] = token
        except Exception as e:
            cls.logger.error(f"添加token异常: {e}")
            raise

    @classmethod
    def get_token_from_dict(cls, username: str) -> Dict[str, str]:
        """
        获取token

        获取token的工具方法，根据传入的账号username，从存放各个账号token的字典里获取此账号的token值
        在发起需要token鉴权的接口请求前，可根据该接口的业务场景，选择需要添加的账号的token作为请求头
        （比如需要管理员权限，就传入一个管理员账号，获取该账号的token。前提是该管理员账号已调用过登录接口并添加到了存放token的HashMap集合中）

        Args:
            username: token所属的账号

        Returns:
            Dict[str, str]: 存放该账号token的字典
        """
        try:
            return {"auth": cls.user_token[username]}
        except KeyError:
            cls.logger.error(f"找不到用户 '{username}' 的token")
            raise
        except Exception as e:
            cls.logger.error(f"获取token异常: {e}")
            raise