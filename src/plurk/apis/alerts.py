from typing import List, Union

from pydantic import Field, parse_obj_as
from typing_extensions import Annotated

from plurk.apis.base import BaseApi
from plurk.exceptions import validate_resp
from plurk.models import (ActionResp, FriendshipAcceptedAlert,
                          FriendshipPendingAlert, FriendshipRequestAlert,
                          MentionedAlert, MyRespondedAlert, NewFanAlert,
                          NewFriendAlert, PlurkLikedAlert, PlurkReplurkedAlert,
                          PrivatePlurkAlert)
from plurk.utils import build_params

Alert = Annotated[
    Union[
        FriendshipAcceptedAlert, FriendshipPendingAlert, FriendshipRequestAlert,
        MentionedAlert, MyRespondedAlert, NewFanAlert, NewFriendAlert, PlurkLikedAlert,
        PlurkReplurkedAlert, PrivatePlurkAlert
    ],
    Field(discriminator='type')
]


class Alerts(BaseApi):
    def get_active(self):
        """Return a JSON list of current active alerts.
        """
        endpoint = f'{self.client.base_url}/APP/Alerts/getActive'
        resp = self.client.http_client.get(endpoint)
        validate_resp(resp)
        return parse_obj_as(List[Alert], resp.json())

    def get_history(self):
        """Return a JSON list of past 30 alerts.
        """
        endpoint = f'{self.client.base_url}/APP/Alerts/getHistory'
        resp = self.client.http_client.get(endpoint)
        validate_resp(resp)
        return parse_obj_as(List[Alert], resp.json())

    def add_as_fan(self, user_id: int):
        """Accept user_id as fan.
        """
        endpoint = f'{self.client.base_url}/APP/Alerts/addAsFan'
        payload = build_params(user_id=user_id)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def add_all_as_fan(self):
        """Accept all friendship requests as fans.
        """
        endpoint = f'{self.client.base_url}/APP/Alerts/addAllAsFan'
        resp = self.client.http_client.post(endpoint)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def add_as_friend(self, user_id: int):
        """Accept user_id as friend.
        """
        endpoint = f'{self.client.base_url}/APP/Alerts/addAsFriend'
        payload = build_params(user_id=user_id)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def add_all_as_friends(self):
        """Accept all friendship requests as friends.
        """
        endpoint = f'{self.client.base_url}/APP/Alerts/addAllAsFriends'
        resp = self.client.http_client.post(endpoint)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def deny_friendship(self, user_id: int):
        """Accept user_id as friend.
        """
        endpoint = f'{self.client.base_url}/APP/Alerts/denyFriendship'
        payload = build_params(user_id=user_id)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def remove_notification(self, user_id: int):
        """Accept user_id as friend.
        """
        endpoint = f'{self.client.base_url}/APP/Alerts/removeNotification'
        payload = build_params(user_id=user_id)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())
