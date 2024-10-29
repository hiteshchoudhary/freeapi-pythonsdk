# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["HTMLResource", "AsyncHTMLResource"]


class HTMLResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HTMLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return HTMLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTMLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return HTMLResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint provides the ability to retrieve an HTML template as a
        response.

        When accessing this endpoint, you will receive an HTML template that can be
        rendered and displayed in a web browser or used for further manipulation.

        This functionality is useful when you need to dynamically generate or retrieve
        HTML templates from your application's backend and deliver them to clients for
        rendering user interfaces or displaying structured content.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/kitchen-sink/response/html",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncHTMLResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHTMLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHTMLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTMLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncHTMLResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint provides the ability to retrieve an HTML template as a
        response.

        When accessing this endpoint, you will receive an HTML template that can be
        rendered and displayed in a web browser or used for further manipulation.

        This functionality is useful when you need to dynamically generate or retrieve
        HTML templates from your application's backend and deliver them to clients for
        rendering user interfaces or displaying structured content.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/kitchen-sink/response/html",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class HTMLResourceWithRawResponse:
    def __init__(self, html: HTMLResource) -> None:
        self._html = html

        self.retrieve = to_raw_response_wrapper(
            html.retrieve,
        )


class AsyncHTMLResourceWithRawResponse:
    def __init__(self, html: AsyncHTMLResource) -> None:
        self._html = html

        self.retrieve = async_to_raw_response_wrapper(
            html.retrieve,
        )


class HTMLResourceWithStreamingResponse:
    def __init__(self, html: HTMLResource) -> None:
        self._html = html

        self.retrieve = to_streamed_response_wrapper(
            html.retrieve,
        )


class AsyncHTMLResourceWithStreamingResponse:
    def __init__(self, html: AsyncHTMLResource) -> None:
        self._html = html

        self.retrieve = async_to_streamed_response_wrapper(
            html.retrieve,
        )
