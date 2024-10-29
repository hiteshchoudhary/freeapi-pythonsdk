# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .xml import (
    XmlResource,
    AsyncXmlResource,
    XmlResourceWithRawResponse,
    AsyncXmlResourceWithRawResponse,
    XmlResourceWithStreamingResponse,
    AsyncXmlResourceWithStreamingResponse,
)
from .html import (
    HTMLResource,
    AsyncHTMLResource,
    HTMLResourceWithRawResponse,
    AsyncHTMLResourceWithRawResponse,
    HTMLResourceWithStreamingResponse,
    AsyncHTMLResourceWithStreamingResponse,
)
from .cache import (
    CacheResource,
    AsyncCacheResource,
    CacheResourceWithRawResponse,
    AsyncCacheResourceWithRawResponse,
    CacheResourceWithStreamingResponse,
    AsyncCacheResourceWithStreamingResponse,
)
from .headers import (
    HeadersResource,
    AsyncHeadersResource,
    HeadersResourceWithRawResponse,
    AsyncHeadersResourceWithRawResponse,
    HeadersResourceWithStreamingResponse,
    AsyncHeadersResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ResponseResource", "AsyncResponseResource"]


class ResponseResource(SyncAPIResource):
    @cached_property
    def headers(self) -> HeadersResource:
        return HeadersResource(self._client)

    @cached_property
    def cache(self) -> CacheResource:
        return CacheResource(self._client)

    @cached_property
    def html(self) -> HTMLResource:
        return HTMLResource(self._client)

    @cached_property
    def xml(self) -> XmlResource:
        return XmlResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResponseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return ResponseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return ResponseResourceWithStreamingResponse(self)


class AsyncResponseResource(AsyncAPIResource):
    @cached_property
    def headers(self) -> AsyncHeadersResource:
        return AsyncHeadersResource(self._client)

    @cached_property
    def cache(self) -> AsyncCacheResource:
        return AsyncCacheResource(self._client)

    @cached_property
    def html(self) -> AsyncHTMLResource:
        return AsyncHTMLResource(self._client)

    @cached_property
    def xml(self) -> AsyncXmlResource:
        return AsyncXmlResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResponseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncResponseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncResponseResourceWithStreamingResponse(self)


class ResponseResourceWithRawResponse:
    def __init__(self, response: ResponseResource) -> None:
        self._response = response

    @cached_property
    def headers(self) -> HeadersResourceWithRawResponse:
        return HeadersResourceWithRawResponse(self._response.headers)

    @cached_property
    def cache(self) -> CacheResourceWithRawResponse:
        return CacheResourceWithRawResponse(self._response.cache)

    @cached_property
    def html(self) -> HTMLResourceWithRawResponse:
        return HTMLResourceWithRawResponse(self._response.html)

    @cached_property
    def xml(self) -> XmlResourceWithRawResponse:
        return XmlResourceWithRawResponse(self._response.xml)


class AsyncResponseResourceWithRawResponse:
    def __init__(self, response: AsyncResponseResource) -> None:
        self._response = response

    @cached_property
    def headers(self) -> AsyncHeadersResourceWithRawResponse:
        return AsyncHeadersResourceWithRawResponse(self._response.headers)

    @cached_property
    def cache(self) -> AsyncCacheResourceWithRawResponse:
        return AsyncCacheResourceWithRawResponse(self._response.cache)

    @cached_property
    def html(self) -> AsyncHTMLResourceWithRawResponse:
        return AsyncHTMLResourceWithRawResponse(self._response.html)

    @cached_property
    def xml(self) -> AsyncXmlResourceWithRawResponse:
        return AsyncXmlResourceWithRawResponse(self._response.xml)


class ResponseResourceWithStreamingResponse:
    def __init__(self, response: ResponseResource) -> None:
        self._response = response

    @cached_property
    def headers(self) -> HeadersResourceWithStreamingResponse:
        return HeadersResourceWithStreamingResponse(self._response.headers)

    @cached_property
    def cache(self) -> CacheResourceWithStreamingResponse:
        return CacheResourceWithStreamingResponse(self._response.cache)

    @cached_property
    def html(self) -> HTMLResourceWithStreamingResponse:
        return HTMLResourceWithStreamingResponse(self._response.html)

    @cached_property
    def xml(self) -> XmlResourceWithStreamingResponse:
        return XmlResourceWithStreamingResponse(self._response.xml)


class AsyncResponseResourceWithStreamingResponse:
    def __init__(self, response: AsyncResponseResource) -> None:
        self._response = response

    @cached_property
    def headers(self) -> AsyncHeadersResourceWithStreamingResponse:
        return AsyncHeadersResourceWithStreamingResponse(self._response.headers)

    @cached_property
    def cache(self) -> AsyncCacheResourceWithStreamingResponse:
        return AsyncCacheResourceWithStreamingResponse(self._response.cache)

    @cached_property
    def html(self) -> AsyncHTMLResourceWithStreamingResponse:
        return AsyncHTMLResourceWithStreamingResponse(self._response.html)

    @cached_property
    def xml(self) -> AsyncXmlResourceWithStreamingResponse:
        return AsyncXmlResourceWithStreamingResponse(self._response.xml)
