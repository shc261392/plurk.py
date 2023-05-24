import pytest
from typing import List

from pytest_httpx import HTTPXMock

from plurk import AsyncClient
from plurk.models import ActionResp, PublicUserData

FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')
FAKE_CLIQUE_NAME = 'fake_clique_name'
FAKE_NEW_NAME = 'fake_new_name'
FAKE_USER_ID = -1


@pytest.mark.asyncio
async def test_get_cliques(httpx_mock: HTTPXMock, get_cliques_resp_fixture):
    resp_json = get_cliques_resp_fixture
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        get_cliques_resp = await client.cliques.get_cliques()
    assert isinstance(get_cliques_resp, list)
    assert get_cliques_resp_fixture == get_cliques_resp


@pytest.mark.asyncio
async def test_get_clique(httpx_mock: HTTPXMock, public_user_data_list_fixture: List[PublicUserData]):
    resp_json = [i.dict_original() for i in public_user_data_list_fixture]
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        resp = await client.cliques.get_clique(FAKE_CLIQUE_NAME)
    assert isinstance(resp, list)
    assert [i.dict_original() for i in resp] == resp_json


@pytest.mark.asyncio
async def test_create_clique(httpx_mock: HTTPXMock, action_resp_fixture):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        resp = await client.cliques.create_clique(FAKE_CLIQUE_NAME)
    assert isinstance(resp, ActionResp)
    assert action_resp_fixture.dict_original() == resp_json


@pytest.mark.asyncio
async def test_rename_clique(httpx_mock: HTTPXMock, action_resp_fixture):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        resp = await client.cliques.rename_clique(FAKE_CLIQUE_NAME, FAKE_NEW_NAME)
    assert isinstance(resp, ActionResp)
    assert action_resp_fixture.dict_original() == resp_json


@pytest.mark.asyncio
async def test_add(httpx_mock: HTTPXMock, action_resp_fixture):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        resp = await client.cliques.add(FAKE_CLIQUE_NAME, FAKE_USER_ID)
    assert isinstance(resp, ActionResp)
    assert action_resp_fixture.dict_original() == resp_json


@pytest.mark.asyncio
async def test_remove(httpx_mock: HTTPXMock, action_resp_fixture):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        resp = await client.cliques.remove(FAKE_CLIQUE_NAME, FAKE_USER_ID)
    assert isinstance(resp, ActionResp)
    assert action_resp_fixture.dict_original() == resp_json
