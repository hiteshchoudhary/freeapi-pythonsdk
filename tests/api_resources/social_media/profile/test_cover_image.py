# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.social_media.profile import CoverImageUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCoverImage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        cover_image = client.social_media.profile.cover_image.update()
        assert_matches_type(CoverImageUpdateResponse, cover_image, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        cover_image = client.social_media.profile.cover_image.update(
            cover_image=b"raw file contents",
        )
        assert_matches_type(CoverImageUpdateResponse, cover_image, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.social_media.profile.cover_image.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cover_image = response.parse()
        assert_matches_type(CoverImageUpdateResponse, cover_image, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.social_media.profile.cover_image.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cover_image = response.parse()
            assert_matches_type(CoverImageUpdateResponse, cover_image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCoverImage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        cover_image = await async_client.social_media.profile.cover_image.update()
        assert_matches_type(CoverImageUpdateResponse, cover_image, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        cover_image = await async_client.social_media.profile.cover_image.update(
            cover_image=b"raw file contents",
        )
        assert_matches_type(CoverImageUpdateResponse, cover_image, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.profile.cover_image.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cover_image = await response.parse()
        assert_matches_type(CoverImageUpdateResponse, cover_image, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.profile.cover_image.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cover_image = await response.parse()
            assert_matches_type(CoverImageUpdateResponse, cover_image, path=["response"])

        assert cast(Any, response.is_closed) is True
