# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "RandomUserListResponse",
    "Data",
    "DataData",
    "DataDataDob",
    "DataDataLocation",
    "DataDataLocationCoordinates",
    "DataDataLocationStreet",
    "DataDataLocationTimezone",
    "DataDataLogin",
    "DataDataName",
    "DataDataPicture",
    "DataDataRegistered",
]


class DataDataDob(BaseModel):
    age: Optional[float] = None

    date: Optional[str] = None


class DataDataLocationCoordinates(BaseModel):
    latitude: Optional[str] = None

    longitude: Optional[str] = None


class DataDataLocationStreet(BaseModel):
    name: Optional[str] = None

    number: Optional[float] = None


class DataDataLocationTimezone(BaseModel):
    description: Optional[str] = None

    offset: Optional[str] = None


class DataDataLocation(BaseModel):
    city: Optional[str] = None

    coordinates: Optional[DataDataLocationCoordinates] = None

    country: Optional[str] = None

    postcode: Union[float, str, float, float, float, float, float, float, None] = None

    state: Optional[str] = None

    street: Optional[DataDataLocationStreet] = None

    timezone: Optional[DataDataLocationTimezone] = None


class DataDataLogin(BaseModel):
    md5: Optional[str] = None

    password: Optional[str] = None

    salt: Optional[str] = None

    sha1: Optional[str] = None

    sha256: Optional[str] = None

    username: Optional[str] = None

    uuid: Optional[str] = None


class DataDataName(BaseModel):
    first: Optional[str] = None

    last: Optional[str] = None

    title: Optional[str] = None


class DataDataPicture(BaseModel):
    large: Optional[str] = None

    medium: Optional[str] = None

    thumbnail: Optional[str] = None


class DataDataRegistered(BaseModel):
    age: Optional[float] = None

    date: Optional[str] = None


class DataData(BaseModel):
    id: Optional[float] = None

    cell: Optional[str] = None

    dob: Optional[DataDataDob] = None

    email: Optional[str] = None

    gender: Optional[str] = None

    location: Optional[DataDataLocation] = None

    login: Optional[DataDataLogin] = None

    name: Optional[DataDataName] = None

    nat: Optional[str] = None

    phone: Optional[str] = None

    picture: Optional[DataDataPicture] = None

    registered: Optional[DataDataRegistered] = None


class Data(BaseModel):
    current_page_items: Optional[float] = FieldInfo(alias="currentPageItems", default=None)

    data: Optional[List[DataData]] = None

    limit: Optional[float] = None

    next_page: Optional[bool] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    previous_page: Optional[bool] = FieldInfo(alias="previousPage", default=None)

    total_items: Optional[float] = FieldInfo(alias="totalItems", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)


class RandomUserListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
