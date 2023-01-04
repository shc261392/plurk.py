from typing import Dict, List, Optional

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


class TimelineActionResp(RespBase):
    """Resp of endpoints that performs an action and only return the success status:
    - `/APP/Timeline/plurkDelete`
    - `/APP/Timeline/toggleComments`
    - `/APP/Timeline/mutePlurks`
    - `/APP/Timeline/unmutePlurks`
    - `/APP/Timeline/favoritePlurks`
    - `/APP/Timeline/unfavoritePlurks`
    - `/APP/Timeline/replurk`
    - `/APP/Timeline/unreplurk`
    - `/APP/Timeline/markAsRead`
    - `/APP/Timeline/reportAbuse`
    """
    success_text: Optional[str]
    success: Optional[bool]
    results: Optional[Dict[str, Dict]]

    def is_successful(self):
        return self.success_text or self.success is not False


class UploadPictureResp(RespBase):
    """Resp of `/APP/Timeline/uploadPicture`
    """
    full: str
    thumbnail: str
