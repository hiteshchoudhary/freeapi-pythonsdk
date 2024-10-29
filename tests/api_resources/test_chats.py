# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types import ChatRemoveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_remove(self, client: Freeapiapp) -> None:
        chat = client.chats.remove(
            "64ce7766307617f3a412b803",
        )
        assert_matches_type(ChatRemoveResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Freeapiapp) -> None:
        response = client.chats.with_raw_response.remove(
            "64ce7766307617f3a412b803",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatRemoveResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Freeapiapp) -> None:
        with client.chats.with_streaming_response.remove(
            "64ce7766307617f3a412b803",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatRemoveResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.remove(
                "",
            )


class TestAsyncChats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_remove(self, async_client: AsyncFreeapiapp) -> None:
        chat = await async_client.chats.remove(
            "64ce7766307617f3a412b803",
        )
        assert_matches_type(ChatRemoveResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.chats.with_raw_response.remove(
            "64ce7766307617f3a412b803",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatRemoveResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.chats.with_streaming_response.remove(
            "64ce7766307617f3a412b803",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatRemoveResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.remove(
                "",
            )
