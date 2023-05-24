# plurk.py
An modern library of interacting with Plurk API 2.0 for Python 3.8+.

![main](https://github.com/shc261392/plurk.py/actions/workflows/ci.yml/badge.svg?branch=main)

## Features

- Access Plurk API with OAuth easily. ([Code example](https://github.com/shc261392/plurk.py/blob/main/examples/quickstart.py))
- Full sync and async API call support.
- Support all API endpoints listed in the official API doc.
- A helper function to subscribe to timeline updates easily. ([Code example](https://github.com/shc261392/plurk.py/blob/main/examples/subscribe_to_updates.py))


## Requirement

- Python 3.8+

Testing dependencies requires Python 3.8+. The package might still works for Python 3.7 though it is not recommended.

## Installation

```shell
$ pip3 install plurk.py
```

## Quickstart

See the example below for how to use **plurk.py**.

Replace the value of `APP_KEY` and `APP_SECRET` with your Plurk app's key and secret.
If you haven't create a Plurk app yet, visit the [App Sign Up](https://www.plurk.com/PlurkApp/create) page
to register your app and retrieve your app key and app secret.

Note that using hardcoded credentials is a bad practice. The script here is only for demonstration purpose, do not use it without modification in production.


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

For async example, check [here](https://github.com/shc261392/plurk.py/blob/main/examples/async_get_plurks.py).

## Development

```shell
$ git clone git@github.com:shc261392/plurk.py.git
$ cd plurk.py
$ make test
$ make install
```

`make install` will automatically create a virtualenv in the current folder named `.venv`.

To run test suite:

```shell
$ make test
```

## Dependencies

**plurk.py** depends on the following brilliant works:
- [Authlib](https://github.com/lepture/authlib) for OAuth. The project uses the [forked version](https://github.com/shc261392/authlib).
- [httpx](https://github.com/encode/httpx), a solid library for both sync and async HTTP requests
- [pydantic](https://github.com/pydantic/pydantic) for building data models with great typing and validation support.
