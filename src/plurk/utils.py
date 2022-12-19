from datetime import datetime
from typing import Union

from pydantic import validator

PLURK_DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'


def parse_plurk_time(date_string: str):
    """Parse the date string used in Plurk API's responses into datetime object.

    The utility function exists because Plurk API does not use ISO8601 datetime format.
    """
    return datetime.strptime(date_string, PLURK_DATETIME_FORMAT)


def format_as_plurk_time(dt: datetime):
    """Return a date string in the format the Plurk API's responses use.
    """
    return dt.strftime(PLURK_DATETIME_FORMAT)


def parse_time_validator(field: str):
    """Used for Pydantic models to parse datetime fields before the other validators.

    Setting up the validators to avoid 'invalid datetime format' when initializing a
    model with datetime fields from Plurk API's response data.

    Usage example:

    class UserData(BaseModel):

        join_date: datetime

        _parse_join_date = parse_time_validator('join_date')
    """
    return validator(field, pre=True, allow_reuse=True)(parse_plurk_time)
