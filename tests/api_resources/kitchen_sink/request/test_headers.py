# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.kitchen_sink.request import HeaderRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHeaders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        header = client.kitchen_sink.request.headers.retrieve()
        assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.request.headers.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        header = response.parse()
        assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.request.headers.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            header = response.parse()
            assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHeaders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        header = await async_client.kitchen_sink.request.headers.retrieve()
        assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.request.headers.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        header = await response.parse()
        assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.request.headers.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            header = await response.parse()
            assert_matches_type(HeaderRetrieveResponse, header, path=["response"])

        assert cast(Any, response.is_closed) is True
