# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types import ResetDBDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResetDB:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        reset_db = client.reset_db.delete()
        assert_matches_type(ResetDBDeleteResponse, reset_db, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.reset_db.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reset_db = response.parse()
        assert_matches_type(ResetDBDeleteResponse, reset_db, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.reset_db.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reset_db = response.parse()
            assert_matches_type(ResetDBDeleteResponse, reset_db, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResetDB:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        reset_db = await async_client.reset_db.delete()
        assert_matches_type(ResetDBDeleteResponse, reset_db, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.reset_db.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reset_db = await response.parse()
        assert_matches_type(ResetDBDeleteResponse, reset_db, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.reset_db.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reset_db = await response.parse()
            assert_matches_type(ResetDBDeleteResponse, reset_db, path=["response"])

        assert cast(Any, response.is_closed) is True
