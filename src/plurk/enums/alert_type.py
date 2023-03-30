from enum import Enum


class AlertType(str, Enum):
    FRIENDSHIP_REQUEST = 'friendship_request'
    FRIENDSHIP_PENDING = 'friendship_pending'
    NEW_FAN = 'new_fan'
    FRIENDSHIP_ACCEPTED = 'friendship_accepted'
    NEW_FRIEND = 'new_friend'
    PRIVATE_PLURK = 'private_plurk'
    PLURK_LIKED = 'plurk_liked'
    PLURK_REPLURKED = 'plurk_replurked'
    MENTIONED = 'mentioned'
    MY_RESPONDED = 'my_responded'
