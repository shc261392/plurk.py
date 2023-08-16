from datetime import datetime
from typing import BinaryIO, List, Optional, Union

from plurk.async_apis.base import BaseApi
from plurk.enums import AbuseCategory, Filter, Language, Qualifier
from plurk.exceptions import validate_resp
from plurk.models import (ActionResp, GetPlurkResp, GetPlurksResp, Plurk,
                          UploadPictureResp)
from plurk.utils import build_params


class Timeline(BaseApi):
    async def get_plurk(self, plurk_id: int, favorers_detail=False, limited_detail=False, replurkers_detail=False):
        """Return a plurk by its plurk_id.

        Note: the response schema described in offical API doc is incorrect. See `GetPlurkResp` model
        for the actual data schema.

        Args:
            plurk_id: the unique id of a plurk.
            favorers_detail: if true, detailed users information about all favorers of this plurk will be
            included into "plurk_users".
            limited_tail: if true, detailed users information about recepients of this plurk will be included
            into "plurk_users" (if this plurk is private).
            replurkers_detail: if true, detailed users information about all replurkers of this plurk will be
            included into "plurk_users".
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/getPlurk'
        params = build_params(
            plurk_id=plurk_id,
            favorers_detail=favorers_detail,
            limited_detail=limited_detail,
            replurkers_detail=replurkers_detail,
        )
        resp = await self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return GetPlurkResp(**resp.json())

    async def get_plurks(
        self,
        offset: Optional[Union[str, datetime]] = None,
        limit: int = 20,
        filter: Optional[Filter] = None,  # pylint: disable=redefined-builtin
        favorers_detail=False,
        limited_detail=False,
        replurkers_detail=False,
    ):
        """Return plurks on timeline.

        Args:
            offset: return plurks older than offset, formatted as `YYYY-mm-DDTHH:MM:SS`. The function can also
                accept a datetime object and convert it automatically to the format for the API.
            limit: how many plurks should be returned. Default: `20`.
            filter: can be `my`, `responded`, `private`, `favorite`, `replurked` or `mentioned`; `mentioned` is only
                available for users with `user.premium = true`.
            favorers_detail: If true, detailed users information about all favorers of this plurk will be included into
                "plurk_users".
            limited_tail: If true, detailed users information about recepients of this plurk will be included into
                "plurk_users" (if this plurk is private).
            replurkers_detail: If true, detailed users information about all replurkers of this plurk will be included
                into "plurk_users".
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/getPlurks'
        if isinstance(offset, datetime):
            offset = offset.strftime('%Y-%m-%dT%H:%M:%S')
        params = build_params(
            offset=offset,
            limit=limit,
            filter=filter,
            favorers_detail=favorers_detail,
            limited_detail=limited_detail,
            replurkers_detail=replurkers_detail,
        )
        resp = await self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return GetPlurksResp(**resp.json())

    async def get_unread_plurks(
        self,
        offset: Optional[Union[str, datetime]] = None,
        limit: int = 20,
        filter: Optional[Filter] = None,  # pylint: disable=redefined-builtin
        favorers_detail=False,
        limited_detail=False,
        replurkers_detail=False,
    ):
        """Return unread plurks on timeline.

        Args:
            offset: return plurks older than offset, formatted as `YYYY-mm-DDTHH:MM:SS`. The function can also
                accept a datetime object and convert it automatically to the format for the API.
            limit: how many plurks should be returned. Default: `20`.
            filter: can be `my`, `responded`, `private`, `favorite`, `replurked` or `mentioned`; `mentioned` is only
                available for users with `user.premium = true`.
            favorers_detail: If true, detailed users information about all favorers of this plurk will be included into
                "plurk_users".
            limited_tail: If true, detailed users information about recepients of this plurk will be included into
                "plurk_users" (if this plurk is private).
            replurkers_detail: If true, detailed users information about all replurkers of this plurk will be included
                into "plurk_users".
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/getUnreadPlurks'
        if isinstance(offset, datetime):
            offset = offset.strftime('%Y-%m-%dT%H:%M:%S')
        params = build_params(
            offset=offset,
            limit=limit,
            filter=filter,
            favorers_detail=favorers_detail,
            limited_detail=limited_detail,
            replurkers_detail=replurkers_detail,
        )
        resp = await self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return GetPlurksResp(**resp.json())

    async def get_public_plurks(
        self,
        user_id: Union[int, str],
        offset: Optional[Union[str, datetime]] = None,
        limit: int = 20,
        filter: Optional[Filter] = None,  # pylint: disable=redefined-builtin
        favorers_detail=False,
        limited_detail=False,
        replurkers_detail=False,
    ):
        """Return public plurks of a specific user on timeline.

        Args:
            user_id: the user_id of the public plurks owner to get, can be the unique user_id (int) or nick_name (str)
            offset: return plurks older than offset, formatted as `YYYY-mm-DDTHH:MM:SS`. The function can also
                accept a datetime object and convert it automatically to the format for the API.
            limit: how many plurks should be returned. Default: `20`.
            filter: can be `my`, `responded`, `private`, `favorite`, `replurked` or `mentioned`; `mentioned` is only
                available for users with `user.premium = true`.
            favorers_detail: If true, detailed users information about all favorers of this plurk will be included into
                "plurk_users".
            limited_tail: If true, detailed users information about recepients of this plurk will be included into
                "plurk_users" (if this plurk is private).
            replurkers_detail: If true, detailed users information about all replurkers of this plurk will be included
                into "plurk_users".
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/getPublicPlurks'
        if isinstance(offset, datetime):
            offset = offset.strftime('%Y-%m-%dT%H:%M:%S')
        params = build_params(
            user_id=user_id,
            offset=offset,
            limit=limit,
            filter=filter,
            favorers_detail=favorers_detail,
            limited_detail=limited_detail,
            replurkers_detail=replurkers_detail,
        )
        resp = await self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return GetPlurksResp(**resp.json())

    async def plurk_add(
        self,
        content: str,
        qualifier: Qualifier = Qualifier.EMPTY,
        limited_to: Optional[List[int]] = None,
        no_comments: Optional[int] = None,
        lang: Optional[Language] = None,
    ):
        """Add a new plurk.

        Args:
            content: the content of the plurk.
            qualifier: the qualifier of the plurk.
            limited_to: a list of user_id. if provided, the plurk will be limited to the list of users.
            no_comments: set to 1 to disable all responses, set to 2 to restrict responses to friend-only.
            lang: the plurk's language. The qualifier will be displayed in the specified language.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/plurkAdd'
        payload = build_params(
            content=content,
            qualifier=qualifier,
            limited_to=str(limited_to),  # API endpoint expects this argument to be stringified
            no_comments=no_comments,
            lang=lang,
        )
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return Plurk(**resp.json())

    async def plurk_delete(self, plurk_id: int):
        """Delete an existing plurk.

        WARNING: the endpoint always returns a `success_text='ok'` response, even when providing a plurk_id
        from a plurk the current user can't delete or already deleted.
        To ensure the plurk is successfully deleted, call get_plurk(plurk_id) and catch the BadRequestError.

        Args:
            plurk_id: the unique id of the plurk.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/plurkDelete'
        payload = build_params(plurk_id=plurk_id)
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    async def plurk_edit(self, plurk_id: int, content: str, limited_to: Optional[List[int]] = None):
        """"Edit an existing plurk.

        Args:
            plurk_id: the unique id of the plurk.
            content: the new content of the plurk.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/plurkEdit'
        payload = build_params(plurk_id=plurk_id, content=content, limited_to=str(limited_to))
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return Plurk(**resp.json())

    async def toggle_comments(self, plurk_id: int, no_comments: int):
        """Edit a plurk's no_comments value.

        Possbile values:
        - `0`: everyone can comment (default)
        - `1`: no one can comment
        - `2`: only friends can comment
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/toggleComments'
        payload = build_params(plurk_id=plurk_id, no_comments=no_comments)
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    async def mute_plurks(self, ids: List[int]):
        """Mute plurks.

        Effectively set all plurks' `is_unread` to `2`.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/mutePlurks'
        payload = build_params(ids=str(ids))
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    async def unmute_plurks(self, ids: List[int]):
        """Unmute plurks.

        Effectively set all plurks `is_unread` back to `0` or `1`, based on what the original value is.
        Plurk seems to have internally stored the original `is_unread` value before a plurk is muted.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/unmutePlurks'
        payload = build_params(ids=str(ids))
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    async def favorite_plurks(self, ids: List[int]):
        """Favorite plurks.

        Effectively set all plurks' `favorite` to `True`.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/favoritePlurks'
        payload = build_params(ids=str(ids))
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    async def unfavorite_plurks(self, ids: List[int]):
        """Unfavorite plurks.

        Effectively set all plurks' `favorite` to `True`.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/unfavoritePlurks'
        payload = build_params(ids=str(ids))
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    async def replurk(self, ids: List[int]):
        """Replurk plurks.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/replurk'
        payload = build_params(ids=str(ids))
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    async def unreplurk(self, ids: List[int]):
        """Unreplurk plurks
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/unreplurk'
        payload = build_params(ids=str(ids))
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    async def mark_as_read(self, ids: List[int], note_position: Optional[bool] = None):
        """Mark plurks as read.

        Effectively set all plurks' `is_unread` to `0`.
        Note that Plurk does not provide any API to undo this action.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/markAsRead'
        payload = build_params(ids=str(ids), note_position=note_position)
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    async def upload_picture(self, image: Union[str, BinaryIO]):
        """Upload an image to Plurk site and get a Plurk CDN image link.

        The provided file must be a valid image, otherwise it will be rejected.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/uploadPicture'
        if isinstance(image, str):
            with open(image, 'rb') as file_object:
                resp = await self.client.http_client.post(
                    endpoint, files={'image': ('image', file_object)}
                )
        else:
            resp = await self.client.http_client.post(
                endpoint, files={'image': ('image', image)}
            )
        validate_resp(resp)
        return UploadPictureResp(**resp.json())

    async def report_abuse(self, plurk_id: int, category: AbuseCategory):
        """Report a plurk as abuse.
        """
        endpoint = f'{self.client.base_url}/APP/Timeline/reportAbuse'
        payload = build_params(plurk_id=plurk_id, category=category)
        resp = await self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())
