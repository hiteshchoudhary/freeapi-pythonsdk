# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AuthenticationRegisterParams"]


class AuthenticationRegisterParams(TypedDict, total=False):
    email: str

    password: str

    role: str

    username: str
