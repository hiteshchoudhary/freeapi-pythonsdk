# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.healthcheck_retrieve_response import HealthcheckRetrieveResponse

__all__ = ["HealthcheckResource", "AsyncHealthcheckResource"]


class HealthcheckResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthcheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return HealthcheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthcheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return HealthcheckResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthcheckRetrieveResponse:
        """
        This API endpoint is commonly used to determine the health status or
        availability of a system or service.

        It is a simple and lightweight endpoint designed to perform a quick health check
        of the application or infrastructure.
        """
        return self._get(
            "/healthcheck",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthcheckRetrieveResponse,
        )


class AsyncHealthcheckResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthcheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHealthcheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthcheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncHealthcheckResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthcheckRetrieveResponse:
        """
        This API endpoint is commonly used to determine the health status or
        availability of a system or service.

        It is a simple and lightweight endpoint designed to perform a quick health check
        of the application or infrastructure.
        """
        return await self._get(
            "/healthcheck",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthcheckRetrieveResponse,
        )


class HealthcheckResourceWithRawResponse:
    def __init__(self, healthcheck: HealthcheckResource) -> None:
        self._healthcheck = healthcheck

        self.retrieve = to_raw_response_wrapper(
            healthcheck.retrieve,
        )


class AsyncHealthcheckResourceWithRawResponse:
    def __init__(self, healthcheck: AsyncHealthcheckResource) -> None:
        self._healthcheck = healthcheck

        self.retrieve = async_to_raw_response_wrapper(
            healthcheck.retrieve,
        )


class HealthcheckResourceWithStreamingResponse:
    def __init__(self, healthcheck: HealthcheckResource) -> None:
        self._healthcheck = healthcheck

        self.retrieve = to_streamed_response_wrapper(
            healthcheck.retrieve,
        )


class AsyncHealthcheckResourceWithStreamingResponse:
    def __init__(self, healthcheck: AsyncHealthcheckResource) -> None:
        self._healthcheck = healthcheck

        self.retrieve = async_to_streamed_response_wrapper(
            healthcheck.retrieve,
        )
