# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ...types import product_list_params, product_create_params, product_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from .category import (
    CategoryResource,
    AsyncCategoryResource,
    CategoryResourceWithRawResponse,
    AsyncCategoryResourceWithRawResponse,
    CategoryResourceWithStreamingResponse,
    AsyncCategoryResourceWithStreamingResponse,
)
from .subimage import (
    SubimageResource,
    AsyncSubimageResource,
    SubimageResourceWithRawResponse,
    AsyncSubimageResourceWithRawResponse,
    SubimageResourceWithStreamingResponse,
    AsyncSubimageResourceWithStreamingResponse,
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
from ...types.product_list_response import ProductListResponse
from ...types.product_create_response import ProductCreateResponse
from ...types.product_delete_response import ProductDeleteResponse
from ...types.product_update_response import ProductUpdateResponse
from ...types.product_retrieve_response import ProductRetrieveResponse

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    @cached_property
    def category(self) -> CategoryResource:
        return CategoryResource(self._client)

    @cached_property
    def subimage(self) -> SubimageResource:
        return SubimageResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        category: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        main_image: FileTypes | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        price: str | NotGiven = NOT_GIVEN,
        stock: str | NotGiven = NOT_GIVEN,
        sub_images: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductCreateResponse:
        """
        The API enables an authenticated user with the role of `ADMIN` to create a
        product by providing various details in the request body using form data.

        The required fields for creating a product includes:

        - name
        - description
        - price
        - stock quantity
        - category (referenced by the category ID),
        - mainImage (representing the main product image),
        - subImages (up to **4** additional images that can be viewed in a carousel on
          the frontend).

        By submitting this information via form data, the API allows administrators to
        efficiently add new products to the system, ensuring accurate and comprehensive
        product listings for users.

        Args:
          main_image: FIle

          sub_images: subImages is a multiple images field having 4 as a maximum number of images
              limit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "category": category,
                "description": description,
                "main_image": main_image,
                "name": name,
                "price": price,
                "stock": stock,
                "sub_images": sub_images,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["mainImage"], ["subImages"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/ecommerce/products",
            body=maybe_transform(body, product_create_params.ProductCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCreateResponse,
        )

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
    ) -> ProductRetrieveResponse:
        """
        The API retrieves a product based on the provided `productId` passed as a path
        variable.

        This API serves as a means to fetch specific product information from the
        backend based on a unique identifier.

        By passing the `productId` in the URL, the API searches and retrieves the
        corresponding product details, including attributes such as name, price,
        description, stock, images and any other relevant information associated with
        the product.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._get(
            f"/ecommerce/products/{product_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductRetrieveResponse,
        )

    def update(
        self,
        product_id: str,
        *,
        category: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        main_image: FileTypes | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        price: str | NotGiven = NOT_GIVEN,
        stock: str | NotGiven = NOT_GIVEN,
        sub_images: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductUpdateResponse:
        """
        The API enables an authenticated user with the role of `ADMIN` to update a
        product's information.

        By passing the `productId` as a path variable, the API allows the user to modify
        the product's attributes such as name, description, price, stock, category
        (referenced by categoryId), mainImage (the primary image), and subImages (up to
        four additional images displayed in a carousel on the frontend).

        All of these fields can be included in the request body as form data, and they
        are optional, meaning that only the provided fields will be updated.

        Args:
          main_image: File

          sub_images: subImages is a multiple images field having 4 as a maximum number of images
              limit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        body = deepcopy_minimal(
            {
                "category": category,
                "description": description,
                "main_image": main_image,
                "name": name,
                "price": price,
                "stock": stock,
                "sub_images": sub_images,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["mainImage"], ["subImages"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._patch(
            f"/ecommerce/products/{product_id}",
            body=maybe_transform(body, product_update_params.ProductUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductUpdateResponse,
        )

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
    ) -> ProductListResponse:
        """
        The API returns all the products available in an e-commerce application.

        When invoked, this API fetches and retrieves the complete list of products
        offered by the e-commerce platform.

        The response typically includes details such as the product name, description,
        price, stock, and other relevant information.

        This API allows users or other systems to access and display the entire catalog
        of products, facilitating browsing and purchasing decisions within the
        e-commerce application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ecommerce/products",
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
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=ProductListResponse,
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
    ) -> ProductDeleteResponse:
        """
        The API allows an authenticated user with the role of `ADMIN` to delete a
        product from the system.

        It expects the `productId` to be passed as a path variable.

        By utilizing this API, administrators can easily remove products from the
        inventory or catalog.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._delete(
            f"/ecommerce/products/{product_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductDeleteResponse,
        )


class AsyncProductsResource(AsyncAPIResource):
    @cached_property
    def category(self) -> AsyncCategoryResource:
        return AsyncCategoryResource(self._client)

    @cached_property
    def subimage(self) -> AsyncSubimageResource:
        return AsyncSubimageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        category: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        main_image: FileTypes | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        price: str | NotGiven = NOT_GIVEN,
        stock: str | NotGiven = NOT_GIVEN,
        sub_images: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductCreateResponse:
        """
        The API enables an authenticated user with the role of `ADMIN` to create a
        product by providing various details in the request body using form data.

        The required fields for creating a product includes:

        - name
        - description
        - price
        - stock quantity
        - category (referenced by the category ID),
        - mainImage (representing the main product image),
        - subImages (up to **4** additional images that can be viewed in a carousel on
          the frontend).

        By submitting this information via form data, the API allows administrators to
        efficiently add new products to the system, ensuring accurate and comprehensive
        product listings for users.

        Args:
          main_image: FIle

          sub_images: subImages is a multiple images field having 4 as a maximum number of images
              limit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "category": category,
                "description": description,
                "main_image": main_image,
                "name": name,
                "price": price,
                "stock": stock,
                "sub_images": sub_images,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["mainImage"], ["subImages"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/ecommerce/products",
            body=await async_maybe_transform(body, product_create_params.ProductCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCreateResponse,
        )

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
    ) -> ProductRetrieveResponse:
        """
        The API retrieves a product based on the provided `productId` passed as a path
        variable.

        This API serves as a means to fetch specific product information from the
        backend based on a unique identifier.

        By passing the `productId` in the URL, the API searches and retrieves the
        corresponding product details, including attributes such as name, price,
        description, stock, images and any other relevant information associated with
        the product.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._get(
            f"/ecommerce/products/{product_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductRetrieveResponse,
        )

    async def update(
        self,
        product_id: str,
        *,
        category: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        main_image: FileTypes | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        price: str | NotGiven = NOT_GIVEN,
        stock: str | NotGiven = NOT_GIVEN,
        sub_images: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductUpdateResponse:
        """
        The API enables an authenticated user with the role of `ADMIN` to update a
        product's information.

        By passing the `productId` as a path variable, the API allows the user to modify
        the product's attributes such as name, description, price, stock, category
        (referenced by categoryId), mainImage (the primary image), and subImages (up to
        four additional images displayed in a carousel on the frontend).

        All of these fields can be included in the request body as form data, and they
        are optional, meaning that only the provided fields will be updated.

        Args:
          main_image: File

          sub_images: subImages is a multiple images field having 4 as a maximum number of images
              limit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        body = deepcopy_minimal(
            {
                "category": category,
                "description": description,
                "main_image": main_image,
                "name": name,
                "price": price,
                "stock": stock,
                "sub_images": sub_images,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["mainImage"], ["subImages"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._patch(
            f"/ecommerce/products/{product_id}",
            body=await async_maybe_transform(body, product_update_params.ProductUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductUpdateResponse,
        )

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
    ) -> ProductListResponse:
        """
        The API returns all the products available in an e-commerce application.

        When invoked, this API fetches and retrieves the complete list of products
        offered by the e-commerce platform.

        The response typically includes details such as the product name, description,
        price, stock, and other relevant information.

        This API allows users or other systems to access and display the entire catalog
        of products, facilitating browsing and purchasing decisions within the
        e-commerce application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ecommerce/products",
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
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=ProductListResponse,
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
    ) -> ProductDeleteResponse:
        """
        The API allows an authenticated user with the role of `ADMIN` to delete a
        product from the system.

        It expects the `productId` to be passed as a path variable.

        By utilizing this API, administrators can easily remove products from the
        inventory or catalog.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._delete(
            f"/ecommerce/products/{product_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductDeleteResponse,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = to_raw_response_wrapper(
            products.retrieve,
        )
        self.update = to_raw_response_wrapper(
            products.update,
        )
        self.list = to_raw_response_wrapper(
            products.list,
        )
        self.delete = to_raw_response_wrapper(
            products.delete,
        )

    @cached_property
    def category(self) -> CategoryResourceWithRawResponse:
        return CategoryResourceWithRawResponse(self._products.category)

    @cached_property
    def subimage(self) -> SubimageResourceWithRawResponse:
        return SubimageResourceWithRawResponse(self._products.subimage)


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            products.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            products.update,
        )
        self.list = async_to_raw_response_wrapper(
            products.list,
        )
        self.delete = async_to_raw_response_wrapper(
            products.delete,
        )

    @cached_property
    def category(self) -> AsyncCategoryResourceWithRawResponse:
        return AsyncCategoryResourceWithRawResponse(self._products.category)

    @cached_property
    def subimage(self) -> AsyncSubimageResourceWithRawResponse:
        return AsyncSubimageResourceWithRawResponse(self._products.subimage)


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            products.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            products.update,
        )
        self.list = to_streamed_response_wrapper(
            products.list,
        )
        self.delete = to_streamed_response_wrapper(
            products.delete,
        )

    @cached_property
    def category(self) -> CategoryResourceWithStreamingResponse:
        return CategoryResourceWithStreamingResponse(self._products.category)

    @cached_property
    def subimage(self) -> SubimageResourceWithStreamingResponse:
        return SubimageResourceWithStreamingResponse(self._products.subimage)


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            products.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            products.update,
        )
        self.list = async_to_streamed_response_wrapper(
            products.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            products.delete,
        )

    @cached_property
    def category(self) -> AsyncCategoryResourceWithStreamingResponse:
        return AsyncCategoryResourceWithStreamingResponse(self._products.category)

    @cached_property
    def subimage(self) -> AsyncSubimageResourceWithStreamingResponse:
        return AsyncSubimageResourceWithStreamingResponse(self._products.subimage)
