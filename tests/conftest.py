from datetime import datetime

import pytest
from pydantic_factories import ModelFactory, Use

from plurk.models import (KarmaStats, OwnProfile, Plurk, PublicProfile,
                          PublicUserData, UpdateAvatarResponse, UserData)
from plurk.utils import format_as_plurk_time


def generate_date_string():
    return format_as_plurk_time(datetime(1999, 1, 1))


class KarmaStatsFactory(ModelFactory):
    __model__ = KarmaStats


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


class UpdateAvatarResponseFactory(ModelFactory):
    __model__ = UpdateAvatarResponse

    date_of_birth = generate_date_string


class UserDataFactory(ModelFactory):
    __model__ = UserData
    __auto_register__ = True

    date_of_birth = generate_date_string
    join_date = generate_date_string


@pytest.fixture()
def karma_stats_fixture(request) -> KarmaStats:
    return KarmaStatsFactory.build()


@pytest.fixture()
def own_profile_fixture(request) -> OwnProfile:
    return OwnProfileFactory.build()


@pytest.fixture()
def public_profile_fixture(request) -> PublicProfile:
    return PublicProfileFactory.build()


@pytest.fixture()
def update_avatar_response_fixture(request) -> UpdateAvatarResponse:
    return UpdateAvatarResponseFactory.build()


@pytest.fixture()
def user_data_fixture(request) -> UserData:
    return UserDataFactory.build()
