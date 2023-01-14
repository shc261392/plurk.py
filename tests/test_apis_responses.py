from pytest_httpx import HTTPXMock

from plurk import Client
from plurk.models import ActionResp, Response, ResponsesGetResp

FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')
FAKE_CONTENT = 'foobar'
FAKE_PLURK_ID = -1
FAKE_RESPONSE_ID = -1


def test_get(httpx_mock: HTTPXMock, responses_get_resp_fixture: ResponsesGetResp):
    resp_json = responses_get_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        resp = client.responses.get(FAKE_PLURK_ID)
    assert isinstance(resp, ResponsesGetResp)
    assert resp.dict_original() == resp_json


def test_response_add(httpx_mock: HTTPXMock, response_fixture: Response):
    resp_json = response_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        response = client.responses.response_add(FAKE_PLURK_ID, FAKE_CONTENT)
    assert isinstance(response, Response)
    assert response.dict_original() == resp_json


def test_response_delete(httpx_mock: HTTPXMock, action_resp_fixture: ActionResp):
    resp_json = action_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        action_resp = client.responses.response_delete(FAKE_PLURK_ID, FAKE_RESPONSE_ID)
    assert isinstance(action_resp, ActionResp)
    assert action_resp.dict_original() == resp_json
