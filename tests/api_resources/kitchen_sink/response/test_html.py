# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHTML:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        html = client.kitchen_sink.response.html.retrieve()
        assert html is None

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.response.html.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        html = response.parse()
        assert html is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.response.html.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            html = response.parse()
            assert html is None

        assert cast(Any, response.is_closed) is True


class TestAsyncHTML:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        html = await async_client.kitchen_sink.response.html.retrieve()
        assert html is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.response.html.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        html = await response.parse()
        assert html is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.response.html.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            html = await response.parse()
            assert html is None

        assert cast(Any, response.is_closed) is True
