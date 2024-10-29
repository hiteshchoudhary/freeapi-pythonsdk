# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import todo_list_params, todo_create_params, todo_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.todo_list_response import TodoListResponse
from ..types.todo_create_response import TodoCreateResponse
from ..types.todo_delete_response import TodoDeleteResponse
from ..types.todo_update_response import TodoUpdateResponse
from ..types.todo_retrieve_response import TodoRetrieveResponse
from ..types.todo_toggle_status_response import TodoToggleStatusResponse

__all__ = ["TodosResource", "AsyncTodosResource"]


class TodosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TodosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return TodosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TodosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return TodosResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoCreateResponse:
        """
        The "Create Todo" API endpoint allows you to create a new todo item by providing
        the title and description as a request body.

        By accessing this endpoint and providing the necessary information, a new todo
        item will be created in the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/todos/",
            body=maybe_transform(
                {
                    "description": description,
                    "title": title,
                },
                todo_create_params.TodoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoCreateResponse,
        )

    def retrieve(
        self,
        todo_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoRetrieveResponse:
        """
        The API endpoint retrieves a specific todo item based on the todo ID provided as
        a path variable in the URL.

        When accessing this endpoint and specifying a valid todo ID in the URL, you will
        receive a response containing the details of the corresponding todo item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not todo_id:
            raise ValueError(f"Expected a non-empty value for `todo_id` but received {todo_id!r}")
        return self._get(
            f"/todos/{todo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoRetrieveResponse,
        )

    def update(
        self,
        todo_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoUpdateResponse:
        """
        The API endpoint is responsible for updating a todo based on the provided todo
        ID in the URL path variable.

        When accessing this endpoint and providing the updated todo title and
        description in the request body, the corresponding todo with the specified ID
        will be modified accordingly.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not todo_id:
            raise ValueError(f"Expected a non-empty value for `todo_id` but received {todo_id!r}")
        return self._patch(
            f"/todos/{todo_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "title": title,
                },
                todo_update_params.TodoUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoUpdateResponse,
        )

    def list(
        self,
        *,
        complete: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoListResponse:
        """
        The API endpoint allows you to retrieve all the added todos.

        When accessing this endpoint, you will receive a response containing a list of
        all the todos that have been added.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/todos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "complete": complete,
                        "query": query,
                    },
                    todo_list_params.TodoListParams,
                ),
            ),
            cast_to=TodoListResponse,
        )

    def delete(
        self,
        todo_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoDeleteResponse:
        """
        The API endpoint is responsible for deleting a todo item based on the provided
        todoID in the path variable.

        When accessing this endpoint and specifying the todoID in the URL, the
        corresponding todo item will be deleted from the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not todo_id:
            raise ValueError(f"Expected a non-empty value for `todo_id` but received {todo_id!r}")
        return self._delete(
            f"/todos/{todo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoDeleteResponse,
        )

    def toggle_status(
        self,
        todo_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoToggleStatusResponse:
        """
        The API endpoint is responsible for toggling the done status of a todo item.

        When accessing this endpoint and providing the necessary data, you can update
        the completion status of a specific todo item, marking it as either done or
        undone based on its current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not todo_id:
            raise ValueError(f"Expected a non-empty value for `todo_id` but received {todo_id!r}")
        return self._patch(
            f"/todos/toggle/status/{todo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoToggleStatusResponse,
        )


class AsyncTodosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTodosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTodosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTodosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncTodosResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoCreateResponse:
        """
        The "Create Todo" API endpoint allows you to create a new todo item by providing
        the title and description as a request body.

        By accessing this endpoint and providing the necessary information, a new todo
        item will be created in the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/todos/",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "title": title,
                },
                todo_create_params.TodoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoCreateResponse,
        )

    async def retrieve(
        self,
        todo_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoRetrieveResponse:
        """
        The API endpoint retrieves a specific todo item based on the todo ID provided as
        a path variable in the URL.

        When accessing this endpoint and specifying a valid todo ID in the URL, you will
        receive a response containing the details of the corresponding todo item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not todo_id:
            raise ValueError(f"Expected a non-empty value for `todo_id` but received {todo_id!r}")
        return await self._get(
            f"/todos/{todo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoRetrieveResponse,
        )

    async def update(
        self,
        todo_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoUpdateResponse:
        """
        The API endpoint is responsible for updating a todo based on the provided todo
        ID in the URL path variable.

        When accessing this endpoint and providing the updated todo title and
        description in the request body, the corresponding todo with the specified ID
        will be modified accordingly.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not todo_id:
            raise ValueError(f"Expected a non-empty value for `todo_id` but received {todo_id!r}")
        return await self._patch(
            f"/todos/{todo_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "title": title,
                },
                todo_update_params.TodoUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoUpdateResponse,
        )

    async def list(
        self,
        *,
        complete: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoListResponse:
        """
        The API endpoint allows you to retrieve all the added todos.

        When accessing this endpoint, you will receive a response containing a list of
        all the todos that have been added.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/todos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "complete": complete,
                        "query": query,
                    },
                    todo_list_params.TodoListParams,
                ),
            ),
            cast_to=TodoListResponse,
        )

    async def delete(
        self,
        todo_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoDeleteResponse:
        """
        The API endpoint is responsible for deleting a todo item based on the provided
        todoID in the path variable.

        When accessing this endpoint and specifying the todoID in the URL, the
        corresponding todo item will be deleted from the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not todo_id:
            raise ValueError(f"Expected a non-empty value for `todo_id` but received {todo_id!r}")
        return await self._delete(
            f"/todos/{todo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoDeleteResponse,
        )

    async def toggle_status(
        self,
        todo_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoToggleStatusResponse:
        """
        The API endpoint is responsible for toggling the done status of a todo item.

        When accessing this endpoint and providing the necessary data, you can update
        the completion status of a specific todo item, marking it as either done or
        undone based on its current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not todo_id:
            raise ValueError(f"Expected a non-empty value for `todo_id` but received {todo_id!r}")
        return await self._patch(
            f"/todos/toggle/status/{todo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoToggleStatusResponse,
        )


class TodosResourceWithRawResponse:
    def __init__(self, todos: TodosResource) -> None:
        self._todos = todos

        self.create = to_raw_response_wrapper(
            todos.create,
        )
        self.retrieve = to_raw_response_wrapper(
            todos.retrieve,
        )
        self.update = to_raw_response_wrapper(
            todos.update,
        )
        self.list = to_raw_response_wrapper(
            todos.list,
        )
        self.delete = to_raw_response_wrapper(
            todos.delete,
        )
        self.toggle_status = to_raw_response_wrapper(
            todos.toggle_status,
        )


class AsyncTodosResourceWithRawResponse:
    def __init__(self, todos: AsyncTodosResource) -> None:
        self._todos = todos

        self.create = async_to_raw_response_wrapper(
            todos.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            todos.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            todos.update,
        )
        self.list = async_to_raw_response_wrapper(
            todos.list,
        )
        self.delete = async_to_raw_response_wrapper(
            todos.delete,
        )
        self.toggle_status = async_to_raw_response_wrapper(
            todos.toggle_status,
        )


class TodosResourceWithStreamingResponse:
    def __init__(self, todos: TodosResource) -> None:
        self._todos = todos

        self.create = to_streamed_response_wrapper(
            todos.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            todos.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            todos.update,
        )
        self.list = to_streamed_response_wrapper(
            todos.list,
        )
        self.delete = to_streamed_response_wrapper(
            todos.delete,
        )
        self.toggle_status = to_streamed_response_wrapper(
            todos.toggle_status,
        )


class AsyncTodosResourceWithStreamingResponse:
    def __init__(self, todos: AsyncTodosResource) -> None:
        self._todos = todos

        self.create = async_to_streamed_response_wrapper(
            todos.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            todos.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            todos.update,
        )
        self.list = async_to_streamed_response_wrapper(
            todos.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            todos.delete,
        )
        self.toggle_status = async_to_streamed_response_wrapper(
            todos.toggle_status,
        )
