import pytest
from authlib.integrations.base_client.errors import OAuthError
from authlib.integrations.httpx_client import OAuth1Client

from plurk import Client


FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')
FAKE_AUTH_CODE = 'auth_code'
FAKE_AUTH_URL = 'http://auth_url'
FAKE_CLIENT_CREDENTIALS = ('fake_oauth_token', 'fake_oauth_secret')
FAKE_REQUEST_TOKEN = {'oauth_token': '', 'oauth_token_secret': ''}


def test_get_request_token(mocker):
    mocker.patch(
        'authlib.integrations.httpx_client.OAuth1Client.fetch_request_token',
        return_value=FAKE_REQUEST_TOKEN
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        request_token = client.get_request_token()
    assert request_token == FAKE_REQUEST_TOKEN


def test_get_request_token_fail(mocker):
    exc_msg = 'fetch_token_denied: Token request failed with code 401'
    mocker.patch(
        'authlib.integrations.httpx_client.OAuth1Client.fetch_request_token',
        side_effect=OAuthError(exc_msg)
    )
    with pytest.raises(OAuthError) as exc:
        with Client(*FAKE_APP_CREDENTIALS) as client:
            client.get_request_token()
    assert exc_msg in str(exc)


def test_get_auth_url(mocker):
    mocker.patch(
        'authlib.integrations.httpx_client.OAuth1Client.create_authorization_url',
        return_value=FAKE_AUTH_URL
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        auth_url = client.get_auth_url(FAKE_REQUEST_TOKEN)
    assert auth_url == FAKE_AUTH_URL


def test_get_auth_url_request_token_key_error(mocker):
    with pytest.raises(KeyError):
        with Client(*FAKE_APP_CREDENTIALS) as client:
            client.get_auth_url({})


def test_fetch_access_token(mocker):
    access_token_fixture = {
        'oauth_token': 'fake_oauth_token',
        'oauth_token_secret': 'fake_oauth_token_secret',
    }
    mocker.patch(
        'authlib.integrations.httpx_client.OAuth1Client.fetch_access_token',
        return_value=access_token_fixture,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        access_token = client.fetch_access_token(
            request_token=FAKE_REQUEST_TOKEN,
            oauth_verifier=FAKE_AUTH_CODE,
        )
        assert access_token == access_token_fixture
        assert client.token == access_token_fixture['oauth_token']
        assert client.token_secret == access_token_fixture['oauth_token_secret']

        # Test that the underlying client is properly configured for auth
        assert client.http_client.auth.__dict__ == OAuth1Client(
            *FAKE_APP_CREDENTIALS,
            token=access_token_fixture['oauth_token'],
            token_secret=access_token_fixture['oauth_token_secret'],
        ).auth.__dict__


def test_fetch_access_token_fail(mocker):
    exc_msg = 'fetch_token_denied: Token request failed with code 400'
    mocker.patch(
        'authlib.integrations.httpx_client.OAuth1Client.fetch_access_token',
        side_effect=OAuthError(exc_msg)
    )
    with pytest.raises(OAuthError) as exc:
        with Client(*FAKE_APP_CREDENTIALS) as client:
            client.fetch_access_token(
                request_token=FAKE_REQUEST_TOKEN,
                oauth_verifier=FAKE_AUTH_CODE,
            )
    assert exc_msg in str(exc)
