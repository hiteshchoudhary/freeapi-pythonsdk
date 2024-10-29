# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageSendResponse", "Data", "DataAttachment", "DataSender", "DataSenderAvatar"]


class DataAttachment(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataSenderAvatar(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    local_path: Optional[str] = FieldInfo(alias="localPath", default=None)

    url: Optional[str] = None


class DataSender(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    avatar: Optional[DataSenderAvatar] = None

    email: Optional[str] = None

    username: Optional[str] = None


class Data(BaseModel):
    api_v: Optional[float] = FieldInfo(alias="__v", default=None)

    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    attachments: Optional[List[DataAttachment]] = None

    chat: Optional[str] = None

    content: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    sender: Optional[DataSender] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class MessageSendResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
