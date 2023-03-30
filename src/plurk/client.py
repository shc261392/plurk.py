from abc import abstractmethod
from typing import Dict, TypeVar

from authlib.integrations.httpx_client import OAuth1Client

from plurk import apis, oauth
from plurk.exceptions import validate_resp

T = TypeVar('T')


class BaseClient():
    """Base class for clients
    """
    @property
    @abstractmethod
    def http_client_class(self):
        pass

    def __init__(self, app_key: str, app_secret: str, base_url='https://www.plurk.com'):
        self.http_client = None
        self.app_key = app_key
        self.app_secret = app_secret
        self.base_url = base_url
        self.token = None
        self.token_secret = None


class Client(BaseClient):
    """Synchronous client for Plurk API
    """
    @property
    def http_client_class(self):
        return OAuth1Client

    def __enter__(self):
        self.setup_client()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.http_client.close()

    def setup_client(self):
        if self.http_client:
            self.http_client.close()
        self.http_client = oauth.get_oauth_client(
            self.app_key,
            self.app_secret,
            self.token,
            self.token_secret,
        )

    def get_request_token(self):
        return oauth.get_request_token(
            self.http_client,
            request_token_url=f'{self.base_url}/OAuth/request_token',
        )

    def get_auth_url(self, request_token: Dict):
        return oauth.get_auth_url(
            self.http_client,
            authenticate_url=f'{self.base_url}/OAuth/authorize',
            request_token=request_token
        )

    def fetch_access_token(self, request_token: Dict, oauth_verifier: str):
        access_token = oauth.fetch_access_token(
            self.app_key, self.app_secret,
            access_token_url=f'{self.base_url}/OAuth/access_token',
            request_token=request_token,
            oauth_verifier=oauth_verifier,
        )
        self.token = access_token['oauth_token']
        self.token_secret = access_token['oauth_token_secret']
        self.setup_client()
        return access_token

    def set_access_token(self, token: str, token_secret: str):
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
    def helpers(self):
        return apis.Helper(self)
