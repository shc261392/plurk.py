from datetime import datetime
from typing import BinaryIO, Optional, Union

from plurk.apis.base import BaseApi
from plurk.exceptions import validate_resp
from plurk.models.karma_stats import KarmaStats
from plurk.models.user_data import Privacy, UpdateAvatarResp, UserData


class Users(BaseApi):
    def me(self):
        """Returns information about current user.
        """
        endpoint = f'{self.client.base_url}/APP/Users/me'
        resp = self.client.http_client.get(endpoint)
        validate_resp(resp)
        return UserData(**resp.json())

    def update(
        self,
        full_name: Optional[str] = None,
        email: Optional[str] = None,
        display_name: Optional[str] = None,
        privacy: Optional[Privacy] = None,
        date_of_birth: Optional[Union[str, datetime]] = None,
    ):
        """TODO: Question sent to official on 2022/12/17
        wait for official response to solve error
        'only verified third party app can update user info'
        """
        endpoint = f'{self.client.base_url}/APP/Users/update'
        payload = {
            'full_name': full_name,
            'email': email,
            'display_name': display_name,
            'privacy': privacy,
            'date_of_birth': date_of_birth,
        }
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return UserData(**resp.json())

    def update_avatar(self, profile_image: Union[str, BinaryIO]):
        """Update a user's profile picture.

        The picture will be scaled down to 3 versions:
        big, medium and small. The optimal size of `profile_image`
        should be 195x195 pixels.
        """
        endpoint = f'{self.client.base_url}/APP/Users/updateAvatar'
        if isinstance(profile_image, str):
            with open(profile_image, 'rb') as file_object:
                resp = self.client.http_client.post(
                    endpoint, files={'profile_image': ('profile_image', file_object)}
                )
        else:
            resp = self.client.http_client.post(
                endpoint, files={'profile_image': ('profile_image', profile_image)}
            )
        # filename must be included in form-data, otherwise the request will fail.
        # arbitrary filename works, no need to have correct file ext.

        validate_resp(resp)
        return UpdateAvatarResp(**resp.json())

    def get_karma_stats(self):
        """Returns info about current user's karma, including current karma, karma growth,
        karma graph and the latest reason why the karma has dropped.
        """
        endpoint = f'{self.client.base_url}/APP/Users/getKarmaStats'
        resp = self.client.http_client.get(endpoint)
        validate_resp(resp)
        return KarmaStats(**resp.json())
