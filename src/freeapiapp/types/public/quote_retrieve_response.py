# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QuoteRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    author: Optional[str] = None

    author_slug: Optional[str] = FieldInfo(alias="authorSlug", default=None)

    content: Optional[str] = None

    date_added: Optional[str] = FieldInfo(alias="dateAdded", default=None)

    date_modified: Optional[str] = FieldInfo(alias="dateModified", default=None)

    length: Optional[float] = None

    tags: Optional[List[str]] = None


class QuoteRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
