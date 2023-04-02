from typing import Dict, List

from plurk.models.base import RespBase
from plurk.models.plurk import Plurk
from plurk.models.user_data import SimpleUserData


class PlurkSearchResp(RespBase):
    """Resp of `/APP/PlurkSearch/search`
    """
    plurks: List[Plurk]
    users: Dict[str, SimpleUserData]


class UserSearchResp(RespBase):
    """Resp of `/APP/UserSearch/search`
    """
    counts: int
    users: List[SimpleUserData]
