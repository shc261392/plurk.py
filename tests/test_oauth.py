import pytest
from authlib.integrations.base_client.errors import OAuthError
from authlib.integrations.httpx_client import OAuth1Client

from plurk import Client


def test_get_request_token(mocker):
    mocker.patch(
        'authlib.integrations.httpx_client.OAuth1Client.fetch_request_token',
        return_value='request_token'
    )
    with Client('app_key', 'app_secret') as client:
        request_token = client.get_request_token()
    assert request_token == 'request_token'


def test_get_request_token_fail(mocker):
    exc_msg = 'fetch_token_denied: Token request failed with code 401'
    mocker.patch(
        'authlib.integrations.httpx_client.OAuth1Client.fetch_request_token',
        side_effect=OAuthError(exc_msg)
    )
    with pytest.raises(OAuthError) as exc:
        with Client('invalid_app_key', 'invalid_app_secret') as client:
            client.get_request_token()
    assert exc_msg in str(exc)


def test_get_auth_url(mocker):
    mocker.patch(
        'authlib.integrations.httpx_client.OAuth1Client.create_authorization_url',
        return_value='http://auth_url'
    )
    with Client('app_key', 'app_secret') as client:
        auth_url = client.get_auth_url({'oauth_token': '', 'oauth_secret': ''})
    assert auth_url == 'http://auth_url'


def test_get_auth_url_request_token_key_error(mocker):
    with pytest.raises(KeyError):
        with Client('app_key', 'app_secret') as client:
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
    with Client('app_key', 'app_secret') as client:
        access_token = client.fetch_access_token(
            request_token={'oauth_token': '', 'oauth_token_secret': ''},
            oauth_verifier='auth_code',
        )
    assert access_token == access_token_fixture
    assert client.token == access_token_fixture['oauth_token']
    assert client.token_secret == access_token_fixture['oauth_token_secret']

    # Test that the underlying client is properly configured for auth
    assert client.http_client.auth.__dict__ == OAuth1Client(
        'app_key',
        'app_secret',
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
        with Client('app_key', 'app_secret') as client:
            client.fetch_access_token(
                request_token={'oauth_token': '', 'oauth_token_secret': ''},
                oauth_verifier='auth_code',
            )
    assert exc_msg in str(exc)
