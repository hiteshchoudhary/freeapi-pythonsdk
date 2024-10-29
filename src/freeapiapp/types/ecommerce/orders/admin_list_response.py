# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AdminListResponse", "Data", "DataOrder", "DataOrderAddress", "DataOrderCustomer"]


class DataOrderAddress(BaseModel):
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


class DataOrderCustomer(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    email: Optional[str] = None

    username: Optional[str] = None


class DataOrder(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    address: Optional[DataOrderAddress] = None

    coupon: Optional[object] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    customer: Optional[DataOrderCustomer] = None

    discounted_order_price: Optional[float] = FieldInfo(alias="discountedOrderPrice", default=None)

    is_payment_done: Optional[bool] = FieldInfo(alias="isPaymentDone", default=None)

    order_price: Optional[float] = FieldInfo(alias="orderPrice", default=None)

    payment_id: Optional[str] = FieldInfo(alias="paymentId", default=None)

    payment_provider: Optional[str] = FieldInfo(alias="paymentProvider", default=None)

    status: Optional[str] = None

    total_order_items: Optional[float] = FieldInfo(alias="totalOrderItems", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class Data(BaseModel):
    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)

    has_prev_page: Optional[bool] = FieldInfo(alias="hasPrevPage", default=None)

    limit: Optional[float] = None

    next_page: Optional[object] = FieldInfo(alias="nextPage", default=None)

    orders: Optional[List[DataOrder]] = None

    page: Optional[float] = None

    prev_page: Optional[float] = FieldInfo(alias="prevPage", default=None)

    serial_number_start_from: Optional[float] = FieldInfo(alias="serialNumberStartFrom", default=None)

    total_orders: Optional[float] = FieldInfo(alias="totalOrders", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)


class AdminListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
