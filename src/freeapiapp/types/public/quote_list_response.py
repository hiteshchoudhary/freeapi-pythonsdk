# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QuoteListResponse", "Data", "DataData"]


class DataData(BaseModel):
    id: Optional[float] = None

    author: Optional[str] = None

    author_slug: Optional[str] = FieldInfo(alias="authorSlug", default=None)

    content: Optional[str] = None

    date_added: Optional[str] = FieldInfo(alias="dateAdded", default=None)

    date_modified: Optional[str] = FieldInfo(alias="dateModified", default=None)

    length: Optional[float] = None

    tags: Optional[List[object]] = None


class Data(BaseModel):
    current_page_items: Optional[float] = FieldInfo(alias="currentPageItems", default=None)

    data: Optional[List[DataData]] = None

    limit: Optional[float] = None

    next_page: Optional[bool] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    previous_page: Optional[bool] = FieldInfo(alias="previousPage", default=None)

    total_items: Optional[float] = FieldInfo(alias="totalItems", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)


class QuoteListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
