from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plurk.client import Client


class BaseApi:
    def __init__(self, client: 'Client'):
        self.client = client
