from typing import Dict, TypeVar

from authlib.integrations.httpx_client import AsyncOAuth1Client

from plurk import async_apis
from plurk.clients.base import BaseClient
from plurk.exceptions import validate_resp

T = TypeVar('T')


class AsyncClient(BaseClient):
    """Asynchronous client for Plurk API
    """
    http_client_class = AsyncOAuth1Client

    async def __aenter__(self):
        await self.setup_client()
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        await self.http_client.aclose()

    async def setup_client(self):
        if self.http_client:
            await self.http_client.aclose()  # type: ignore
        self.http_client = self.http_client_class(
            self.app_key,
            self.app_secret,
            self.token,
            self.token_secret,
        )

    async def get_request_token(self):
        return await self.http_client.fetch_request_token(
            url=f'{self.base_url}/OAuth/request_token',
        )

    def get_auth_url(self, request_token: Dict):
        return self.http_client.create_authorization_url(
            f'{self.base_url}/OAuth/authorize',
            request_token['oauth_token'],
        )

    async def fetch_access_token(self, request_token: Dict, oauth_verifier: str):
        """Fetch access token using request token and oauth verifier

        Args:
            request_token (Dict): The request token obtained during authorization
            oauth_verifier (str): The oauth verifier returned by Plurk after user authorization

        Returns:
            Dict: The access token information
        """
        self.token = request_token['oauth_token']
        self.token_secret = request_token['oauth_token_secret']
        await self.setup_client()
        access_token = await self.http_client.fetch_access_token(
            url=f'{self.base_url}/OAuth/access_token',
            oauth_verifier=oauth_verifier,
        )
        self.token = access_token['oauth_token']
        self.token_secret = access_token['oauth_token_secret']
        await self.setup_client()
        return access_token

    async def set_access_token(self, token: str, token_secret: str):
        """Set the access token and token secret for the client

        Args:
            token (str): The access token
            token_secret (str): The access token secret
        """
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
