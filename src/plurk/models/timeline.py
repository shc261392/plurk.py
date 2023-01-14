from typing import Dict, List

from plurk.models.base import RespBase
from plurk.models.plurk import Plurk
from plurk.models.user_data import SimpleUserData


class GetPlurkResp(RespBase):
    """Resp of `/APP/Timeline/getPlurk`
    """
    plurk: Plurk
    user: SimpleUserData
    plurk_users: Dict[str, SimpleUserData]


class GetPlurksResp(RespBase):
    """Resp of
    - `/APP/Timeline/getPlurks`
    - `/APP/Timeline/getUnreadPlurks`
    - `/APP/Timeline/getPublicPlurks`
    """
    plurks: List[Plurk]
    plurk_users: Dict[str, SimpleUserData]


class UploadPictureResp(RespBase):
    """Resp of `/APP/Timeline/uploadPicture`
    """
    full: str
    thumbnail: str
