from typing import Optional

from plurk.async_apis.base import BaseApi
from plurk.exceptions import validate_resp
from plurk.models import PlurkSearchResp
from plurk.utils import build_params


class PlurkSearch(BaseApi):
    async def search(self, query: str, offset: Optional[int] = None):
        """Returns the latest 20 plurks on a search term.
        """
        endpoint = f'{self.client.base_url}/APP/PlurkSearch/search'
        params = build_params(query=query, offset=offset)
        resp = await self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return PlurkSearchResp(**resp.json())
