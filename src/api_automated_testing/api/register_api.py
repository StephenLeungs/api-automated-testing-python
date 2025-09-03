from typing import Dict

import requests
from requests import Response

from config import config


class RegisterAPI:
    """
    注册接口类
    
    封装注册接口
    """

    def __init__(self):
        """
        构造函数
        
        实例化时自动完成读取config配置文件里的基准路径并拼接注册接口url的操作
        """
        self.register_url = config.BASE_URL + '/register'

    def register(self, data: Dict[str, str]) -> Response:
        """
        注册接口请求

        封装requests库post()方法，构造注册接口的请求

        Args:
            data: 存放注册接口测试数据的字典

        Returns:
            Response: 注册接口返回的响应
        """
        return requests.post(self.register_url, data=data)
