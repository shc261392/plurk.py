from typing import List

from plurk.models.base import RespBase
from plurk.models.user_data import SimpleUserData


class GetBlocksResp(RespBase):
    """Resp of `/APP/Blocks/get`
    """
    total: int
    users: List[SimpleUserData]
