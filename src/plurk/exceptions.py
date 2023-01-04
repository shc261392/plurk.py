import json
import re

from httpx import HTTPStatusError, Response


class AuthenticationError(Exception):
    """API response with 401 or 403 status code"""


class BadRequestError(Exception):
    """API response with 400 status code"""


class ServerError(Exception):
    """API response with 50x status code"""


class RespValidationError(Exception):
    """API Response is not in the expected format
    """


class UnknownError(Exception):
    """API response with another non-succesfful status code"""


def extract_error_message(r: Response):
    """Normally the API returns a dict with 'error_text' key
    for detailed error message. However, under some circumstances
    (ex. the server fails to parse the request body)
    """
    try:
        msg = r.json()['error_text']
    except KeyError:
        # Response is JSON, but error_text key missing
        msg = r.text
    except json.decoder.JSONDecodeError:
        # Response is not JSON. Usually it's HTML body
        msg_match = re.search('<\\s*p[^>]*>(.*?)<\\s*/\\s*p>', r.text)  # look for <p>msg</p>
        if msg_match:
            msg = msg_match.group(0)
        else:
            msg = ''
    except Exception:
        msg = r.text
    return msg


def validate_resp(r: Response):
    try:
        r.raise_for_status()
    except HTTPStatusError as exc:
        exception_class = None
        extra_msg = ''
        if r.status_code in [401, 403]:
            exception_class = AuthenticationError
        elif r.status_code == 400:
            exception_class = BadRequestError
        elif r.status_code >= 500:
            exception_class = ServerError
        else:
            exception_class = UnknownError
        extra_msg = extract_error_message(r)
        raise exception_class(extra_msg) from exc
    return r
