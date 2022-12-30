from plurk.apis.base import BaseApi
from plurk.exceptions import validate_response
from plurk.models import UserChannel


class Realtime(BaseApi):
    def get_user_channel(self):
        """Returns data that's private for the current user.

        This can be used to construct a profile and render a timeline of the latest plurks.
        """
        endpoint = f'{self.client.base_url}/APP/Realtime/getUserChannel'
        resp = self.client.http_client.get(endpoint)
        validate_response(resp)
        return UserChannel(**resp.json())
