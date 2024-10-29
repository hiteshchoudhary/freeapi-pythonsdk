# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VideoListParams"]


class VideoListParams(TypedDict, total=False):
    limit: str

    page: str

    query: str

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
