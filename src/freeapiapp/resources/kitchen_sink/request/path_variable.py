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
from ....types.kitchen_sink.request.path_variable_retrieve_response import PathVariableRetrieveResponse

__all__ = ["PathVariableResource", "AsyncPathVariableResource"]


class PathVariableResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PathVariableResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return PathVariableResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PathVariableResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return PathVariableResourceWithStreamingResponse(self)

    def retrieve(
        self,
        path_variable: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PathVariableRetrieveResponse:
        """
        The API endpoint allows you to retrieve the path variable being supplied in the
        URL.

        By accessing this endpoint, you can obtain the specific value provided as a path
        parameter in the URL.

        This functionality is useful when you need to access and utilize **the dynamic
        portion of the URL** within your application or for further processing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_variable:
            raise ValueError(f"Expected a non-empty value for `path_variable` but received {path_variable!r}")
        return self._get(
            f"/kitchen-sink/request/path-variable/{path_variable}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PathVariableRetrieveResponse,
        )


class AsyncPathVariableResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPathVariableResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPathVariableResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPathVariableResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncPathVariableResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        path_variable: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PathVariableRetrieveResponse:
        """
        The API endpoint allows you to retrieve the path variable being supplied in the
        URL.

        By accessing this endpoint, you can obtain the specific value provided as a path
        parameter in the URL.

        This functionality is useful when you need to access and utilize **the dynamic
        portion of the URL** within your application or for further processing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_variable:
            raise ValueError(f"Expected a non-empty value for `path_variable` but received {path_variable!r}")
        return await self._get(
            f"/kitchen-sink/request/path-variable/{path_variable}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PathVariableRetrieveResponse,
        )


class PathVariableResourceWithRawResponse:
    def __init__(self, path_variable: PathVariableResource) -> None:
        self._path_variable = path_variable

        self.retrieve = to_raw_response_wrapper(
            path_variable.retrieve,
        )


class AsyncPathVariableResourceWithRawResponse:
    def __init__(self, path_variable: AsyncPathVariableResource) -> None:
        self._path_variable = path_variable

        self.retrieve = async_to_raw_response_wrapper(
            path_variable.retrieve,
        )


class PathVariableResourceWithStreamingResponse:
    def __init__(self, path_variable: PathVariableResource) -> None:
        self._path_variable = path_variable

        self.retrieve = to_streamed_response_wrapper(
            path_variable.retrieve,
        )


class AsyncPathVariableResourceWithStreamingResponse:
    def __init__(self, path_variable: AsyncPathVariableResource) -> None:
        self._path_variable = path_variable

        self.retrieve = async_to_streamed_response_wrapper(
            path_variable.retrieve,
        )
