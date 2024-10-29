# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.social_media.follow import FollowingListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFollowing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        following = client.social_media.follow.following.list(
            username="abdiel_breitenberg22",
        )
        assert_matches_type(FollowingListResponse, following, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        following = client.social_media.follow.following.list(
            username="abdiel_breitenberg22",
            limit="5",
            page="1",
        )
        assert_matches_type(FollowingListResponse, following, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.social_media.follow.following.with_raw_response.list(
            username="abdiel_breitenberg22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = response.parse()
        assert_matches_type(FollowingListResponse, following, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.social_media.follow.following.with_streaming_response.list(
            username="abdiel_breitenberg22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = response.parse()
            assert_matches_type(FollowingListResponse, following, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.social_media.follow.following.with_raw_response.list(
                username="",
            )


class TestAsyncFollowing:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        following = await async_client.social_media.follow.following.list(
            username="abdiel_breitenberg22",
        )
        assert_matches_type(FollowingListResponse, following, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        following = await async_client.social_media.follow.following.list(
            username="abdiel_breitenberg22",
            limit="5",
            page="1",
        )
        assert_matches_type(FollowingListResponse, following, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.follow.following.with_raw_response.list(
            username="abdiel_breitenberg22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = await response.parse()
        assert_matches_type(FollowingListResponse, following, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.follow.following.with_streaming_response.list(
            username="abdiel_breitenberg22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = await response.parse()
            assert_matches_type(FollowingListResponse, following, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.social_media.follow.following.with_raw_response.list(
                username="",
            )
