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
from ...types.ecommerce.cart_clear_response import CartClearResponse

__all__ = ["CartResource", "AsyncCartResource"]


class CartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return CartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return CartResourceWithStreamingResponse(self)

    def clear(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartClearResponse:
        """
        The API endpoint allows a logged-in user to clear their entire shopping cart.

        By invoking this API, the user can remove all items from their cart, effectively
        clearing it and starting afresh.

        This feature provides a convenient way for users to manage their shopping carts
        and begin a new shopping session.
        """
        return self._delete(
            "/ecommerce/cart/clear",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartClearResponse,
        )


class AsyncCartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncCartResourceWithStreamingResponse(self)

    async def clear(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartClearResponse:
        """
        The API endpoint allows a logged-in user to clear their entire shopping cart.

        By invoking this API, the user can remove all items from their cart, effectively
        clearing it and starting afresh.

        This feature provides a convenient way for users to manage their shopping carts
        and begin a new shopping session.
        """
        return await self._delete(
            "/ecommerce/cart/clear",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartClearResponse,
        )


class CartResourceWithRawResponse:
    def __init__(self, cart: CartResource) -> None:
        self._cart = cart

        self.clear = to_raw_response_wrapper(
            cart.clear,
        )


class AsyncCartResourceWithRawResponse:
    def __init__(self, cart: AsyncCartResource) -> None:
        self._cart = cart

        self.clear = async_to_raw_response_wrapper(
            cart.clear,
        )


class CartResourceWithStreamingResponse:
    def __init__(self, cart: CartResource) -> None:
        self._cart = cart

        self.clear = to_streamed_response_wrapper(
            cart.clear,
        )


class AsyncCartResourceWithStreamingResponse:
    def __init__(self, cart: AsyncCartResource) -> None:
        self._cart = cart

        self.clear = async_to_streamed_response_wrapper(
            cart.clear,
        )
