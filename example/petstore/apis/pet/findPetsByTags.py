from __future__ import annotations

import pydantic
import datetime
import asyncio
import typing

from pydantic import BaseModel

from swagger_codegen.api.request import ApiRequest


class Tag(BaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None


class Category(BaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None


class Pet(BaseModel):
    category: typing.Optional[Category] = None
    id: typing.Optional[int] = None
    name: str
    photoUrls: typing.List[str]
    status: typing.Optional[str] = None
    tags: typing.Optional[typing.List[Tag]] = None


def make_request(self, tags: typing.List[str] = ...,) -> typing.List[Pet]:
    """Finds Pets by tags"""
    m = ApiRequest(
        method="GET",
        path="/api/v3/pet/findByTags".format(),
        content_type=None,
        body=None,
        headers=self._only_provided({}),
        query_params=self._only_provided({"tags": tags,}),
        cookies=self._only_provided({}),
    )
    return self.make_request(
        {
            "200": {
                "application/json": typing.List[Pet],
                "application/xml": typing.List[Pet],
            },
        },
        m,
    )
