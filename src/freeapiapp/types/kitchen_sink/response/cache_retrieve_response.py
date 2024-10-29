# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CacheRetrieveResponse", "Data", "DataHeaders"]


class DataHeaders(BaseModel):
    access_control_allow_credentials: Optional[str] = FieldInfo(alias="access-control-allow-credentials", default=None)

    access_control_allow_origin: Optional[str] = FieldInfo(alias="access-control-allow-origin", default=None)

    cache_control: Optional[str] = FieldInfo(alias="cache-control", default=None)

    x_powered_by: Optional[str] = FieldInfo(alias="x-powered-by", default=None)


class Data(BaseModel):
    headers: Optional[DataHeaders] = None


class CacheRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
