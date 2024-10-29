# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.kitchen_sink.status_code_list_response import StatusCodeListResponse

__all__ = ["StatusCodesResource", "AsyncStatusCodesResource"]


class StatusCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return StatusCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return StatusCodesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        status_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This API endpoint allows users to retrieve detailed information about a specific
        `HTTP` status code.

        By providing the desired status code as a parameter in the URL, users can obtain
        relevant information, including the meaning, description, and type associated
        with that particular status code.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not status_code:
            raise ValueError(f"Expected a non-empty value for `status_code` but received {status_code!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/kitchen-sink/status-codes/{status_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusCodeListResponse:
        """
        This API endpoint is designed to provide a comprehensive list of all possible
        **HTTP** status codes defined by the `HTTP/1.1` specification.

        It serves as a reference or informational resource to retrieve detailed
        information about each **HTTP** status code and its corresponding meaning.
        """
        return self._get(
            "/kitchen-sink/status-codes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatusCodeListResponse,
        )


class AsyncStatusCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatusCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncStatusCodesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        status_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This API endpoint allows users to retrieve detailed information about a specific
        `HTTP` status code.

        By providing the desired status code as a parameter in the URL, users can obtain
        relevant information, including the meaning, description, and type associated
        with that particular status code.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not status_code:
            raise ValueError(f"Expected a non-empty value for `status_code` but received {status_code!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/kitchen-sink/status-codes/{status_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusCodeListResponse:
        """
        This API endpoint is designed to provide a comprehensive list of all possible
        **HTTP** status codes defined by the `HTTP/1.1` specification.

        It serves as a reference or informational resource to retrieve detailed
        information about each **HTTP** status code and its corresponding meaning.
        """
        return await self._get(
            "/kitchen-sink/status-codes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatusCodeListResponse,
        )


class StatusCodesResourceWithRawResponse:
    def __init__(self, status_codes: StatusCodesResource) -> None:
        self._status_codes = status_codes

        self.retrieve = to_raw_response_wrapper(
            status_codes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            status_codes.list,
        )


class AsyncStatusCodesResourceWithRawResponse:
    def __init__(self, status_codes: AsyncStatusCodesResource) -> None:
        self._status_codes = status_codes

        self.retrieve = async_to_raw_response_wrapper(
            status_codes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            status_codes.list,
        )


class StatusCodesResourceWithStreamingResponse:
    def __init__(self, status_codes: StatusCodesResource) -> None:
        self._status_codes = status_codes

        self.retrieve = to_streamed_response_wrapper(
            status_codes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            status_codes.list,
        )


class AsyncStatusCodesResourceWithStreamingResponse:
    def __init__(self, status_codes: AsyncStatusCodesResource) -> None:
        self._status_codes = status_codes

        self.retrieve = async_to_streamed_response_wrapper(
            status_codes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            status_codes.list,
        )
