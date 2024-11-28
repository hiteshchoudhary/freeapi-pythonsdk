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
from ..._base_client import make_request_options
from ...types.products import category_retrieve_params
from ...types.products.category_retrieve_response import CategoryRetrieveResponse

__all__ = ["CategoryResource", "AsyncCategoryResource"]


class CategoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CategoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return CategoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CategoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return CategoryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        category_id: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryRetrieveResponse:
        """
        The API retrieves a product based on the category it belongs to.

        The category is determined by the `categoryId` provided as a path variable.

        By passing the appropriate `categoryId`, this API returns the product that falls
        within that specific category.

        This enables users to easily access and retrieve relevant products based on
        their desired category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            f"/ecommerce/products/category/{category_id}",
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
                    category_retrieve_params.CategoryRetrieveParams,
                ),
            ),
            cast_to=CategoryRetrieveResponse,
        )


class AsyncCategoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCategoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCategoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCategoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncCategoryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        category_id: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryRetrieveResponse:
        """
        The API retrieves a product based on the category it belongs to.

        The category is determined by the `categoryId` provided as a path variable.

        By passing the appropriate `categoryId`, this API returns the product that falls
        within that specific category.

        This enables users to easily access and retrieve relevant products based on
        their desired category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            f"/ecommerce/products/category/{category_id}",
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
                    category_retrieve_params.CategoryRetrieveParams,
                ),
            ),
            cast_to=CategoryRetrieveResponse,
        )


class CategoryResourceWithRawResponse:
    def __init__(self, category: CategoryResource) -> None:
        self._category = category

        self.retrieve = to_raw_response_wrapper(
            category.retrieve,
        )


class AsyncCategoryResourceWithRawResponse:
    def __init__(self, category: AsyncCategoryResource) -> None:
        self._category = category

        self.retrieve = async_to_raw_response_wrapper(
            category.retrieve,
        )


class CategoryResourceWithStreamingResponse:
    def __init__(self, category: CategoryResource) -> None:
        self._category = category

        self.retrieve = to_streamed_response_wrapper(
            category.retrieve,
        )


class AsyncCategoryResourceWithStreamingResponse:
    def __init__(self, category: AsyncCategoryResource) -> None:
        self._category = category

        self.retrieve = async_to_streamed_response_wrapper(
            category.retrieve,
        )
