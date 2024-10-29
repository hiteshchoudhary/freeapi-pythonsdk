# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ItemDeleteResponse", "Data", "DataProduct", "DataProductMainImage"]


class DataProductMainImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataProduct(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    description: Optional[str] = None

    main_image: Optional[DataProductMainImage] = FieldInfo(alias="mainImage", default=None)

    name: Optional[str] = None

    price: Optional[float] = None

    stock: Optional[float] = None


class Data(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    product: Optional[DataProduct] = None

    quantity: Optional[float] = None


class ItemDeleteResponse(BaseModel):
    data: Optional[List[Data]] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
