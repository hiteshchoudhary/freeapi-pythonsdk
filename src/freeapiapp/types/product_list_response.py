# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductListResponse", "Data", "DataProduct", "DataProductMainImage", "DataProductSubImage"]


class DataProductMainImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataProductSubImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataProduct(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    category: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    main_image: Optional[DataProductMainImage] = FieldInfo(alias="mainImage", default=None)

    name: Optional[str] = None

    owner: Optional[str] = None

    price: Optional[float] = None

    stock: Optional[float] = None

    sub_images: Optional[List[DataProductSubImage]] = FieldInfo(alias="subImages", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class Data(BaseModel):
    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)

    has_prev_page: Optional[bool] = FieldInfo(alias="hasPrevPage", default=None)

    limit: Optional[float] = None

    next_page: Optional[float] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    prev_page: Optional[object] = FieldInfo(alias="prevPage", default=None)

    products: Optional[List[DataProduct]] = None

    serial_number_start_from: Optional[float] = FieldInfo(alias="serialNumberStartFrom", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)

    total_products: Optional[float] = FieldInfo(alias="totalProducts", default=None)


class ProductListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
