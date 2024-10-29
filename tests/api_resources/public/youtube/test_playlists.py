# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.public.youtube import PlaylistListResponse, PlaylistRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlaylists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        playlist = client.public.youtube.playlists.retrieve(
            "PLRAV69dS1uWSx4erHGq8hW_GE-Eaj60r-",
        )
        assert_matches_type(PlaylistRetrieveResponse, playlist, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.public.youtube.playlists.with_raw_response.retrieve(
            "PLRAV69dS1uWSx4erHGq8hW_GE-Eaj60r-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = response.parse()
        assert_matches_type(PlaylistRetrieveResponse, playlist, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.public.youtube.playlists.with_streaming_response.retrieve(
            "PLRAV69dS1uWSx4erHGq8hW_GE-Eaj60r-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = response.parse()
            assert_matches_type(PlaylistRetrieveResponse, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `playlist_id` but received ''"):
            client.public.youtube.playlists.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        playlist = client.public.youtube.playlists.list()
        assert_matches_type(PlaylistListResponse, playlist, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        playlist = client.public.youtube.playlists.list(
            limit="5",
            page="1",
        )
        assert_matches_type(PlaylistListResponse, playlist, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.public.youtube.playlists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = response.parse()
        assert_matches_type(PlaylistListResponse, playlist, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.public.youtube.playlists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = response.parse()
            assert_matches_type(PlaylistListResponse, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPlaylists:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        playlist = await async_client.public.youtube.playlists.retrieve(
            "PLRAV69dS1uWSx4erHGq8hW_GE-Eaj60r-",
        )
        assert_matches_type(PlaylistRetrieveResponse, playlist, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.public.youtube.playlists.with_raw_response.retrieve(
            "PLRAV69dS1uWSx4erHGq8hW_GE-Eaj60r-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = await response.parse()
        assert_matches_type(PlaylistRetrieveResponse, playlist, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.public.youtube.playlists.with_streaming_response.retrieve(
            "PLRAV69dS1uWSx4erHGq8hW_GE-Eaj60r-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = await response.parse()
            assert_matches_type(PlaylistRetrieveResponse, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `playlist_id` but received ''"):
            await async_client.public.youtube.playlists.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        playlist = await async_client.public.youtube.playlists.list()
        assert_matches_type(PlaylistListResponse, playlist, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        playlist = await async_client.public.youtube.playlists.list(
            limit="5",
            page="1",
        )
        assert_matches_type(PlaylistListResponse, playlist, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.public.youtube.playlists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playlist = await response.parse()
        assert_matches_type(PlaylistListResponse, playlist, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.public.youtube.playlists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playlist = await response.parse()
            assert_matches_type(PlaylistListResponse, playlist, path=["response"])

        assert cast(Any, response.is_closed) is True
