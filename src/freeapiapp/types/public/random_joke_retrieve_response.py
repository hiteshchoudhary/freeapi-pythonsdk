# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RandomJokeRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    categories: Optional[List[object]] = None

    content: Optional[str] = None


class RandomJokeRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
