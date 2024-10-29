# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.ecommerce import (
    CategoryListResponse,
    CategoryCreateResponse,
    CategoryDeleteResponse,
    CategoryUpdateResponse,
    CategoryRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        category = client.ecommerce.categories.create()
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        category = client.ecommerce.categories.create(
            name="shirts",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.ecommerce.categories.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.ecommerce.categories.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryCreateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        category = client.ecommerce.categories.retrieve(
            "6478dcdc025e3dd56c7acb79",
        )
        assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.ecommerce.categories.with_raw_response.retrieve(
            "6478dcdc025e3dd56c7acb79",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.ecommerce.categories.with_streaming_response.retrieve(
            "6478dcdc025e3dd56c7acb79",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.ecommerce.categories.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        category = client.ecommerce.categories.update(
            category_id="6478dcdc025e3dd56c7acb79",
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        category = client.ecommerce.categories.update(
            category_id="6478dcdc025e3dd56c7acb79",
            name="womens-wear",
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.ecommerce.categories.with_raw_response.update(
            category_id="6478dcdc025e3dd56c7acb79",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.ecommerce.categories.with_streaming_response.update(
            category_id="6478dcdc025e3dd56c7acb79",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryUpdateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.ecommerce.categories.with_raw_response.update(
                category_id="",
            )

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        category = client.ecommerce.categories.list()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        category = client.ecommerce.categories.list(
            limit="5",
            page="1",
        )
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.ecommerce.categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.ecommerce.categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        category = client.ecommerce.categories.delete(
            "6478dcdc025e3dd56c7acb79",
        )
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.ecommerce.categories.with_raw_response.delete(
            "6478dcdc025e3dd56c7acb79",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.ecommerce.categories.with_streaming_response.delete(
            "6478dcdc025e3dd56c7acb79",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryDeleteResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.ecommerce.categories.with_raw_response.delete(
                "",
            )


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        category = await async_client.ecommerce.categories.create()
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        category = await async_client.ecommerce.categories.create(
            name="shirts",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.categories.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.categories.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryCreateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        category = await async_client.ecommerce.categories.retrieve(
            "6478dcdc025e3dd56c7acb79",
        )
        assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.categories.with_raw_response.retrieve(
            "6478dcdc025e3dd56c7acb79",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.categories.with_streaming_response.retrieve(
            "6478dcdc025e3dd56c7acb79",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.ecommerce.categories.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        category = await async_client.ecommerce.categories.update(
            category_id="6478dcdc025e3dd56c7acb79",
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        category = await async_client.ecommerce.categories.update(
            category_id="6478dcdc025e3dd56c7acb79",
            name="womens-wear",
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.categories.with_raw_response.update(
            category_id="6478dcdc025e3dd56c7acb79",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.categories.with_streaming_response.update(
            category_id="6478dcdc025e3dd56c7acb79",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryUpdateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.ecommerce.categories.with_raw_response.update(
                category_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        category = await async_client.ecommerce.categories.list()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        category = await async_client.ecommerce.categories.list(
            limit="5",
            page="1",
        )
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        category = await async_client.ecommerce.categories.delete(
            "6478dcdc025e3dd56c7acb79",
        )
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.categories.with_raw_response.delete(
            "6478dcdc025e3dd56c7acb79",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.categories.with_streaming_response.delete(
            "6478dcdc025e3dd56c7acb79",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryDeleteResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.ecommerce.categories.with_raw_response.delete(
                "",
            )
