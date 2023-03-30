from typing import Any, Dict, List, Optional

from pydantic import parse_obj_as

from plurk.apis.base import BaseApi
from plurk.exceptions import validate_resp
from plurk.models import ActionResp, PublicUserData
from plurk.utils import build_params


class FriendsFans(BaseApi):
    def get_friends_by_offset(self, user_id: int, offset: Optional[int] = None, limit: int = 10):
        """Returns `user_id`'s friend list.

        User can toggle their friend list visibility in privacy settings. If the current user
        can't see the user's friend list, the result will be an empty list.
        """
        endpoint = f'{self.client.base_url}/APP/FriendsFans/getFriendsByOffset'
        params = build_params(user_id=user_id, offset=offset, limit=limit)
        resp = self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return parse_obj_as(List[PublicUserData], resp.json())

    def get_fans_by_offset(self, user_id: int, offset: Optional[int] = None, limit: int = 10):
        """Returns `user_id`'s fan list.

        User can toggle their fan list visibility in privacy settings. If the current user
        can't see the user's fan list, the result will be an empty list.
        """
        endpoint = f'{self.client.base_url}/APP/FriendsFans/getFansByOffset'
        params = build_params(user_id=user_id, offset=offset, limit=limit)
        resp = self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return parse_obj_as(List[PublicUserData], resp.json())

    def get_following_by_offset(self, offset: Optional[int] = None, limit: int = 10):
        """Returns current user's following list.
        """
        endpoint = f'{self.client.base_url}/APP/FriendsFans/getFollowingByOffset'
        params = build_params(offset=offset, limit=limit)
        resp = self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return parse_obj_as(List[PublicUserData], resp.json())

    def become_friend(self, friend_id: int):
        """Create a friend request to `friend_id`. User with `friend_id` has to accept a friendship.
        """
        endpoint = f'{self.client.base_url}/APP/FriendsFans/becomeFriend'
        payload = build_params(friend_id=friend_id)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def remove_as_friend(self, friend_id: int):
        """Remove friend with ID `friend_id`. `friend_id` won't be notified.
        """
        endpoint = f'{self.client.base_url}/APP/FriendsFans/removeAsFriend'
        payload = build_params(friend_id=friend_id)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def become_fan(self, fan_id: int):
        """Become fan of fan_id.
        """
        endpoint = f'{self.client.base_url}/APP/FriendsFans/becomeFan'
        payload = build_params(fan_id=fan_id)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def set_following(self, user_id: int, follow: bool):
        """Update following of user_id. A user can befriend someone, but can unfollow them.
        This request is also used to stop following someone as a fan.
        """
        endpoint = f'{self.client.base_url}/APP/FriendsFans/setFollowing'
        payload = build_params(user_id=user_id, follow=follow)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def remove_as_fan(self, user_id: int):
        """Stop being a fan of the target user.

        The function is shortcut using the setFollowing endpoint, not mapping to a standalone endpoint.
        """
        return self.set_following(user_id, follow=False)

    def get_completion(self) -> Dict[str, Dict[str, Any]]:
        """Returns a JSON object of the logged in users friends (nick name and full name).
        This information can be used to construct auto-completion for private plurking.
        Notice that a friend list can be big, depending on how many friends a user has,
        so this list should be lazy-loaded in your application.

        Example returning data:
        {
            '123': {
                'full_name': 'Plurk User',
                'nick_name': 'plurk',
                'avatar': 12345,
                'display_name': 'Plurker'
            }
        }

        where '123' is the user id.
        """
        endpoint = f'{self.client.base_url}/APP/FriendsFans/getCompletion'
        resp = self.client.http_client.get(endpoint)
        validate_resp(resp)
        return resp.json()
