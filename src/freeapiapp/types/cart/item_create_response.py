# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ItemCreateResponse",
    "Data",
    "DataItem",
    "DataItemProduct",
    "DataItemProductMainImage",
    "DataItemProductSubImage",
]


class DataItemProductMainImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataItemProductSubImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataItemProduct(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    category: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    main_image: Optional[DataItemProductMainImage] = FieldInfo(alias="mainImage", default=None)

    name: Optional[str] = None

    owner: Optional[str] = None

    price: Optional[float] = None

    stock: Optional[float] = None

    sub_images: Optional[List[DataItemProductSubImage]] = FieldInfo(alias="subImages", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class DataItem(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    coupon: Optional[object] = None

    product: Optional[DataItemProduct] = None

    quantity: Optional[float] = None


class Data(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    cart_total: Optional[float] = FieldInfo(alias="cartTotal", default=None)

    discounted_total: Optional[float] = FieldInfo(alias="discountedTotal", default=None)

    items: Optional[List[DataItem]] = None


class ItemCreateResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
