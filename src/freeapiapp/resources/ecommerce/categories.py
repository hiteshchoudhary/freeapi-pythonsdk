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
from ...types.ecommerce import category_list_params, category_create_params, category_update_params
from ...types.ecommerce.category_list_response import CategoryListResponse
from ...types.ecommerce.category_create_response import CategoryCreateResponse
from ...types.ecommerce.category_delete_response import CategoryDeleteResponse
from ...types.ecommerce.category_update_response import CategoryUpdateResponse
from ...types.ecommerce.category_retrieve_response import CategoryRetrieveResponse

__all__ = ["CategoriesResource", "AsyncCategoriesResource"]


class CategoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return CategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return CategoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryCreateResponse:
        """
        The API endpoint allows an administrator user with the appropriate role to
        create a new category.

        By sending a request to this endpoint with the desired category `name` provided
        in the request body, the API will create a new category in the system.

        This functionality is restricted to users with an `ADMIN` role to ensure proper
        access control and authorization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ecommerce/categories",
            body=maybe_transform({"name": name}, category_create_params.CategoryCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryCreateResponse,
        )

    def retrieve(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryRetrieveResponse:
        """
        The API endpoint allows users to fetch a category based on the `categoryId`
        provided as a path variable in the URL.

        When accessing this endpoint and providing a valid `categoryId`, the response
        will contain the details and information associated with the specified category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            f"/ecommerce/categories/{category_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryRetrieveResponse,
        )

    def update(
        self,
        category_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryUpdateResponse:
        """
        The API endpoint allows users with an `ADMIN` role to update a category by
        providing the category `name` key in the request body and the `categoryId` in
        the URL path variable.

        This functionality enables administrators to modify and manage category
        information within the system.

        By accessing this endpoint, authorized administrators can update the specified
        category's name key to reflect any necessary changes or updates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._patch(
            f"/ecommerce/categories/{category_id}",
            body=maybe_transform({"name": name}, category_update_params.CategoryUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryUpdateResponse,
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
    ) -> CategoryListResponse:
        """
        The API endpoint allows users to fetch all the available categories in an
        e-commerce application.

        When accessing this endpoint, users will receive a response containing a list of
        categories that exist within the e-commerce app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ecommerce/categories",
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
                    category_list_params.CategoryListParams,
                ),
            ),
            cast_to=CategoryListResponse,
        )

    def delete(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryDeleteResponse:
        """
        The API endpoint allows an administrator to delete a category by providing the
        `categoryId` as a path variable in the URL.

        This functionality is specific to users with an `ADMIN` role and is designed to
        facilitate category management tasks.

        By accessing this endpoint and specifying the `categoryId`, the category
        associated with that ID will be permanently deleted from the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._delete(
            f"/ecommerce/categories/{category_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryDeleteResponse,
        )


class AsyncCategoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncCategoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryCreateResponse:
        """
        The API endpoint allows an administrator user with the appropriate role to
        create a new category.

        By sending a request to this endpoint with the desired category `name` provided
        in the request body, the API will create a new category in the system.

        This functionality is restricted to users with an `ADMIN` role to ensure proper
        access control and authorization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ecommerce/categories",
            body=await async_maybe_transform({"name": name}, category_create_params.CategoryCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryCreateResponse,
        )

    async def retrieve(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryRetrieveResponse:
        """
        The API endpoint allows users to fetch a category based on the `categoryId`
        provided as a path variable in the URL.

        When accessing this endpoint and providing a valid `categoryId`, the response
        will contain the details and information associated with the specified category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            f"/ecommerce/categories/{category_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryRetrieveResponse,
        )

    async def update(
        self,
        category_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryUpdateResponse:
        """
        The API endpoint allows users with an `ADMIN` role to update a category by
        providing the category `name` key in the request body and the `categoryId` in
        the URL path variable.

        This functionality enables administrators to modify and manage category
        information within the system.

        By accessing this endpoint, authorized administrators can update the specified
        category's name key to reflect any necessary changes or updates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._patch(
            f"/ecommerce/categories/{category_id}",
            body=await async_maybe_transform({"name": name}, category_update_params.CategoryUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryUpdateResponse,
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
    ) -> CategoryListResponse:
        """
        The API endpoint allows users to fetch all the available categories in an
        e-commerce application.

        When accessing this endpoint, users will receive a response containing a list of
        categories that exist within the e-commerce app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ecommerce/categories",
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
                    category_list_params.CategoryListParams,
                ),
            ),
            cast_to=CategoryListResponse,
        )

    async def delete(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CategoryDeleteResponse:
        """
        The API endpoint allows an administrator to delete a category by providing the
        `categoryId` as a path variable in the URL.

        This functionality is specific to users with an `ADMIN` role and is designed to
        facilitate category management tasks.

        By accessing this endpoint and specifying the `categoryId`, the category
        associated with that ID will be permanently deleted from the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._delete(
            f"/ecommerce/categories/{category_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryDeleteResponse,
        )


class CategoriesResourceWithRawResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.create = to_raw_response_wrapper(
            categories.create,
        )
        self.retrieve = to_raw_response_wrapper(
            categories.retrieve,
        )
        self.update = to_raw_response_wrapper(
            categories.update,
        )
        self.list = to_raw_response_wrapper(
            categories.list,
        )
        self.delete = to_raw_response_wrapper(
            categories.delete,
        )


class AsyncCategoriesResourceWithRawResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.create = async_to_raw_response_wrapper(
            categories.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            categories.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            categories.update,
        )
        self.list = async_to_raw_response_wrapper(
            categories.list,
        )
        self.delete = async_to_raw_response_wrapper(
            categories.delete,
        )


class CategoriesResourceWithStreamingResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.create = to_streamed_response_wrapper(
            categories.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            categories.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            categories.update,
        )
        self.list = to_streamed_response_wrapper(
            categories.list,
        )
        self.delete = to_streamed_response_wrapper(
            categories.delete,
        )


class AsyncCategoriesResourceWithStreamingResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.create = async_to_streamed_response_wrapper(
            categories.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            categories.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            categories.update,
        )
        self.list = async_to_streamed_response_wrapper(
            categories.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            categories.delete,
        )
