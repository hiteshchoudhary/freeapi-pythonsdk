# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.ecommerce.coupons import CustomerAvailableListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomerAvailable:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        customer_available = client.ecommerce.coupons.customer_available.list()
        assert_matches_type(CustomerAvailableListResponse, customer_available, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        customer_available = client.ecommerce.coupons.customer_available.list(
            limit="5",
            page="1",
        )
        assert_matches_type(CustomerAvailableListResponse, customer_available, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.ecommerce.coupons.customer_available.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_available = response.parse()
        assert_matches_type(CustomerAvailableListResponse, customer_available, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.ecommerce.coupons.customer_available.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_available = response.parse()
            assert_matches_type(CustomerAvailableListResponse, customer_available, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomerAvailable:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        customer_available = await async_client.ecommerce.coupons.customer_available.list()
        assert_matches_type(CustomerAvailableListResponse, customer_available, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        customer_available = await async_client.ecommerce.coupons.customer_available.list(
            limit="5",
            page="1",
        )
        assert_matches_type(CustomerAvailableListResponse, customer_available, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.coupons.customer_available.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_available = await response.parse()
        assert_matches_type(CustomerAvailableListResponse, customer_available, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.coupons.customer_available.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_available = await response.parse()
            assert_matches_type(CustomerAvailableListResponse, customer_available, path=["response"])

        assert cast(Any, response.is_closed) is True
