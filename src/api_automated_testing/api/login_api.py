from typing import Dict

import requests
from requests import Response

from config import config


class LoginAPI:
    """
    登录接口类

    封装登录接口
    """
    def __init__(self):
        """
        构造函数

        实例化时自动完成读取config配置文件里的基准路径并拼接登录接口url的操作
        """
        self.login_url = config.BASE_URL + '/login'

    def login(self, data: Dict[str, str]) -> Response:
        """
        登录接口请求

        封装requests库post()方法，构造登录接口的请求

        Args:
            data: 存放登录接口测试数据的字典

        Returns:
            Response: 登录接口返回的响应
        """
        return requests.post(self.login_url, data=data)
