# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.kitchen_sinks import (
    CookieCreateResponse,
    CookieRemoveResponse,
    CookieRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCookies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        cookie = client.kitchen_sinks.cookies.create()
        assert_matches_type(CookieCreateResponse, cookie, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        cookie = client.kitchen_sinks.cookies.create(
            foo="bar",
        )
        assert_matches_type(CookieCreateResponse, cookie, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.cookies.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cookie = response.parse()
        assert_matches_type(CookieCreateResponse, cookie, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.cookies.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cookie = response.parse()
            assert_matches_type(CookieCreateResponse, cookie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        cookie = client.kitchen_sinks.cookies.retrieve()
        assert_matches_type(CookieRetrieveResponse, cookie, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.cookies.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cookie = response.parse()
        assert_matches_type(CookieRetrieveResponse, cookie, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.cookies.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cookie = response.parse()
            assert_matches_type(CookieRetrieveResponse, cookie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove(self, client: Freeapiapp) -> None:
        cookie = client.kitchen_sinks.cookies.remove()
        assert_matches_type(CookieRemoveResponse, cookie, path=["response"])

    @parametrize
    def test_method_remove_with_all_params(self, client: Freeapiapp) -> None:
        cookie = client.kitchen_sinks.cookies.remove(
            cookie_key="foo",
        )
        assert_matches_type(CookieRemoveResponse, cookie, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.cookies.with_raw_response.remove()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cookie = response.parse()
        assert_matches_type(CookieRemoveResponse, cookie, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.cookies.with_streaming_response.remove() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cookie = response.parse()
            assert_matches_type(CookieRemoveResponse, cookie, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCookies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        cookie = await async_client.kitchen_sinks.cookies.create()
        assert_matches_type(CookieCreateResponse, cookie, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        cookie = await async_client.kitchen_sinks.cookies.create(
            foo="bar",
        )
        assert_matches_type(CookieCreateResponse, cookie, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.cookies.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cookie = await response.parse()
        assert_matches_type(CookieCreateResponse, cookie, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.cookies.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cookie = await response.parse()
            assert_matches_type(CookieCreateResponse, cookie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        cookie = await async_client.kitchen_sinks.cookies.retrieve()
        assert_matches_type(CookieRetrieveResponse, cookie, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.cookies.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cookie = await response.parse()
        assert_matches_type(CookieRetrieveResponse, cookie, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.cookies.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cookie = await response.parse()
            assert_matches_type(CookieRetrieveResponse, cookie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove(self, async_client: AsyncFreeapiapp) -> None:
        cookie = await async_client.kitchen_sinks.cookies.remove()
        assert_matches_type(CookieRemoveResponse, cookie, path=["response"])

    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        cookie = await async_client.kitchen_sinks.cookies.remove(
            cookie_key="foo",
        )
        assert_matches_type(CookieRemoveResponse, cookie, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.cookies.with_raw_response.remove()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cookie = await response.parse()
        assert_matches_type(CookieRemoveResponse, cookie, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.cookies.with_streaming_response.remove() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cookie = await response.parse()
            assert_matches_type(CookieRemoveResponse, cookie, path=["response"])

        assert cast(Any, response.is_closed) is True
