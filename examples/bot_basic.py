"""Bot basic example

Most of the time, a Plurk bot app will be used together with a Plurk user
created for the app. That means the user who runs the script (the app owner)
also has full control over the user who allow the app to authenticate via OAuth.

In other words, in the most common scenario for a Plurk bot, the OAuth access token
can be obtained in advance (by using the client, or by Purk test console
https://www.plurk.com/OAuth/test)

The script is an example for using the plurk.py if you already have the bot
user's access token.

Note that using hardcoded credentials is a bad practice.
The script here is only for demonstration purpose, do not use it without modification in production.
"""

from plurk import Client

APP_KEY = '<your-plurk-app-key>'
APP_SECRET = '<your-plurk-app-secret>'
TOKEN = '<your-bot-user-token>'
TOKEN_SECRET = '<your-bot-user-token-secret>'


with Client(APP_KEY, APP_SECRET) as client:
    # Set app user's access token directly
    client.set_access_token(TOKEN, TOKEN_SECRET)

    # Access Plurk API
    user_data = client.users.me()
    print('Display name: ', user_data.display_name)
    print('Plurks created: ', user_data.plurks_count)
