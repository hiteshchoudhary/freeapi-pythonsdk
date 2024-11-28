# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .product import (
    ProductResource,
    AsyncProductResource,
    ProductResourceWithRawResponse,
    AsyncProductResourceWithRawResponse,
    ProductResourceWithStreamingResponse,
    AsyncProductResourceWithStreamingResponse,
)
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
from ....types.public import random_product_list_params
from ....types.public.random_product_list_response import RandomProductListResponse
from ....types.public.random_product_retrieve_response import RandomProductRetrieveResponse

__all__ = ["RandomProductsResource", "AsyncRandomProductsResource"]


class RandomProductsResource(SyncAPIResource):
    @cached_property
    def product(self) -> ProductResource:
        return ProductResource(self._client)

    @cached_property
    def with_raw_response(self) -> RandomProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return RandomProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RandomProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return RandomProductsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RandomProductRetrieveResponse:
        """
        The API endpoint allows you to retrieve a product based on the specified product
        ID.

        When accessing this endpoint and providing a valid product ID as a parameter,
        you will receive a response containing the details of the product matching the
        provided ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._get(
            f"/public/randomproducts/{product_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RandomProductRetrieveResponse,
        )

    def list(
        self,
        *,
        inc: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RandomProductListResponse:
        """
        The API endpoint returns a list of dummy products.

        When accessing this endpoint, you will receive a response containing a
        collection of dummy product information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/randomproducts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "inc": inc,
                        "limit": limit,
                        "page": page,
                        "query": query,
                    },
                    random_product_list_params.RandomProductListParams,
                ),
            ),
            cast_to=RandomProductListResponse,
        )


class AsyncRandomProductsResource(AsyncAPIResource):
    @cached_property
    def product(self) -> AsyncProductResource:
        return AsyncProductResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRandomProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRandomProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRandomProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncRandomProductsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RandomProductRetrieveResponse:
        """
        The API endpoint allows you to retrieve a product based on the specified product
        ID.

        When accessing this endpoint and providing a valid product ID as a parameter,
        you will receive a response containing the details of the product matching the
        provided ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._get(
            f"/public/randomproducts/{product_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RandomProductRetrieveResponse,
        )

    async def list(
        self,
        *,
        inc: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RandomProductListResponse:
        """
        The API endpoint returns a list of dummy products.

        When accessing this endpoint, you will receive a response containing a
        collection of dummy product information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/randomproducts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "inc": inc,
                        "limit": limit,
                        "page": page,
                        "query": query,
                    },
                    random_product_list_params.RandomProductListParams,
                ),
            ),
            cast_to=RandomProductListResponse,
        )


class RandomProductsResourceWithRawResponse:
    def __init__(self, random_products: RandomProductsResource) -> None:
        self._random_products = random_products

        self.retrieve = to_raw_response_wrapper(
            random_products.retrieve,
        )
        self.list = to_raw_response_wrapper(
            random_products.list,
        )

    @cached_property
    def product(self) -> ProductResourceWithRawResponse:
        return ProductResourceWithRawResponse(self._random_products.product)


class AsyncRandomProductsResourceWithRawResponse:
    def __init__(self, random_products: AsyncRandomProductsResource) -> None:
        self._random_products = random_products

        self.retrieve = async_to_raw_response_wrapper(
            random_products.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            random_products.list,
        )

    @cached_property
    def product(self) -> AsyncProductResourceWithRawResponse:
        return AsyncProductResourceWithRawResponse(self._random_products.product)


class RandomProductsResourceWithStreamingResponse:
    def __init__(self, random_products: RandomProductsResource) -> None:
        self._random_products = random_products

        self.retrieve = to_streamed_response_wrapper(
            random_products.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            random_products.list,
        )

    @cached_property
    def product(self) -> ProductResourceWithStreamingResponse:
        return ProductResourceWithStreamingResponse(self._random_products.product)


class AsyncRandomProductsResourceWithStreamingResponse:
    def __init__(self, random_products: AsyncRandomProductsResource) -> None:
        self._random_products = random_products

        self.retrieve = async_to_streamed_response_wrapper(
            random_products.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            random_products.list,
        )

    @cached_property
    def product(self) -> AsyncProductResourceWithStreamingResponse:
        return AsyncProductResourceWithStreamingResponse(self._random_products.product)
