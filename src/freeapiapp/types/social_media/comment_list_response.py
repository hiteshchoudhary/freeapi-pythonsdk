# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CommentListResponse",
    "Data",
    "DataComment",
    "DataCommentAuthor",
    "DataCommentAuthorAccount",
    "DataCommentAuthorAccountAvatar",
]


class DataCommentAuthorAccountAvatar(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataCommentAuthorAccount(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    avatar: Optional[DataCommentAuthorAccountAvatar] = None

    email: Optional[str] = None

    username: Optional[str] = None


class DataCommentAuthor(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    account: Optional[DataCommentAuthorAccount] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)


class DataComment(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    author: Optional[DataCommentAuthor] = None

    content: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    is_liked: Optional[bool] = FieldInfo(alias="isLiked", default=None)

    likes: Optional[float] = None

    post_id: Optional[str] = FieldInfo(alias="postId", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class Data(BaseModel):
    comments: Optional[List[DataComment]] = None

    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)

    has_prev_page: Optional[bool] = FieldInfo(alias="hasPrevPage", default=None)

    limit: Optional[float] = None

    next_page: Optional[float] = FieldInfo(alias="nextPage", default=None)

    page: Optional[float] = None

    prev_page: Optional[object] = FieldInfo(alias="prevPage", default=None)

    serial_number_start_from: Optional[float] = FieldInfo(alias="serialNumberStartFrom", default=None)

    total_comments: Optional[float] = FieldInfo(alias="totalComments", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)


class CommentListResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
