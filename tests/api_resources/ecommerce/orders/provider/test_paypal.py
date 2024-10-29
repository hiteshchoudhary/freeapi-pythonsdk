# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.ecommerce.orders.provider import (
    PaypalCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaypal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        paypal = client.ecommerce.orders.provider.paypal.create()
        assert_matches_type(PaypalCreateResponse, paypal, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        paypal = client.ecommerce.orders.provider.paypal.create(
            address_id="64b0589005c0bdf2d75643b7",
        )
        assert_matches_type(PaypalCreateResponse, paypal, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.ecommerce.orders.provider.paypal.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paypal = response.parse()
        assert_matches_type(PaypalCreateResponse, paypal, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.ecommerce.orders.provider.paypal.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paypal = response.parse()
            assert_matches_type(PaypalCreateResponse, paypal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_verify_payment(self, client: Freeapiapp) -> None:
        paypal = client.ecommerce.orders.provider.paypal.verify_payment()
        assert paypal is None

    @parametrize
    def test_method_verify_payment_with_all_params(self, client: Freeapiapp) -> None:
        paypal = client.ecommerce.orders.provider.paypal.verify_payment(
            order_id="8AS341282K124974P",
        )
        assert paypal is None

    @parametrize
    def test_raw_response_verify_payment(self, client: Freeapiapp) -> None:
        response = client.ecommerce.orders.provider.paypal.with_raw_response.verify_payment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paypal = response.parse()
        assert paypal is None

    @parametrize
    def test_streaming_response_verify_payment(self, client: Freeapiapp) -> None:
        with client.ecommerce.orders.provider.paypal.with_streaming_response.verify_payment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paypal = response.parse()
            assert paypal is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPaypal:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        paypal = await async_client.ecommerce.orders.provider.paypal.create()
        assert_matches_type(PaypalCreateResponse, paypal, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        paypal = await async_client.ecommerce.orders.provider.paypal.create(
            address_id="64b0589005c0bdf2d75643b7",
        )
        assert_matches_type(PaypalCreateResponse, paypal, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.orders.provider.paypal.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paypal = await response.parse()
        assert_matches_type(PaypalCreateResponse, paypal, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.orders.provider.paypal.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paypal = await response.parse()
            assert_matches_type(PaypalCreateResponse, paypal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_verify_payment(self, async_client: AsyncFreeapiapp) -> None:
        paypal = await async_client.ecommerce.orders.provider.paypal.verify_payment()
        assert paypal is None

    @parametrize
    async def test_method_verify_payment_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        paypal = await async_client.ecommerce.orders.provider.paypal.verify_payment(
            order_id="8AS341282K124974P",
        )
        assert paypal is None

    @parametrize
    async def test_raw_response_verify_payment(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.orders.provider.paypal.with_raw_response.verify_payment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paypal = await response.parse()
        assert paypal is None

    @parametrize
    async def test_streaming_response_verify_payment(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.orders.provider.paypal.with_streaming_response.verify_payment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paypal = await response.parse()
            assert paypal is None

        assert cast(Any, response.is_closed) is True
