import requests

from config import config


class CheckUsernameAPI:
    def __init__(self):
        self.check_username_url = config.BASE_URL + '/check-username'

    def check_username(self, headers):
        return requests.get(self.check_username_url, headers=headers)
