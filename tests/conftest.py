from datetime import datetime
from typing import List

import pytest
from pydantic_factories import ModelFactory

from plurk.models import (ActionResp, GetPlurkResp, GetPlurksResp, KarmaStats,
                          OwnProfile, Plurk, PublicProfile, PublicUserData,
                          Response, ResponsesGetResp, SimpleUserData,
                          UpdateAvatarResp, UploadPictureResp, UserChannel,
                          UserData)
from plurk.utils import format_as_plurk_time


def generate_date_string():
    return format_as_plurk_time(datetime(1999, 1, 1))


class ActionRespFactory(ModelFactory):
    __model__ = ActionResp


class KarmaStatsFactory(ModelFactory):
    __model__ = KarmaStats


class GetPlurkRespFactory(ModelFactory):
    __model__ = GetPlurkResp


class GetPlurksRespFactory(ModelFactory):
    __model__ = GetPlurksResp


class OwnProfileFactory(ModelFactory):
    __model__ = OwnProfile


class PublicUserDataFactory(ModelFactory):
    __model__ = PublicUserData
    __auto_register__ = True

    date_of_birth = generate_date_string


class PlurkFactory(ModelFactory):
    __model__ = Plurk
    __auto_register__ = True

    last_edited = generate_date_string
    posted = generate_date_string


class PublicProfileFactory(ModelFactory):
    __model__ = PublicProfile


class ResponseFactory(ModelFactory):
    __model__ = Response
    __auto_register__ = True

    last_edited = generate_date_string
    posted = generate_date_string


class ResponsesGetRespFactory(ModelFactory):
    __model__ = ResponsesGetResp


class SimpleUserDataFactory(ModelFactory):
    __model__ = SimpleUserData
    __auto_register__ = True

    date_of_birth = generate_date_string


class UpdateAvatarRespFactory(ModelFactory):
    __model__ = UpdateAvatarResp

    date_of_birth = generate_date_string


class UploadPictureRespFactory(ModelFactory):
    __model__ = UploadPictureResp


class UserChannelFactory(ModelFactory):
    __model__ = UserChannel


class UserDataFactory(ModelFactory):
    __model__ = UserData
    __auto_register__ = True

    date_of_birth = generate_date_string
    join_date = generate_date_string


@pytest.fixture()
def action_resp_fixture(request) -> ActionResp:
    return ActionRespFactory.build()


@pytest.fixture()
def karma_stats_fixture(request) -> KarmaStats:
    return KarmaStatsFactory.build()


@pytest.fixture()
def get_plurk_resp_fixture(request) -> GetPlurkResp:
    return GetPlurkRespFactory.build()


@pytest.fixture()
def get_plurks_resp_fixture(request) -> GetPlurksResp:
    return GetPlurksRespFactory.build()


@pytest.fixture()
def own_profile_fixture(request) -> OwnProfile:
    return OwnProfileFactory.build()


@pytest.fixture()
def plurk_fixture(request) -> Plurk:
    return PlurkFactory.build()


@pytest.fixture()
def public_profile_fixture(request) -> PublicProfile:
    return PublicProfileFactory.build()


@pytest.fixture()
def public_user_data_list_fixture(request) -> List[PublicUserData]:
    return PublicUserDataFactory.batch(10)


@pytest.fixture()
def response_fixture(request) -> Response:
    return ResponseFactory.build()


@pytest.fixture()
def responses_get_resp_fixture(request) -> ResponsesGetResp:
    return ResponsesGetRespFactory.build()


@pytest.fixture()
def update_avatar_resp_fixture(request) -> UpdateAvatarResp:
    return UpdateAvatarRespFactory.build()


@pytest.fixture()
def upload_picture_resp_fixture(request) -> UploadPictureResp:
    return UploadPictureRespFactory.build()


@pytest.fixture()
def user_channel_fixture(request) -> UserChannel:
    return UserChannelFactory.build()


@pytest.fixture()
def user_data_fixture(request) -> UserData:
    return UserDataFactory.build()
