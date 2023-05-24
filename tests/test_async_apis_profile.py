import pytest
from pytest_httpx import HTTPXMock

from plurk import AsyncClient
from plurk.models import OwnProfile, PublicProfile


FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')


@pytest.mark.asyncio
async def test_get_own_profile(httpx_mock: HTTPXMock, own_profile_fixture):
    resp_json = own_profile_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        own_profile = await client.profile.get_own_profile()
    assert isinstance(own_profile, OwnProfile)
    assert own_profile.dict_original() == resp_json


@pytest.mark.asyncio
async def test_get_public_profile(httpx_mock: HTTPXMock, public_profile_fixture):
    resp_json = public_profile_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    async with AsyncClient(*FAKE_APP_CREDENTIALS) as client:
        public_profile = await client.profile.get_public_profile()
    assert isinstance(public_profile, PublicProfile)
    assert public_profile.dict_original() == resp_json
