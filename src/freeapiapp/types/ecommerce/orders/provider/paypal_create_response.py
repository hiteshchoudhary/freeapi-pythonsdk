# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["PaypalCreateResponse", "Data", "DataLink"]


class DataLink(BaseModel):
    href: Optional[str] = None

    method: Optional[str] = None

    rel: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    links: Optional[List[DataLink]] = None

    status: Optional[str] = None


class PaypalCreateResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
