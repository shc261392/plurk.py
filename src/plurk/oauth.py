from typing import Dict

from authlib.integrations.httpx_client import OAuth1Client


def get_oauth_client(
    client_id: str, client_secret: str,
    token=None, token_secret=None,
    redirect_uri=None,
):
    return OAuth1Client(
        client_id, client_secret,
        token=token, token_secret=token_secret,
        redirect_uri=redirect_uri,
    )


def get_request_token(client: OAuth1Client, request_token_url: str):
    return client.fetch_request_token(request_token_url)


def get_auth_url(client: OAuth1Client, authenticate_url: str, request_token: Dict[str, str]):
    return client.create_authorization_url(authenticate_url, request_token['oauth_token'])


def fetch_access_token(
    client_id: str, client_secret: str, access_token_url: str,
    request_token: Dict[str, str], oauth_verifier: str,
):
    with OAuth1Client(
        client_id,
        client_secret,
        token=request_token['oauth_token'],
        token_secret=request_token['oauth_token_secret']
    ) as client:
        token = client.fetch_access_token(access_token_url, oauth_verifier)
    return token
