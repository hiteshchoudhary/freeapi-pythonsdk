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
from ....types.ecommerce.profile import my_order_list_params
from ....types.ecommerce.profile.my_order_list_response import MyOrderListResponse

__all__ = ["MyOrdersResource", "AsyncMyOrdersResource"]


class MyOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MyOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return MyOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MyOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return MyOrdersResourceWithStreamingResponse(self)

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
    ) -> MyOrderListResponse:
        """
        The API endpoint allows you to retrieve the placed orders of the logged-in user
        in an ecommerce application.

        When accessing this endpoint, you will receive a response containing the list of
        orders that have been placed by the currently authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ecommerce/profile/my-orders",
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
                    my_order_list_params.MyOrderListParams,
                ),
            ),
            cast_to=MyOrderListResponse,
        )


class AsyncMyOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMyOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMyOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMyOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncMyOrdersResourceWithStreamingResponse(self)

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
    ) -> MyOrderListResponse:
        """
        The API endpoint allows you to retrieve the placed orders of the logged-in user
        in an ecommerce application.

        When accessing this endpoint, you will receive a response containing the list of
        orders that have been placed by the currently authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ecommerce/profile/my-orders",
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
                    my_order_list_params.MyOrderListParams,
                ),
            ),
            cast_to=MyOrderListResponse,
        )


class MyOrdersResourceWithRawResponse:
    def __init__(self, my_orders: MyOrdersResource) -> None:
        self._my_orders = my_orders

        self.list = to_raw_response_wrapper(
            my_orders.list,
        )


class AsyncMyOrdersResourceWithRawResponse:
    def __init__(self, my_orders: AsyncMyOrdersResource) -> None:
        self._my_orders = my_orders

        self.list = async_to_raw_response_wrapper(
            my_orders.list,
        )


class MyOrdersResourceWithStreamingResponse:
    def __init__(self, my_orders: MyOrdersResource) -> None:
        self._my_orders = my_orders

        self.list = to_streamed_response_wrapper(
            my_orders.list,
        )


class AsyncMyOrdersResourceWithStreamingResponse:
    def __init__(self, my_orders: AsyncMyOrdersResource) -> None:
        self._my_orders = my_orders

        self.list = async_to_streamed_response_wrapper(
            my_orders.list,
        )
