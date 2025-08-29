import requests

from config import config


class LoginAPI:
    def __init__(self):
        self.login_url = config.BASE_URL + '/login'

    def login(self, data):
        return requests.post(self.login_url, data=data)
