from pytest_httpx import HTTPXMock
from pytest_mock import MockerFixture

from plurk import Client
from plurk.models import KarmaStats, UpdateAvatarResp, UserData


FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')
FAKE_FILEPATH = '/dev/null'


def test_me(httpx_mock: HTTPXMock, user_data_fixture):
    resp_json = user_data_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        user_data = client.users.me()
    assert isinstance(user_data, UserData)
    assert user_data.dict_original() == resp_json


def test_update_avatar(httpx_mock: HTTPXMock, mocker: MockerFixture, update_avatar_resp_fixture):
    resp_json = update_avatar_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    mocker.patch('builtins.open', mocker.mock_open(read_data=b''))
    with Client(*FAKE_APP_CREDENTIALS) as client:
        update_avatar_resp = client.users.update_avatar(FAKE_FILEPATH)
    assert isinstance(update_avatar_resp, UpdateAvatarResp)
    assert update_avatar_resp.dict_original() == resp_json


def test_get_karma_stats(httpx_mock: HTTPXMock, karma_stats_fixture):
    resp_json = karma_stats_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        karma_stats = client.users.get_karma_stats()
    assert isinstance(karma_stats, KarmaStats)
    assert karma_stats.dict_original() == resp_json
