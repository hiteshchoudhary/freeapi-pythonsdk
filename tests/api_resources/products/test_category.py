# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.products import CategoryRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        category = client.products.category.retrieve(
            category_id="649e792a64e7dba29b7265fe",
        )
        assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Freeapiapp) -> None:
        category = client.products.category.retrieve(
            category_id="649e792a64e7dba29b7265fe",
            limit="5",
            page="1",
        )
        assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.products.category.with_raw_response.retrieve(
            category_id="649e792a64e7dba29b7265fe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.products.category.with_streaming_response.retrieve(
            category_id="649e792a64e7dba29b7265fe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.products.category.with_raw_response.retrieve(
                category_id="",
            )


class TestAsyncCategory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        category = await async_client.products.category.retrieve(
            category_id="649e792a64e7dba29b7265fe",
        )
        assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        category = await async_client.products.category.retrieve(
            category_id="649e792a64e7dba29b7265fe",
            limit="5",
            page="1",
        )
        assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.products.category.with_raw_response.retrieve(
            category_id="649e792a64e7dba29b7265fe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.products.category.with_streaming_response.retrieve(
            category_id="649e792a64e7dba29b7265fe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryRetrieveResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.products.category.with_raw_response.retrieve(
                category_id="",
            )
