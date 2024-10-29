# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ChannelListResponse",
    "Data",
    "DataInfo",
    "DataInfoBrandingSettings",
    "DataInfoBrandingSettingsChannel",
    "DataInfoBrandingSettingsImage",
    "DataInfoSnippet",
    "DataInfoSnippetLocalized",
    "DataInfoSnippetThumbnails",
    "DataInfoSnippetThumbnailsDefault",
    "DataInfoSnippetThumbnailsHigh",
    "DataInfoSnippetThumbnailsMedium",
    "DataInfoStatistics",
]


class DataInfoBrandingSettingsChannel(BaseModel):
    country: Optional[str] = None

    description: Optional[str] = None

    keywords: Optional[str] = None

    title: Optional[str] = None

    unsubscribed_trailer: Optional[str] = FieldInfo(alias="unsubscribedTrailer", default=None)


class DataInfoBrandingSettingsImage(BaseModel):
    banner_external_url: Optional[str] = FieldInfo(alias="bannerExternalUrl", default=None)


class DataInfoBrandingSettings(BaseModel):
    channel: Optional[DataInfoBrandingSettingsChannel] = None

    image: Optional[DataInfoBrandingSettingsImage] = None


class DataInfoSnippetLocalized(BaseModel):
    description: Optional[str] = None

    title: Optional[str] = None


class DataInfoSnippetThumbnailsDefault(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataInfoSnippetThumbnailsHigh(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataInfoSnippetThumbnailsMedium(BaseModel):
    height: Optional[float] = None

    url: Optional[str] = None

    width: Optional[float] = None


class DataInfoSnippetThumbnails(BaseModel):
    default: Optional[DataInfoSnippetThumbnailsDefault] = None

    high: Optional[DataInfoSnippetThumbnailsHigh] = None

    medium: Optional[DataInfoSnippetThumbnailsMedium] = None


class DataInfoSnippet(BaseModel):
    country: Optional[str] = None

    custom_url: Optional[str] = FieldInfo(alias="customUrl", default=None)

    description: Optional[str] = None

    localized: Optional[DataInfoSnippetLocalized] = None

    published_at: Optional[str] = FieldInfo(alias="publishedAt", default=None)

    thumbnails: Optional[DataInfoSnippetThumbnails] = None

    title: Optional[str] = None


class DataInfoStatistics(BaseModel):
    hidden_subscriber_count: Optional[bool] = FieldInfo(alias="hiddenSubscriberCount", default=None)

    subscriber_count: Optional[str] = FieldInfo(alias="subscriberCount", default=None)

    video_count: Optional[str] = FieldInfo(alias="videoCount", default=None)

    view_count: Optional[str] = FieldInfo(alias="viewCount", default=None)


class DataInfo(BaseModel):
    id: Optional[str] = None

    branding_settings: Optional[DataInfoBrandingSettings] = FieldInfo(alias="brandingSettings", default=None)

    kind: Optional[str] = None

    snippet: Optional[DataInfoSnippet] = None

    statistics: Optional[DataInfoStatistics] = None


class Data(BaseModel):
    info: Optional[DataInfo] = None

    kind: Optional[str] = None


class ChannelListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
