# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types import (
    TodoListResponse,
    TodoCreateResponse,
    TodoDeleteResponse,
    TodoUpdateResponse,
    TodoRetrieveResponse,
    TodoToggleStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTodos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        todo = client.todos.create()
        assert_matches_type(TodoCreateResponse, todo, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        todo = client.todos.create(
            description="Some description about todo which is optional",
            title="Contibute ReactJs",
        )
        assert_matches_type(TodoCreateResponse, todo, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.todos.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = response.parse()
        assert_matches_type(TodoCreateResponse, todo, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.todos.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = response.parse()
            assert_matches_type(TodoCreateResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        todo = client.todos.retrieve(
            "648e0741aeefd0cfa40adddd",
        )
        assert_matches_type(TodoRetrieveResponse, todo, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.todos.with_raw_response.retrieve(
            "648e0741aeefd0cfa40adddd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = response.parse()
        assert_matches_type(TodoRetrieveResponse, todo, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.todos.with_streaming_response.retrieve(
            "648e0741aeefd0cfa40adddd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = response.parse()
            assert_matches_type(TodoRetrieveResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `todo_id` but received ''"):
            client.todos.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        todo = client.todos.update(
            todo_id="648e0741aeefd0cfa40adddd",
        )
        assert_matches_type(TodoUpdateResponse, todo, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        todo = client.todos.update(
            todo_id="648e0741aeefd0cfa40adddd",
            description="A new description for the todo",
            title="A new title for the todo",
        )
        assert_matches_type(TodoUpdateResponse, todo, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.todos.with_raw_response.update(
            todo_id="648e0741aeefd0cfa40adddd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = response.parse()
        assert_matches_type(TodoUpdateResponse, todo, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.todos.with_streaming_response.update(
            todo_id="648e0741aeefd0cfa40adddd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = response.parse()
            assert_matches_type(TodoUpdateResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `todo_id` but received ''"):
            client.todos.with_raw_response.update(
                todo_id="",
            )

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        todo = client.todos.list()
        assert_matches_type(TodoListResponse, todo, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        todo = client.todos.list(
            complete="false",
            query="reactjs",
        )
        assert_matches_type(TodoListResponse, todo, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.todos.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = response.parse()
        assert_matches_type(TodoListResponse, todo, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.todos.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = response.parse()
            assert_matches_type(TodoListResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        todo = client.todos.delete(
            "648e0741aeefd0cfa40adddd",
        )
        assert_matches_type(TodoDeleteResponse, todo, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.todos.with_raw_response.delete(
            "648e0741aeefd0cfa40adddd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = response.parse()
        assert_matches_type(TodoDeleteResponse, todo, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.todos.with_streaming_response.delete(
            "648e0741aeefd0cfa40adddd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = response.parse()
            assert_matches_type(TodoDeleteResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `todo_id` but received ''"):
            client.todos.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_toggle_status(self, client: Freeapiapp) -> None:
        todo = client.todos.toggle_status(
            "648e0c0722147847623e0a00",
        )
        assert_matches_type(TodoToggleStatusResponse, todo, path=["response"])

    @parametrize
    def test_raw_response_toggle_status(self, client: Freeapiapp) -> None:
        response = client.todos.with_raw_response.toggle_status(
            "648e0c0722147847623e0a00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = response.parse()
        assert_matches_type(TodoToggleStatusResponse, todo, path=["response"])

    @parametrize
    def test_streaming_response_toggle_status(self, client: Freeapiapp) -> None:
        with client.todos.with_streaming_response.toggle_status(
            "648e0c0722147847623e0a00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = response.parse()
            assert_matches_type(TodoToggleStatusResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_toggle_status(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `todo_id` but received ''"):
            client.todos.with_raw_response.toggle_status(
                "",
            )


class TestAsyncTodos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        todo = await async_client.todos.create()
        assert_matches_type(TodoCreateResponse, todo, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        todo = await async_client.todos.create(
            description="Some description about todo which is optional",
            title="Contibute ReactJs",
        )
        assert_matches_type(TodoCreateResponse, todo, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.todos.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = await response.parse()
        assert_matches_type(TodoCreateResponse, todo, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.todos.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = await response.parse()
            assert_matches_type(TodoCreateResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        todo = await async_client.todos.retrieve(
            "648e0741aeefd0cfa40adddd",
        )
        assert_matches_type(TodoRetrieveResponse, todo, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.todos.with_raw_response.retrieve(
            "648e0741aeefd0cfa40adddd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = await response.parse()
        assert_matches_type(TodoRetrieveResponse, todo, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.todos.with_streaming_response.retrieve(
            "648e0741aeefd0cfa40adddd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = await response.parse()
            assert_matches_type(TodoRetrieveResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `todo_id` but received ''"):
            await async_client.todos.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        todo = await async_client.todos.update(
            todo_id="648e0741aeefd0cfa40adddd",
        )
        assert_matches_type(TodoUpdateResponse, todo, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        todo = await async_client.todos.update(
            todo_id="648e0741aeefd0cfa40adddd",
            description="A new description for the todo",
            title="A new title for the todo",
        )
        assert_matches_type(TodoUpdateResponse, todo, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.todos.with_raw_response.update(
            todo_id="648e0741aeefd0cfa40adddd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = await response.parse()
        assert_matches_type(TodoUpdateResponse, todo, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.todos.with_streaming_response.update(
            todo_id="648e0741aeefd0cfa40adddd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = await response.parse()
            assert_matches_type(TodoUpdateResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `todo_id` but received ''"):
            await async_client.todos.with_raw_response.update(
                todo_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        todo = await async_client.todos.list()
        assert_matches_type(TodoListResponse, todo, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        todo = await async_client.todos.list(
            complete="false",
            query="reactjs",
        )
        assert_matches_type(TodoListResponse, todo, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.todos.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = await response.parse()
        assert_matches_type(TodoListResponse, todo, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.todos.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = await response.parse()
            assert_matches_type(TodoListResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        todo = await async_client.todos.delete(
            "648e0741aeefd0cfa40adddd",
        )
        assert_matches_type(TodoDeleteResponse, todo, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.todos.with_raw_response.delete(
            "648e0741aeefd0cfa40adddd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = await response.parse()
        assert_matches_type(TodoDeleteResponse, todo, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.todos.with_streaming_response.delete(
            "648e0741aeefd0cfa40adddd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = await response.parse()
            assert_matches_type(TodoDeleteResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `todo_id` but received ''"):
            await async_client.todos.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_toggle_status(self, async_client: AsyncFreeapiapp) -> None:
        todo = await async_client.todos.toggle_status(
            "648e0c0722147847623e0a00",
        )
        assert_matches_type(TodoToggleStatusResponse, todo, path=["response"])

    @parametrize
    async def test_raw_response_toggle_status(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.todos.with_raw_response.toggle_status(
            "648e0c0722147847623e0a00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        todo = await response.parse()
        assert_matches_type(TodoToggleStatusResponse, todo, path=["response"])

    @parametrize
    async def test_streaming_response_toggle_status(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.todos.with_streaming_response.toggle_status(
            "648e0c0722147847623e0a00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            todo = await response.parse()
            assert_matches_type(TodoToggleStatusResponse, todo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_toggle_status(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `todo_id` but received ''"):
            await async_client.todos.with_raw_response.toggle_status(
                "",
            )
