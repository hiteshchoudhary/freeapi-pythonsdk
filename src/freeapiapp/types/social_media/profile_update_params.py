# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProfileUpdateParams"]


class ProfileUpdateParams(TypedDict, total=False):
    bio: str

    country_code: Annotated[str, PropertyInfo(alias="countryCode")]

    dob: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    location: str

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
