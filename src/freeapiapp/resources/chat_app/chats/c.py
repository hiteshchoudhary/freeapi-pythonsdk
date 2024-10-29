# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ....types.chat_app.chats.c_create_response import CCreateResponse

__all__ = ["CResource", "AsyncCResource"]


class CResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return CResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return CResourceWithStreamingResponse(self)

    def create(
        self,
        receiver_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CCreateResponse:
        """
        This API endpoint enables a logged-in user to initiate a personalized one-on-one
        chat interaction with another user.

        By providing correct `receiverId`, the API facilitates the creation of a private
        chat environment where participants can engage in direct and focused
        conversations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not receiver_id:
            raise ValueError(f"Expected a non-empty value for `receiver_id` but received {receiver_id!r}")
        return self._post(
            f"/chat-app/chats/c/{receiver_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CCreateResponse,
        )


class AsyncCResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncCResourceWithStreamingResponse(self)

    async def create(
        self,
        receiver_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CCreateResponse:
        """
        This API endpoint enables a logged-in user to initiate a personalized one-on-one
        chat interaction with another user.

        By providing correct `receiverId`, the API facilitates the creation of a private
        chat environment where participants can engage in direct and focused
        conversations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not receiver_id:
            raise ValueError(f"Expected a non-empty value for `receiver_id` but received {receiver_id!r}")
        return await self._post(
            f"/chat-app/chats/c/{receiver_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CCreateResponse,
        )


class CResourceWithRawResponse:
    def __init__(self, c: CResource) -> None:
        self._c = c

        self.create = to_raw_response_wrapper(
            c.create,
        )


class AsyncCResourceWithRawResponse:
    def __init__(self, c: AsyncCResource) -> None:
        self._c = c

        self.create = async_to_raw_response_wrapper(
            c.create,
        )


class CResourceWithStreamingResponse:
    def __init__(self, c: CResource) -> None:
        self._c = c

        self.create = to_streamed_response_wrapper(
            c.create,
        )


class AsyncCResourceWithStreamingResponse:
    def __init__(self, c: AsyncCResource) -> None:
        self._c = c

        self.create = async_to_streamed_response_wrapper(
            c.create,
        )
