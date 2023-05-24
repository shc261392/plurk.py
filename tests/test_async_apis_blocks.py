import pytest
from pytest_httpx import HTTPXMock

from plurk import AsyncClient
from plurk.models import ActionResp, GetBlocksResp

FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')
FAKE_USER_ID = -1


@pytest.mark.asyncio
async def test_get(httpx_mock: HTTPXMock, get_blocks_resp_fixture):
    resp_json = get_blocks_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        get_blocks_resp = await client.blocks.get()
    assert isinstance(get_blocks_resp, GetBlocksResp)
    assert get_blocks_resp_fixture.dict_original() == resp_json


@pytest.mark.asyncio
async def test_block(httpx_mock: HTTPXMock, action_resp_fixture):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        resp = await client.blocks.block(FAKE_USER_ID)
    assert isinstance(resp, ActionResp)
    assert action_resp_fixture.dict_original() == resp_json


@pytest.mark.asyncio
async def test_unblock(httpx_mock: HTTPXMock, action_resp_fixture):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        resp = await client.blocks.unblock(FAKE_USER_ID)
    assert isinstance(resp, ActionResp)
    assert action_resp_fixture.dict_original() == resp_json
