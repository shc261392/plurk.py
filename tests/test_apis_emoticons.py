from typing import Dict

from pytest_httpx import HTTPXMock

from plurk import Client

FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')


def test_get(httpx_mock: HTTPXMock, get_emoticons_fixture):
    resp_json = get_emoticons_fixture
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.emoticons.get()
    assert isinstance(resp, Dict)
    assert get_emoticons_fixture == resp
