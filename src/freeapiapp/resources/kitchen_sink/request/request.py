# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ip import (
    IPResource,
    AsyncIPResource,
    IPResourceWithRawResponse,
    AsyncIPResourceWithRawResponse,
    IPResourceWithStreamingResponse,
    AsyncIPResourceWithStreamingResponse,
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
from .user_agent import (
    UserAgentResource,
    AsyncUserAgentResource,
    UserAgentResourceWithRawResponse,
    AsyncUserAgentResourceWithRawResponse,
    UserAgentResourceWithStreamingResponse,
    AsyncUserAgentResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .path_variable import (
    PathVariableResource,
    AsyncPathVariableResource,
    PathVariableResourceWithRawResponse,
    AsyncPathVariableResourceWithRawResponse,
    PathVariableResourceWithStreamingResponse,
    AsyncPathVariableResourceWithStreamingResponse,
)
from .query_parameter import (
    QueryParameterResource,
    AsyncQueryParameterResource,
    QueryParameterResourceWithRawResponse,
    AsyncQueryParameterResourceWithRawResponse,
    QueryParameterResourceWithStreamingResponse,
    AsyncQueryParameterResourceWithStreamingResponse,
)

__all__ = ["RequestResource", "AsyncRequestResource"]


class RequestResource(SyncAPIResource):
    @cached_property
    def headers(self) -> HeadersResource:
        return HeadersResource(self._client)

    @cached_property
    def ip(self) -> IPResource:
        return IPResource(self._client)

    @cached_property
    def user_agent(self) -> UserAgentResource:
        return UserAgentResource(self._client)

    @cached_property
    def path_variable(self) -> PathVariableResource:
        return PathVariableResource(self._client)

    @cached_property
    def query_parameter(self) -> QueryParameterResource:
        return QueryParameterResource(self._client)

    @cached_property
    def with_raw_response(self) -> RequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return RequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return RequestResourceWithStreamingResponse(self)


class AsyncRequestResource(AsyncAPIResource):
    @cached_property
    def headers(self) -> AsyncHeadersResource:
        return AsyncHeadersResource(self._client)

    @cached_property
    def ip(self) -> AsyncIPResource:
        return AsyncIPResource(self._client)

    @cached_property
    def user_agent(self) -> AsyncUserAgentResource:
        return AsyncUserAgentResource(self._client)

    @cached_property
    def path_variable(self) -> AsyncPathVariableResource:
        return AsyncPathVariableResource(self._client)

    @cached_property
    def query_parameter(self) -> AsyncQueryParameterResource:
        return AsyncQueryParameterResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncRequestResourceWithStreamingResponse(self)


class RequestResourceWithRawResponse:
    def __init__(self, request: RequestResource) -> None:
        self._request = request

    @cached_property
    def headers(self) -> HeadersResourceWithRawResponse:
        return HeadersResourceWithRawResponse(self._request.headers)

    @cached_property
    def ip(self) -> IPResourceWithRawResponse:
        return IPResourceWithRawResponse(self._request.ip)

    @cached_property
    def user_agent(self) -> UserAgentResourceWithRawResponse:
        return UserAgentResourceWithRawResponse(self._request.user_agent)

    @cached_property
    def path_variable(self) -> PathVariableResourceWithRawResponse:
        return PathVariableResourceWithRawResponse(self._request.path_variable)

    @cached_property
    def query_parameter(self) -> QueryParameterResourceWithRawResponse:
        return QueryParameterResourceWithRawResponse(self._request.query_parameter)


class AsyncRequestResourceWithRawResponse:
    def __init__(self, request: AsyncRequestResource) -> None:
        self._request = request

    @cached_property
    def headers(self) -> AsyncHeadersResourceWithRawResponse:
        return AsyncHeadersResourceWithRawResponse(self._request.headers)

    @cached_property
    def ip(self) -> AsyncIPResourceWithRawResponse:
        return AsyncIPResourceWithRawResponse(self._request.ip)

    @cached_property
    def user_agent(self) -> AsyncUserAgentResourceWithRawResponse:
        return AsyncUserAgentResourceWithRawResponse(self._request.user_agent)

    @cached_property
    def path_variable(self) -> AsyncPathVariableResourceWithRawResponse:
        return AsyncPathVariableResourceWithRawResponse(self._request.path_variable)

    @cached_property
    def query_parameter(self) -> AsyncQueryParameterResourceWithRawResponse:
        return AsyncQueryParameterResourceWithRawResponse(self._request.query_parameter)


class RequestResourceWithStreamingResponse:
    def __init__(self, request: RequestResource) -> None:
        self._request = request

    @cached_property
    def headers(self) -> HeadersResourceWithStreamingResponse:
        return HeadersResourceWithStreamingResponse(self._request.headers)

    @cached_property
    def ip(self) -> IPResourceWithStreamingResponse:
        return IPResourceWithStreamingResponse(self._request.ip)

    @cached_property
    def user_agent(self) -> UserAgentResourceWithStreamingResponse:
        return UserAgentResourceWithStreamingResponse(self._request.user_agent)

    @cached_property
    def path_variable(self) -> PathVariableResourceWithStreamingResponse:
        return PathVariableResourceWithStreamingResponse(self._request.path_variable)

    @cached_property
    def query_parameter(self) -> QueryParameterResourceWithStreamingResponse:
        return QueryParameterResourceWithStreamingResponse(self._request.query_parameter)


class AsyncRequestResourceWithStreamingResponse:
    def __init__(self, request: AsyncRequestResource) -> None:
        self._request = request

    @cached_property
    def headers(self) -> AsyncHeadersResourceWithStreamingResponse:
        return AsyncHeadersResourceWithStreamingResponse(self._request.headers)

    @cached_property
    def ip(self) -> AsyncIPResourceWithStreamingResponse:
        return AsyncIPResourceWithStreamingResponse(self._request.ip)

    @cached_property
    def user_agent(self) -> AsyncUserAgentResourceWithStreamingResponse:
        return AsyncUserAgentResourceWithStreamingResponse(self._request.user_agent)

    @cached_property
    def path_variable(self) -> AsyncPathVariableResourceWithStreamingResponse:
        return AsyncPathVariableResourceWithStreamingResponse(self._request.path_variable)

    @cached_property
    def query_parameter(self) -> AsyncQueryParameterResourceWithStreamingResponse:
        return AsyncQueryParameterResourceWithStreamingResponse(self._request.query_parameter)
