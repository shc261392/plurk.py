from plurk.async_apis.base import BaseApi
from plurk.exceptions import validate_resp
from plurk.models import ActionResp, GetBlocksResp
from plurk.utils import build_params


class Blocks(BaseApi):
    async def get(self):
        r"""Get users that are blocked by the current user.
        """
        endpoint = f'{self.client.base_url}/APP/Blocks/get'
        resp = await self.client.http_client.get(endpoint)
        validate_resp(resp)
        return GetBlocksResp(**resp.json())

    async def block(self, user_id: int):
        r"""Block a user.
        """
        endpoint = f'{self.client.base_url}/APP/Blocks/block'
        payload = build_params(user_id=user_id)
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    async def unblock(self, user_id: int):
        r"""Unblock a user.
        """
        endpoint = f'{self.client.base_url}/APP/Blocks/unblock'
        payload = build_params(user_id=user_id)
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())
