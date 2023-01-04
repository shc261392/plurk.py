from datetime import datetime
from typing import Any, List, Literal, Optional

from plurk.enums import ChannelDataEntryType
from plurk.models.base import RespBase
from plurk.utils import parse_time_validator


class Plurk(RespBase):
    """Data of a plurk.

    A plurk's data returned from different endpoint varies.
    The official doc does not describe the exact return value of each endpoint. If an optional
    field is absent in the data, it might be available through other endpoints or it might simply not available.
    """
    plurk_id: int
    content: str
    content_raw: str
    qualifier: str
    posted: datetime
    last_edited: Optional[datetime]
    owner_id: Optional[int]
    user_id: int
    response_count: int
    limited_to: Optional[Any]  # ?
    excluded: Optional[Any]  # ?
    lang: str
    is_unread: int
    no_comments: int
    replurked: bool
    replurker_id: Optional[int]
    replurkers: List[int]
    replurkers_count: int
    favorers: List[int]
    favorite: bool
    favorite_count: int
    anonymous: bool
    plurk_type: int
    coins: int
    id: Optional[int]
    responses_seen: int
    porn: bool
    publish_to_followers: bool
    with_poll: bool
    has_gift: bool
    responded: int
    mentioned: int
    bookmark: Optional[bool]
    qualifier_translated: Optional[str]
    replurkable: Optional[bool]

    _parse_last_edited = parse_time_validator('last_edited')
    _parse_posted = parse_time_validator('posted')


class NewPlurk(Plurk):
    """Plurk data returned from comet channel URL
    """
    type: Literal[ChannelDataEntryType.NEW_PLURK]
