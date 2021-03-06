from __future__ import annotations

import pydantic
import datetime
import asyncio
import typing

from pydantic import BaseModel

from swagger_codegen.api.request import ApiRequest


def make_request(self, username: str = ..., password: str = ...,) -> str:
    """Logs user into the system"""
    m = ApiRequest(
        method="GET",
        path="/api/v3/user/login".format(),
        content_type=None,
        body=None,
        headers=self._only_provided({}),
        query_params=self._only_provided({"username": username, "password": password,}),
        cookies=self._only_provided({}),
    )
    return self.make_request(
        {"200": {"application/json": str, "application/xml": str,},}, m
    )
