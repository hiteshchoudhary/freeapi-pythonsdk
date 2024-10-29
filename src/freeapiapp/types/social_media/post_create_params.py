# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["PostCreateParams"]


class PostCreateParams(TypedDict, total=False):
    content: str

    images: FileTypes
    """Upto 6 images per post are allowed"""

    tags_0: Annotated[str, PropertyInfo(alias="tags[0]")]

    tags_1: Annotated[str, PropertyInfo(alias="tags[1]")]

    tags_2: Annotated[str, PropertyInfo(alias="tags[2]")]
