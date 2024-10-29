# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CategoryDeleteResponse", "Data", "DataDeletedCategory"]


class DataDeletedCategory(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    name: Optional[str] = None

    owner: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class Data(BaseModel):
    deleted_category: Optional[DataDeletedCategory] = FieldInfo(alias="deletedCategory", default=None)


class CategoryDeleteResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
