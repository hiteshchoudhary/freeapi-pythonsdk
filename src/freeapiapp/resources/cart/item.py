# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cart import item_create_params
from ..._base_client import make_request_options
from ...types.cart.item_create_response import ItemCreateResponse
from ...types.cart.item_delete_response import ItemDeleteResponse

__all__ = ["ItemResource", "AsyncItemResource"]


class ItemResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return ItemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return ItemResourceWithStreamingResponse(self)

    def create(
        self,
        product_id: str,
        *,
        quantity: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemCreateResponse:
        """
        The API allows users to add a product to their cart or update the quantity of an
        already added product.

        The frontend can send a request to this API, passing the `productId` as a path
        variable and the desired `quantity` as a number in the request body.

        This API handles both adding new products to the cart and updating the quantity
        of existing products, providing a convenient way for users to manage their
        shopping cart. E.g. If user has `4` products already in cart and if user click
        on `add more` button frontend should send quantity as `5` in the same api.

        _**NOTES:**_

        _Quanity that is passed in the request body will be assigned directly and will
        be treated as a new quantity for the respective product._

        _Minimum quantity should be 1. Once user decrements it from 1, instead of
        sending 0 call remove item from cart api._

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._post(
            f"/ecommerce/cart/item/{product_id}",
            body=maybe_transform({"quantity": quantity}, item_create_params.ItemCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemCreateResponse,
        )

    def delete(
        self,
        product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemDeleteResponse:
        """
        The API allows users to remove/discard a complete product from their shopping
        cart, regardless of its quantity.

        The `productId` is passed as a path variable in the URL.

        **This API endpoint is designed to remove the specified product entirely** from
        the user's shopping cart, disregarding any quantity that may have been added
        previously.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._delete(
            f"/ecommerce/cart/item/{product_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemDeleteResponse,
        )


class AsyncItemResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncItemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncItemResourceWithStreamingResponse(self)

    async def create(
        self,
        product_id: str,
        *,
        quantity: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemCreateResponse:
        """
        The API allows users to add a product to their cart or update the quantity of an
        already added product.

        The frontend can send a request to this API, passing the `productId` as a path
        variable and the desired `quantity` as a number in the request body.

        This API handles both adding new products to the cart and updating the quantity
        of existing products, providing a convenient way for users to manage their
        shopping cart. E.g. If user has `4` products already in cart and if user click
        on `add more` button frontend should send quantity as `5` in the same api.

        _**NOTES:**_

        _Quanity that is passed in the request body will be assigned directly and will
        be treated as a new quantity for the respective product._

        _Minimum quantity should be 1. Once user decrements it from 1, instead of
        sending 0 call remove item from cart api._

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._post(
            f"/ecommerce/cart/item/{product_id}",
            body=await async_maybe_transform({"quantity": quantity}, item_create_params.ItemCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemCreateResponse,
        )

    async def delete(
        self,
        product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemDeleteResponse:
        """
        The API allows users to remove/discard a complete product from their shopping
        cart, regardless of its quantity.

        The `productId` is passed as a path variable in the URL.

        **This API endpoint is designed to remove the specified product entirely** from
        the user's shopping cart, disregarding any quantity that may have been added
        previously.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._delete(
            f"/ecommerce/cart/item/{product_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemDeleteResponse,
        )


class ItemResourceWithRawResponse:
    def __init__(self, item: ItemResource) -> None:
        self._item = item

        self.create = to_raw_response_wrapper(
            item.create,
        )
        self.delete = to_raw_response_wrapper(
            item.delete,
        )


class AsyncItemResourceWithRawResponse:
    def __init__(self, item: AsyncItemResource) -> None:
        self._item = item

        self.create = async_to_raw_response_wrapper(
            item.create,
        )
        self.delete = async_to_raw_response_wrapper(
            item.delete,
        )


class ItemResourceWithStreamingResponse:
    def __init__(self, item: ItemResource) -> None:
        self._item = item

        self.create = to_streamed_response_wrapper(
            item.create,
        )
        self.delete = to_streamed_response_wrapper(
            item.delete,
        )


class AsyncItemResourceWithStreamingResponse:
    def __init__(self, item: AsyncItemResource) -> None:
        self._item = item

        self.create = async_to_streamed_response_wrapper(
            item.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            item.delete,
        )
