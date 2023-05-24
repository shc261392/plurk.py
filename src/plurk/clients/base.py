from abc import abstractmethod


class BaseClient():
    """Base class for clients
    """
    @property
    @abstractmethod
    def http_client_class(self):
        pass

    def __init__(self, app_key: str, app_secret: str, base_url='https://www.plurk.com'):
        self.http_client = None
        self.app_key = app_key
        self.app_secret = app_secret
        self.base_url = base_url
        self.token = None
        self.token_secret = None
