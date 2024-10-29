# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.ecommerce.orders.provider import (
    RazorpayCreateResponse,
    RazorpayVerifyPaymentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRazorpay:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        razorpay = client.ecommerce.orders.provider.razorpay.create()
        assert_matches_type(RazorpayCreateResponse, razorpay, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        razorpay = client.ecommerce.orders.provider.razorpay.create(
            address_id="64b0589005c0bdf2d75643b7",
        )
        assert_matches_type(RazorpayCreateResponse, razorpay, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.ecommerce.orders.provider.razorpay.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        razorpay = response.parse()
        assert_matches_type(RazorpayCreateResponse, razorpay, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.ecommerce.orders.provider.razorpay.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            razorpay = response.parse()
            assert_matches_type(RazorpayCreateResponse, razorpay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_verify_payment(self, client: Freeapiapp) -> None:
        razorpay = client.ecommerce.orders.provider.razorpay.verify_payment()
        assert_matches_type(RazorpayVerifyPaymentResponse, razorpay, path=["response"])

    @parametrize
    def test_method_verify_payment_with_all_params(self, client: Freeapiapp) -> None:
        razorpay = client.ecommerce.orders.provider.razorpay.verify_payment(
            razorpay_order_id="order_LyeEiwrtVj1rLh",
            razorpay_payment_id="pay_LyeHd4Puzr6c8h",
            razorpay_signature="b1fea28efbca9a5090b60c4f2b5ffabd9b651d2da8c543eaf86a703a7f598c3d",
        )
        assert_matches_type(RazorpayVerifyPaymentResponse, razorpay, path=["response"])

    @parametrize
    def test_raw_response_verify_payment(self, client: Freeapiapp) -> None:
        response = client.ecommerce.orders.provider.razorpay.with_raw_response.verify_payment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        razorpay = response.parse()
        assert_matches_type(RazorpayVerifyPaymentResponse, razorpay, path=["response"])

    @parametrize
    def test_streaming_response_verify_payment(self, client: Freeapiapp) -> None:
        with client.ecommerce.orders.provider.razorpay.with_streaming_response.verify_payment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            razorpay = response.parse()
            assert_matches_type(RazorpayVerifyPaymentResponse, razorpay, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRazorpay:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        razorpay = await async_client.ecommerce.orders.provider.razorpay.create()
        assert_matches_type(RazorpayCreateResponse, razorpay, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        razorpay = await async_client.ecommerce.orders.provider.razorpay.create(
            address_id="64b0589005c0bdf2d75643b7",
        )
        assert_matches_type(RazorpayCreateResponse, razorpay, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.orders.provider.razorpay.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        razorpay = await response.parse()
        assert_matches_type(RazorpayCreateResponse, razorpay, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.orders.provider.razorpay.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            razorpay = await response.parse()
            assert_matches_type(RazorpayCreateResponse, razorpay, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_verify_payment(self, async_client: AsyncFreeapiapp) -> None:
        razorpay = await async_client.ecommerce.orders.provider.razorpay.verify_payment()
        assert_matches_type(RazorpayVerifyPaymentResponse, razorpay, path=["response"])

    @parametrize
    async def test_method_verify_payment_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        razorpay = await async_client.ecommerce.orders.provider.razorpay.verify_payment(
            razorpay_order_id="order_LyeEiwrtVj1rLh",
            razorpay_payment_id="pay_LyeHd4Puzr6c8h",
            razorpay_signature="b1fea28efbca9a5090b60c4f2b5ffabd9b651d2da8c543eaf86a703a7f598c3d",
        )
        assert_matches_type(RazorpayVerifyPaymentResponse, razorpay, path=["response"])

    @parametrize
    async def test_raw_response_verify_payment(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.orders.provider.razorpay.with_raw_response.verify_payment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        razorpay = await response.parse()
        assert_matches_type(RazorpayVerifyPaymentResponse, razorpay, path=["response"])

    @parametrize
    async def test_streaming_response_verify_payment(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.orders.provider.razorpay.with_streaming_response.verify_payment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            razorpay = await response.parse()
            assert_matches_type(RazorpayVerifyPaymentResponse, razorpay, path=["response"])

        assert cast(Any, response.is_closed) is True
