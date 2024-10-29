# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ChatListResponse", "Data", "DataParticipant", "DataParticipantAvatar"]


class DataParticipantAvatar(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataParticipant(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    avatar: Optional[DataParticipantAvatar] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    email: Optional[str] = None

    is_email_verified: Optional[bool] = FieldInfo(alias="isEmailVerified", default=None)

    login_type: Optional[str] = FieldInfo(alias="loginType", default=None)

    role: Optional[str] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    username: Optional[str] = None


class Data(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    admin: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    is_group_chat: Optional[bool] = FieldInfo(alias="isGroupChat", default=None)

    name: Optional[str] = None

    participants: Optional[List[DataParticipant]] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class ChatListResponse(BaseModel):
    data: Optional[List[Data]] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
