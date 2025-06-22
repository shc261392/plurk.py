# plurk.py

[![PyPI version](https://badge.fury.io/py/plurk.py.svg)](https://badge.fury.io/py/plurk.py)
[![Python versions](https://img.shields.io/pypi/pyversions/plurk.py.svg)](https://pypi.org/project/plurk.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/shc261392/plurk.py/actions/workflows/python-package.yml/badge.svg)](https://github.com/shc261392/plurk.py/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/shc261392/plurk.py/branch/main/graph/badge.svg)](https://codecov.io/gh/shc261392/plurk.py)

A modern Python library for the Plurk API 2.0, providing an easy-to-use interface for both synchronous and asynchronous interactions.

## Features

- Effortless Plurk API access with OAuth. ([Code example](https://github.com/shc261392/plurk.py/blob/main/examples/quickstart.py))
- Full support for both synchronous and asynchronous API calls.
- Complete coverage of all API endpoints listed in the official documentation.
- A convenient helper function for subscribing to timeline updates. ([Code example](https://github.com/shc261392/plurk.py/blob/main/examples/subscribe_to_updates.py))

## Requirements

- Python 3.8+

## Installation

```shell
pip3 install plurk.py
```

## Quickstart

Follow these steps to get started with **plurk.py**.

### 1. Obtain Plurk API Credentials

If you don't have a Plurk app, create one on the [App Sign Up](https.www.plurk.com/PlurkApp/create) page to get your app key and secret.

### 2. Set Up Environment Variables

Create a `.env` file in your project's root directory and add your Plurk app's key and secret:

```dotenv
APP_KEY=<your-plurk-app-key>
APP_SECRET=<your-plurk-app-secret>
```

A `.env.example` file is provided as a template.

### 3. Install Dependencies

Install the required libraries, including `python-dotenv` for managing environment variables:

```shell
pip3 install -r requirements.txt
```

### 4. Run the Example

The following example demonstrates how to authenticate and access the Plurk API using **plurk.py**:

```python
import os
from dotenv import load_dotenv
from plurk import Client

load_dotenv()

APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')


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

For an asynchronous example, check the [async example](https://github.com/shc261392/plurk.py/blob/main/examples/async_get_plurks.py).

## Development

```shell
git clone git@github.com:shc261392/plurk.py.git
cd plurk.py
make install
```

`make install` will create a virtual environment in the `.venv` folder.

To run the test suite:

```shell
make test
```

## Dependencies

**plurk.py** relies on these excellent libraries:

- [Authlib](https://github.com/lepture/authlib) for OAuth, using a [forked version](https://github.com/shc261392/authlib).
- [httpx](https://github.com/encode/httpx) for both synchronous and asynchronous HTTP requests.
- [pydantic](https://github.com/pydantic/pydantic) for data models with robust typing and validation.
- [python-dotenv](https://github.com/theskumar/python-dotenv) for managing environment variables.
