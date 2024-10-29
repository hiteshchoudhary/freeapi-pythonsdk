# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.seed.ecommerce_create_response import EcommerceCreateResponse

__all__ = ["EcommerceResource", "AsyncEcommerceResource"]


class EcommerceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EcommerceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return EcommerceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EcommerceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return EcommerceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EcommerceCreateResponse:
        """
        This API endpoint is responsible for populating all the essential entities
        required for an ecommerce service in the database.

        It provides a convenient way for developers to initialize the ecommerce system
        with dummy or sample data for testing or development purposes.
        """
        return self._post(
            "/seed/ecommerce",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EcommerceCreateResponse,
        )


class AsyncEcommerceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEcommerceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEcommerceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEcommerceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncEcommerceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EcommerceCreateResponse:
        """
        This API endpoint is responsible for populating all the essential entities
        required for an ecommerce service in the database.

        It provides a convenient way for developers to initialize the ecommerce system
        with dummy or sample data for testing or development purposes.
        """
        return await self._post(
            "/seed/ecommerce",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EcommerceCreateResponse,
        )


class EcommerceResourceWithRawResponse:
    def __init__(self, ecommerce: EcommerceResource) -> None:
        self._ecommerce = ecommerce

        self.create = to_raw_response_wrapper(
            ecommerce.create,
        )


class AsyncEcommerceResourceWithRawResponse:
    def __init__(self, ecommerce: AsyncEcommerceResource) -> None:
        self._ecommerce = ecommerce

        self.create = async_to_raw_response_wrapper(
            ecommerce.create,
        )


class EcommerceResourceWithStreamingResponse:
    def __init__(self, ecommerce: EcommerceResource) -> None:
        self._ecommerce = ecommerce

        self.create = to_streamed_response_wrapper(
            ecommerce.create,
        )


class AsyncEcommerceResourceWithStreamingResponse:
    def __init__(self, ecommerce: AsyncEcommerceResource) -> None:
        self._ecommerce = ecommerce

        self.create = async_to_streamed_response_wrapper(
            ecommerce.create,
        )
