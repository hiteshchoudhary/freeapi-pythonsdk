# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.kitchen_sink.request import QueryParameterRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueryParameter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        query_parameter = client.kitchen_sink.request.query_parameter.retrieve()
        assert_matches_type(QueryParameterRetrieveResponse, query_parameter, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Freeapiapp) -> None:
        query_parameter = client.kitchen_sink.request.query_parameter.retrieve(
            query1="value1",
            query2="value2",
            query3="value3",
        )
        assert_matches_type(QueryParameterRetrieveResponse, query_parameter, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.request.query_parameter.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query_parameter = response.parse()
        assert_matches_type(QueryParameterRetrieveResponse, query_parameter, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.request.query_parameter.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query_parameter = response.parse()
            assert_matches_type(QueryParameterRetrieveResponse, query_parameter, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQueryParameter:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        query_parameter = await async_client.kitchen_sink.request.query_parameter.retrieve()
        assert_matches_type(QueryParameterRetrieveResponse, query_parameter, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        query_parameter = await async_client.kitchen_sink.request.query_parameter.retrieve(
            query1="value1",
            query2="value2",
            query3="value3",
        )
        assert_matches_type(QueryParameterRetrieveResponse, query_parameter, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.request.query_parameter.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query_parameter = await response.parse()
        assert_matches_type(QueryParameterRetrieveResponse, query_parameter, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.request.query_parameter.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query_parameter = await response.parse()
            assert_matches_type(QueryParameterRetrieveResponse, query_parameter, path=["response"])

        assert cast(Any, response.is_closed) is True
