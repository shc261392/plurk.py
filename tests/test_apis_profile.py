from pytest_httpx import HTTPXMock

from plurk import Client


def test_get_own_profile(httpx_mock: HTTPXMock, own_profile_fixture):
    resp_json = own_profile_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client('app_key', 'app_secret') as client:
        own_profile = client.profile.get_own_profile()
    assert own_profile.dict_original() == resp_json


def test_get_public_profile(httpx_mock: HTTPXMock, public_profile_fixture):
    resp_json = public_profile_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client('app_key', 'app_secret') as client:
        public_profile = client.profile.get_public_profile()
    assert public_profile.dict_original() == resp_json
