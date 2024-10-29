# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.seed.todo_create_response import TodoCreateResponse

__all__ = ["TodosResource", "AsyncTodosResource"]


class TodosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TodosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return TodosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TodosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return TodosResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoCreateResponse:
        """
        This API endpoint is responsible for populating the database with dummy todo
        items.

        It allows developers to easily seed the database with a set of predefined todos
        for testing or development purposes.
        """
        return self._post(
            "/seed/todos",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoCreateResponse,
        )


class AsyncTodosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTodosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTodosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTodosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncTodosResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TodoCreateResponse:
        """
        This API endpoint is responsible for populating the database with dummy todo
        items.

        It allows developers to easily seed the database with a set of predefined todos
        for testing or development purposes.
        """
        return await self._post(
            "/seed/todos",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TodoCreateResponse,
        )


class TodosResourceWithRawResponse:
    def __init__(self, todos: TodosResource) -> None:
        self._todos = todos

        self.create = to_raw_response_wrapper(
            todos.create,
        )


class AsyncTodosResourceWithRawResponse:
    def __init__(self, todos: AsyncTodosResource) -> None:
        self._todos = todos

        self.create = async_to_raw_response_wrapper(
            todos.create,
        )


class TodosResourceWithStreamingResponse:
    def __init__(self, todos: TodosResource) -> None:
        self._todos = todos

        self.create = to_streamed_response_wrapper(
            todos.create,
        )


class AsyncTodosResourceWithStreamingResponse:
    def __init__(self, todos: AsyncTodosResource) -> None:
        self._todos = todos

        self.create = async_to_streamed_response_wrapper(
            todos.create,
        )
