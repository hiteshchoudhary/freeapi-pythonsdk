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
from ....types.kitchen_sink.request.header_retrieve_response import HeaderRetrieveResponse

__all__ = ["HeadersResource", "AsyncHeadersResource"]


class HeadersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HeadersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return HeadersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HeadersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return HeadersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HeaderRetrieveResponse:
        """
        This API endpoint is designed to provide information about the headers included
        in an HTTP request made to the API.

        It allows users to retrieve the details of the headers sent in the request,
        including their names, values, and any additional relevant information.
        """
        return self._get(
            "/kitchen-sink/request/headers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeaderRetrieveResponse,
        )


class AsyncHeadersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHeadersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncHeadersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHeadersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncHeadersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HeaderRetrieveResponse:
        """
        This API endpoint is designed to provide information about the headers included
        in an HTTP request made to the API.

        It allows users to retrieve the details of the headers sent in the request,
        including their names, values, and any additional relevant information.
        """
        return await self._get(
            "/kitchen-sink/request/headers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeaderRetrieveResponse,
        )


class HeadersResourceWithRawResponse:
    def __init__(self, headers: HeadersResource) -> None:
        self._headers = headers

        self.retrieve = to_raw_response_wrapper(
            headers.retrieve,
        )


class AsyncHeadersResourceWithRawResponse:
    def __init__(self, headers: AsyncHeadersResource) -> None:
        self._headers = headers

        self.retrieve = async_to_raw_response_wrapper(
            headers.retrieve,
        )


class HeadersResourceWithStreamingResponse:
    def __init__(self, headers: HeadersResource) -> None:
        self._headers = headers

        self.retrieve = to_streamed_response_wrapper(
            headers.retrieve,
        )


class AsyncHeadersResourceWithStreamingResponse:
    def __init__(self, headers: AsyncHeadersResource) -> None:
        self._headers = headers

        self.retrieve = async_to_streamed_response_wrapper(
            headers.retrieve,
        )
