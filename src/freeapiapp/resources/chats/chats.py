# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .group import (
    GroupResource,
    AsyncGroupResource,
    GroupResourceWithRawResponse,
    AsyncGroupResourceWithRawResponse,
    GroupResourceWithStreamingResponse,
    AsyncGroupResourceWithStreamingResponse,
)
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
from ...types.chat_remove_response import ChatRemoveResponse

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    @cached_property
    def group(self) -> GroupResource:
        return GroupResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return ChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return ChatsResourceWithStreamingResponse(self)

    def remove(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatRemoveResponse:
        """
        This API endpoint empowers logged-in users to seamlessly delete a one-on-one
        chat conversation in which they are a participant.

        By sending a `DELETE` request to this endpoint with the relevant `chatId`, users
        can effectively remove the specified one-on-one chat, thereby enhancing their
        control over their chat interactions and facilitating a streamlined and
        personalized messaging experience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._delete(
            f"/chat-app/chats/remove/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatRemoveResponse,
        )


class AsyncChatsResource(AsyncAPIResource):
    @cached_property
    def group(self) -> AsyncGroupResource:
        return AsyncGroupResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncChatsResourceWithStreamingResponse(self)

    async def remove(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatRemoveResponse:
        """
        This API endpoint empowers logged-in users to seamlessly delete a one-on-one
        chat conversation in which they are a participant.

        By sending a `DELETE` request to this endpoint with the relevant `chatId`, users
        can effectively remove the specified one-on-one chat, thereby enhancing their
        control over their chat interactions and facilitating a streamlined and
        personalized messaging experience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._delete(
            f"/chat-app/chats/remove/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatRemoveResponse,
        )


class ChatsResourceWithRawResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.remove = to_raw_response_wrapper(
            chats.remove,
        )

    @cached_property
    def group(self) -> GroupResourceWithRawResponse:
        return GroupResourceWithRawResponse(self._chats.group)


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.remove = async_to_raw_response_wrapper(
            chats.remove,
        )

    @cached_property
    def group(self) -> AsyncGroupResourceWithRawResponse:
        return AsyncGroupResourceWithRawResponse(self._chats.group)


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.remove = to_streamed_response_wrapper(
            chats.remove,
        )

    @cached_property
    def group(self) -> GroupResourceWithStreamingResponse:
        return GroupResourceWithStreamingResponse(self._chats.group)


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.remove = async_to_streamed_response_wrapper(
            chats.remove,
        )

    @cached_property
    def group(self) -> AsyncGroupResourceWithStreamingResponse:
        return AsyncGroupResourceWithStreamingResponse(self._chats.group)
