import pytest
from pytest_httpx import HTTPXMock
from pytest_mock import MockerFixture

from plurk import AsyncClient
from plurk.enums import AbuseCategory
from plurk.models import (ActionResp, GetPlurkResp, GetPlurksResp, Plurk,
                          UploadPictureResp)

FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')
FAKE_CONTENT = 'foobar'
FAKE_PLURK_ID = -1
FAKE_USER_ID = -1
FAKE_FILEPATH = '/dev/null'


@pytest.mark.asyncio
async def test_get_plurk(httpx_mock: HTTPXMock, get_plurk_resp_fixture: GetPlurkResp):
    resp_json = get_plurk_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        get_plurk_resp = await client.timeline.get_plurk(FAKE_PLURK_ID)
    assert isinstance(get_plurk_resp, GetPlurkResp)
    assert get_plurk_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_get_plurks(httpx_mock: HTTPXMock, get_plurks_resp_fixture: GetPlurksResp):
    resp_json = get_plurks_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        get_plurks_resp = await client.timeline.get_plurks()
    assert isinstance(get_plurks_resp, GetPlurksResp)
    assert get_plurks_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_get_unread_plurks(httpx_mock: HTTPXMock, get_plurks_resp_fixture: GetPlurksResp):
    resp_json = get_plurks_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        get_plurks_resp = await client.timeline.get_unread_plurks()
    assert isinstance(get_plurks_resp, GetPlurksResp)
    assert get_plurks_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_get_public_plurks(httpx_mock: HTTPXMock, get_plurks_resp_fixture: GetPlurksResp):
    resp_json = get_plurks_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        get_plurks_resp = await client.timeline.get_public_plurks(FAKE_USER_ID)
    assert isinstance(get_plurks_resp, GetPlurksResp)
    assert get_plurks_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_plurk_add(httpx_mock: HTTPXMock, plurk_fixture: Plurk):
    resp_json = plurk_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        plurk = await client.timeline.plurk_add(FAKE_CONTENT)
    assert isinstance(plurk, Plurk)
    assert plurk.dict_original() == resp_json


@pytest.mark.asyncio
async def test_plurk_delete(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        action_resp = await client.timeline.plurk_delete(FAKE_PLURK_ID)
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_plurk_edit(httpx_mock: HTTPXMock, plurk_fixture: Plurk):
    resp_json = plurk_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        plurk = await client.timeline.plurk_edit(FAKE_PLURK_ID, FAKE_CONTENT)
    assert isinstance(plurk, Plurk)
    assert plurk.dict_original() == resp_json


@pytest.mark.asyncio
async def test_toggle_comments(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        action_resp = await client.timeline.toggle_comments(FAKE_PLURK_ID, 0)
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_mute_plurks(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        action_resp = await client.timeline.mute_plurks([FAKE_PLURK_ID])
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_unmute_plurks(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        action_resp = await client.timeline.unmute_plurks([FAKE_PLURK_ID])
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_favorite_plurks(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        action_resp = await client.timeline.favorite_plurks([FAKE_PLURK_ID])
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_unfavorite_plurks(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        action_resp = await client.timeline.unfavorite_plurks([FAKE_PLURK_ID])
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_replurk(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        action_resp = await client.timeline.replurk([FAKE_PLURK_ID])
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_unreplurk(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        action_resp = await client.timeline.unreplurk([FAKE_PLURK_ID])
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_mark_as_read(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        action_resp = await client.timeline.mark_as_read([FAKE_PLURK_ID])
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_upload_picture(
    httpx_mock: HTTPXMock,
    mocker: MockerFixture,
    upload_picture_resp_fixture: UploadPictureResp,
):
    resp_json = upload_picture_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    mocker.patch('builtins.open', mocker.mock_open(read_data=b''))
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        upload_picture_resp = await client.timeline.upload_picture(FAKE_FILEPATH)
    assert isinstance(upload_picture_resp, UploadPictureResp)
    assert upload_picture_resp.dict_original() == resp_json


@pytest.mark.asyncio
async def test_report_abuse(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        action_resp = await client.timeline.report_abuse(FAKE_PLURK_ID, AbuseCategory.SPAM)
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json
