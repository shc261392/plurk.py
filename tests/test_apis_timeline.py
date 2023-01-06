from pytest_httpx import HTTPXMock
from pytest_mock import MockerFixture

from plurk import Client
from plurk.models import UploadPictureResp, GetPlurkResp, GetPlurksResp, TimelineActionResp


FAKE_APP_CREDENTIALS = ('fake_app_key', 'fake_app_secret')
FAKE_PLURK_ID = -1
FAKE_USER_ID = -1
FAKE_FILEPATH = '/dev/null'


def test_get_plurk(httpx_mock: HTTPXMock, get_plurk_resp_fixture):
    resp_json = get_plurk_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    with Client(*FAKE_APP_CREDENTIALS) as client:
        get_plurk_resp = client.timeline.get_plurk(FAKE_PLURK_ID)
    assert isinstance(get_plurk_resp, GetPlurkResp)
    assert get_plurk_resp.dict_original() == resp_json


def test_upload_picture(httpx_mock: HTTPXMock, mocker: MockerFixture, upload_picture_resp_fixture):
    resp_json = upload_picture_resp_fixture.dict_original()
    httpx_mock.add_response(
        status_code=200,
        json=resp_json,
    )
    mocker.patch('builtins.open', mocker.mock_open(read_data=b''))
    with Client(*FAKE_APP_CREDENTIALS) as client:
        upload_picture_resp = client.timeline.upload_picture(FAKE_FILEPATH)
    assert isinstance(upload_picture_resp, UploadPictureResp)
    assert upload_picture_resp.dict_original() == resp_json
