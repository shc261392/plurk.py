"""Bot basic example

Most of the time, a Plurk bot app will be used together with a Plurk user
created for the app. That means the user who runs the script (the app owner)
also has full control over the user who allow the app to authenticate via OAuth.

In other words, in the most common scenario for a Plurk bot, the OAuth access token
can be obtained in advance (by using the client, or by Purk test console
https://www.plurk.com/OAuth/test)

The script is an example for using the plurk.py if you already have the bot
user's access token.

Prerequisites:
- Create a Plurk app at https://www.plurk.com/PlurkApp/create
- Obtain an access token and token secret for your bot user.
- Create a .env file with your APP_KEY, APP_SECRET, TOKEN, and TOKEN_SECRET.
"""

import os
import sys
from typing import cast

from dotenv import load_dotenv

from plurk import Client

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

    # Access Plurk API
    user_data = client.users.me()
    print('Display name: ', user_data.display_name)
    print('Plurks created: ', user_data.plurks_count)
