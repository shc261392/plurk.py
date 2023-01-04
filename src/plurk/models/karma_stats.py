from datetime import datetime
from typing import List

from plurk.models.base import RespBase


class KarmaStats(RespBase):
    """Data returned by `/APP/Users/getKarmaStats` endpoint
    """
    current_karma: float
    karma_trend: List[str]
    karma_graph: str
    karma_fall_reason: str

    def karma_trend_to_tuples(self):
        """The raw karma_trend data is formatted as '{unixtimestamp}-{karma_value}'.
        The helper function returns a list of tuples based on raw data as
        datetime and karma-value tuples.
        """
        return [
            (datetime.fromtimestamp(int(i.split('-')[0])), float(i.split('-')[1]))
            for i in self.karma_trend
        ]
