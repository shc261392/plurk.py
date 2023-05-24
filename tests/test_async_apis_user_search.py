import pytest
from pytest_httpx import HTTPXMock

from plurk import AsyncClient
from plurk.models import UserSearchResp

FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')


@pytest.mark.asyncio
async def test_search(httpx_mock: HTTPXMock, user_search_resp_fixture):
    resp_json = user_search_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        user_search_resp = await client.user_search.search('')
    assert isinstance(user_search_resp, UserSearchResp)
    assert user_search_resp_fixture.dict_original() == resp_json
