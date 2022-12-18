# plurk.py
An unofficial library of interacting with Plurk API 2.0 for Python 3.7+.

![main](https://github.com/shc261392/plurk.py/actions/workflows/ci.yml/badge.svg?branch=main)

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
$ make install
$ make test
```

`make install` will automatically create a virtualenv in the current folder named `.venv`.

## TODOs

- Complete implementation for other endpoints
- Add async support
