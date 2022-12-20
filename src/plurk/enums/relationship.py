from enum import Enum


class Relationship(str, Enum):
    NOT_SAYING = 'not_saying'
    SINGLE = 'single'
    MARRIED = 'married'
    DIVORCED = 'divorced'
    ENGAGED = 'engaged'
    IN_RELATIONSHIP = 'in_relationship'
    COMPLICATED = 'complicated'
    WIDOWED = 'widowed'
    UNSTABLE_RELATIONSHIP = 'unstable_relationship'
    OPEN_RELATIONSHIP = 'open_relationship'
