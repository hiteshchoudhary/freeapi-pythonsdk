# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types import (
    KitchenSinkResponseGzipResponse,
    KitchenSinkResponseBrotliResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKitchenSinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_image_svg(self, client: Freeapiapp) -> None:
        kitchen_sink = client.kitchen_sinks.image_svg()
        assert kitchen_sink is None

    @parametrize
    def test_raw_response_image_svg(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.with_raw_response.image_svg()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = response.parse()
        assert kitchen_sink is None

    @parametrize
    def test_streaming_response_image_svg(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.with_streaming_response.image_svg() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_images_jpeg(self, client: Freeapiapp) -> None:
        kitchen_sink = client.kitchen_sinks.images_jpeg()
        assert kitchen_sink is None

    @parametrize
    def test_raw_response_images_jpeg(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.with_raw_response.images_jpeg()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = response.parse()
        assert kitchen_sink is None

    @parametrize
    def test_streaming_response_images_jpeg(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.with_streaming_response.images_jpeg() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_images_jpg(self, client: Freeapiapp) -> None:
        kitchen_sink = client.kitchen_sinks.images_jpg()
        assert kitchen_sink is None

    @parametrize
    def test_raw_response_images_jpg(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.with_raw_response.images_jpg()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = response.parse()
        assert kitchen_sink is None

    @parametrize
    def test_streaming_response_images_jpg(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.with_streaming_response.images_jpg() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_images_png(self, client: Freeapiapp) -> None:
        kitchen_sink = client.kitchen_sinks.images_png()
        assert kitchen_sink is None

    @parametrize
    def test_raw_response_images_png(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.with_raw_response.images_png()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = response.parse()
        assert kitchen_sink is None

    @parametrize
    def test_streaming_response_images_png(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.with_streaming_response.images_png() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_images_webp(self, client: Freeapiapp) -> None:
        kitchen_sink = client.kitchen_sinks.images_webp()
        assert kitchen_sink is None

    @parametrize
    def test_raw_response_images_webp(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.with_raw_response.images_webp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = response.parse()
        assert kitchen_sink is None

    @parametrize
    def test_streaming_response_images_webp(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.with_streaming_response.images_webp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_redirect_to(self, client: Freeapiapp) -> None:
        kitchen_sink = client.kitchen_sinks.redirect_to()
        assert kitchen_sink is None

    @parametrize
    def test_method_redirect_to_with_all_params(self, client: Freeapiapp) -> None:
        kitchen_sink = client.kitchen_sinks.redirect_to(
            url="https://github.com",
        )
        assert kitchen_sink is None

    @parametrize
    def test_raw_response_redirect_to(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.with_raw_response.redirect_to()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = response.parse()
        assert kitchen_sink is None

    @parametrize
    def test_streaming_response_redirect_to(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.with_streaming_response.redirect_to() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_response_brotli(self, client: Freeapiapp) -> None:
        kitchen_sink = client.kitchen_sinks.response_brotli()
        assert_matches_type(KitchenSinkResponseBrotliResponse, kitchen_sink, path=["response"])

    @parametrize
    def test_raw_response_response_brotli(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.with_raw_response.response_brotli()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = response.parse()
        assert_matches_type(KitchenSinkResponseBrotliResponse, kitchen_sink, path=["response"])

    @parametrize
    def test_streaming_response_response_brotli(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.with_streaming_response.response_brotli() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = response.parse()
            assert_matches_type(KitchenSinkResponseBrotliResponse, kitchen_sink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_response_gzip(self, client: Freeapiapp) -> None:
        kitchen_sink = client.kitchen_sinks.response_gzip()
        assert_matches_type(KitchenSinkResponseGzipResponse, kitchen_sink, path=["response"])

    @parametrize
    def test_raw_response_response_gzip(self, client: Freeapiapp) -> None:
        response = client.kitchen_sinks.with_raw_response.response_gzip()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = response.parse()
        assert_matches_type(KitchenSinkResponseGzipResponse, kitchen_sink, path=["response"])

    @parametrize
    def test_streaming_response_response_gzip(self, client: Freeapiapp) -> None:
        with client.kitchen_sinks.with_streaming_response.response_gzip() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = response.parse()
            assert_matches_type(KitchenSinkResponseGzipResponse, kitchen_sink, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKitchenSinks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_image_svg(self, async_client: AsyncFreeapiapp) -> None:
        kitchen_sink = await async_client.kitchen_sinks.image_svg()
        assert kitchen_sink is None

    @parametrize
    async def test_raw_response_image_svg(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.with_raw_response.image_svg()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = await response.parse()
        assert kitchen_sink is None

    @parametrize
    async def test_streaming_response_image_svg(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.with_streaming_response.image_svg() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = await response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_images_jpeg(self, async_client: AsyncFreeapiapp) -> None:
        kitchen_sink = await async_client.kitchen_sinks.images_jpeg()
        assert kitchen_sink is None

    @parametrize
    async def test_raw_response_images_jpeg(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.with_raw_response.images_jpeg()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = await response.parse()
        assert kitchen_sink is None

    @parametrize
    async def test_streaming_response_images_jpeg(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.with_streaming_response.images_jpeg() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = await response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_images_jpg(self, async_client: AsyncFreeapiapp) -> None:
        kitchen_sink = await async_client.kitchen_sinks.images_jpg()
        assert kitchen_sink is None

    @parametrize
    async def test_raw_response_images_jpg(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.with_raw_response.images_jpg()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = await response.parse()
        assert kitchen_sink is None

    @parametrize
    async def test_streaming_response_images_jpg(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.with_streaming_response.images_jpg() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = await response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_images_png(self, async_client: AsyncFreeapiapp) -> None:
        kitchen_sink = await async_client.kitchen_sinks.images_png()
        assert kitchen_sink is None

    @parametrize
    async def test_raw_response_images_png(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.with_raw_response.images_png()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = await response.parse()
        assert kitchen_sink is None

    @parametrize
    async def test_streaming_response_images_png(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.with_streaming_response.images_png() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = await response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_images_webp(self, async_client: AsyncFreeapiapp) -> None:
        kitchen_sink = await async_client.kitchen_sinks.images_webp()
        assert kitchen_sink is None

    @parametrize
    async def test_raw_response_images_webp(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.with_raw_response.images_webp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = await response.parse()
        assert kitchen_sink is None

    @parametrize
    async def test_streaming_response_images_webp(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.with_streaming_response.images_webp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = await response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_redirect_to(self, async_client: AsyncFreeapiapp) -> None:
        kitchen_sink = await async_client.kitchen_sinks.redirect_to()
        assert kitchen_sink is None

    @parametrize
    async def test_method_redirect_to_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        kitchen_sink = await async_client.kitchen_sinks.redirect_to(
            url="https://github.com",
        )
        assert kitchen_sink is None

    @parametrize
    async def test_raw_response_redirect_to(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.with_raw_response.redirect_to()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = await response.parse()
        assert kitchen_sink is None

    @parametrize
    async def test_streaming_response_redirect_to(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.with_streaming_response.redirect_to() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = await response.parse()
            assert kitchen_sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_response_brotli(self, async_client: AsyncFreeapiapp) -> None:
        kitchen_sink = await async_client.kitchen_sinks.response_brotli()
        assert_matches_type(KitchenSinkResponseBrotliResponse, kitchen_sink, path=["response"])

    @parametrize
    async def test_raw_response_response_brotli(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.with_raw_response.response_brotli()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = await response.parse()
        assert_matches_type(KitchenSinkResponseBrotliResponse, kitchen_sink, path=["response"])

    @parametrize
    async def test_streaming_response_response_brotli(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.with_streaming_response.response_brotli() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = await response.parse()
            assert_matches_type(KitchenSinkResponseBrotliResponse, kitchen_sink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_response_gzip(self, async_client: AsyncFreeapiapp) -> None:
        kitchen_sink = await async_client.kitchen_sinks.response_gzip()
        assert_matches_type(KitchenSinkResponseGzipResponse, kitchen_sink, path=["response"])

    @parametrize
    async def test_raw_response_response_gzip(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sinks.with_raw_response.response_gzip()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kitchen_sink = await response.parse()
        assert_matches_type(KitchenSinkResponseGzipResponse, kitchen_sink, path=["response"])

    @parametrize
    async def test_streaming_response_response_gzip(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sinks.with_streaming_response.response_gzip() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kitchen_sink = await response.parse()
            assert_matches_type(KitchenSinkResponseGzipResponse, kitchen_sink, path=["response"])

        assert cast(Any, response.is_closed) is True
