from typing import Dict, TypeVar

from authlib.integrations.httpx_client import OAuth1Client

from plurk import apis
from plurk.clients.base import BaseClient
from plurk.exceptions import validate_resp

T = TypeVar('T')


class Client(BaseClient):
    """Synchronous client for Plurk API
    """
    http_client_class = OAuth1Client

    def __enter__(self):
        self.setup_client()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.http_client.close()

    def setup_client(self):
        if self.http_client:
            self.http_client.close()
        self.http_client = self.http_client_class(
            self.app_key,
            self.app_secret,
            self.token,
            self.token_secret,
        )

    def get_request_token(self):
        return self.http_client.fetch_request_token(
            url=f'{self.base_url}/OAuth/request_token',
        )

    def get_auth_url(self, request_token: Dict):
        return self.http_client.create_authorization_url(
            f'{self.base_url}/OAuth/authorize',
            request_token['oauth_token'],
        )

    def fetch_access_token(self, request_token: Dict, oauth_verifier: str):
        """Fetch access token using request token and oauth verifier

        Args:
            request_token (Dict): The request token obtained during authorization
            oauth_verifier (str): The oauth verifier returned by Plurk after user authorization

        Returns:
            Dict: The access token information
        """
        self.token = request_token['oauth_token']
        self.token_secret = request_token['oauth_token_secret']
        self.setup_client()
        access_token = self.http_client.fetch_access_token(
            url=f'{self.base_url}/OAuth/access_token',
            oauth_verifier=oauth_verifier,
        )
        self.token = access_token['oauth_token']
        self.token_secret = access_token['oauth_token_secret']
        self.setup_client()
        return access_token

    def set_access_token(self, token: str, token_secret: str):
        """Set the access token and token secret for the client

        Args:
            token (str): The access token
            token_secret (str): The access token secret
        """
        self.token = token
        self.token_secret = token_secret
        self.setup_client()

    def checkToken(self):
        endpoint = f'{self.base_url}/APP/checkToken'
        resp = self.http_client.post(endpoint)
        validate_resp(resp)
        return resp.json()

    def expireToken(self):
        endpoint = f'{self.base_url}/APP/expireToken'
        resp = self.http_client.post(endpoint)
        validate_resp(resp)
        return resp.json()

    def checkTime(self):
        endpoint = f'{self.base_url}/APP/checkTime'
        resp = self.http_client.post(endpoint)
        validate_resp(resp)
        return resp.json()

    def echo(self, data: Dict[str, T]) -> Dict[str, T]:
        endpoint = f'{self.base_url}/APP/echo'
        resp = self.http_client.post(endpoint, data=data)
        validate_resp(resp)
        return resp.json()

    @property
    def users(self):
        return apis.Users(self)

    @property
    def profile(self):
        return apis.Profile(self)

    @property
    def realtime(self):
        return apis.Realtime(self)

    @property
    def timeline(self):
        return apis.Timeline(self)

    @property
    def responses(self):
        return apis.Responses(self)

    @property
    def friends_fans(self):
        return apis.FriendsFans(self)

    @property
    def alerts(self):
        return apis.Alerts(self)

    @property
    def plurk_search(self):
        return apis.PlurkSearch(self)

    @property
    def user_search(self):
        return apis.UserSearch(self)

    @property
    def emoticons(self):
        return apis.Emoticons(self)

    @property
    def blocks(self):
        return apis.Blocks(self)

    @property
    def cliques(self):
        return apis.Cliques(self)

    @property
    def helpers(self):
        return apis.Helper(self)
