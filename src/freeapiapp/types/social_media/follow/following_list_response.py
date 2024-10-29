# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "FollowingListResponse",
    "Data",
    "DataFollowing",
    "DataFollowingAvatar",
    "DataFollowingProfile",
    "DataFollowingProfileCoverImage",
    "DataUser",
    "DataUserAvatar",
    "DataUserProfile",
    "DataUserProfileCoverImage",
]


class DataFollowingAvatar(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataFollowingProfileCoverImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataFollowingProfile(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    bio: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    cover_image: Optional[DataFollowingProfileCoverImage] = FieldInfo(alias="coverImage", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    dob: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    location: Optional[str] = None

    owner: Optional[str] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class DataFollowing(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    avatar: Optional[DataFollowingAvatar] = None

    email: Optional[str] = None

    is_following: Optional[bool] = FieldInfo(alias="isFollowing", default=None)

    profile: Optional[DataFollowingProfile] = None

    username: Optional[str] = None


class DataUserAvatar(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataUserProfileCoverImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataUserProfile(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    bio: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    cover_image: Optional[DataUserProfileCoverImage] = FieldInfo(alias="coverImage", default=None)

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    location: Optional[str] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)


class DataUser(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    avatar: Optional[DataUserAvatar] = None

    email: Optional[str] = None

    is_email_verified: Optional[bool] = FieldInfo(alias="isEmailVerified", default=None)

    profile: Optional[DataUserProfile] = None

    username: Optional[str] = None


class Data(BaseModel):
    following: Optional[List[DataFollowing]] = None

    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)

    has_prev_page: Optional[bool] = FieldInfo(alias="hasPrevPage", default=None)

    limit: Optional[float] = None

    next_page: Optional[float] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    prev_page: Optional[object] = FieldInfo(alias="prevPage", default=None)

    serial_number_start_from: Optional[float] = FieldInfo(alias="serialNumberStartFrom", default=None)

    total_following: Optional[float] = FieldInfo(alias="totalFollowing", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)

    user: Optional[DataUser] = None


class FollowingListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
