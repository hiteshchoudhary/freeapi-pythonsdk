# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.ecommerce.coupons import StatusUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        status = client.ecommerce.coupons.status.update(
            coupon_id="6489654c8b460248066d8430",
        )
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        status = client.ecommerce.coupons.status.update(
            coupon_id="6489654c8b460248066d8430",
            is_active=True,
        )
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.ecommerce.coupons.status.with_raw_response.update(
            coupon_id="6489654c8b460248066d8430",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.ecommerce.coupons.status.with_streaming_response.update(
            coupon_id="6489654c8b460248066d8430",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusUpdateResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            client.ecommerce.coupons.status.with_raw_response.update(
                coupon_id="",
            )


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        status = await async_client.ecommerce.coupons.status.update(
            coupon_id="6489654c8b460248066d8430",
        )
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        status = await async_client.ecommerce.coupons.status.update(
            coupon_id="6489654c8b460248066d8430",
            is_active=True,
        )
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.coupons.status.with_raw_response.update(
            coupon_id="6489654c8b460248066d8430",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.coupons.status.with_streaming_response.update(
            coupon_id="6489654c8b460248066d8430",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusUpdateResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            await async_client.ecommerce.coupons.status.with_raw_response.update(
                coupon_id="",
            )
