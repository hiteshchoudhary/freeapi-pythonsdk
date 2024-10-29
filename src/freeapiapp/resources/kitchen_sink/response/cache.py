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
from ....types.kitchen_sink.response.cache_retrieve_response import CacheRetrieveResponse

__all__ = ["CacheResource", "AsyncCacheResource"]


class CacheResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return CacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return CacheResourceWithStreamingResponse(self)

    def retrieve(
        self,
        cache_response_directive: str,
        *,
        time_to_live: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheRetrieveResponse:
        """
        - `Cache-control` is an HTTP header used to specify browser caching policies in
          both client requests and server responses.

        - Policies include how a resource is cached, where it’s cached and its maximum
          age before expiring (i.e., time to live)

        _For example,_

        `cache-control: max-age=120` means that the returned resource is valid for
        **120** seconds, after which the browser has to request a newer version.

        - The `public` (cacheResponseDirective) response directive indicates that a
          resource can be cached by any cache.

        - The `private` (cacheResponseDirective) response directive indicates that a
          resource is user specific - it can still be cached, but only on a client
          device. For example, a web page response marked as private can be cached by a
          desktop browser, but not a content delivery network (CDN).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not time_to_live:
            raise ValueError(f"Expected a non-empty value for `time_to_live` but received {time_to_live!r}")
        if not cache_response_directive:
            raise ValueError(
                f"Expected a non-empty value for `cache_response_directive` but received {cache_response_directive!r}"
            )
        return self._get(
            f"/kitchen-sink/response/cache/{time_to_live}/{cache_response_directive}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CacheRetrieveResponse,
        )


class AsyncCacheResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncCacheResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        cache_response_directive: str,
        *,
        time_to_live: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheRetrieveResponse:
        """
        - `Cache-control` is an HTTP header used to specify browser caching policies in
          both client requests and server responses.

        - Policies include how a resource is cached, where it’s cached and its maximum
          age before expiring (i.e., time to live)

        _For example,_

        `cache-control: max-age=120` means that the returned resource is valid for
        **120** seconds, after which the browser has to request a newer version.

        - The `public` (cacheResponseDirective) response directive indicates that a
          resource can be cached by any cache.

        - The `private` (cacheResponseDirective) response directive indicates that a
          resource is user specific - it can still be cached, but only on a client
          device. For example, a web page response marked as private can be cached by a
          desktop browser, but not a content delivery network (CDN).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not time_to_live:
            raise ValueError(f"Expected a non-empty value for `time_to_live` but received {time_to_live!r}")
        if not cache_response_directive:
            raise ValueError(
                f"Expected a non-empty value for `cache_response_directive` but received {cache_response_directive!r}"
            )
        return await self._get(
            f"/kitchen-sink/response/cache/{time_to_live}/{cache_response_directive}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CacheRetrieveResponse,
        )


class CacheResourceWithRawResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.retrieve = to_raw_response_wrapper(
            cache.retrieve,
        )


class AsyncCacheResourceWithRawResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.retrieve = async_to_raw_response_wrapper(
            cache.retrieve,
        )


class CacheResourceWithStreamingResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.retrieve = to_streamed_response_wrapper(
            cache.retrieve,
        )


class AsyncCacheResourceWithStreamingResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.retrieve = async_to_streamed_response_wrapper(
            cache.retrieve,
        )
