import pytest
from authlib.integrations.base_client.errors import OAuthError
from authlib.integrations.httpx_client import AsyncOAuth1Client

from plurk import AsyncClient


FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')
FAKE_AUTH_CODE = 'auth_code'
FAKE_AUTH_URL = 'http://auth_url'
FAKE_CLIENT_CREDENTIALS = ('fake_oauth_token', 'fake_oauth_secret')
FAKE_REQUEST_TOKEN = {'oauth_token': '', 'oauth_token_secret': ''}


@pytest.mark.asyncio
async def test_get_request_token(mocker):
    mocker.patch(
        'authlib.integrations.httpx_client.AsyncOAuth1Client.fetch_request_token',
        return_value=FAKE_REQUEST_TOKEN
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        request_token = await client.get_request_token()
    assert request_token == FAKE_REQUEST_TOKEN


@pytest.mark.asyncio
async def test_get_request_token_fail(mocker):
    exc_msg = 'fetch_token_denied: Token request failed with code 401'
    mocker.patch(
        'authlib.integrations.httpx_client.AsyncOAuth1Client.fetch_request_token',
        side_effect=OAuthError(exc_msg)
    )
    with pytest.raises(OAuthError) as exc:
        async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
            await client.get_request_token()
    assert exc_msg in str(exc)


@pytest.mark.asyncio
async def test_get_auth_url(mocker):
    mocker.patch(
        'authlib.integrations.httpx_client.AsyncOAuth1Client.create_authorization_url',
        return_value=FAKE_AUTH_URL
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        auth_url = client.get_auth_url(FAKE_REQUEST_TOKEN)
    assert auth_url == FAKE_AUTH_URL


@pytest.mark.asyncio
async def test_get_auth_url_request_token_key_error(mocker):
    with pytest.raises(KeyError):
        async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
            client.get_auth_url({})


@pytest.mark.asyncio
async def test_fetch_access_token(mocker):
    access_token_fixture = {
        'oauth_token': 'fake_oauth_token',
        'oauth_token_secret': 'fake_oauth_token_secret',
    }
    mocker.patch(
        'authlib.integrations.httpx_client.AsyncOAuth1Client.fetch_access_token',
        return_value=access_token_fixture,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        access_token = await client.fetch_access_token(
            request_token=FAKE_REQUEST_TOKEN,
            oauth_verifier=FAKE_AUTH_CODE,
        )
        assert access_token == access_token_fixture
        assert client.token == access_token_fixture['oauth_token']
        assert client.token_secret == access_token_fixture['oauth_token_secret']

        # Test that the underlying client is properly configured for auth
        assert client.http_client.auth.__dict__ == AsyncOAuth1Client(
            *FAKE_APP_CREDENTIALS,
            token=access_token_fixture['oauth_token'],
            token_secret=access_token_fixture['oauth_token_secret'],
        ).auth.__dict__


@pytest.mark.asyncio
async def test_fetch_access_token_fail(mocker):
    exc_msg = 'fetch_token_denied: Token request failed with code 400'
    mocker.patch(
        'authlib.integrations.httpx_client.AsyncOAuth1Client.fetch_access_token',
        side_effect=OAuthError(exc_msg)
    )
    with pytest.raises(OAuthError) as exc:
        async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
            await client.fetch_access_token(
                request_token=FAKE_REQUEST_TOKEN,
                oauth_verifier=FAKE_AUTH_CODE,
            )
    assert exc_msg in str(exc)
