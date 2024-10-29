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
from ...types.seed.chat_app_create_response import ChatAppCreateResponse

__all__ = ["ChatAppResource", "AsyncChatAppResource"]


class ChatAppResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatAppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return ChatAppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatAppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return ChatAppResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatAppCreateResponse:
        """
        This API endpoint is responsible for populating all the essential entities
        required for a chat app service in the database. It provides a convenient way
        for developers to initialize the chat app with dummy or sample data for testing
        or development purposes.
        """
        return self._post(
            "/seed/chat-app",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatAppCreateResponse,
        )


class AsyncChatAppResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatAppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncChatAppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatAppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncChatAppResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatAppCreateResponse:
        """
        This API endpoint is responsible for populating all the essential entities
        required for a chat app service in the database. It provides a convenient way
        for developers to initialize the chat app with dummy or sample data for testing
        or development purposes.
        """
        return await self._post(
            "/seed/chat-app",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatAppCreateResponse,
        )


class ChatAppResourceWithRawResponse:
    def __init__(self, chat_app: ChatAppResource) -> None:
        self._chat_app = chat_app

        self.create = to_raw_response_wrapper(
            chat_app.create,
        )


class AsyncChatAppResourceWithRawResponse:
    def __init__(self, chat_app: AsyncChatAppResource) -> None:
        self._chat_app = chat_app

        self.create = async_to_raw_response_wrapper(
            chat_app.create,
        )


class ChatAppResourceWithStreamingResponse:
    def __init__(self, chat_app: ChatAppResource) -> None:
        self._chat_app = chat_app

        self.create = to_streamed_response_wrapper(
            chat_app.create,
        )


class AsyncChatAppResourceWithStreamingResponse:
    def __init__(self, chat_app: AsyncChatAppResource) -> None:
        self._chat_app = chat_app

        self.create = async_to_streamed_response_wrapper(
            chat_app.create,
        )
