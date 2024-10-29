# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AddressCreateParams"]


class AddressCreateParams(TypedDict, total=False):
    address_line1: Annotated[str, PropertyInfo(alias="addressLine1")]

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]

    city: str

    country: str

    pincode: str

    state: str
