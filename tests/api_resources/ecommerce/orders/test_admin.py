# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.ecommerce.orders import AdminListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        admin = client.ecommerce.orders.admin.list()
        assert_matches_type(AdminListResponse, admin, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        admin = client.ecommerce.orders.admin.list(
            limit="10",
            page="2",
            status="PENDING",
        )
        assert_matches_type(AdminListResponse, admin, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.ecommerce.orders.admin.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminListResponse, admin, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.ecommerce.orders.admin.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminListResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        admin = await async_client.ecommerce.orders.admin.list()
        assert_matches_type(AdminListResponse, admin, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        admin = await async_client.ecommerce.orders.admin.list(
            limit="10",
            page="2",
            status="PENDING",
        )
        assert_matches_type(AdminListResponse, admin, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.orders.admin.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminListResponse, admin, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.orders.admin.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminListResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True
