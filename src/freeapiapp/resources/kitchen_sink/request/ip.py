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
from ....types.kitchen_sink.request.ip_retrieve_response import IPRetrieveResponse

__all__ = ["IPResource", "AsyncIPResource"]


class IPResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return IPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return IPResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPRetrieveResponse:
        """
        This API endpoint is designed to provide the current client's IP (Internet
        Protocol) address.

        It allows users to retrieve the IP address from which the client is making the
        request to the API.
        """
        return self._get(
            "/kitchen-sink/request/ip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRetrieveResponse,
        )


class AsyncIPResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncIPResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPRetrieveResponse:
        """
        This API endpoint is designed to provide the current client's IP (Internet
        Protocol) address.

        It allows users to retrieve the IP address from which the client is making the
        request to the API.
        """
        return await self._get(
            "/kitchen-sink/request/ip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRetrieveResponse,
        )


class IPResourceWithRawResponse:
    def __init__(self, ip: IPResource) -> None:
        self._ip = ip

        self.retrieve = to_raw_response_wrapper(
            ip.retrieve,
        )


class AsyncIPResourceWithRawResponse:
    def __init__(self, ip: AsyncIPResource) -> None:
        self._ip = ip

        self.retrieve = async_to_raw_response_wrapper(
            ip.retrieve,
        )


class IPResourceWithStreamingResponse:
    def __init__(self, ip: IPResource) -> None:
        self._ip = ip

        self.retrieve = to_streamed_response_wrapper(
            ip.retrieve,
        )


class AsyncIPResourceWithStreamingResponse:
    def __init__(self, ip: AsyncIPResource) -> None:
        self._ip = ip

        self.retrieve = async_to_streamed_response_wrapper(
            ip.retrieve,
        )
