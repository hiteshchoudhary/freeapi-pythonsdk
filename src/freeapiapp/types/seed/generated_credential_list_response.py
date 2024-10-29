# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GeneratedCredentialListResponse", "Data"]


class Data(BaseModel):
    password: Optional[str] = None

    role: Optional[str] = None

    username: Optional[str] = None


class GeneratedCredentialListResponse(BaseModel):
    data: Optional[List[Data]] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
