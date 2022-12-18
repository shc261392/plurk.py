from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel

from plurk.utils import parse_time_validator


class FilterSetting(BaseModel):
    porn: int
    anonymous: int
    keywords: str


class Anniversary(BaseModel):
    years: int
    days: int


class Relationship(str, Enum):
    NOT_SAYING = 'not_saying'
    SINGLE = 'single'
    MARRIED = 'married'
    DIVORCED = 'divorced'
    ENGAGED = 'engaged'
    IN_RELATIONSHIP = 'in_relationship'
    COMPLICATED = 'complicated'
    WIDOWED = 'widowed'
    UNSTABLE_RELATIONSHIP = 'unstable_relationship'
    OPEN_RELATIONSHIP = 'open_relationship'


class AvatarSize(str, Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    BIG = 'big'


class Privacy(str, Enum):
    WORLD = 'world'
    ONLY_FRIENDS = 'only_friends'


class BaseUserData(BaseModel):
    """Base class for user data
    """
    id: int
    status: str
    has_profile_image: int
    timeline_privacy: int
    nick_name: str
    display_name: Optional[str]
    date_of_birth: Optional[datetime]
    avatar: int
    gender: int  # 1 is male, 0 is female, 2 is not stating/other.
    karma: float
    premium: bool
    verified_account: bool
    dateformat: int
    default_lang: str
    friend_list_privacy: str
    name_color: str
    full_name: str
    location: str
    timezone: str
    phone_verified: Optional[Any]  # not sure; only saw None in real data
    bday_privacy: int  # 0: hide birthday, 1: show birth date but not birth year, 2: show all
    pinned_plurk_id: int
    background_id: int
    show_ads: bool

    _parse_date_of_birth = parse_time_validator('date_of_birth')

    @property
    def avatar_url_small(self):
        """Constructed avatar URL. It is recommended to use attribute avatar_small instead.
        """
        return self._get_avatar_url(AvatarSize.SMALL)

    @property
    def avatar_url_medium(self):
        """Constructed avatar URL. It is recommended to use attribute avatar_medium instead.
        """
        return self._get_avatar_url(AvatarSize.MEDIUM)

    @property
    def avatar_url_big(self):
        """Constructed avatar URL. It is recommended to use attribute avatar_big instead.
        """
        return self._get_avatar_url(AvatarSize.BIG)

    def _get_avatar_url(self, size: AvatarSize = AvatarSize.BIG):
        """Construct avatar URL based on UserData and desired image size.

        The rule for getting the URL is described in official API doc: https://www.plurk.com/API
        The actual data returned as for now already includes avatar URLs, so there's no need to
        construct URLs now.
        """
        url_template = '{base_url}/{user_id}-{size}{avatar}.{ext}'

        if self.has_profile_image == 1:
            base_url = 'https://avatars.plurk.com'
            user_id = self.id
            if size == AvatarSize.BIG:
                ext = 'jpg'
            else:
                ext = 'gif'
        else:
            base_url = 'https://www.plurk.com/static'
            user_id = 'default'
            ext = 'jpg'

        avatar = self.avatar if (self.has_profile_image == 1 and self.avatar) else ''

        return url_template.format(
            base_url=base_url,
            user_id=user_id,
            size=size.value,
            avatar=avatar,
            ext=ext,
        )


class UserData(BaseUserData):
    """Data returned by `/APP/Users/me` endpoint
    """
    plurks_count: int
    response_count: int
    profile_views: int
    avatar_small: str
    avatar_medium: str
    avatar_big: str
    about: str
    about_renderred: str
    page_title: str
    recruited: int
    relationship: Relationship
    friends_count: int
    fans_count: int
    join_date: datetime
    hide_plurks_before: Optional[Any]  # not sure; only saw None in real data
    privacy: str
    accept_private_plurk_from: str
    post_anonymous_plurk: bool
    badges: List[str]
    setup_twitter_sync: bool
    filter: FilterSetting
    anniversary: Anniversary
    phone_number: Optional[str]
    creature: int
    creature_url: Optional[str]
    creature_special: int
    creature_special_url: Optional[str]

    _parse_join_date = parse_time_validator('join_date')

    class Config:
        use_enum_values = True


class UpdateAvatarResponse(BaseUserData):
    """Data returned by `/APP/Users/updateAvatar` endpoint
    """