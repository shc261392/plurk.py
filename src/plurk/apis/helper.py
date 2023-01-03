from plurk.apis.base import BaseApi


class Helper(BaseApi):
    """The class represents the collection of helper methods build on
    existing Plurk APIs. It does not represent an API endpoint directly.
    """
    def subscribe_to_user_channel(self, include_empty_data=False):
        """Returns a generator that yields plurks posted to the user channel.

        The method uses the `/APP/Realtime/getUserChannel` endpoint to get the current users channel
        and yield received results.

        The generator will yield results indefinitely in a `while True:` loop.
        """
        user_channel = self.client.realtime.get_user_channel()
        new_offset = None
        while True:
            channel_resp = self.client.realtime.get_channel_response(
                user_channel.comet_server, timeout=120, new_offset=new_offset
            )
            new_offset = channel_resp.new_offset
            if channel_resp.data or include_empty_data:
                yield channel_resp
