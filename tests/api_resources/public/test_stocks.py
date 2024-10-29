# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.public import StockListResponse, StockRandomResponse, StockRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStocks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        stock = client.public.stocks.retrieve(
            "INFY",
        )
        assert_matches_type(StockRetrieveResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.public.stocks.with_raw_response.retrieve(
            "INFY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockRetrieveResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.public.stocks.with_streaming_response.retrieve(
            "INFY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockRetrieveResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stock_symbol` but received ''"):
            client.public.stocks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        stock = client.public.stocks.list()
        assert_matches_type(StockListResponse, stock, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        stock = client.public.stocks.list(
            inc="Symbol,Name,MarketCap,CurrentPrice",
            limit="2",
            page="1",
            query="tata",
        )
        assert_matches_type(StockListResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.public.stocks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockListResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.public.stocks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockListResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_random(self, client: Freeapiapp) -> None:
        stock = client.public.stocks.random()
        assert_matches_type(StockRandomResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_random(self, client: Freeapiapp) -> None:
        response = client.public.stocks.with_raw_response.random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockRandomResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_random(self, client: Freeapiapp) -> None:
        with client.public.stocks.with_streaming_response.random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockRandomResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStocks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        stock = await async_client.public.stocks.retrieve(
            "INFY",
        )
        assert_matches_type(StockRetrieveResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.public.stocks.with_raw_response.retrieve(
            "INFY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockRetrieveResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.public.stocks.with_streaming_response.retrieve(
            "INFY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockRetrieveResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stock_symbol` but received ''"):
            await async_client.public.stocks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        stock = await async_client.public.stocks.list()
        assert_matches_type(StockListResponse, stock, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        stock = await async_client.public.stocks.list(
            inc="Symbol,Name,MarketCap,CurrentPrice",
            limit="2",
            page="1",
            query="tata",
        )
        assert_matches_type(StockListResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.public.stocks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockListResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.public.stocks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockListResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_random(self, async_client: AsyncFreeapiapp) -> None:
        stock = await async_client.public.stocks.random()
        assert_matches_type(StockRandomResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_random(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.public.stocks.with_raw_response.random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockRandomResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_random(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.public.stocks.with_streaming_response.random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockRandomResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True
