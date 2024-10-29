# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ecommerce.coupons import customer_available_list_params
from ....types.ecommerce.coupons.customer_available_list_response import CustomerAvailableListResponse

__all__ = ["CustomerAvailableResource", "AsyncCustomerAvailableResource"]


class CustomerAvailableResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomerAvailableResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return CustomerAvailableResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomerAvailableResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return CustomerAvailableResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerAvailableListResponse:
        """
        The API allows a logged-in user to retrieve a list of coupons based on their
        total shopping cart amount.

        The API takes into account the user's current cart total and returns a list of
        valid coupon codes that the user is eligible to apply.

        This functionality helps users find applicable discounts for their purchases,
        enhancing their shopping experience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ecommerce/coupons/customer/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    customer_available_list_params.CustomerAvailableListParams,
                ),
            ),
            cast_to=CustomerAvailableListResponse,
        )


class AsyncCustomerAvailableResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomerAvailableResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomerAvailableResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomerAvailableResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncCustomerAvailableResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerAvailableListResponse:
        """
        The API allows a logged-in user to retrieve a list of coupons based on their
        total shopping cart amount.

        The API takes into account the user's current cart total and returns a list of
        valid coupon codes that the user is eligible to apply.

        This functionality helps users find applicable discounts for their purchases,
        enhancing their shopping experience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ecommerce/coupons/customer/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    customer_available_list_params.CustomerAvailableListParams,
                ),
            ),
            cast_to=CustomerAvailableListResponse,
        )


class CustomerAvailableResourceWithRawResponse:
    def __init__(self, customer_available: CustomerAvailableResource) -> None:
        self._customer_available = customer_available

        self.list = to_raw_response_wrapper(
            customer_available.list,
        )


class AsyncCustomerAvailableResourceWithRawResponse:
    def __init__(self, customer_available: AsyncCustomerAvailableResource) -> None:
        self._customer_available = customer_available

        self.list = async_to_raw_response_wrapper(
            customer_available.list,
        )


class CustomerAvailableResourceWithStreamingResponse:
    def __init__(self, customer_available: CustomerAvailableResource) -> None:
        self._customer_available = customer_available

        self.list = to_streamed_response_wrapper(
            customer_available.list,
        )


class AsyncCustomerAvailableResourceWithStreamingResponse:
    def __init__(self, customer_available: AsyncCustomerAvailableResource) -> None:
        self._customer_available = customer_available

        self.list = async_to_streamed_response_wrapper(
            customer_available.list,
        )
