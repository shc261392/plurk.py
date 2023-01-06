""" Subscribe to updates example

Prerequiste:
- Create a Plurk app at https://www.plurk.com/PlurkApp/create)

What this example script does:
1. Perform OAuth with pre-fetched tokens.
2. Use the helper function to run indefintely and print all received updates.
"""

from plurk import Client
from plurk.models import NewPlurk, NewResponse

APP_KEY = '<your-plurk-app-key>'
APP_SECRET = '<your-plurk-app-secret>'
TOKEN = '<your-bot-user-token>'
TOKEN_SECRET = '<your-bot-user-token-secret>'


with Client(APP_KEY, APP_SECRET) as client:
    # Set app user's access token directly
    client.set_access_token(TOKEN, TOKEN_SECRET)

    print('Subscribed to timeline updates...')
    for channel_data in client.helpers.subscribe_to_user_channel():
        for entry in channel_data.data:
            if isinstance(entry, NewPlurk):
                print(f'New plurk detected. plurk_id: {entry.plurk_id}, content_raw: {entry.content_raw}')
            elif isinstance(entry, NewResponse):
                print(f'New response detected. plurk_id: {entry.plurk_id}')
