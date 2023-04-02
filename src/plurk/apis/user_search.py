from typing import Optional

from plurk.apis.base import BaseApi
from plurk.exceptions import validate_resp
from plurk.models import UserSearchResp
from plurk.utils import build_params


class UserSearch(BaseApi):
    def search(self, query: str, offset: Optional[int] = None):
        """Returns 10 users that match query, users are sorted by karma.
        """
        endpoint = f'{self.client.base_url}/APP/UserSearch/search'
        params = build_params(query=query, offset=offset)
        resp = self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return UserSearchResp(**resp.json())
