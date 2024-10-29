# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CouponDeleteResponse", "Data", "DataDeletedCoupon"]


class DataDeletedCoupon(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    coupon_code: Optional[str] = FieldInfo(alias="couponCode", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    discount_value: Optional[float] = FieldInfo(alias="discountValue", default=None)

    expiry_date: Optional[str] = FieldInfo(alias="expiryDate", default=None)

    minimum_cart_value: Optional[float] = FieldInfo(alias="minimumCartValue", default=None)

    name: Optional[str] = None

    owner: Optional[str] = None

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)

    type: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class Data(BaseModel):
    deleted_coupon: Optional[DataDeletedCoupon] = FieldInfo(alias="deletedCoupon", default=None)


class CouponDeleteResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
