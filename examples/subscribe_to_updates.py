""" Subscribe to updates example

Prerequisites:
- Create a Plurk app at https://www.plurk.com/PlurkApp/create
- Obtain an access token and token secret for your bot user.
- Create a .env file with your APP_KEY, APP_SECRET, TOKEN, and TOKEN_SECRET.

What this example script does:
1.  Loads credentials from the .env file.
2.  Performs OAuth with pre-fetched tokens.
3.  Uses the helper function to run indefinitely and print all received updates.
"""

import os
import sys
from typing import cast

from dotenv import load_dotenv

from plurk import Client
from plurk.models import NewPlurk, NewResponse

load_dotenv()

APP_KEY = cast(str, os.getenv('APP_KEY'))
APP_SECRET = cast(str, os.getenv('APP_SECRET'))
TOKEN = cast(str, os.getenv('TOKEN'))
TOKEN_SECRET = cast(str, os.getenv('TOKEN_SECRET'))

if not all([APP_KEY, APP_SECRET, TOKEN, TOKEN_SECRET]):
    print('APP_KEY, APP_SECRET, TOKEN, and TOKEN_SECRET must be set in your .env file.', file=sys.stderr)
    sys.exit(1)


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
