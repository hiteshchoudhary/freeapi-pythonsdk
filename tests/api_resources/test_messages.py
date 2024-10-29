# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types import MessageListResponse, MessageSendResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        message = client.messages.list(
            "64d6722a5bda3332e4f368a9",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.messages.with_raw_response.list(
            "64d6722a5bda3332e4f368a9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.messages.with_streaming_response.list(
            "64d6722a5bda3332e4f368a9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.messages.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_send(self, client: Freeapiapp) -> None:
        message = client.messages.send(
            chat_id="64d6722a5bda3332e4f368a9",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    def test_method_send_with_all_params(self, client: Freeapiapp) -> None:
        message = client.messages.send(
            chat_id="64d6722a5bda3332e4f368a9",
            attachments=b"raw file contents",
            content="This is the messageer message prob long one for this testing the images",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    def test_raw_response_send(self, client: Freeapiapp) -> None:
        response = client.messages.with_raw_response.send(
            chat_id="64d6722a5bda3332e4f368a9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_send(self, client: Freeapiapp) -> None:
        with client.messages.with_streaming_response.send(
            chat_id="64d6722a5bda3332e4f368a9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.messages.with_raw_response.send(
                chat_id="",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        message = await async_client.messages.list(
            "64d6722a5bda3332e4f368a9",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.messages.with_raw_response.list(
            "64d6722a5bda3332e4f368a9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.messages.with_streaming_response.list(
            "64d6722a5bda3332e4f368a9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.messages.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_send(self, async_client: AsyncFreeapiapp) -> None:
        message = await async_client.messages.send(
            chat_id="64d6722a5bda3332e4f368a9",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        message = await async_client.messages.send(
            chat_id="64d6722a5bda3332e4f368a9",
            attachments=b"raw file contents",
            content="This is the messageer message prob long one for this testing the images",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.messages.with_raw_response.send(
            chat_id="64d6722a5bda3332e4f368a9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.messages.with_streaming_response.send(
            chat_id="64d6722a5bda3332e4f368a9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.messages.with_raw_response.send(
                chat_id="",
            )
