# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "PlaylistListResponse",
    "Data",
    "DataData",
    "DataDataSnippet",
    "DataDataSnippetLocalized",
    "DataDataSnippetThumbnails",
    "DataDataSnippetThumbnailsDefault",
    "DataDataSnippetThumbnailsHigh",
    "DataDataSnippetThumbnailsMaxres",
    "DataDataSnippetThumbnailsMedium",
    "DataDataSnippetThumbnailsStandard",
]


class DataDataSnippetLocalized(BaseModel):
    description: Optional[str] = None

    title: Optional[str] = None


class DataDataSnippetThumbnailsDefault(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataSnippetThumbnailsHigh(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataSnippetThumbnailsMaxres(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataSnippetThumbnailsMedium(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataSnippetThumbnailsStandard(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataSnippetThumbnails(BaseModel):
    default: Optional[DataDataSnippetThumbnailsDefault] = None

    high: Optional[DataDataSnippetThumbnailsHigh] = None

    maxres: Optional[DataDataSnippetThumbnailsMaxres] = None

    medium: Optional[DataDataSnippetThumbnailsMedium] = None

    standard: Optional[DataDataSnippetThumbnailsStandard] = None


class DataDataSnippet(BaseModel):
    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)

    channel_title: Optional[str] = FieldInfo(alias="channelTitle", default=None)

    description: Optional[str] = None

    localized: Optional[DataDataSnippetLocalized] = None

    published_at: Optional[str] = FieldInfo(alias="publishedAt", default=None)

    thumbnails: Optional[DataDataSnippetThumbnails] = None

    title: Optional[str] = None


class DataData(BaseModel):
    id: Optional[str] = None

    kind: Optional[str] = None

    snippet: Optional[DataDataSnippet] = None


class Data(BaseModel):
    current_page_items: Optional[float] = FieldInfo(alias="currentPageItems", default=None)

    data: Optional[List[DataData]] = None

    limit: Optional[float] = None

    next_page: Optional[bool] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    previous_page: Optional[bool] = FieldInfo(alias="previousPage", default=None)

    total_items: Optional[float] = FieldInfo(alias="totalItems", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)


class PlaylistListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
