# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProfileUpdateResponse", "Data"]


class Data(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    owner: Optional[str] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class ProfileUpdateResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
