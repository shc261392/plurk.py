from datetime import datetime
from typing import Any, List, Optional

from plurk.models.base import ResponseBase
from plurk.utils import parse_time_validator


class Plurk(ResponseBase):
    """Data of a plurk
    """
    anonymous: bool
    bookmark: bool
    coins: int
    content: str
    content_raw: str
    excluded: Optional[Any]  # ?
    favorers: List[int]
    favorite: bool
    favorite_count: int
    has_gift: bool
    is_unread: int
    lang: str
    last_edited: Optional[datetime]
    limited_to: Optional[Any]  # ?
    mentioned: int
    no_comments: int
    owner_id: int
    plurk_id: int
    plurk_type: int
    porn: bool
    posted: datetime
    publish_to_followers: bool
    qualifier: str
    qualifier_translated: str
    replurkable: bool
    replurked: bool
    replurker_id: Optional[int]
    replurkers: List[int]
    replurkers_count: int
    responded: int
    response_count: int
    responses_seen: int
    user_id: int
    with_poll: bool

    _parse_last_edited = parse_time_validator('last_edited')
    _parse_posted = parse_time_validator('posted')
