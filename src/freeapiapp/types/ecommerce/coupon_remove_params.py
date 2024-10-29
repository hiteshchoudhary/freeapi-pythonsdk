# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CouponRemoveParams"]


class CouponRemoveParams(TypedDict, total=False):
    coupon_code: Annotated[str, PropertyInfo(alias="couponCode")]
