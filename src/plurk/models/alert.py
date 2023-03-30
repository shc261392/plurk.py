from datetime import datetime
from typing import Literal

from plurk.enums import AlertType
from plurk.models.base import RespBase
from plurk.models.user_data import PublicUserData
from plurk.utils import parse_time_validator


class AlertBase(RespBase):
    """
    General data structures
    The data returned by getActive and getHistory can be of following nature:
    Friendship request: (requires action from the user)
    {"type": "friendship_request", "from_user": {"nick_name": ...}, "posted": ...}

    Friendship pending: (requires action from the user)
    {"type": "friendship_pending", "to_user": {"nick_name": ...}, "posted": ...}

    """
    type: AlertType
    posted: datetime

    _parse_posted = parse_time_validator('posted')


class FriendshipRequestAlert(AlertBase):
    type: Literal[AlertType.FRIENDSHIP_REQUEST]
    from_user: PublicUserData


class FriendshipPendingAlert(AlertBase):
    type: Literal[AlertType.FRIENDSHIP_PENDING]
    to_user: PublicUserData


class NewFanAlert(AlertBase):
    type: Literal[AlertType.NEW_FAN]
    new_fan: PublicUserData


class FriendshipAcceptedAlert(AlertBase):
    type: Literal[AlertType.FRIENDSHIP_ACCEPTED]
    friend_info: PublicUserData


class NewFriendAlert(AlertBase):
    type: Literal[AlertType.NEW_FRIEND]
    new_friend: PublicUserData


class PrivatePlurkAlert(AlertBase):
    type: Literal[AlertType.PRIVATE_PLURK]
    owner: PublicUserData
    plurk_id: int


class PlurkLikedAlert(AlertBase):
    type: Literal[AlertType.PLURK_LIKED]
    from_user: PublicUserData
    plurk_id: int
    num_others: int


class PlurkReplurkedAlert(AlertBase):
    type: Literal[AlertType.PLURK_REPLURKED]
    from_user: PublicUserData
    plurk_id: int
    num_others: int


class MentionedAlert(AlertBase):
    type: Literal[AlertType.MENTIONED]
    from_user: PublicUserData
    plurk_id: int
    num_others: int
    response_id: int


class MyRespondedAlert(AlertBase):
    type: Literal[AlertType.MY_RESPONDED]
    from_user: PublicUserData
    plurk_id: int
    num_others: int
    response_id: int
