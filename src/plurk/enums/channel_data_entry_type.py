from enum import Enum


class ChannelDataEntryType(str, Enum):
    NEW_PLURK = 'new_plurk'
    NEW_RESPONSE = 'new_response'
