from enum import Enum


class AbuseCategory(str, Enum):
    PORN = 'porn'
    SPAM = 'spam'
    PRIVACY = 'privacy'
    VIOLENCE = 'violence'
    OTHERS = 'others'
