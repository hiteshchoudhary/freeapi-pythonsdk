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
from ....types.public.youtube.channel_list_response import ChannelListResponse

__all__ = ["ChannelResource", "AsyncChannelResource"]


class ChannelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChannelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return ChannelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return ChannelResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelListResponse:
        """
        This Channel Details API is your gateway to access comprehensive information
        about a specific YouTube channel.

        By leveraging a static JSON file, you can effortlessly retrieve and explore
        vital details, statistics, and metadata associated with the channel to build
        stunning YouTube like channel page UI.

        **Disclaimer:**

        Data provided by the API is static and not real-time.

        This simplifies the process of developing a **YouTube clone**, allowing
        developers to solely focus on UI design and creativity, without worrying about
        complex API key configuration.
        """
        return self._get(
            "/public/youtube/channel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelListResponse,
        )


class AsyncChannelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChannelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncChannelResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelListResponse:
        """
        This Channel Details API is your gateway to access comprehensive information
        about a specific YouTube channel.

        By leveraging a static JSON file, you can effortlessly retrieve and explore
        vital details, statistics, and metadata associated with the channel to build
        stunning YouTube like channel page UI.

        **Disclaimer:**

        Data provided by the API is static and not real-time.

        This simplifies the process of developing a **YouTube clone**, allowing
        developers to solely focus on UI design and creativity, without worrying about
        complex API key configuration.
        """
        return await self._get(
            "/public/youtube/channel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelListResponse,
        )


class ChannelResourceWithRawResponse:
    def __init__(self, channel: ChannelResource) -> None:
        self._channel = channel

        self.list = to_raw_response_wrapper(
            channel.list,
        )


class AsyncChannelResourceWithRawResponse:
    def __init__(self, channel: AsyncChannelResource) -> None:
        self._channel = channel

        self.list = async_to_raw_response_wrapper(
            channel.list,
        )


class ChannelResourceWithStreamingResponse:
    def __init__(self, channel: ChannelResource) -> None:
        self._channel = channel

        self.list = to_streamed_response_wrapper(
            channel.list,
        )


class AsyncChannelResourceWithStreamingResponse:
    def __init__(self, channel: AsyncChannelResource) -> None:
        self._channel = channel

        self.list = async_to_streamed_response_wrapper(
            channel.list,
        )
