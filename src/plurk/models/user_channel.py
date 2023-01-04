from typing import List, Optional, Union
from typing_extensions import Annotated

from pydantic import Field

from plurk.models.base import RespBase
from plurk.models.plurk import NewPlurk
from plurk.models.response import NewResponse


ChannelDataEntry = Annotated[Union[NewPlurk, NewResponse], Field(discriminator='type')]


class ChannelData(RespBase):
    """Data returned from comet channel URL
    """
    new_offset: int
    data: Optional[List[ChannelDataEntry]]


class UserChannel(RespBase):
    """Data returned by `APP/Realtime/getUserChannel` endpoint
    """
    channel_name: str
    comet_server: str
