# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthenticationVerifyEmailResponse", "Data"]


class Data(BaseModel):
    is_email_verified: Optional[bool] = FieldInfo(alias="isEmailVerified", default=None)


class AuthenticationVerifyEmailResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
