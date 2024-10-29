# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "BookListResponse",
    "Data",
    "DataData",
    "DataDataVolumeInfo",
    "DataDataVolumeInfoImageLinks",
    "DataDataVolumeInfoIndustryIdentifier",
    "DataDataVolumeInfoPanelizationSummary",
    "DataDataVolumeInfoReadingModes",
]


class DataDataVolumeInfoImageLinks(BaseModel):
    small_thumbnail: Optional[str] = FieldInfo(alias="smallThumbnail", default=None)

    thumbnail: Optional[str] = None


class DataDataVolumeInfoIndustryIdentifier(BaseModel):
    identifier: Optional[str] = None

    type: Optional[str] = None


class DataDataVolumeInfoPanelizationSummary(BaseModel):
    contains_epub_bubbles: Optional[bool] = FieldInfo(alias="containsEpubBubbles", default=None)

    contains_image_bubbles: Optional[bool] = FieldInfo(alias="containsImageBubbles", default=None)


class DataDataVolumeInfoReadingModes(BaseModel):
    image: Optional[bool] = None

    text: Optional[bool] = None


class DataDataVolumeInfo(BaseModel):
    allow_anon_logging: Optional[bool] = FieldInfo(alias="allowAnonLogging", default=None)

    authors: Optional[List[str]] = None

    average_rating: Optional[float] = FieldInfo(alias="averageRating", default=None)

    canonical_volume_link: Optional[str] = FieldInfo(alias="canonicalVolumeLink", default=None)

    categories: Optional[List[str]] = None

    content_version: Optional[str] = FieldInfo(alias="contentVersion", default=None)

    description: Optional[str] = None

    image_links: Optional[DataDataVolumeInfoImageLinks] = FieldInfo(alias="imageLinks", default=None)

    industry_identifiers: Optional[List[DataDataVolumeInfoIndustryIdentifier]] = FieldInfo(
        alias="industryIdentifiers", default=None
    )

    info_link: Optional[str] = FieldInfo(alias="infoLink", default=None)

    language: Optional[str] = None

    maturity_rating: Optional[str] = FieldInfo(alias="maturityRating", default=None)

    page_count: Optional[float] = FieldInfo(alias="pageCount", default=None)

    panelization_summary: Optional[DataDataVolumeInfoPanelizationSummary] = FieldInfo(
        alias="panelizationSummary", default=None
    )

    preview_link: Optional[str] = FieldInfo(alias="previewLink", default=None)

    print_type: Optional[str] = FieldInfo(alias="printType", default=None)

    published_date: Optional[str] = FieldInfo(alias="publishedDate", default=None)

    publisher: Optional[str] = None

    ratings_count: Optional[float] = FieldInfo(alias="ratingsCount", default=None)

    reading_modes: Optional[DataDataVolumeInfoReadingModes] = FieldInfo(alias="readingModes", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None


class DataData(BaseModel):
    id: Optional[float] = None

    etag: Optional[str] = None

    kind: Optional[str] = None

    volume_info: Optional[DataDataVolumeInfo] = FieldInfo(alias="volumeInfo", default=None)


class Data(BaseModel):
    current_page_items: Optional[float] = FieldInfo(alias="currentPageItems", default=None)

    data: Optional[List[DataData]] = None

    limit: Optional[float] = None

    next_page: Optional[bool] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    previous_page: Optional[bool] = FieldInfo(alias="previousPage", default=None)

    total_items: Optional[float] = FieldInfo(alias="totalItems", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)


class BookListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
