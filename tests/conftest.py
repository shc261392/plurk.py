from datetime import datetime

import pytest
from pydantic_factories import ModelFactory

from plurk.models import KarmaStats, UpdateAvatarResponse, UserData
from plurk.utils import format_as_plurk_time


def generate_date_string():
    return format_as_plurk_time(datetime(1999, 1, 1))


class UserDataFactory(ModelFactory):
    __model__ = UserData

    date_of_birth = generate_date_string
    join_date = generate_date_string


@pytest.fixture()
def user_data_fixture(request) -> UserData:
    return UserDataFactory.build()


class UpdateAvatarResponseFactory(ModelFactory):
    __model__ = UpdateAvatarResponse

    date_of_birth = generate_date_string


@pytest.fixture()
def update_avatar_response_fixture(request) -> UpdateAvatarResponse:
    return UpdateAvatarResponseFactory.build()


class KarmaStatsFactory(ModelFactory):
    __model__ = KarmaStats


@pytest.fixture()
def karma_stats_fixture(request) -> KarmaStats:
    return KarmaStatsFactory.build()
