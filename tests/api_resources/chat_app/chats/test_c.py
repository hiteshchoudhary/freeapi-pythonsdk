# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.chat_app.chats import CCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestC:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        c = client.chat_app.chats.c.create(
            "64c940d8ffe6c671f4d049d6",
        )
        assert_matches_type(CCreateResponse, c, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.chat_app.chats.c.with_raw_response.create(
            "64c940d8ffe6c671f4d049d6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        c = response.parse()
        assert_matches_type(CCreateResponse, c, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.chat_app.chats.c.with_streaming_response.create(
            "64c940d8ffe6c671f4d049d6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            c = response.parse()
            assert_matches_type(CCreateResponse, c, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `receiver_id` but received ''"):
            client.chat_app.chats.c.with_raw_response.create(
                "",
            )


class TestAsyncC:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        c = await async_client.chat_app.chats.c.create(
            "64c940d8ffe6c671f4d049d6",
        )
        assert_matches_type(CCreateResponse, c, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.chat_app.chats.c.with_raw_response.create(
            "64c940d8ffe6c671f4d049d6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        c = await response.parse()
        assert_matches_type(CCreateResponse, c, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.chat_app.chats.c.with_streaming_response.create(
            "64c940d8ffe6c671f4d049d6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            c = await response.parse()
            assert_matches_type(CCreateResponse, c, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `receiver_id` but received ''"):
            await async_client.chat_app.chats.c.with_raw_response.create(
                "",
            )
