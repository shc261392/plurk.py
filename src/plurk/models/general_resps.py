from typing import Dict, Optional

from plurk.models.base import RespBase


class ActionResp(RespBase):
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
    - `/APP/Responses/responseDelete`
    """
    success_text: Optional[str]
    success: Optional[bool]
    results: Optional[Dict[str, Dict]]

    def is_successful(self):
        return self.success_text or self.success is not False
