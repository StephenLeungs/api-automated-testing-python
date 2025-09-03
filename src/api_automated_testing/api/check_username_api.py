from typing import Dict

import requests
from requests import Response

from config import config


class CheckUsernameAPI:
    """
    查询当前账号接口类

    封装查询当前账号接口
    """

    def __init__(self):
        """
        构造函数

        实例化时自动完成读取config配置文件里的基准路径并拼接查询当前账号接口url的操作
        """
        self.check_username_url = config.BASE_URL + '/check-username'

    def check_username(self, headers: Dict[str, str]) -> Response:
        """
        查询当前账号接口请求

        封装requests库get()方法，构造查询当前账号接口的请求

        Args:
            headers: 要查询的账号的token

        Returns:
            Response: 查询当前账号接口的响应
        """
        return requests.get(self.check_username_url, headers=headers)
