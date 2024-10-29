# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RandomProductListParams"]


class RandomProductListParams(TypedDict, total=False):
    inc: str

    limit: str

    page: str

    query: str
