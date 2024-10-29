# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "OrderRetrieveResponse",
    "Data",
    "DataOrder",
    "DataOrderAddress",
    "DataOrderCoupon",
    "DataOrderCustomer",
    "DataOrderItem",
    "DataOrderItemProduct",
    "DataOrderItemProductMainImage",
    "DataOrderItemProductSubImage",
]


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


class DataOrderCoupon(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    coupon_code: Optional[str] = FieldInfo(alias="couponCode", default=None)

    name: Optional[str] = None


class DataOrderCustomer(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    email: Optional[str] = None

    username: Optional[str] = None


class DataOrderItemProductMainImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataOrderItemProductSubImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataOrderItemProduct(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    category: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    main_image: Optional[DataOrderItemProductMainImage] = FieldInfo(alias="mainImage", default=None)

    name: Optional[str] = None

    owner: Optional[str] = None

    price: Optional[float] = None

    stock: Optional[float] = None

    sub_images: Optional[List[DataOrderItemProductSubImage]] = FieldInfo(alias="subImages", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class DataOrderItem(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    product: Optional[DataOrderItemProduct] = None

    quantity: Optional[float] = None


class DataOrder(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    address: Optional[DataOrderAddress] = None

    coupon: Optional[DataOrderCoupon] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    customer: Optional[DataOrderCustomer] = None

    discounted_order_price: Optional[float] = FieldInfo(alias="discountedOrderPrice", default=None)

    is_payment_done: Optional[bool] = FieldInfo(alias="isPaymentDone", default=None)

    items: Optional[List[DataOrderItem]] = None

    order_price: Optional[float] = FieldInfo(alias="orderPrice", default=None)

    payment_id: Optional[str] = FieldInfo(alias="paymentId", default=None)

    payment_provider: Optional[str] = FieldInfo(alias="paymentProvider", default=None)

    status: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class Data(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    order: Optional[DataOrder] = None


class OrderRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
