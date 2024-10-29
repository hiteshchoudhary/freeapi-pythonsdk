# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "CommentRetrieveResponse",
    "Data",
    "DataSnippet",
    "DataSnippetTopLevelComment",
    "DataSnippetTopLevelCommentSnippet",
]


class DataSnippetTopLevelCommentSnippet(BaseModel):
    author_display_name: Optional[str] = FieldInfo(alias="authorDisplayName", default=None)

    author_profile_image_url: Optional[str] = FieldInfo(alias="authorProfileImageUrl", default=None)

    like_count: Optional[float] = FieldInfo(alias="likeCount", default=None)

    published_at: Optional[str] = FieldInfo(alias="publishedAt", default=None)

    text_display: Optional[str] = FieldInfo(alias="textDisplay", default=None)

    text_original: Optional[str] = FieldInfo(alias="textOriginal", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class DataSnippetTopLevelComment(BaseModel):
    id: Optional[str] = None

    snippet: Optional[DataSnippetTopLevelCommentSnippet] = None


class DataSnippet(BaseModel):
    top_level_comment: Optional[DataSnippetTopLevelComment] = FieldInfo(alias="topLevelComment", default=None)

    total_reply_count: Optional[float] = FieldInfo(alias="totalReplyCount", default=None)

    video_id: Optional[str] = FieldInfo(alias="videoId", default=None)


class Data(BaseModel):
    id: Optional[str] = None

    snippet: Optional[DataSnippet] = None


class CommentRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
