# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .admin import (
    AdminResource,
    AsyncAdminResource,
    AdminResourceWithRawResponse,
    AsyncAdminResourceWithRawResponse,
    AdminResourceWithStreamingResponse,
    AsyncAdminResourceWithStreamingResponse,
)
from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from .provider import (
    ProviderResource,
    AsyncProviderResource,
    ProviderResourceWithRawResponse,
    AsyncProviderResourceWithRawResponse,
    ProviderResourceWithStreamingResponse,
    AsyncProviderResourceWithStreamingResponse,
)
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
from .provider.provider import ProviderResource, AsyncProviderResource
from ....types.ecommerce.order_retrieve_response import OrderRetrieveResponse

__all__ = ["OrdersResource", "AsyncOrdersResource"]


class OrdersResource(SyncAPIResource):
    @cached_property
    def admin(self) -> AdminResource:
        return AdminResource(self._client)

    @cached_property
    def provider(self) -> ProviderResource:
        return ProviderResource(self._client)

    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return OrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return OrdersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        order_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderRetrieveResponse:
        """
        The API allows users to retrieve information about an order placed by a user by
        specifying the `orderId` as a path variable.

        This can be used to get complete details of the order for admin or user who has
        placed the order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._get(
            f"/ecommerce/orders/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderRetrieveResponse,
        )


class AsyncOrdersResource(AsyncAPIResource):
    @cached_property
    def admin(self) -> AsyncAdminResource:
        return AsyncAdminResource(self._client)

    @cached_property
    def provider(self) -> AsyncProviderResource:
        return AsyncProviderResource(self._client)

    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncOrdersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        order_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderRetrieveResponse:
        """
        The API allows users to retrieve information about an order placed by a user by
        specifying the `orderId` as a path variable.

        This can be used to get complete details of the order for admin or user who has
        placed the order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._get(
            f"/ecommerce/orders/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderRetrieveResponse,
        )


class OrdersResourceWithRawResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.retrieve = to_raw_response_wrapper(
            orders.retrieve,
        )

    @cached_property
    def admin(self) -> AdminResourceWithRawResponse:
        return AdminResourceWithRawResponse(self._orders.admin)

    @cached_property
    def provider(self) -> ProviderResourceWithRawResponse:
        return ProviderResourceWithRawResponse(self._orders.provider)

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._orders.status)


class AsyncOrdersResourceWithRawResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.retrieve = async_to_raw_response_wrapper(
            orders.retrieve,
        )

    @cached_property
    def admin(self) -> AsyncAdminResourceWithRawResponse:
        return AsyncAdminResourceWithRawResponse(self._orders.admin)

    @cached_property
    def provider(self) -> AsyncProviderResourceWithRawResponse:
        return AsyncProviderResourceWithRawResponse(self._orders.provider)

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._orders.status)


class OrdersResourceWithStreamingResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.retrieve = to_streamed_response_wrapper(
            orders.retrieve,
        )

    @cached_property
    def admin(self) -> AdminResourceWithStreamingResponse:
        return AdminResourceWithStreamingResponse(self._orders.admin)

    @cached_property
    def provider(self) -> ProviderResourceWithStreamingResponse:
        return ProviderResourceWithStreamingResponse(self._orders.provider)

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._orders.status)


class AsyncOrdersResourceWithStreamingResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.retrieve = async_to_streamed_response_wrapper(
            orders.retrieve,
        )

    @cached_property
    def admin(self) -> AsyncAdminResourceWithStreamingResponse:
        return AsyncAdminResourceWithStreamingResponse(self._orders.admin)

    @cached_property
    def provider(self) -> AsyncProviderResourceWithStreamingResponse:
        return AsyncProviderResourceWithStreamingResponse(self._orders.provider)

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._orders.status)
