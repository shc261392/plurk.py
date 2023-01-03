from typing import Annotated, List, Optional, Union

from pydantic import Field

from plurk.models.base import ResponseBase
from plurk.models.plurk import NewPlurk
from plurk.models.response import NewResponse


ChannelDataEntry = Annotated[Union[NewPlurk, NewResponse], Field(discriminator='type')]


class ChannelData(ResponseBase):
    """Data returned from comet channel URL
    """
    new_offset: int
    data: Optional[List[ChannelDataEntry]]


class UserChannel(ResponseBase):
    """Data returned by `APP/Realtime/getUserChannel` endpoint
    """
    channel_name: str
    comet_server: str
