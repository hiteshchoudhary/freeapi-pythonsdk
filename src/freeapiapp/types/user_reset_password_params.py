# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserResetPasswordParams"]


class UserResetPasswordParams(TypedDict, total=False):
    new_password: Annotated[str, PropertyInfo(alias="newPassword")]
