from enum import Enum


class Privacy(str, Enum):
    WORLD = 'world'
    ONLY_FRIENDS = 'only_friends'
