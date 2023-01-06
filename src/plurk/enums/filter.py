from enum import Enum


class Filter(str, Enum):
    """Filter is a optional parameter for some endpoints that returns multiple plurks.
    Possible values:
    - `my`
    - `responded`
    - `private`
    - `favorite`
    - `replurked`
    - `mentioned` (only available to premium users)
    """
    MY = 'my'
    RESPONSED = 'responded'
    PRIVATE = 'private'
    FAVORITE = 'favorite'
    REPLURKED = 'replurked'
    MENTIONED = 'mentioned'
