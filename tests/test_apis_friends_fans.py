from typing import Dict, List

from pytest_httpx import HTTPXMock

from plurk import Client
from plurk.models import ActionResp, PublicUserData

FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')
FAKE_CONTENT = 'foobar'
FAKE_USER_ID = -1


def test_get_friends_by_offset(httpx_mock: HTTPXMock, public_user_data_list_fixture: List[PublicUserData]):
    resp_json = [i.dict_original() for i in public_user_data_list_fixture]
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.friends_fans.get_friends_by_offset(FAKE_USER_ID)
    assert isinstance(resp, List)
    assert [i.dict_original() for i in resp] == resp_json


def test_get_fans_by_offset(httpx_mock: HTTPXMock, public_user_data_list_fixture: List[PublicUserData]):
    resp_json = [i.dict_original() for i in public_user_data_list_fixture]
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.friends_fans.get_fans_by_offset(FAKE_USER_ID)
    assert isinstance(resp, List)
    assert [i.dict_original() for i in resp] == resp_json


def test_get_following_by_offset(httpx_mock: HTTPXMock, public_user_data_list_fixture: List[PublicUserData]):
    resp_json = [i.dict_original() for i in public_user_data_list_fixture]
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.friends_fans.get_following_by_offset(FAKE_USER_ID)
    assert isinstance(resp, List)
    assert [i.dict_original() for i in resp] == resp_json


def test_become_friend(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.friends_fans.become_friend(FAKE_USER_ID)
    assert isinstance(resp, ActionResp)
    assert resp.dict_original() == resp_json


def test_remove_as_friend(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.friends_fans.remove_as_friend(FAKE_USER_ID)
    assert isinstance(resp, ActionResp)
    assert resp.dict_original() == resp_json


def test_become_fan(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.friends_fans.become_fan(FAKE_USER_ID)
    assert isinstance(resp, ActionResp)
    assert resp.dict_original() == resp_json


def test_set_following(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.friends_fans.set_following(FAKE_USER_ID, False)
    assert isinstance(resp, ActionResp)
    assert resp.dict_original() == resp_json


def test_remove_as_fan(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.friends_fans.remove_as_fan(FAKE_USER_ID)
    assert isinstance(resp, ActionResp)
    assert resp.dict_original() == resp_json


def test_get_completion(httpx_mock: HTTPXMock):
    resp_json = {
        '123': {
            'full_name': 'Plurk User',
            'nick_name': 'plurk',
            'avatar': 12345,
            'display_name': 'Plurker'
        }
    }
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.friends_fans.get_completion()
    assert isinstance(resp, Dict)
    assert resp == resp_json
