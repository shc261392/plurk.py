from pytest_httpx import HTTPXMock

from plurk import Client
from plurk.models import UserChannel


def test_get_user_channel(httpx_mock: HTTPXMock, user_channel_fixture):
    resp_json = user_channel_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client('app_key', 'app_secret') as client:
        user_channel = client.realtime.get_user_channel()
    assert isinstance(user_channel, UserChannel)
    assert user_channel.dict_original() == resp_json
