# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HTTPMethodCreateResponse", "Data", "DataHeaders"]


class DataHeaders(BaseModel):
    accept: Optional[str] = None

    accept_encoding: Optional[str] = FieldInfo(alias="accept-encoding", default=None)

    cache_control: Optional[str] = FieldInfo(alias="cache-control", default=None)

    connection: Optional[str] = None

    content_length: Optional[str] = FieldInfo(alias="content-length", default=None)

    cookie: Optional[str] = None

    host: Optional[str] = None

    postman_token: Optional[str] = FieldInfo(alias="postman-token", default=None)

    user_agent: Optional[str] = FieldInfo(alias="user-agent", default=None)


class Data(BaseModel):
    headers: Optional[DataHeaders] = None

    method: Optional[str] = None

    origin: Optional[str] = None

    url: Optional[str] = None


class HTTPMethodCreateResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
