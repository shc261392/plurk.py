from datetime import datetime

from httpx._multipart import MultipartStream
from pytest_httpx import HTTPXMock
from pytest_mock import MockerFixture

from plurk import Client
from plurk.utils import parse_plurk_time


def test_me(httpx_mock: HTTPXMock, user_data_fixture):
    resp_json = user_data_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client('app_key', 'app_secret') as client:
        user_data = client.users.me()
    for k, v in user_data.dict().items():
        if isinstance(v, datetime):
            assert v == parse_plurk_time(resp_json[k])
        else:
            assert v == resp_json[k]


def test_update_avatar(httpx_mock: HTTPXMock, mocker: MockerFixture, update_avatar_response_fixture):
    resp_json = update_avatar_response_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    mocker.patch('builtins.open', mocker.mock_open(read_data=b''))
    with Client('app_key', 'app_secret') as client:
        user_data = client.users.update_avatar('')
    for k, v in user_data.dict().items():
        if isinstance(v, datetime):
            assert v == parse_plurk_time(resp_json[k])
        else:
            assert v == resp_json[k]


def test_get_karma_stats(httpx_mock: HTTPXMock, karma_stats_fixture):
    resp_json = karma_stats_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client('app_key', 'app_secret') as client:
        karma_stats = client.users.get_karma_stats()
        assert karma_stats.dict() == resp_json
