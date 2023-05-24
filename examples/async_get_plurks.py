"""Quickstart example

Prerequiste:
- Create a Plurk app at https://www.plurk.com/PlurkApp/create)

What this example script does:
1. Perform the OAuth 1.0 flow
    a. Get request token
    b. Get authorization URL
    c. Ask user to open authorization URL with browser, and take auth code as input
    d. Fetch user's access token with the request token and auth code

2. Call /APP/Timeline/getPlurks to get 10 plurks on timeline

3. Call /APP/Responses/get asynchronously to get responses in each plurk

4. Print the results

Note that using hardcoded credentials is a bad practice.
The script here is only for demonstration purpose, do not use it without modification in production.
"""
import asyncio
from typing import List, cast

from plurk import AsyncClient
from plurk.models import Plurk, ResponsesGetResp

APP_KEY = '<your-plurk-app-key>'
APP_SECRET = '<your-plurk-app-secret>'


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
