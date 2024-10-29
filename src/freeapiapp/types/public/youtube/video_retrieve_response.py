# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "VideoRetrieveResponse",
    "Data",
    "DataChannel",
    "DataChannelInfo",
    "DataChannelInfoLocalized",
    "DataChannelInfoThumbnails",
    "DataChannelInfoThumbnailsDefault",
    "DataChannelInfoThumbnailsHigh",
    "DataChannelInfoThumbnailsMedium",
    "DataChannelStatistics",
    "DataVideo",
    "DataVideoItems",
    "DataVideoItemsContentDetails",
    "DataVideoItemsSnippet",
    "DataVideoItemsSnippetLocalized",
    "DataVideoItemsSnippetThumbnails",
    "DataVideoItemsSnippetThumbnailsDefault",
    "DataVideoItemsSnippetThumbnailsHigh",
    "DataVideoItemsSnippetThumbnailsMaxres",
    "DataVideoItemsSnippetThumbnailsMedium",
    "DataVideoItemsSnippetThumbnailsStandard",
    "DataVideoItemsStatistics",
]


class DataChannelInfoLocalized(BaseModel):
    description: Optional[str] = None

    title: Optional[str] = None


class DataChannelInfoThumbnailsDefault(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataChannelInfoThumbnailsHigh(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataChannelInfoThumbnailsMedium(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataChannelInfoThumbnails(BaseModel):
    default: Optional[DataChannelInfoThumbnailsDefault] = None

    high: Optional[DataChannelInfoThumbnailsHigh] = None

    medium: Optional[DataChannelInfoThumbnailsMedium] = None


class DataChannelInfo(BaseModel):
    country: Optional[str] = None

    custom_url: Optional[str] = FieldInfo(alias="customUrl", default=None)

    description: Optional[str] = None

    localized: Optional[DataChannelInfoLocalized] = None

    published_at: Optional[str] = FieldInfo(alias="publishedAt", default=None)

    thumbnails: Optional[DataChannelInfoThumbnails] = None

    title: Optional[str] = None


class DataChannelStatistics(BaseModel):
    hidden_subscriber_count: Optional[bool] = FieldInfo(alias="hiddenSubscriberCount", default=None)

    subscriber_count: Optional[str] = FieldInfo(alias="subscriberCount", default=None)

    video_count: Optional[str] = FieldInfo(alias="videoCount", default=None)

    view_count: Optional[str] = FieldInfo(alias="viewCount", default=None)


class DataChannel(BaseModel):
    info: Optional[DataChannelInfo] = None

    statistics: Optional[DataChannelStatistics] = None


class DataVideoItemsContentDetails(BaseModel):
    caption: Optional[str] = None

    content_rating: Optional[object] = FieldInfo(alias="contentRating", default=None)

    definition: Optional[str] = None

    dimension: Optional[str] = None

    duration: Optional[str] = None

    licensed_content: Optional[bool] = FieldInfo(alias="licensedContent", default=None)

    projection: Optional[str] = None


class DataVideoItemsSnippetLocalized(BaseModel):
    description: Optional[str] = None

    title: Optional[str] = None


class DataVideoItemsSnippetThumbnailsDefault(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataVideoItemsSnippetThumbnailsHigh(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataVideoItemsSnippetThumbnailsMaxres(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataVideoItemsSnippetThumbnailsMedium(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataVideoItemsSnippetThumbnailsStandard(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataVideoItemsSnippetThumbnails(BaseModel):
    default: Optional[DataVideoItemsSnippetThumbnailsDefault] = None

    high: Optional[DataVideoItemsSnippetThumbnailsHigh] = None

    maxres: Optional[DataVideoItemsSnippetThumbnailsMaxres] = None

    medium: Optional[DataVideoItemsSnippetThumbnailsMedium] = None

    standard: Optional[DataVideoItemsSnippetThumbnailsStandard] = None


class DataVideoItemsSnippet(BaseModel):
    category_id: Optional[str] = FieldInfo(alias="categoryId", default=None)

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)

    channel_title: Optional[str] = FieldInfo(alias="channelTitle", default=None)

    default_audio_language: Optional[str] = FieldInfo(alias="defaultAudioLanguage", default=None)

    description: Optional[str] = None

    live_broadcast_content: Optional[str] = FieldInfo(alias="liveBroadcastContent", default=None)

    localized: Optional[DataVideoItemsSnippetLocalized] = None

    published_at: Optional[str] = FieldInfo(alias="publishedAt", default=None)

    tags: Optional[List[str]] = None

    thumbnails: Optional[DataVideoItemsSnippetThumbnails] = None

    title: Optional[str] = None


class DataVideoItemsStatistics(BaseModel):
    comment_count: Optional[str] = FieldInfo(alias="commentCount", default=None)

    favorite_count: Optional[str] = FieldInfo(alias="favoriteCount", default=None)

    like_count: Optional[str] = FieldInfo(alias="likeCount", default=None)

    view_count: Optional[str] = FieldInfo(alias="viewCount", default=None)


class DataVideoItems(BaseModel):
    id: Optional[str] = None

    content_details: Optional[DataVideoItemsContentDetails] = FieldInfo(alias="contentDetails", default=None)

    kind: Optional[str] = None

    snippet: Optional[DataVideoItemsSnippet] = None

    statistics: Optional[DataVideoItemsStatistics] = None


class DataVideo(BaseModel):
    items: Optional[DataVideoItems] = None

    kind: Optional[str] = None


class Data(BaseModel):
    channel: Optional[DataChannel] = None

    video: Optional[DataVideo] = None


class VideoRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
