"""Asynchronous quickstart example

Prerequisites:
- Create a Plurk app at https://www.plurk.com/PlurkApp/create
- Create a .env file with your APP_KEY and APP_SECRET

What this example script does:
1.  Loads credentials from the .env file.
2.  Performs the OAuth 1.0 flow asynchronously:
    a. Gets a request token.
    b. Generates an authorization URL.
    c. Prompts the user to authorize the app and provide the auth code.
    d. Fetches the user's access token.
3.  Calls `/APP/Timeline/getPlurks` to retrieve the 10 latest plurks.
4.  Asynchronously calls `/APP/Responses/get` to fetch responses for each plurk.
5.  Prints the results.
"""
import asyncio
import os
import sys
from typing import List, cast

from dotenv import load_dotenv

from plurk import AsyncClient
from plurk.models import Plurk, ResponsesGetResp

load_dotenv()

APP_KEY = cast(str, os.getenv('APP_KEY'))
APP_SECRET = cast(str, os.getenv('APP_SECRET'))

if not APP_KEY or not APP_SECRET:
    print('APP_KEY and APP_SECRET must be set in your .env file.', file=sys.stderr)
    sys.exit(1)


async def get_responses_list(client: AsyncClient, plurks: List[Plurk]):
    tasks = []
    for plurk in plurks:
        tasks.append(client.responses.get(plurk.plurk_id))
    responses_get_resps = await asyncio.gather(*tasks)
    responses_get_resps = cast(List[ResponsesGetResp], responses_get_resps)
    responses_list = [r.responses for r in responses_get_resps]
    return responses_list


async def main():
    async with AsyncClient(APP_KEY, APP_SECRET) as client:
        # Get app user's access token
        request_token = await client.get_request_token()
        auth_url = client.get_auth_url(request_token)
        print('Plurk OAuth authorization URL (open it with browser): ', auth_url)
        auth_code = input('Please input the authorization code retrieved from authorization URL: ')
        await client.fetch_access_token(request_token, auth_code)

        # Get 10 plurks and get their responses asynchronously
        get_plurks_resp = await client.timeline.get_plurks(limit=10)
        responses_list = await get_responses_list(client, get_plurks_resp.plurks)
        for plurk, responses in zip(get_plurks_resp.plurks, responses_list):
            print(f'[plurk_id:{plurk.plurk_id}]')
            for response in responses:
                print(f'    - [user_id:{response.user_id}]: {response.content_raw}')
            print('')


if __name__ == '__main__':
    asyncio.run(main())
