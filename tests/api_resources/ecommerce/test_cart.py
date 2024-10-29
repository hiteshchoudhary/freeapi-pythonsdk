# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.ecommerce import CartClearResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_clear(self, client: Freeapiapp) -> None:
        cart = client.ecommerce.cart.clear()
        assert_matches_type(CartClearResponse, cart, path=["response"])

    @parametrize
    def test_raw_response_clear(self, client: Freeapiapp) -> None:
        response = client.ecommerce.cart.with_raw_response.clear()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = response.parse()
        assert_matches_type(CartClearResponse, cart, path=["response"])

    @parametrize
    def test_streaming_response_clear(self, client: Freeapiapp) -> None:
        with client.ecommerce.cart.with_streaming_response.clear() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = response.parse()
            assert_matches_type(CartClearResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCart:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_clear(self, async_client: AsyncFreeapiapp) -> None:
        cart = await async_client.ecommerce.cart.clear()
        assert_matches_type(CartClearResponse, cart, path=["response"])

    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.cart.with_raw_response.clear()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = await response.parse()
        assert_matches_type(CartClearResponse, cart, path=["response"])

    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.cart.with_streaming_response.clear() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = await response.parse()
            assert_matches_type(CartClearResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True
