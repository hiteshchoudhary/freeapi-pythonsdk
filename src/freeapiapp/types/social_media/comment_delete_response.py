# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CommentDeleteResponse", "Data", "DataDeletedComment"]


class DataDeletedComment(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    author: Optional[str] = None

    content: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    post_id: Optional[str] = FieldInfo(alias="postId", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class Data(BaseModel):
    deleted_comment: Optional[DataDeletedComment] = FieldInfo(alias="deletedComment", default=None)


class CommentDeleteResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
