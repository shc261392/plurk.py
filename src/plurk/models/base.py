from datetime import datetime

from pydantic import BaseModel

from plurk.utils import format_as_plurk_time


class ResponseBase(BaseModel):
    def dict_original(self):
        """Return a dict representation of the UserData while restoring the original
        data like Plurk API date string format.
        """
        ret = self.dict()
        for k, v in ret.items():
            if isinstance(v, datetime):
                ret[k] = format_as_plurk_time(v)
        return ret
