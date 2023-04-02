from pytest_httpx import HTTPXMock

from plurk import Client
from plurk.models import PlurkSearchResp

FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')


def test_search(httpx_mock: HTTPXMock, plurk_search_resp_fixture):
    resp_json = plurk_search_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        plurk_search_resp = client.plurk_search.search('')
    assert isinstance(plurk_search_resp, PlurkSearchResp)
    assert plurk_search_resp_fixture.dict_original() == resp_json
