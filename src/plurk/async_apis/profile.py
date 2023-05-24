from plurk.async_apis.base import BaseApi
from plurk.exceptions import validate_resp
from plurk.models.profile import OwnProfile, PublicProfile


class Profile(BaseApi):
    async def get_own_profile(self):
        """Returns data that's private for the current user.

        This can be used to construct a profile and render a timeline of the latest plurks.
        """
        endpoint = f'{self.client.base_url}/APP/Profile/getOwnProfile'
        resp = await self.client.http_client.get(endpoint)
        validate_resp(resp)
        return OwnProfile(**resp.json())

    async def get_public_profile(self):
        """Fetches public information such as a user's public plurks and basic information.

        Fetches also if the current user is following the user, are friends with or is a fan.

        WARNING: The API is currently unavailable as the endpoint returns 404 status code.
        """
        endpoint = f'{self.client.base_url}/APP/Users/getPublicProfile'
        resp = await self.client.http_client.get(endpoint)
        validate_resp(resp)
        return PublicProfile(**resp.json())
