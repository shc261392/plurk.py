from pytest_httpx import HTTPXMock

from plurk import Client
from plurk.models import OwnProfile, PublicProfile


FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')


def test_get_own_profile(httpx_mock: HTTPXMock, own_profile_fixture):
    resp_json = own_profile_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        own_profile = client.profile.get_own_profile()
    assert isinstance(own_profile, OwnProfile)
    assert own_profile.dict_original() == resp_json


def test_get_public_profile(httpx_mock: HTTPXMock, public_profile_fixture):
    resp_json = public_profile_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        public_profile = client.profile.get_public_profile()
    assert isinstance(public_profile, PublicProfile)
    assert public_profile.dict_original() == resp_json
