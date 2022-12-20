from datetime import datetime

from pydantic import BaseModel, ValidationError

from plurk.exceptions import ResponseValidationError
from plurk.utils import format_as_plurk_time


class ResponseBase(BaseModel):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
        except ValidationError as exc:
            raise ResponseValidationError(self.__class__.__name__) from exc

    def dict_original(self):
        """Return a dict representation of the UserData while restoring the original
        data like Plurk API date string format.
        """
        ret = self.dict()
        for k, v in ret.items():
            if isinstance(v, datetime):
                ret[k] = format_as_plurk_time(v)
        return ret
