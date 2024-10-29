# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "BookmarkRetrieveResponse",
    "Data",
    "DataBookmarkedPost",
    "DataBookmarkedPostAuthor",
    "DataBookmarkedPostAuthorAccount",
    "DataBookmarkedPostAuthorAccountAvatar",
    "DataBookmarkedPostAuthorCoverImage",
    "DataBookmarkedPostImage",
]


class DataBookmarkedPostAuthorAccountAvatar(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataBookmarkedPostAuthorAccount(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    avatar: Optional[DataBookmarkedPostAuthorAccountAvatar] = None

    email: Optional[str] = None

    username: Optional[str] = None


class DataBookmarkedPostAuthorCoverImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataBookmarkedPostAuthor(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    account: Optional[DataBookmarkedPostAuthorAccount] = None

    bio: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    cover_image: Optional[DataBookmarkedPostAuthorCoverImage] = FieldInfo(alias="coverImage", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    dob: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    location: Optional[str] = None

    owner: Optional[str] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class DataBookmarkedPostImage(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataBookmarkedPost(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    author: Optional[DataBookmarkedPostAuthor] = None

    comments: Optional[float] = None

    content: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    images: Optional[List[DataBookmarkedPostImage]] = None

    is_bookmarked: Optional[bool] = FieldInfo(alias="isBookmarked", default=None)

    is_liked: Optional[bool] = FieldInfo(alias="isLiked", default=None)

    likes: Optional[float] = None

    tags: Optional[List[str]] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class Data(BaseModel):
    bookmarked_posts: Optional[List[DataBookmarkedPost]] = FieldInfo(alias="bookmarkedPosts", default=None)

    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)

    has_prev_page: Optional[bool] = FieldInfo(alias="hasPrevPage", default=None)

    limit: Optional[float] = None

    next_page: Optional[object] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    prev_page: Optional[object] = FieldInfo(alias="prevPage", default=None)

    serial_number_start_from: Optional[float] = FieldInfo(alias="serialNumberStartFrom", default=None)

    total_bookmarked_posts: Optional[float] = FieldInfo(alias="totalBookmarkedPosts", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)


class BookmarkRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
