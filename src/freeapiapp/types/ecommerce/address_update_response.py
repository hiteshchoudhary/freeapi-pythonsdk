# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AddressUpdateResponse", "Data"]


class Data(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    address_line1: Optional[str] = FieldInfo(alias="addressLine1", default=None)

    address_line2: Optional[str] = FieldInfo(alias="addressLine2", default=None)

    city: Optional[str] = None

    country: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    owner: Optional[str] = None

    pincode: Optional[str] = None

    state: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class AddressUpdateResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
