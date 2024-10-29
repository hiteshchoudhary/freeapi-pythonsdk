# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "UserRandomResponse",
    "Data",
    "DataDob",
    "DataLocation",
    "DataLocationCoordinates",
    "DataLocationStreet",
    "DataLocationTimezone",
    "DataLogin",
    "DataName",
    "DataPicture",
    "DataRegistered",
]


class DataDob(BaseModel):
    age: Optional[float] = None

    date: Optional[str] = None


class DataLocationCoordinates(BaseModel):
    latitude: Optional[str] = None

    longitude: Optional[str] = None


class DataLocationStreet(BaseModel):
    name: Optional[str] = None

    number: Optional[float] = None


class DataLocationTimezone(BaseModel):
    description: Optional[str] = None

    offset: Optional[str] = None


class DataLocation(BaseModel):
    city: Optional[str] = None

    coordinates: Optional[DataLocationCoordinates] = None

    country: Optional[str] = None

    postcode: Optional[float] = None

    state: Optional[str] = None

    street: Optional[DataLocationStreet] = None

    timezone: Optional[DataLocationTimezone] = None


class DataLogin(BaseModel):
    md5: Optional[str] = None

    password: Optional[str] = None

    salt: Optional[str] = None

    sha1: Optional[str] = None

    sha256: Optional[str] = None

    username: Optional[str] = None

    uuid: Optional[str] = None


class DataName(BaseModel):
    first: Optional[str] = None

    last: Optional[str] = None

    title: Optional[str] = None


class DataPicture(BaseModel):
    large: Optional[str] = None

    medium: Optional[str] = None

    thumbnail: Optional[str] = None


class DataRegistered(BaseModel):
    age: Optional[float] = None

    date: Optional[str] = None


class Data(BaseModel):
    id: Optional[float] = None

    cell: Optional[str] = None

    dob: Optional[DataDob] = None

    email: Optional[str] = None

    gender: Optional[str] = None

    location: Optional[DataLocation] = None

    login: Optional[DataLogin] = None

    name: Optional[DataName] = None

    nat: Optional[str] = None

    phone: Optional[str] = None

    picture: Optional[DataPicture] = None

    registered: Optional[DataRegistered] = None


class UserRandomResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
