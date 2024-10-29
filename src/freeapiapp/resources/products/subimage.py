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
from ...types.products.subimage_remove_response import SubimageRemoveResponse

__all__ = ["SubimageResource", "AsyncSubimageResource"]


class SubimageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubimageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return SubimageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubimageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return SubimageResourceWithStreamingResponse(self)

    def remove(
        self,
        sub_image_id: str,
        *,
        product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubimageRemoveResponse:
        """
        The API enables an `ADMIN` user to remove sub-images associated with a product
        by providing `productId` and `subImageId`.

        It provides functionality for the frontend to offer the `ADMIN` user an option
        to manage the sub-images of a product.

        Using this API, the `ADMIN` user can remove specific sub-images from the
        product, thereby allowing them to effectively control and update the visual
        representation of the product.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        if not sub_image_id:
            raise ValueError(f"Expected a non-empty value for `sub_image_id` but received {sub_image_id!r}")
        return self._patch(
            f"/ecommerce/products/remove/subimage/{product_id}/{sub_image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubimageRemoveResponse,
        )


class AsyncSubimageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubimageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubimageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubimageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncSubimageResourceWithStreamingResponse(self)

    async def remove(
        self,
        sub_image_id: str,
        *,
        product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubimageRemoveResponse:
        """
        The API enables an `ADMIN` user to remove sub-images associated with a product
        by providing `productId` and `subImageId`.

        It provides functionality for the frontend to offer the `ADMIN` user an option
        to manage the sub-images of a product.

        Using this API, the `ADMIN` user can remove specific sub-images from the
        product, thereby allowing them to effectively control and update the visual
        representation of the product.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        if not sub_image_id:
            raise ValueError(f"Expected a non-empty value for `sub_image_id` but received {sub_image_id!r}")
        return await self._patch(
            f"/ecommerce/products/remove/subimage/{product_id}/{sub_image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubimageRemoveResponse,
        )


class SubimageResourceWithRawResponse:
    def __init__(self, subimage: SubimageResource) -> None:
        self._subimage = subimage

        self.remove = to_raw_response_wrapper(
            subimage.remove,
        )


class AsyncSubimageResourceWithRawResponse:
    def __init__(self, subimage: AsyncSubimageResource) -> None:
        self._subimage = subimage

        self.remove = async_to_raw_response_wrapper(
            subimage.remove,
        )


class SubimageResourceWithStreamingResponse:
    def __init__(self, subimage: SubimageResource) -> None:
        self._subimage = subimage

        self.remove = to_streamed_response_wrapper(
            subimage.remove,
        )


class AsyncSubimageResourceWithStreamingResponse:
    def __init__(self, subimage: AsyncSubimageResource) -> None:
        self._subimage = subimage

        self.remove = async_to_streamed_response_wrapper(
            subimage.remove,
        )
