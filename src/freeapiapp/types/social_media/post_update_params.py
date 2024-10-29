# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["PostUpdateParams"]


class PostUpdateParams(TypedDict, total=False):
    content: str

    images: FileTypes
    """Upto 6 total images are allowed per post"""

    tags_0: Annotated[str, PropertyInfo(alias="tags[0]")]
