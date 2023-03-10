# plurk.py
An unofficial library of interacting with Plurk API 2.0 for Python 3.8+.

![main](https://github.com/shc261392/plurk.py/actions/workflows/ci.yml/badge.svg?branch=main)

## WIP

This is a WIP project. Currently available features:

- Access Plurk API with OAuth easily. See [example](https://github.com/shc261392/plurk.py/blob/main/examples/quickstart.py) for how to do it.
- All API endpoints under `/APP/Users`
- All API endpoints under `/APP/Profile`
- All API endpoints under `/APP/Realtime`
- All API endpoints under `/APP/Timeline`
- All API endpoints listed as OAuth utilities in official API doc.
- A helper function to subscribe to timeline updates easily. See [example](https://github.com/shc261392/plurk.py/blob/main/examples/quickstart.py) for how to do it.

To-do list:

- API endpoints under `/APP/Responses`
- API endpoints under `/APP/FriendsFans`
- API endpoints under `/APP/Alerts`
- API endpoints `/APP/PlurkSearch`
- API endpoints `/APP/UserSearch`
- API endpoints under `/APP/Emoticons`
- API endpoints under `/APP/Blocks`
- API endpoints under `/APP/Cliques`

## Requirement

- Python 3.8+

Tests will fail when using Python 3.7 since the package used in testing requires Python 3.8+.
The package might still works for Python 3.7, though it is not recommended to use the package with Python 3.7

## Installation

```shell
$ pip3 install git+https://github.com/shc261392/plurk.py
```

## Quickstart

See the example below for how to use **plurk.py**.

Replace the value of `APP_KEY` and `APP_SECRET` with your Plurk app's key and secret.
If you haven't create a Plurk app yet, visit the [App Sign Up](https://www.plurk.com/PlurkApp/create) page
to register your app and retrieve your app key and app secret.


```python
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
```

## Development

```shell
$ git clone git@github.com:shc261392/plurk.py.git
$ cd plurk.py
$ make test
$ make install
```

`make install` will automatically create a virtualenv in the current folder named `.venv`.

## Dependencies

**plurk.py** depends on the following brilliant works:
- [Authlib](https://github.com/lepture/authlib) for OAuth. The project uses the [forked version](https://github.com/shc261392/authlib).
- [httpx](https://github.com/encode/httpx), an solid library for both sync and async HTTP requests
- [pydantic](https://github.com/pydantic/pydantic) for building data models with great typing and validation support.

## TODOs

- Complete implementation for other endpoints
- Add async support
