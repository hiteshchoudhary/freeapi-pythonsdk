# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DogRetrieveResponse", "Data", "DataHeight", "DataImage", "DataWeight"]


class DataHeight(BaseModel):
    imperial: Optional[str] = None

    metric: Optional[str] = None


class DataImage(BaseModel):
    id: Optional[str] = None

    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataWeight(BaseModel):
    imperial: Optional[str] = None

    metric: Optional[str] = None


class Data(BaseModel):
    id: Optional[float] = None

    bred_for: Optional[str] = None

    breed_group: Optional[str] = None

    height: Optional[DataHeight] = None

    image: Optional[DataImage] = None

    life_span: Optional[str] = None

    name: Optional[str] = None

    reference_image_id: Optional[str] = None

    temperament: Optional[str] = None

    weight: Optional[DataWeight] = None


class DogRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
