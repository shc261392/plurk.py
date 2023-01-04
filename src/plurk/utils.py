
from enum import Enum
import json
import re
from datetime import datetime
from typing import Optional

from pydantic import validator

PLURK_DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'


def build_params(**kwargs):
    """Return a dict built from non-null kwargs.

    If a kwarg is an Enum, the value of enum will be used for building the params.
    Used for building query params or request body.
    """
    ret = {}
    for k, v in kwargs.items():
        if v is None:
            continue
        if isinstance(v, Enum):
            ret[k] = v.value
        else:
            ret[k] = v
    return ret


def format_as_plurk_time(dt: datetime):
    """Return a date string in the format the Plurk API's responses use.
    """
    return dt.strftime(PLURK_DATETIME_FORMAT)


def parse_plurk_time(date_string: Optional[str]):
    """Parse the date string used in Plurk API's responses into datetime object.

    The utility function exists because Plurk API does not use ISO8601 datetime format.
    """
    if not date_string:
        return None
    return datetime.strptime(date_string, PLURK_DATETIME_FORMAT)


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


def read_jsonp(jsonp_str: str):
    json_str_match = re.match('.*?({.*}).*', jsonp_str)
    if json_str_match:
        try:
            return json.loads(json_str_match.group(1))
        except json.decoder.JSONDecodeError:
            pass
    raise ValueError('Input is not a valid JSONP string')
