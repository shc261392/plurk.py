from typing import Dict, List

from plurk.enums import Privacy
from plurk.models.base import RespBase
from plurk.models.plurk import Plurk
from plurk.models.user_data import PublicUserData, UserData


class ProfileBase(RespBase):
    """Base class for profile
    """
    fans_count: int
    friends_count: int
    privacy: Privacy
    plurks: List[Plurk]
    user_info: UserData


class OwnProfile(ProfileBase):
    """Data returned by `/APP/Profile/getOwnProfile` endpoint
    """
    alerts_count: int
    has_read_permission: bool
    plurks_users: Dict[str, PublicUserData]
    """A dict of public user data.

    Each key is a stringified user id and the value is its public user data.
    """
    unread_count: int


class PublicProfile(ProfileBase):
    """Data returned by `/APP/Profile/getPublicProfile` endpoint

    WARNING: The data model has not yet been verified.
    """
