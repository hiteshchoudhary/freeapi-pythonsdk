# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ProductRandomResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    brand: Optional[str] = None

    category: Optional[str] = None

    description: Optional[str] = None

    discount_percentage: Optional[float] = FieldInfo(alias="discountPercentage", default=None)

    images: Optional[List[str]] = None

    price: Optional[float] = None

    rating: Optional[float] = None

    stock: Optional[float] = None

    thumbnail: Optional[str] = None

    title: Optional[str] = None


class ProductRandomResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
