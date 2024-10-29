# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CatRetrieveResponse", "Data", "DataWeight"]


class DataWeight(BaseModel):
    imperial: Optional[str] = None

    metric: Optional[str] = None


class Data(BaseModel):
    id: Optional[float] = None

    adaptability: Optional[float] = None

    affection_level: Optional[float] = None

    alt_names: Optional[str] = None

    cfa_url: Optional[str] = None

    child_friendly: Optional[float] = None

    country_code: Optional[str] = None

    country_codes: Optional[str] = None

    description: Optional[str] = None

    dog_friendly: Optional[float] = None

    energy_level: Optional[float] = None

    experimental: Optional[float] = None

    grooming: Optional[float] = None

    hairless: Optional[float] = None

    health_issues: Optional[float] = None

    hypoallergenic: Optional[float] = None

    image: Optional[str] = None

    indoor: Optional[float] = None

    intelligence: Optional[float] = None

    lap: Optional[float] = None

    life_span: Optional[str] = None

    name: Optional[str] = None

    natural: Optional[float] = None

    origin: Optional[str] = None

    rare: Optional[float] = None

    rex: Optional[float] = None

    shedding_level: Optional[float] = None

    short_legs: Optional[float] = None

    social_needs: Optional[float] = None

    stranger_friendly: Optional[float] = None

    suppressed_tail: Optional[float] = None

    temperament: Optional[str] = None

    vcahospitals_url: Optional[str] = None

    vetstreet_url: Optional[str] = None

    vocalisation: Optional[float] = None

    weight: Optional[DataWeight] = None

    wikipedia_url: Optional[str] = None


class CatRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
