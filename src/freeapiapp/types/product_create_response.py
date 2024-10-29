# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductCreateResponse", "Data"]


class Data(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    category: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    main_image: Optional[str] = FieldInfo(alias="mainImage", default=None)

    name: Optional[str] = None

    owner: Optional[str] = None

    price: Optional[float] = None

    stock: Optional[float] = None

    sub_images: Optional[List[str]] = FieldInfo(alias="subImages", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class ProductCreateResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
