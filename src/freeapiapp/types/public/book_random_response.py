# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "BookRandomResponse",
    "Data",
    "DataAccessInfo",
    "DataAccessInfoEpub",
    "DataAccessInfoPdf",
    "DataSaleInfo",
    "DataSearchInfo",
    "DataVolumeInfo",
    "DataVolumeInfoImageLinks",
    "DataVolumeInfoIndustryIdentifier",
    "DataVolumeInfoPanelizationSummary",
    "DataVolumeInfoReadingModes",
]


class DataAccessInfoEpub(BaseModel):
    download_link: Optional[str] = FieldInfo(alias="downloadLink", default=None)

    is_available: Optional[bool] = FieldInfo(alias="isAvailable", default=None)


class DataAccessInfoPdf(BaseModel):
    is_available: Optional[bool] = FieldInfo(alias="isAvailable", default=None)


class DataAccessInfo(BaseModel):
    access_view_status: Optional[str] = FieldInfo(alias="accessViewStatus", default=None)

    country: Optional[str] = None

    embeddable: Optional[bool] = None

    epub: Optional[DataAccessInfoEpub] = None

    pdf: Optional[DataAccessInfoPdf] = None

    public_domain: Optional[bool] = FieldInfo(alias="publicDomain", default=None)

    quote_sharing_allowed: Optional[bool] = FieldInfo(alias="quoteSharingAllowed", default=None)

    text_to_speech_permission: Optional[str] = FieldInfo(alias="textToSpeechPermission", default=None)

    viewability: Optional[str] = None

    web_reader_link: Optional[str] = FieldInfo(alias="webReaderLink", default=None)


class DataSaleInfo(BaseModel):
    buy_link: Optional[str] = FieldInfo(alias="buyLink", default=None)

    country: Optional[str] = None

    is_ebook: Optional[bool] = FieldInfo(alias="isEbook", default=None)

    saleability: Optional[str] = None


class DataSearchInfo(BaseModel):
    text_snippet: Optional[str] = FieldInfo(alias="textSnippet", default=None)


class DataVolumeInfoImageLinks(BaseModel):
    small_thumbnail: Optional[str] = FieldInfo(alias="smallThumbnail", default=None)

    thumbnail: Optional[str] = None


class DataVolumeInfoIndustryIdentifier(BaseModel):
    identifier: Optional[str] = None

    type: Optional[str] = None


class DataVolumeInfoPanelizationSummary(BaseModel):
    contains_epub_bubbles: Optional[bool] = FieldInfo(alias="containsEpubBubbles", default=None)

    contains_image_bubbles: Optional[bool] = FieldInfo(alias="containsImageBubbles", default=None)


class DataVolumeInfoReadingModes(BaseModel):
    image: Optional[bool] = None

    text: Optional[bool] = None


class DataVolumeInfo(BaseModel):
    allow_anon_logging: Optional[bool] = FieldInfo(alias="allowAnonLogging", default=None)

    authors: Optional[List[str]] = None

    canonical_volume_link: Optional[str] = FieldInfo(alias="canonicalVolumeLink", default=None)

    categories: Optional[List[str]] = None

    content_version: Optional[str] = FieldInfo(alias="contentVersion", default=None)

    description: Optional[str] = None

    image_links: Optional[DataVolumeInfoImageLinks] = FieldInfo(alias="imageLinks", default=None)

    industry_identifiers: Optional[List[DataVolumeInfoIndustryIdentifier]] = FieldInfo(
        alias="industryIdentifiers", default=None
    )

    info_link: Optional[str] = FieldInfo(alias="infoLink", default=None)

    language: Optional[str] = None

    maturity_rating: Optional[str] = FieldInfo(alias="maturityRating", default=None)

    page_count: Optional[float] = FieldInfo(alias="pageCount", default=None)

    panelization_summary: Optional[DataVolumeInfoPanelizationSummary] = FieldInfo(
        alias="panelizationSummary", default=None
    )

    preview_link: Optional[str] = FieldInfo(alias="previewLink", default=None)

    print_type: Optional[str] = FieldInfo(alias="printType", default=None)

    published_date: Optional[str] = FieldInfo(alias="publishedDate", default=None)

    reading_modes: Optional[DataVolumeInfoReadingModes] = FieldInfo(alias="readingModes", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None


class Data(BaseModel):
    id: Optional[float] = None

    access_info: Optional[DataAccessInfo] = FieldInfo(alias="accessInfo", default=None)

    etag: Optional[str] = None

    kind: Optional[str] = None

    sale_info: Optional[DataSaleInfo] = FieldInfo(alias="saleInfo", default=None)

    search_info: Optional[DataSearchInfo] = FieldInfo(alias="searchInfo", default=None)

    self_link: Optional[str] = FieldInfo(alias="selfLink", default=None)

    volume_info: Optional[DataVolumeInfo] = FieldInfo(alias="volumeInfo", default=None)


class BookRandomResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
