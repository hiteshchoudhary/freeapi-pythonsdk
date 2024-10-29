# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProfileRetrieveResponse", "Data", "DataAccount", "DataAccountAvatar", "DataCoverImage"]


class DataAccountAvatar(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataAccount(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    avatar: Optional[DataAccountAvatar] = None

    email: Optional[str] = None

    is_email_verified: Optional[bool] = FieldInfo(alias="isEmailVerified", default=None)

    username: Optional[str] = None


class DataCoverImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class Data(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    account: Optional[DataAccount] = None

    bio: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    cover_image: Optional[DataCoverImage] = FieldInfo(alias="coverImage", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    dob: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    followers_count: Optional[float] = FieldInfo(alias="followersCount", default=None)

    following_count: Optional[float] = FieldInfo(alias="followingCount", default=None)

    is_following: Optional[bool] = FieldInfo(alias="isFollowing", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    location: Optional[str] = None

    owner: Optional[str] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class ProfileRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
