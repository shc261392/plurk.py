import pytest

from plurk.client import Client
from plurk.oauth import OAuth1Client


class MockOAuth1Client(OAuth1Client):
    pass


class MockClient(Client):
    pass


@pytest.fixture(scope='session', autouse=True)
def client(request):
    return Client('app_key', 'app_secret')
