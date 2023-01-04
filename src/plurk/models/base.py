from datetime import datetime
from typing import Any, Dict, List, Union

from pydantic import BaseModel, ValidationError

from plurk.exceptions import RespValidationError
from plurk.utils import format_as_plurk_time


def format_datetime_deep(obj: Union[Dict, List, int, str, bool, datetime, None]):
    if isinstance(obj, datetime):
        return format_as_plurk_time(obj)
    if isinstance(obj, list):
        return [format_datetime_deep(item) for item in obj]
    if isinstance(obj, dict):
        return {k: format_datetime_deep(v) for k, v in obj.items()}
    return obj


class RespBase(BaseModel):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
        except ValidationError as exc:
            raise RespValidationError(self.__class__.__name__) from exc

    def dict_original(self) -> Dict[str, Any]:
        """Return a dict representation of the UserData while restoring the original
        data like Plurk API date string format.
        """
        return format_datetime_deep(self.dict())  # type: ignore
