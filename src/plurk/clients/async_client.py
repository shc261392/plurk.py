from typing import Dict, TypeVar

from authlib.integrations.httpx_client import AsyncOAuth1Client

from plurk import async_apis, async_oauth
from plurk.clients.base import BaseClient
from plurk.exceptions import validate_resp


T = TypeVar('T')


class AsyncClient(BaseClient):
    """Asynchronous client for Plurk API
    """
    @property
    def http_client_class(self):
        return AsyncOAuth1Client

    async def __aenter__(self):
        await self.setup_client()
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        await self.http_client.aclose()

    async def setup_client(self):
        if self.http_client:
            await self.http_client.aclose()  # type: ignore
        self.http_client = async_oauth.get_oauth_client(
            self.app_key,
            self.app_secret,
            self.token,
            self.token_secret,
        )

    async def get_request_token(self):
        return await async_oauth.get_request_token(
            self.http_client,
            request_token_url=f'{self.base_url}/OAuth/request_token',
        )

    def get_auth_url(self, request_token: Dict):
        return async_oauth.get_auth_url(
            self.http_client,
            authenticate_url=f'{self.base_url}/OAuth/authorize',
            request_token=request_token
        )

    async def fetch_access_token(self, request_token: Dict, oauth_verifier: str):
        access_token = await async_oauth.fetch_access_token(
            self.app_key, self.app_secret,
            access_token_url=f'{self.base_url}/OAuth/access_token',
            request_token=request_token,
            oauth_verifier=oauth_verifier,
        )
        self.token = access_token['oauth_token']
        self.token_secret = access_token['oauth_token_secret']
        await self.setup_client()
        return access_token

    async def set_access_token(self, token: str, token_secret: str):
        self.token = token
        self.token_secret = token_secret
        await self.setup_client()

    async def checkToken(self):
        endpoint = f'{self.base_url}/APP/checkToken'
        resp = await self.http_client.post(endpoint)
        validate_resp(resp)
        return resp.json()

    async def expireToken(self):
        endpoint = f'{self.base_url}/APP/expireToken'
        resp = await self.http_client.post(endpoint)
        validate_resp(resp)
        return resp.json()

    async def checkTime(self):
        endpoint = f'{self.base_url}/APP/checkTime'
        resp = await self.http_client.post(endpoint)
        validate_resp(resp)
        return resp.json()

    async def echo(self, data: Dict[str, T]) -> Dict[str, T]:
        endpoint = f'{self.base_url}/APP/echo'
        resp = await self.http_client.post(endpoint, data=data)
        validate_resp(resp)
        return resp.json()

    @property
    def users(self):
        return async_apis.Users(self)

    @property
    def profile(self):
        return async_apis.Profile(self)

    @property
    def realtime(self):
        return async_apis.Realtime(self)

    @property
    def timeline(self):
        return async_apis.Timeline(self)

    @property
    def responses(self):
        return async_apis.Responses(self)

    @property
    def friends_fans(self):
        return async_apis.FriendsFans(self)

    @property
    def alerts(self):
        return async_apis.Alerts(self)

    @property
    def plurk_search(self):
        return async_apis.PlurkSearch(self)

    @property
    def user_search(self):
        return async_apis.UserSearch(self)

    @property
    def emoticons(self):
        return async_apis.Emoticons(self)

    @property
    def blocks(self):
        return async_apis.Blocks(self)

    @property
    def cliques(self):
        return async_apis.Cliques(self)

    @property
    def helpers(self):
        return async_apis.Helper(self)
