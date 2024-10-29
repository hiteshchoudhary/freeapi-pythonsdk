# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.chat_app import MessageDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        message = client.chat_app.messages.delete(
            message_id="660c01cef9b076f062b161a8",
            chat_id="64ce7766307617f3a412b803",
        )
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.chat_app.messages.with_raw_response.delete(
            message_id="660c01cef9b076f062b161a8",
            chat_id="64ce7766307617f3a412b803",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.chat_app.messages.with_streaming_response.delete(
            message_id="660c01cef9b076f062b161a8",
            chat_id="64ce7766307617f3a412b803",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageDeleteResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chat_app.messages.with_raw_response.delete(
                message_id="660c01cef9b076f062b161a8",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.chat_app.messages.with_raw_response.delete(
                message_id="",
                chat_id="64ce7766307617f3a412b803",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        message = await async_client.chat_app.messages.delete(
            message_id="660c01cef9b076f062b161a8",
            chat_id="64ce7766307617f3a412b803",
        )
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.chat_app.messages.with_raw_response.delete(
            message_id="660c01cef9b076f062b161a8",
            chat_id="64ce7766307617f3a412b803",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.chat_app.messages.with_streaming_response.delete(
            message_id="660c01cef9b076f062b161a8",
            chat_id="64ce7766307617f3a412b803",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageDeleteResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chat_app.messages.with_raw_response.delete(
                message_id="660c01cef9b076f062b161a8",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.chat_app.messages.with_raw_response.delete(
                message_id="",
                chat_id="64ce7766307617f3a412b803",
            )
