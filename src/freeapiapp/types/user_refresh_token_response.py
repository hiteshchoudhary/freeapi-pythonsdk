# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserRefreshTokenResponse", "Data"]


class Data(BaseModel):
    access_token: Optional[str] = FieldInfo(alias="accessToken", default=None)

    refresh_token: Optional[str] = FieldInfo(alias="refreshToken", default=None)


class UserRefreshTokenResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
