# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.cart import ItemCreateResponse, ItemDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItem:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        item = client.cart.item.create(
            product_id="649e7bfcdbf96264731f57e0",
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        item = client.cart.item.create(
            product_id="649e7bfcdbf96264731f57e0",
            quantity="quantity",
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.cart.item.with_raw_response.create(
            product_id="649e7bfcdbf96264731f57e0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.cart.item.with_streaming_response.create(
            product_id="649e7bfcdbf96264731f57e0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemCreateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.cart.item.with_raw_response.create(
                product_id="",
            )

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        item = client.cart.item.delete(
            "649e7bfcdbf96264731f57e0",
        )
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.cart.item.with_raw_response.delete(
            "649e7bfcdbf96264731f57e0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.cart.item.with_streaming_response.delete(
            "649e7bfcdbf96264731f57e0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemDeleteResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.cart.item.with_raw_response.delete(
                "",
            )


class TestAsyncItem:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        item = await async_client.cart.item.create(
            product_id="649e7bfcdbf96264731f57e0",
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        item = await async_client.cart.item.create(
            product_id="649e7bfcdbf96264731f57e0",
            quantity="quantity",
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.cart.item.with_raw_response.create(
            product_id="649e7bfcdbf96264731f57e0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.cart.item.with_streaming_response.create(
            product_id="649e7bfcdbf96264731f57e0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemCreateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.cart.item.with_raw_response.create(
                product_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        item = await async_client.cart.item.delete(
            "649e7bfcdbf96264731f57e0",
        )
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.cart.item.with_raw_response.delete(
            "649e7bfcdbf96264731f57e0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.cart.item.with_streaming_response.delete(
            "649e7bfcdbf96264731f57e0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemDeleteResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.cart.item.with_raw_response.delete(
                "",
            )
