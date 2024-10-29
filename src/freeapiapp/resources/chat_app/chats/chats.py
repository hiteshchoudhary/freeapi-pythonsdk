# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .c import (
    CResource,
    AsyncCResource,
    CResourceWithRawResponse,
    AsyncCResourceWithRawResponse,
    CResourceWithStreamingResponse,
    AsyncCResourceWithStreamingResponse,
)
from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.chat_app.chat_list_response import ChatListResponse

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def c(self) -> CResource:
        return CResource(self._client)

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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatListResponse:
        """
        Retrieve all chats associated with the logged-in user.

        This endpoint provides a comprehensive list of both individual and group chats,
        offering a centralized view of the user's communication interactions.

        Developers can utilize this endpoint to seamlessly gather chat metadata,
        facilitating efficient tracking and management of conversations within the
        application.
        """
        return self._get(
            "/chat-app/chats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatListResponse,
        )


class AsyncChatsResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def c(self) -> AsyncCResource:
        return AsyncCResource(self._client)

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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatListResponse:
        """
        Retrieve all chats associated with the logged-in user.

        This endpoint provides a comprehensive list of both individual and group chats,
        offering a centralized view of the user's communication interactions.

        Developers can utilize this endpoint to seamlessly gather chat metadata,
        facilitating efficient tracking and management of conversations within the
        application.
        """
        return await self._get(
            "/chat-app/chats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatListResponse,
        )


class ChatsResourceWithRawResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.list = to_raw_response_wrapper(
            chats.list,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._chats.users)

    @cached_property
    def c(self) -> CResourceWithRawResponse:
        return CResourceWithRawResponse(self._chats.c)


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.list = async_to_raw_response_wrapper(
            chats.list,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._chats.users)

    @cached_property
    def c(self) -> AsyncCResourceWithRawResponse:
        return AsyncCResourceWithRawResponse(self._chats.c)


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.list = to_streamed_response_wrapper(
            chats.list,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._chats.users)

    @cached_property
    def c(self) -> CResourceWithStreamingResponse:
        return CResourceWithStreamingResponse(self._chats.c)


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.list = async_to_streamed_response_wrapper(
            chats.list,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._chats.users)

    @cached_property
    def c(self) -> AsyncCResourceWithStreamingResponse:
        return AsyncCResourceWithStreamingResponse(self._chats.c)
