# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["RazorpayVerifyPaymentResponse", "Data", "DataItem"]


class DataItem(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    product_id: Optional[str] = FieldInfo(alias="productId", default=None)

    quantity: Optional[float] = None


class Data(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    address: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    customer: Optional[str] = None

    is_payment_done: Optional[bool] = FieldInfo(alias="isPaymentDone", default=None)

    items: Optional[List[DataItem]] = None

    order_price: Optional[float] = FieldInfo(alias="orderPrice", default=None)

    payment_id: Optional[str] = FieldInfo(alias="paymentId", default=None)

    payment_provider: Optional[str] = FieldInfo(alias="paymentProvider", default=None)

    status: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class RazorpayVerifyPaymentResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
