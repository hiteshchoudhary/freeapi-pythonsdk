# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DogListResponse", "Data", "DataData", "DataDataHeight", "DataDataImage", "DataDataWeight"]


class DataDataHeight(BaseModel):
    imperial: Optional[str] = None

    metric: Optional[str] = None


class DataDataImage(BaseModel):
    id: Optional[str] = None

    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataWeight(BaseModel):
    imperial: Optional[str] = None

    metric: Optional[str] = None


class DataData(BaseModel):
    id: Optional[float] = None

    bred_for: Optional[str] = None

    breed_group: Optional[str] = None

    height: Optional[DataDataHeight] = None

    image: Optional[DataDataImage] = None

    life_span: Optional[str] = None

    name: Optional[str] = None

    origin: Optional[str] = None

    reference_image_id: Optional[str] = None

    temperament: Optional[str] = None

    weight: Optional[DataDataWeight] = None


class Data(BaseModel):
    current_page_items: Optional[float] = FieldInfo(alias="currentPageItems", default=None)

    data: Optional[List[DataData]] = None

    limit: Optional[float] = None

    next_page: Optional[bool] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    previous_page: Optional[bool] = FieldInfo(alias="previousPage", default=None)

    total_items: Optional[float] = FieldInfo(alias="totalItems", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)


class DogListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
