"""Quickstart example

Prerequiste:
1. Create a Plurk app at https://www.plurk.com/PlurkApp/create)
2. 

What this example script does:
1. Perform the OAuth 1.0 flow
    a. Get request token
    b. Get authorization URL
    c. Ask user to open authorization URL with browser, and take auth code as input
    d. Fetch user's access token with the request token and auth code

2. Call /APP/Users/me to get the current user's user data, and print some fields for demonstration
"""

from plurk import Client

APP_KEY = '<your-plurk-app-key>'
APP_SECRET = '<your-plurk-app-secret>'


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
