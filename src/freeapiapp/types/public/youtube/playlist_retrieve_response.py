# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "PlaylistRetrieveResponse",
    "Data",
    "DataChannel",
    "DataChannelInfo",
    "DataChannelInfoLocalized",
    "DataChannelInfoThumbnails",
    "DataChannelInfoThumbnailsDefault",
    "DataChannelInfoThumbnailsHigh",
    "DataChannelInfoThumbnailsMedium",
    "DataChannelStatistics",
    "DataPlaylist",
    "DataPlaylistSnippet",
    "DataPlaylistSnippetLocalized",
    "DataPlaylistSnippetThumbnails",
    "DataPlaylistSnippetThumbnailsDefault",
    "DataPlaylistSnippetThumbnailsHigh",
    "DataPlaylistSnippetThumbnailsMaxres",
    "DataPlaylistSnippetThumbnailsMedium",
    "DataPlaylistSnippetThumbnailsStandard",
    "DataPlaylistItem",
    "DataPlaylistItemSnippet",
    "DataPlaylistItemSnippetResourceID",
    "DataPlaylistItemSnippetThumbnails",
    "DataPlaylistItemSnippetThumbnailsDefault",
    "DataPlaylistItemSnippetThumbnailsHigh",
    "DataPlaylistItemSnippetThumbnailsMaxres",
    "DataPlaylistItemSnippetThumbnailsMedium",
    "DataPlaylistItemSnippetThumbnailsStandard",
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


class DataPlaylistSnippetLocalized(BaseModel):
    description: Optional[str] = None

    title: Optional[str] = None


class DataPlaylistSnippetThumbnailsDefault(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataPlaylistSnippetThumbnailsHigh(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataPlaylistSnippetThumbnailsMaxres(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataPlaylistSnippetThumbnailsMedium(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataPlaylistSnippetThumbnailsStandard(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataPlaylistSnippetThumbnails(BaseModel):
    default: Optional[DataPlaylistSnippetThumbnailsDefault] = None

    high: Optional[DataPlaylistSnippetThumbnailsHigh] = None

    maxres: Optional[DataPlaylistSnippetThumbnailsMaxres] = None

    medium: Optional[DataPlaylistSnippetThumbnailsMedium] = None

    standard: Optional[DataPlaylistSnippetThumbnailsStandard] = None


class DataPlaylistSnippet(BaseModel):
    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)

    channel_title: Optional[str] = FieldInfo(alias="channelTitle", default=None)

    description: Optional[str] = None

    localized: Optional[DataPlaylistSnippetLocalized] = None

    published_at: Optional[str] = FieldInfo(alias="publishedAt", default=None)

    thumbnails: Optional[DataPlaylistSnippetThumbnails] = None

    title: Optional[str] = None


class DataPlaylist(BaseModel):
    id: Optional[str] = None

    kind: Optional[str] = None

    snippet: Optional[DataPlaylistSnippet] = None


class DataPlaylistItemSnippetResourceID(BaseModel):
    kind: Optional[str] = None

    video_id: Optional[str] = FieldInfo(alias="videoId", default=None)


class DataPlaylistItemSnippetThumbnailsDefault(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataPlaylistItemSnippetThumbnailsHigh(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataPlaylistItemSnippetThumbnailsMaxres(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataPlaylistItemSnippetThumbnailsMedium(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataPlaylistItemSnippetThumbnailsStandard(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataPlaylistItemSnippetThumbnails(BaseModel):
    default: Optional[DataPlaylistItemSnippetThumbnailsDefault] = None

    high: Optional[DataPlaylistItemSnippetThumbnailsHigh] = None

    maxres: Optional[DataPlaylistItemSnippetThumbnailsMaxres] = None

    medium: Optional[DataPlaylistItemSnippetThumbnailsMedium] = None

    standard: Optional[DataPlaylistItemSnippetThumbnailsStandard] = None


class DataPlaylistItemSnippet(BaseModel):
    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)

    channel_title: Optional[str] = FieldInfo(alias="channelTitle", default=None)

    description: Optional[str] = None

    playlist_id: Optional[str] = FieldInfo(alias="playlistId", default=None)

    position: Optional[float] = None

    published_at: Optional[str] = FieldInfo(alias="publishedAt", default=None)

    resource_id: Optional[DataPlaylistItemSnippetResourceID] = FieldInfo(alias="resourceId", default=None)

    thumbnails: Optional[DataPlaylistItemSnippetThumbnails] = None

    title: Optional[str] = None

    video_owner_channel_id: Optional[str] = FieldInfo(alias="videoOwnerChannelId", default=None)

    video_owner_channel_title: Optional[str] = FieldInfo(alias="videoOwnerChannelTitle", default=None)


class DataPlaylistItem(BaseModel):
    id: Optional[str] = None

    kind: Optional[str] = None

    snippet: Optional[DataPlaylistItemSnippet] = None


class Data(BaseModel):
    channel: Optional[DataChannel] = None

    playlist: Optional[DataPlaylist] = None

    playlist_items: Optional[List[DataPlaylistItem]] = FieldInfo(alias="playlistItems", default=None)


class PlaylistRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
