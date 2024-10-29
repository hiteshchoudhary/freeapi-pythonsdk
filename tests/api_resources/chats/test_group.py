# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.chats import (
    GroupLeaveResponse,
    GroupCreateResponse,
    GroupDeleteResponse,
    GroupUpdateResponse,
    GroupRetrieveResponse,
    GroupParticipantAddResponse,
    GroupParticipantRemoveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        group = client.chats.group.create()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        group = client.chats.group.create(
            name="My first group",
            participants=["64c940d8ffe6c671f4d049d0", "64c940d8ffe6c671f4d049cd"],
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.chats.group.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.chats.group.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupCreateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        group = client.chats.group.retrieve(
            "64ca9e166cabe93cce077e0a",
        )
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.chats.group.with_raw_response.retrieve(
            "64ca9e166cabe93cce077e0a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.chats.group.with_streaming_response.retrieve(
            "64ca9e166cabe93cce077e0a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupRetrieveResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.group.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        group = client.chats.group.update(
            chat_id="64ca9e166cabe93cce077e0a",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        group = client.chats.group.update(
            chat_id="64ca9e166cabe93cce077e0a",
            name="New friends",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.chats.group.with_raw_response.update(
            chat_id="64ca9e166cabe93cce077e0a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.chats.group.with_streaming_response.update(
            chat_id="64ca9e166cabe93cce077e0a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupUpdateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.group.with_raw_response.update(
                chat_id="",
            )

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        group = client.chats.group.delete(
            "64ca9e166cabe93cce077e0a",
        )
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.chats.group.with_raw_response.delete(
            "64ca9e166cabe93cce077e0a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.chats.group.with_streaming_response.delete(
            "64ca9e166cabe93cce077e0a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupDeleteResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.group.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_leave(self, client: Freeapiapp) -> None:
        group = client.chats.group.leave(
            "64dfc9f439dd3fa3cade4f3c",
        )
        assert_matches_type(GroupLeaveResponse, group, path=["response"])

    @parametrize
    def test_raw_response_leave(self, client: Freeapiapp) -> None:
        response = client.chats.group.with_raw_response.leave(
            "64dfc9f439dd3fa3cade4f3c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupLeaveResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_leave(self, client: Freeapiapp) -> None:
        with client.chats.group.with_streaming_response.leave(
            "64dfc9f439dd3fa3cade4f3c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupLeaveResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_leave(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.group.with_raw_response.leave(
                "",
            )

    @parametrize
    def test_method_participant_add(self, client: Freeapiapp) -> None:
        group = client.chats.group.participant_add(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        )
        assert_matches_type(GroupParticipantAddResponse, group, path=["response"])

    @parametrize
    def test_raw_response_participant_add(self, client: Freeapiapp) -> None:
        response = client.chats.group.with_raw_response.participant_add(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupParticipantAddResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_participant_add(self, client: Freeapiapp) -> None:
        with client.chats.group.with_streaming_response.participant_add(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupParticipantAddResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_participant_add(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.group.with_raw_response.participant_add(
                participant_id="64c940d8ffe6c671f4d049cd",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            client.chats.group.with_raw_response.participant_add(
                participant_id="",
                chat_id="64ca9e166cabe93cce077e0a",
            )

    @parametrize
    def test_method_participant_remove(self, client: Freeapiapp) -> None:
        group = client.chats.group.participant_remove(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        )
        assert_matches_type(GroupParticipantRemoveResponse, group, path=["response"])

    @parametrize
    def test_raw_response_participant_remove(self, client: Freeapiapp) -> None:
        response = client.chats.group.with_raw_response.participant_remove(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupParticipantRemoveResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_participant_remove(self, client: Freeapiapp) -> None:
        with client.chats.group.with_streaming_response.participant_remove(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupParticipantRemoveResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_participant_remove(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.group.with_raw_response.participant_remove(
                participant_id="64c940d8ffe6c671f4d049cd",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            client.chats.group.with_raw_response.participant_remove(
                participant_id="",
                chat_id="64ca9e166cabe93cce077e0a",
            )


class TestAsyncGroup:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        group = await async_client.chats.group.create()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        group = await async_client.chats.group.create(
            name="My first group",
            participants=["64c940d8ffe6c671f4d049d0", "64c940d8ffe6c671f4d049cd"],
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.chats.group.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.chats.group.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupCreateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        group = await async_client.chats.group.retrieve(
            "64ca9e166cabe93cce077e0a",
        )
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.chats.group.with_raw_response.retrieve(
            "64ca9e166cabe93cce077e0a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.chats.group.with_streaming_response.retrieve(
            "64ca9e166cabe93cce077e0a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupRetrieveResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.group.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        group = await async_client.chats.group.update(
            chat_id="64ca9e166cabe93cce077e0a",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        group = await async_client.chats.group.update(
            chat_id="64ca9e166cabe93cce077e0a",
            name="New friends",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.chats.group.with_raw_response.update(
            chat_id="64ca9e166cabe93cce077e0a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.chats.group.with_streaming_response.update(
            chat_id="64ca9e166cabe93cce077e0a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupUpdateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.group.with_raw_response.update(
                chat_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        group = await async_client.chats.group.delete(
            "64ca9e166cabe93cce077e0a",
        )
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.chats.group.with_raw_response.delete(
            "64ca9e166cabe93cce077e0a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.chats.group.with_streaming_response.delete(
            "64ca9e166cabe93cce077e0a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupDeleteResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.group.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_leave(self, async_client: AsyncFreeapiapp) -> None:
        group = await async_client.chats.group.leave(
            "64dfc9f439dd3fa3cade4f3c",
        )
        assert_matches_type(GroupLeaveResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_leave(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.chats.group.with_raw_response.leave(
            "64dfc9f439dd3fa3cade4f3c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupLeaveResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_leave(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.chats.group.with_streaming_response.leave(
            "64dfc9f439dd3fa3cade4f3c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupLeaveResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_leave(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.group.with_raw_response.leave(
                "",
            )

    @parametrize
    async def test_method_participant_add(self, async_client: AsyncFreeapiapp) -> None:
        group = await async_client.chats.group.participant_add(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        )
        assert_matches_type(GroupParticipantAddResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_participant_add(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.chats.group.with_raw_response.participant_add(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupParticipantAddResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_participant_add(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.chats.group.with_streaming_response.participant_add(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupParticipantAddResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_participant_add(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.group.with_raw_response.participant_add(
                participant_id="64c940d8ffe6c671f4d049cd",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            await async_client.chats.group.with_raw_response.participant_add(
                participant_id="",
                chat_id="64ca9e166cabe93cce077e0a",
            )

    @parametrize
    async def test_method_participant_remove(self, async_client: AsyncFreeapiapp) -> None:
        group = await async_client.chats.group.participant_remove(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        )
        assert_matches_type(GroupParticipantRemoveResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_participant_remove(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.chats.group.with_raw_response.participant_remove(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupParticipantRemoveResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_participant_remove(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.chats.group.with_streaming_response.participant_remove(
            participant_id="64c940d8ffe6c671f4d049cd",
            chat_id="64ca9e166cabe93cce077e0a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupParticipantRemoveResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_participant_remove(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.group.with_raw_response.participant_remove(
                participant_id="64c940d8ffe6c671f4d049cd",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            await async_client.chats.group.with_raw_response.participant_remove(
                participant_id="",
                chat_id="64ca9e166cabe93cce077e0a",
            )
