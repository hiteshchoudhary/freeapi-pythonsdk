# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CouponCreateParams"]


class CouponCreateParams(TypedDict, total=False):
    coupon_code: Annotated[str, PropertyInfo(alias="couponCode")]

    discount_value: Annotated[float, PropertyInfo(alias="discountValue")]

    expiry_date: Annotated[Union[str, datetime], PropertyInfo(alias="expiryDate", format="iso8601")]

    minimum_cart_value: Annotated[float, PropertyInfo(alias="minimumCartValue")]

    name: str

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]

    type: Literal["FLAT"]
