# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "RelatedListResponse",
    "Data",
    "DataData",
    "DataDataItems",
    "DataDataItemsContentDetails",
    "DataDataItemsSnippet",
    "DataDataItemsSnippetLocalized",
    "DataDataItemsSnippetThumbnails",
    "DataDataItemsSnippetThumbnailsDefault",
    "DataDataItemsSnippetThumbnailsHigh",
    "DataDataItemsSnippetThumbnailsMaxres",
    "DataDataItemsSnippetThumbnailsMedium",
    "DataDataItemsSnippetThumbnailsStandard",
    "DataDataItemsStatistics",
]


class DataDataItemsContentDetails(BaseModel):
    caption: Optional[str] = None

    content_rating: Optional[object] = FieldInfo(alias="contentRating", default=None)

    definition: Optional[str] = None

    dimension: Optional[str] = None

    duration: Optional[str] = None

    licensed_content: Optional[bool] = FieldInfo(alias="licensedContent", default=None)

    projection: Optional[str] = None


class DataDataItemsSnippetLocalized(BaseModel):
    description: Optional[str] = None

    title: Optional[str] = None


class DataDataItemsSnippetThumbnailsDefault(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataItemsSnippetThumbnailsHigh(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataItemsSnippetThumbnailsMaxres(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataItemsSnippetThumbnailsMedium(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataItemsSnippetThumbnailsStandard(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataDataItemsSnippetThumbnails(BaseModel):
    default: Optional[DataDataItemsSnippetThumbnailsDefault] = None

    high: Optional[DataDataItemsSnippetThumbnailsHigh] = None

    maxres: Optional[DataDataItemsSnippetThumbnailsMaxres] = None

    medium: Optional[DataDataItemsSnippetThumbnailsMedium] = None

    standard: Optional[DataDataItemsSnippetThumbnailsStandard] = None


class DataDataItemsSnippet(BaseModel):
    category_id: Optional[str] = FieldInfo(alias="categoryId", default=None)

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)

    channel_title: Optional[str] = FieldInfo(alias="channelTitle", default=None)

    default_audio_language: Optional[str] = FieldInfo(alias="defaultAudioLanguage", default=None)

    description: Optional[str] = None

    live_broadcast_content: Optional[str] = FieldInfo(alias="liveBroadcastContent", default=None)

    localized: Optional[DataDataItemsSnippetLocalized] = None

    published_at: Optional[str] = FieldInfo(alias="publishedAt", default=None)

    tags: Optional[List[str]] = None

    thumbnails: Optional[DataDataItemsSnippetThumbnails] = None

    title: Optional[str] = None


class DataDataItemsStatistics(BaseModel):
    comment_count: Optional[str] = FieldInfo(alias="commentCount", default=None)

    favorite_count: Optional[str] = FieldInfo(alias="favoriteCount", default=None)

    like_count: Optional[str] = FieldInfo(alias="likeCount", default=None)

    view_count: Optional[str] = FieldInfo(alias="viewCount", default=None)


class DataDataItems(BaseModel):
    id: Optional[str] = None

    content_details: Optional[DataDataItemsContentDetails] = FieldInfo(alias="contentDetails", default=None)

    kind: Optional[str] = None

    snippet: Optional[DataDataItemsSnippet] = None

    statistics: Optional[DataDataItemsStatistics] = None


class DataData(BaseModel):
    items: Optional[DataDataItems] = None

    kind: Optional[str] = None


class Data(BaseModel):
    current_page_items: Optional[float] = FieldInfo(alias="currentPageItems", default=None)

    data: Optional[List[DataData]] = None

    limit: Optional[float] = None

    next_page: Optional[bool] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    previous_page: Optional[bool] = FieldInfo(alias="previousPage", default=None)

    total_items: Optional[float] = FieldInfo(alias="totalItems", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)


class RelatedListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
