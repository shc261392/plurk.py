"""Quickstart example

Prerequisites:
- Create a Plurk app at https://www.plurk.com/PlurkApp/create
- Create a .env file with your APP_KEY and APP_SECRET

What this example script does:
1.  Loads credentials from the .env file.
2.  Performs the OAuth 1.0 flow:
    a. Gets a request token.
    b. Generates an authorization URL.
    c. Prompts the user to authorize the app and provide the auth code.
    d. Fetches the user's access token.
3.  Calls /APP/Users/me to get the current user's data and prints some fields for demonstration.
"""

import os
import sys
from typing import cast

from dotenv import load_dotenv

from plurk import Client

load_dotenv()

APP_KEY = cast(str, os.getenv('APP_KEY'))
APP_SECRET = cast(str, os.getenv('APP_SECRET'))

if not APP_KEY or not APP_SECRET:
    print('APP_KEY and APP_SECRET must be set in your .env file.', file=sys.stderr)
    sys.exit(1)


with Client(APP_KEY, APP_SECRET) as client:
    # Get app user's access token
    request_token = client.get_request_token()
    auth_url = client.get_auth_url(request_token)
    print('Plurk OAuth authorization URL (open it with browser): ', auth_url)
    auth_code = input('Please input the authorization code retrieved from authorization URL: ')
    client.fetch_access_token(request_token, auth_code)

    # Access Plurk API
    user_data = client.users.me()
    print('Display name: ', user_data.display_name)
    print('Plurks created: ', user_data.plurks_count)
