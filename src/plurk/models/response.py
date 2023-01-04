from typing import Dict, Literal

from plurk.enums import ChannelDataEntryType
from plurk.models.base import RespBase
from plurk.models.plurk import Plurk
from plurk.models.user_data import SimpleUserData


class NewResponse(RespBase):
    """Response data returned from comet channel URL
    """
    plurk_id: int
    plurk: Plurk
    user: Dict[str, SimpleUserData]
    type: Literal[ChannelDataEntryType.NEW_RESPONSE]
