import pytest
from pytest_httpx import HTTPXMock

from plurk import AsyncClient
from plurk.models import UserChannel


FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')


@pytest.mark.asyncio
async def test_get_user_channel(httpx_mock: HTTPXMock, user_channel_fixture):
    resp_json = user_channel_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        user_channel = await client.realtime.get_user_channel()
    assert isinstance(user_channel, UserChannel)
    assert user_channel.dict_original() == resp_json
