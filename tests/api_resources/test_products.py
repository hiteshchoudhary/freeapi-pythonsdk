# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types import (
    ProductListResponse,
    ProductCreateResponse,
    ProductDeleteResponse,
    ProductUpdateResponse,
    ProductRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        product = client.products.create()
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        product = client.products.create(
            category="649865ab297b287175aec1d7",
            description="New description number 2",
            main_image=b"raw file contents",
            name="Kids product",
            price="230",
            stock="30",
            sub_images=b"raw file contents",
        )
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.products.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.products.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductCreateResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        product = client.products.retrieve(
            "649d23e0aceaf82a41d5d34c",
        )
        assert_matches_type(ProductRetrieveResponse, product, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.products.with_raw_response.retrieve(
            "649d23e0aceaf82a41d5d34c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductRetrieveResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.products.with_streaming_response.retrieve(
            "649d23e0aceaf82a41d5d34c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductRetrieveResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        product = client.products.update(
            product_id="649d23e0aceaf82a41d5d34c",
        )
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        product = client.products.update(
            product_id="649d23e0aceaf82a41d5d34c",
            category="647c406165391b736260db2b",
            description="Updated desc",
            main_image=b"raw file contents",
            name="Updated name",
            price="1234",
            stock="20",
            sub_images=b"raw file contents",
        )
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.products.with_raw_response.update(
            product_id="649d23e0aceaf82a41d5d34c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.products.with_streaming_response.update(
            product_id="649d23e0aceaf82a41d5d34c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductUpdateResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.with_raw_response.update(
                product_id="",
            )

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        product = client.products.list()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        product = client.products.list(
            limit="10",
            page="1",
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        product = client.products.delete(
            "649d23e0aceaf82a41d5d34c",
        )
        assert_matches_type(ProductDeleteResponse, product, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.products.with_raw_response.delete(
            "649d23e0aceaf82a41d5d34c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductDeleteResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.products.with_streaming_response.delete(
            "649d23e0aceaf82a41d5d34c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductDeleteResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.with_raw_response.delete(
                "",
            )


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        product = await async_client.products.create()
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        product = await async_client.products.create(
            category="649865ab297b287175aec1d7",
            description="New description number 2",
            main_image=b"raw file contents",
            name="Kids product",
            price="230",
            stock="30",
            sub_images=b"raw file contents",
        )
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.products.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.products.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductCreateResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        product = await async_client.products.retrieve(
            "649d23e0aceaf82a41d5d34c",
        )
        assert_matches_type(ProductRetrieveResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.products.with_raw_response.retrieve(
            "649d23e0aceaf82a41d5d34c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductRetrieveResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.products.with_streaming_response.retrieve(
            "649d23e0aceaf82a41d5d34c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductRetrieveResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        product = await async_client.products.update(
            product_id="649d23e0aceaf82a41d5d34c",
        )
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        product = await async_client.products.update(
            product_id="649d23e0aceaf82a41d5d34c",
            category="647c406165391b736260db2b",
            description="Updated desc",
            main_image=b"raw file contents",
            name="Updated name",
            price="1234",
            stock="20",
            sub_images=b"raw file contents",
        )
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.products.with_raw_response.update(
            product_id="649d23e0aceaf82a41d5d34c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.products.with_streaming_response.update(
            product_id="649d23e0aceaf82a41d5d34c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductUpdateResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.with_raw_response.update(
                product_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        product = await async_client.products.list()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        product = await async_client.products.list(
            limit="10",
            page="1",
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        product = await async_client.products.delete(
            "649d23e0aceaf82a41d5d34c",
        )
        assert_matches_type(ProductDeleteResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.products.with_raw_response.delete(
            "649d23e0aceaf82a41d5d34c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductDeleteResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.products.with_streaming_response.delete(
            "649d23e0aceaf82a41d5d34c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductDeleteResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.with_raw_response.delete(
                "",
            )
