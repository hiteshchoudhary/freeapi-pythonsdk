# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import FileTypes

__all__ = ["MessageSendParams"]


class MessageSendParams(TypedDict, total=False):
    attachments: FileTypes
    """Image file maximum 5 images allowed.

    Pass multiple `attachments` keys to send multiple images.
    """

    content: str
