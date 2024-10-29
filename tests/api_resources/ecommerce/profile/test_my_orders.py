# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.ecommerce.profile import MyOrderListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMyOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        my_order = client.ecommerce.profile.my_orders.list()
        assert_matches_type(MyOrderListResponse, my_order, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        my_order = client.ecommerce.profile.my_orders.list(
            limit="10",
            page="1",
        )
        assert_matches_type(MyOrderListResponse, my_order, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.ecommerce.profile.my_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        my_order = response.parse()
        assert_matches_type(MyOrderListResponse, my_order, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.ecommerce.profile.my_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            my_order = response.parse()
            assert_matches_type(MyOrderListResponse, my_order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMyOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        my_order = await async_client.ecommerce.profile.my_orders.list()
        assert_matches_type(MyOrderListResponse, my_order, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        my_order = await async_client.ecommerce.profile.my_orders.list(
            limit="10",
            page="1",
        )
        assert_matches_type(MyOrderListResponse, my_order, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.profile.my_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        my_order = await response.parse()
        assert_matches_type(MyOrderListResponse, my_order, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.profile.my_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            my_order = await response.parse()
            assert_matches_type(MyOrderListResponse, my_order, path=["response"])

        assert cast(Any, response.is_closed) is True
