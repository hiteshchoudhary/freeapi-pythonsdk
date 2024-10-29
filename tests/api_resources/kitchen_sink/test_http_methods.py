# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.kitchen_sink import (
    HTTPMethodGetResponse,
    HTTPMethodPutResponse,
    HTTPMethodCreateResponse,
    HTTPMethodDeleteResponse,
    HTTPMethodUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHTTPMethods:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        http_method = client.kitchen_sink.http_methods.create()
        assert_matches_type(HTTPMethodCreateResponse, http_method, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.http_methods.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_method = response.parse()
        assert_matches_type(HTTPMethodCreateResponse, http_method, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.http_methods.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_method = response.parse()
            assert_matches_type(HTTPMethodCreateResponse, http_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        http_method = client.kitchen_sink.http_methods.update()
        assert_matches_type(HTTPMethodUpdateResponse, http_method, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.http_methods.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_method = response.parse()
        assert_matches_type(HTTPMethodUpdateResponse, http_method, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.http_methods.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_method = response.parse()
            assert_matches_type(HTTPMethodUpdateResponse, http_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        http_method = client.kitchen_sink.http_methods.delete()
        assert_matches_type(HTTPMethodDeleteResponse, http_method, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.http_methods.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_method = response.parse()
        assert_matches_type(HTTPMethodDeleteResponse, http_method, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.http_methods.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_method = response.parse()
            assert_matches_type(HTTPMethodDeleteResponse, http_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Freeapiapp) -> None:
        http_method = client.kitchen_sink.http_methods.get()
        assert_matches_type(HTTPMethodGetResponse, http_method, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.http_methods.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_method = response.parse()
        assert_matches_type(HTTPMethodGetResponse, http_method, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.http_methods.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_method = response.parse()
            assert_matches_type(HTTPMethodGetResponse, http_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_put(self, client: Freeapiapp) -> None:
        http_method = client.kitchen_sink.http_methods.put()
        assert_matches_type(HTTPMethodPutResponse, http_method, path=["response"])

    @parametrize
    def test_raw_response_put(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.http_methods.with_raw_response.put()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_method = response.parse()
        assert_matches_type(HTTPMethodPutResponse, http_method, path=["response"])

    @parametrize
    def test_streaming_response_put(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.http_methods.with_streaming_response.put() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_method = response.parse()
            assert_matches_type(HTTPMethodPutResponse, http_method, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHTTPMethods:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        http_method = await async_client.kitchen_sink.http_methods.create()
        assert_matches_type(HTTPMethodCreateResponse, http_method, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.http_methods.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_method = await response.parse()
        assert_matches_type(HTTPMethodCreateResponse, http_method, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.http_methods.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_method = await response.parse()
            assert_matches_type(HTTPMethodCreateResponse, http_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        http_method = await async_client.kitchen_sink.http_methods.update()
        assert_matches_type(HTTPMethodUpdateResponse, http_method, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.http_methods.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_method = await response.parse()
        assert_matches_type(HTTPMethodUpdateResponse, http_method, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.http_methods.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_method = await response.parse()
            assert_matches_type(HTTPMethodUpdateResponse, http_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        http_method = await async_client.kitchen_sink.http_methods.delete()
        assert_matches_type(HTTPMethodDeleteResponse, http_method, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.http_methods.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_method = await response.parse()
        assert_matches_type(HTTPMethodDeleteResponse, http_method, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.http_methods.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_method = await response.parse()
            assert_matches_type(HTTPMethodDeleteResponse, http_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncFreeapiapp) -> None:
        http_method = await async_client.kitchen_sink.http_methods.get()
        assert_matches_type(HTTPMethodGetResponse, http_method, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.http_methods.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_method = await response.parse()
        assert_matches_type(HTTPMethodGetResponse, http_method, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.http_methods.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_method = await response.parse()
            assert_matches_type(HTTPMethodGetResponse, http_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_put(self, async_client: AsyncFreeapiapp) -> None:
        http_method = await async_client.kitchen_sink.http_methods.put()
        assert_matches_type(HTTPMethodPutResponse, http_method, path=["response"])

    @parametrize
    async def test_raw_response_put(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.http_methods.with_raw_response.put()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_method = await response.parse()
        assert_matches_type(HTTPMethodPutResponse, http_method, path=["response"])

    @parametrize
    async def test_streaming_response_put(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.http_methods.with_streaming_response.put() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_method = await response.parse()
            assert_matches_type(HTTPMethodPutResponse, http_method, path=["response"])

        assert cast(Any, response.is_closed) is True
