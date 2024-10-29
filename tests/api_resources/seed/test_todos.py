# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.seed import TodoCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTodos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        todo = client.seed.todos.create()
        assert_matches_type(TodoCreateResponse, todo, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.seed.todos.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = response.parse()
        assert_matches_type(TodoCreateResponse, todo, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.seed.todos.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = response.parse()
            assert_matches_type(TodoCreateResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTodos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        todo = await async_client.seed.todos.create()
        assert_matches_type(TodoCreateResponse, todo, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.seed.todos.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = await response.parse()
        assert_matches_type(TodoCreateResponse, todo, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.seed.todos.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = await response.parse()
            assert_matches_type(TodoCreateResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True
