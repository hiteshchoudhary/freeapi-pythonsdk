# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .request import (
    RequestResource,
    AsyncRequestResource,
    RequestResourceWithRawResponse,
    AsyncRequestResourceWithRawResponse,
    RequestResourceWithStreamingResponse,
    AsyncRequestResourceWithStreamingResponse,
)
from .response import (
    ResponseResource,
    AsyncResponseResource,
    ResponseResourceWithRawResponse,
    AsyncResponseResourceWithRawResponse,
    ResponseResourceWithStreamingResponse,
    AsyncResponseResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .http_methods import (
    HTTPMethodsResource,
    AsyncHTTPMethodsResource,
    HTTPMethodsResourceWithRawResponse,
    AsyncHTTPMethodsResourceWithRawResponse,
    HTTPMethodsResourceWithStreamingResponse,
    AsyncHTTPMethodsResourceWithStreamingResponse,
)
from .status_codes import (
    StatusCodesResource,
    AsyncStatusCodesResource,
    StatusCodesResourceWithRawResponse,
    AsyncStatusCodesResourceWithRawResponse,
    StatusCodesResourceWithStreamingResponse,
    AsyncStatusCodesResourceWithStreamingResponse,
)
from .request.request import RequestResource, AsyncRequestResource
from .response.response import ResponseResource, AsyncResponseResource

__all__ = ["KitchenSinkResource", "AsyncKitchenSinkResource"]


class KitchenSinkResource(SyncAPIResource):
    @cached_property
    def http_methods(self) -> HTTPMethodsResource:
        return HTTPMethodsResource(self._client)

    @cached_property
    def status_codes(self) -> StatusCodesResource:
        return StatusCodesResource(self._client)

    @cached_property
    def request(self) -> RequestResource:
        return RequestResource(self._client)

    @cached_property
    def response(self) -> ResponseResource:
        return ResponseResource(self._client)

    @cached_property
    def with_raw_response(self) -> KitchenSinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return KitchenSinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KitchenSinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return KitchenSinkResourceWithStreamingResponse(self)


class AsyncKitchenSinkResource(AsyncAPIResource):
    @cached_property
    def http_methods(self) -> AsyncHTTPMethodsResource:
        return AsyncHTTPMethodsResource(self._client)

    @cached_property
    def status_codes(self) -> AsyncStatusCodesResource:
        return AsyncStatusCodesResource(self._client)

    @cached_property
    def request(self) -> AsyncRequestResource:
        return AsyncRequestResource(self._client)

    @cached_property
    def response(self) -> AsyncResponseResource:
        return AsyncResponseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKitchenSinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKitchenSinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKitchenSinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncKitchenSinkResourceWithStreamingResponse(self)


class KitchenSinkResourceWithRawResponse:
    def __init__(self, kitchen_sink: KitchenSinkResource) -> None:
        self._kitchen_sink = kitchen_sink

    @cached_property
    def http_methods(self) -> HTTPMethodsResourceWithRawResponse:
        return HTTPMethodsResourceWithRawResponse(self._kitchen_sink.http_methods)

    @cached_property
    def status_codes(self) -> StatusCodesResourceWithRawResponse:
        return StatusCodesResourceWithRawResponse(self._kitchen_sink.status_codes)

    @cached_property
    def request(self) -> RequestResourceWithRawResponse:
        return RequestResourceWithRawResponse(self._kitchen_sink.request)

    @cached_property
    def response(self) -> ResponseResourceWithRawResponse:
        return ResponseResourceWithRawResponse(self._kitchen_sink.response)


class AsyncKitchenSinkResourceWithRawResponse:
    def __init__(self, kitchen_sink: AsyncKitchenSinkResource) -> None:
        self._kitchen_sink = kitchen_sink

    @cached_property
    def http_methods(self) -> AsyncHTTPMethodsResourceWithRawResponse:
        return AsyncHTTPMethodsResourceWithRawResponse(self._kitchen_sink.http_methods)

    @cached_property
    def status_codes(self) -> AsyncStatusCodesResourceWithRawResponse:
        return AsyncStatusCodesResourceWithRawResponse(self._kitchen_sink.status_codes)

    @cached_property
    def request(self) -> AsyncRequestResourceWithRawResponse:
        return AsyncRequestResourceWithRawResponse(self._kitchen_sink.request)

    @cached_property
    def response(self) -> AsyncResponseResourceWithRawResponse:
        return AsyncResponseResourceWithRawResponse(self._kitchen_sink.response)


class KitchenSinkResourceWithStreamingResponse:
    def __init__(self, kitchen_sink: KitchenSinkResource) -> None:
        self._kitchen_sink = kitchen_sink

    @cached_property
    def http_methods(self) -> HTTPMethodsResourceWithStreamingResponse:
        return HTTPMethodsResourceWithStreamingResponse(self._kitchen_sink.http_methods)

    @cached_property
    def status_codes(self) -> StatusCodesResourceWithStreamingResponse:
        return StatusCodesResourceWithStreamingResponse(self._kitchen_sink.status_codes)

    @cached_property
    def request(self) -> RequestResourceWithStreamingResponse:
        return RequestResourceWithStreamingResponse(self._kitchen_sink.request)

    @cached_property
    def response(self) -> ResponseResourceWithStreamingResponse:
        return ResponseResourceWithStreamingResponse(self._kitchen_sink.response)


class AsyncKitchenSinkResourceWithStreamingResponse:
    def __init__(self, kitchen_sink: AsyncKitchenSinkResource) -> None:
        self._kitchen_sink = kitchen_sink

    @cached_property
    def http_methods(self) -> AsyncHTTPMethodsResourceWithStreamingResponse:
        return AsyncHTTPMethodsResourceWithStreamingResponse(self._kitchen_sink.http_methods)

    @cached_property
    def status_codes(self) -> AsyncStatusCodesResourceWithStreamingResponse:
        return AsyncStatusCodesResourceWithStreamingResponse(self._kitchen_sink.status_codes)

    @cached_property
    def request(self) -> AsyncRequestResourceWithStreamingResponse:
        return AsyncRequestResourceWithStreamingResponse(self._kitchen_sink.request)

    @cached_property
    def response(self) -> AsyncResponseResourceWithStreamingResponse:
        return AsyncResponseResourceWithStreamingResponse(self._kitchen_sink.response)
