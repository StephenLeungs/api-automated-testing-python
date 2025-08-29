import requests

from config import config


class RegisterAPI:
    def __init__(self):
        self.register_url = config.BASE_URL + '/register'

    def register(self, data):
        return requests.post(self.register_url, data=data)
