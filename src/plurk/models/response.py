from datetime import datetime
from typing import Dict, List, Literal, Optional

from plurk.enums import ChannelDataEntryType, Language, Qualifier
from plurk.models.base import RespBase
from plurk.models.plurk import Plurk
from plurk.models.user_data import PublicUserData, SimpleUserData
from plurk.utils import parse_time_validator


class NewResponse(RespBase):
    """Part of data returned from comet channel URL
    """
    plurk_id: int
    plurk: Plurk
    user: Dict[str, SimpleUserData]
    type: Literal[ChannelDataEntryType.NEW_RESPONSE]


class Response(RespBase):
    """Data of a plurk response
    """
    coins: Optional[int]
    """How many plurk coins are gifted to the response.
    """
    content: str
    content_raw: str
    editability: int
    """Whether the response can be edited by the current user. The value is either 0 or 1.
    `0`: It can not be edited.
    `1`: It can be edited.
    """
    id: int
    """The response id.
    """
    lang: Language
    last_edited: Optional[datetime]
    plurk_id: int
    posted: datetime
    qualifier: Qualifier
    qualifier_translated: Optional[str]
    user_id: int
    with_random_emos: Optional[bool]

    _parse_last_edited = parse_time_validator('last_edited')
    _parse_posted = parse_time_validator('posted')


class ResponsesGetResp(RespBase):
    """Resp of `/APP/Responses/get`
    """
    friends: Dict[str, PublicUserData]
    response_count: int
    responses_seen: int
    responses: List[Response]
