# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthenticationRegisterResponse", "Data", "DataUser", "DataUserAvatar"]


class DataUserAvatar(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataUser(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    avatar: Optional[DataUserAvatar] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    email: Optional[str] = None

    is_email_verified: Optional[bool] = FieldInfo(alias="isEmailVerified", default=None)

    login_type: Optional[str] = FieldInfo(alias="loginType", default=None)

    role: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    username: Optional[str] = None


class Data(BaseModel):
    user: Optional[DataUser] = None


class AuthenticationRegisterResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
