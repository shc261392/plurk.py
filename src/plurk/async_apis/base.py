from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plurk.clients import AsyncClient


class BaseApi:
    def __init__(self, client: 'AsyncClient'):
        self.client = client
