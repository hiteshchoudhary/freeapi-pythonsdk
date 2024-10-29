# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .chats import (
    ChatsResource,
    AsyncChatsResource,
    ChatsResourceWithRawResponse,
    AsyncChatsResourceWithRawResponse,
    ChatsResourceWithStreamingResponse,
    AsyncChatsResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .chats.chats import ChatsResource, AsyncChatsResource

__all__ = ["ChatAppResource", "AsyncChatAppResource"]


class ChatAppResource(SyncAPIResource):
    @cached_property
    def chats(self) -> ChatsResource:
        return ChatsResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatAppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return ChatAppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatAppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return ChatAppResourceWithStreamingResponse(self)


class AsyncChatAppResource(AsyncAPIResource):
    @cached_property
    def chats(self) -> AsyncChatsResource:
        return AsyncChatsResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatAppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatAppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatAppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncChatAppResourceWithStreamingResponse(self)


class ChatAppResourceWithRawResponse:
    def __init__(self, chat_app: ChatAppResource) -> None:
        self._chat_app = chat_app

    @cached_property
    def chats(self) -> ChatsResourceWithRawResponse:
        return ChatsResourceWithRawResponse(self._chat_app.chats)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._chat_app.messages)


class AsyncChatAppResourceWithRawResponse:
    def __init__(self, chat_app: AsyncChatAppResource) -> None:
        self._chat_app = chat_app

    @cached_property
    def chats(self) -> AsyncChatsResourceWithRawResponse:
        return AsyncChatsResourceWithRawResponse(self._chat_app.chats)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._chat_app.messages)


class ChatAppResourceWithStreamingResponse:
    def __init__(self, chat_app: ChatAppResource) -> None:
        self._chat_app = chat_app

    @cached_property
    def chats(self) -> ChatsResourceWithStreamingResponse:
        return ChatsResourceWithStreamingResponse(self._chat_app.chats)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._chat_app.messages)


class AsyncChatAppResourceWithStreamingResponse:
    def __init__(self, chat_app: AsyncChatAppResource) -> None:
        self._chat_app = chat_app

    @cached_property
    def chats(self) -> AsyncChatsResourceWithStreamingResponse:
        return AsyncChatsResourceWithStreamingResponse(self._chat_app.chats)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._chat_app.messages)
