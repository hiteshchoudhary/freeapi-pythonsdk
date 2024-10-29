# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.ecommerce.orders import StatusUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        status = client.ecommerce.orders.status.update(
            order_id="64801f2a81acfc368d253158",
        )
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        status = client.ecommerce.orders.status.update(
            order_id="64801f2a81acfc368d253158",
            status="DELIVERED",
        )
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.ecommerce.orders.status.with_raw_response.update(
            order_id="64801f2a81acfc368d253158",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.ecommerce.orders.status.with_streaming_response.update(
            order_id="64801f2a81acfc368d253158",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusUpdateResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.ecommerce.orders.status.with_raw_response.update(
                order_id="",
            )


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        status = await async_client.ecommerce.orders.status.update(
            order_id="64801f2a81acfc368d253158",
        )
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        status = await async_client.ecommerce.orders.status.update(
            order_id="64801f2a81acfc368d253158",
            status="DELIVERED",
        )
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.orders.status.with_raw_response.update(
            order_id="64801f2a81acfc368d253158",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusUpdateResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.orders.status.with_streaming_response.update(
            order_id="64801f2a81acfc368d253158",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusUpdateResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.ecommerce.orders.status.with_raw_response.update(
                order_id="",
            )
