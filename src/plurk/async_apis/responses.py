from typing import Optional, Coroutine, Awaitable, Any

from plurk.async_apis.base import BaseApi
from plurk.enums import Qualifier
from plurk.exceptions import validate_resp
from plurk.models import ActionResp, Response, ResponsesGetResp
from plurk.utils import build_params


class Responses(BaseApi):
    async def get(
        self,
        plurk_id: int,
        from_response: Optional[int] = None,
        minimal_data: Optional[bool] = None,
        count: Optional[int] = None,
    ) -> Coroutine[Any, Any, Awaitable[ResponsesGetResp]]:
        """Fetches responses for plurk with `plurk_id` and some basic info about the users.
        """
        endpoint = f'{self.client.base_url}/APP/Responses/get'
        params = build_params(
            plurk_id=plurk_id,
            from_response=from_response,
            minimal_data=minimal_data,
            count=count,
        )
        resp = await self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return ResponsesGetResp(**resp.json())

    async def response_add(self, plurk_id: int, content: str, qualifier: Qualifier = Qualifier.EMPTY):
        """Adds a responses to `plurk_id`. Language is inherited from the plurk.
        """
        endpoint = f'{self.client.base_url}/APP/Responses/responseAdd'
        payload = build_params(
            plurk_id=plurk_id,
            content=content,
            qualifier=qualifier,
        )
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return Response(**resp.json())

    async def response_delete(self, plurk_id: int, response_id: int):
        """Deletes a response. A user can delete own responses or responses that are posted to own plurks.
        """
        endpoint = f'{self.client.base_url}/APP/Responses/responseDelete'
        payload = build_params(
            response_id=response_id,
            plurk_id=plurk_id,
        )
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())
