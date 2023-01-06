from typing import List, Union
from typing_extensions import Annotated

from pydantic import Field

from plurk.models.base import RespBase
from plurk.models.plurk import NewPlurk
from plurk.models.response import NewResponse


ChannelDataEntry = Annotated[Union[NewPlurk, NewResponse], Field(discriminator='type')]


class BaseChannelResp(RespBase):
    """Resp returned from comet channel URL
    """
    new_offset: int


class NoDataChannelResp(BaseChannelResp):
    """Resp returned from comet channel URL that indicates no updates
    """


class ChannelResp(BaseChannelResp):
    """Resp returned from comet channel URL that contains at least one data entry
    """
    data: List[ChannelDataEntry]


class UserChannel(RespBase):
    """Data returned by `APP/Realtime/getUserChannel` endpoint
    """
    channel_name: str
    comet_server: str
