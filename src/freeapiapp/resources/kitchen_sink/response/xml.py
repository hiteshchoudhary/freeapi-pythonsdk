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

__all__ = ["XmlResource", "AsyncXmlResource"]


class XmlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> XmlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return XmlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> XmlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return XmlResourceWithStreamingResponse(self)

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
        The API endpoint allows you to retrieve an XML template as a response.

        When accessing this endpoint, you will receive an XML template that can be used
        for various purposes, such as data interchange, configuration, or structured
        content representation.

        This functionality is particularly useful when you need to dynamically generate
        or retrieve XML templates from your application's backend and deliver them to
        clients for processing, parsing, or integration with other systems that support
        XML data formats.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/kitchen-sink/response/xml",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncXmlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncXmlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncXmlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncXmlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncXmlResourceWithStreamingResponse(self)

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
        The API endpoint allows you to retrieve an XML template as a response.

        When accessing this endpoint, you will receive an XML template that can be used
        for various purposes, such as data interchange, configuration, or structured
        content representation.

        This functionality is particularly useful when you need to dynamically generate
        or retrieve XML templates from your application's backend and deliver them to
        clients for processing, parsing, or integration with other systems that support
        XML data formats.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/kitchen-sink/response/xml",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class XmlResourceWithRawResponse:
    def __init__(self, xml: XmlResource) -> None:
        self._xml = xml

        self.retrieve = to_raw_response_wrapper(
            xml.retrieve,
        )


class AsyncXmlResourceWithRawResponse:
    def __init__(self, xml: AsyncXmlResource) -> None:
        self._xml = xml

        self.retrieve = async_to_raw_response_wrapper(
            xml.retrieve,
        )


class XmlResourceWithStreamingResponse:
    def __init__(self, xml: XmlResource) -> None:
        self._xml = xml

        self.retrieve = to_streamed_response_wrapper(
            xml.retrieve,
        )


class AsyncXmlResourceWithStreamingResponse:
    def __init__(self, xml: AsyncXmlResource) -> None:
        self._xml = xml

        self.retrieve = async_to_streamed_response_wrapper(
            xml.retrieve,
        )
