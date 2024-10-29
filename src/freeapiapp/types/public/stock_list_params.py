# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StockListParams"]


class StockListParams(TypedDict, total=False):
    inc: str

    limit: str

    page: str

    query: str
