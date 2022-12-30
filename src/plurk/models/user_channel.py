from plurk.models.base import ResponseBase


class UserChannel(ResponseBase):
    """Data returned by `APP/Realtime/getUserChannel` endpoint
    """
    channel_name: str
    comet_server: str
