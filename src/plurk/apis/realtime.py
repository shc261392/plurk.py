import re
from typing import Optional

from plurk.apis.base import BaseApi
from plurk.exceptions import RespValidationError, validate_resp
from plurk.models import ChannelResp, NoDataChannelResp, UserChannel
from plurk.utils import read_jsonp


def update_new_offset(url: str, new_offset: Optional[int] = None):
    """Update the new_offset query param value in URL and return the new URL
    """
    if new_offset:
        url = re.sub(r'new_offset=-?\d+', f'new_offset={new_offset}', url)
    return url


class Realtime(BaseApi):
    def get_user_channel(self):
        """Returns the user channel info for the curren user.

        You'll get an URL from `/APP/Realtime/getUserChannel` and you do GET requests
        to this URL to get new data.
        Your request will sleep for about 50 seconds before returning a response if there
        is no new data added to your channel. You won't get notifications on responses that
        the logged in user adds, but you will get notifications for new plurks.

        The comet channel will return JSONP format response.
        Comet channel response example: `CometChannel.scriptCallback({"new_offset": 1});`
        """
        endpoint = f'{self.client.base_url}/APP/Realtime/getUserChannel'
        resp = self.client.http_client.get(endpoint)
        validate_resp(resp)
        return UserChannel(**resp.json())

    def get_channel_response(self, comet_channel_url: str, timeout: int = 120, new_offset: Optional[int] = None):
        """Read data from user channel.

        comet_channel_url can be retrieved by calling `get_user_channel()` method
        and access the `comet_channel` attribute.

        By default the request timeout is 120s. The official API doc states the
        request could be pending for about 50s before returning a response.
        """
        endpoint = update_new_offset(comet_channel_url, new_offset)
        resp = self.client.http_client.get(endpoint, timeout=timeout)
        validate_resp(resp)
        jsonp_resp = read_jsonp(resp.text)
        try:
            return ChannelResp(**jsonp_resp)
        except RespValidationError:
            return NoDataChannelResp(**jsonp_resp)
