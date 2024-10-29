# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["KitchenSinkResponseGzipResponse", "Data"]


class Data(BaseModel):
    content_encoding: Optional[str] = FieldInfo(alias="contentEncoding", default=None)

    string: Optional[str] = None


class KitchenSinkResponseGzipResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
