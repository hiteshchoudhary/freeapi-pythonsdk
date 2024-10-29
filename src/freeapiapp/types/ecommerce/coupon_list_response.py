# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CouponListResponse", "Data", "DataCoupon"]


class DataCoupon(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    coupon_code: Optional[str] = FieldInfo(alias="couponCode", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    discount_value: Optional[float] = FieldInfo(alias="discountValue", default=None)

    expiry_date: Optional[str] = FieldInfo(alias="expiryDate", default=None)

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    minimum_cart_value: Optional[float] = FieldInfo(alias="minimumCartValue", default=None)

    name: Optional[str] = None

    owner: Optional[str] = None

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)

    type: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class Data(BaseModel):
    coupons: Optional[List[DataCoupon]] = None

    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)

    has_prev_page: Optional[bool] = FieldInfo(alias="hasPrevPage", default=None)

    limit: Optional[float] = None

    next_page: Optional[float] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    prev_page: Optional[object] = FieldInfo(alias="prevPage", default=None)

    serial_number_start_from: Optional[float] = FieldInfo(alias="serialNumberStartFrom", default=None)

    total_coupons: Optional[float] = FieldInfo(alias="totalCoupons", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)


class CouponListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
