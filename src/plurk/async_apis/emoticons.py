from typing import Dict

from plurk.async_apis.base import BaseApi
from plurk.exceptions import validate_resp


class Emoticons(BaseApi):
    async def get(self) -> Dict[str, Dict]:
        r"""Emoticons are a big part of Plurk since they make it easy to express feelings.

        This call returns a JSON object that looks like:
        ```
        {"karma": {"0": [[":-))", "https:\/\/s.plurk.com\/xxxxx.gif"], ...], ...},
        "recruited": {"10": [["(bigeyes)", "https:\/\/s.plurk.com\/xxxxx.gif"], ...], ...} }
        ```
        """
        endpoint = f'{self.client.base_url}/APP/Emoticons/get'
        resp = await self.client.http_client.get(endpoint)
        validate_resp(resp)
        return resp.json()
