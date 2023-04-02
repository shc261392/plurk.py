from typing import List

from pydantic import parse_obj_as

from plurk.apis.base import BaseApi
from plurk.exceptions import validate_resp
from plurk.models import ActionResp, PublicUserData
from plurk.utils import build_params


class Cliques(BaseApi):
    def get_cliques(self) -> List[str]:
        r"""Return a list of clique names.
        """
        endpoint = f'{self.client.base_url}/APP/Cliques/getCliques'
        resp = self.client.http_client.get(endpoint)
        validate_resp(resp)
        return resp.json()

    def get_clique(self, clique_name):
        r"""Get users in a clique.
        """
        endpoint = f'{self.client.base_url}/APP/Cliques/getClique'
        params = build_params(clique_name=clique_name)
        resp = self.client.http_client.get(endpoint, params=params)
        validate_resp(resp)
        return parse_obj_as(List[PublicUserData], resp.json())

    def create_clique(self, clique_name: str):
        r"""Create a new clique.
        """
        endpoint = f'{self.client.base_url}/APP/Cliques/createClique'
        payload = build_params(clique_name=clique_name)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def rename_clique(self, clique_name: str, new_name: str):
        r"""Rename a clique.
        """
        endpoint = f'{self.client.base_url}/APP/Cliques/renameClique'
        payload = build_params(clique_name=clique_name, new_name=new_name)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def add(self, clique_name: str, user_id: int):
        r"""Add a user to the clique.
        """
        endpoint = f'{self.client.base_url}/APP/Cliques/add'
        payload = build_params(clique_name=clique_name, user_id=user_id)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())

    def remove(self, clique_name: str, user_id: int):
        r"""Add a user to the clique.
        """
        endpoint = f'{self.client.base_url}/APP/Cliques/remove'
        payload = build_params(clique_name=clique_name, user_id=user_id)
        resp = self.client.http_client.post(endpoint, json=payload)
        validate_resp(resp)
        return ActionResp(**resp.json())
