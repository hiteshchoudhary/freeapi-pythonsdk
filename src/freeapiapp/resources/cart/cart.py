# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .item import (
    ItemResource,
    AsyncItemResource,
    ItemResourceWithRawResponse,
    AsyncItemResourceWithRawResponse,
    ItemResourceWithStreamingResponse,
    AsyncItemResourceWithStreamingResponse,
)
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
from ...types.cart_retrieve_response import CartRetrieveResponse

__all__ = ["CartResource", "AsyncCartResource"]


class CartResource(SyncAPIResource):
    @cached_property
    def item(self) -> ItemResource:
        return ItemResource(self._client)

    @cached_property
    def with_raw_response(self) -> CartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return CartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return CartResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartRetrieveResponse:
        """
        The API endpoint returns the cart of the logged-in user.

        This API allows authenticated users to retrieve the contents of their shopping
        cart.

        The response typically includes information about the products or items added to
        the cart, such as their names, quantities, prices, and any relevant details.

        This endpoint ensures that only authorized users can access and view their own
        cart data.
        """
        return self._get(
            "/ecommerce/cart",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartRetrieveResponse,
        )


class AsyncCartResource(AsyncAPIResource):
    @cached_property
    def item(self) -> AsyncItemResource:
        return AsyncItemResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncCartResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartRetrieveResponse:
        """
        The API endpoint returns the cart of the logged-in user.

        This API allows authenticated users to retrieve the contents of their shopping
        cart.

        The response typically includes information about the products or items added to
        the cart, such as their names, quantities, prices, and any relevant details.

        This endpoint ensures that only authorized users can access and view their own
        cart data.
        """
        return await self._get(
            "/ecommerce/cart",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartRetrieveResponse,
        )


class CartResourceWithRawResponse:
    def __init__(self, cart: CartResource) -> None:
        self._cart = cart

        self.retrieve = to_raw_response_wrapper(
            cart.retrieve,
        )

    @cached_property
    def item(self) -> ItemResourceWithRawResponse:
        return ItemResourceWithRawResponse(self._cart.item)


class AsyncCartResourceWithRawResponse:
    def __init__(self, cart: AsyncCartResource) -> None:
        self._cart = cart

        self.retrieve = async_to_raw_response_wrapper(
            cart.retrieve,
        )

    @cached_property
    def item(self) -> AsyncItemResourceWithRawResponse:
        return AsyncItemResourceWithRawResponse(self._cart.item)


class CartResourceWithStreamingResponse:
    def __init__(self, cart: CartResource) -> None:
        self._cart = cart

        self.retrieve = to_streamed_response_wrapper(
            cart.retrieve,
        )

    @cached_property
    def item(self) -> ItemResourceWithStreamingResponse:
        return ItemResourceWithStreamingResponse(self._cart.item)


class AsyncCartResourceWithStreamingResponse:
    def __init__(self, cart: AsyncCartResource) -> None:
        self._cart = cart

        self.retrieve = async_to_streamed_response_wrapper(
            cart.retrieve,
        )

    @cached_property
    def item(self) -> AsyncItemResourceWithStreamingResponse:
        return AsyncItemResourceWithStreamingResponse(self._cart.item)
