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
from ....types.ecommerce.orders import admin_list_params
from ....types.ecommerce.orders.admin_list_response import AdminListResponse

__all__ = ["AdminResource", "AsyncAdminResource"]


class AdminResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AdminResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminListResponse:
        """
        The API allows users with the `ADMIN` role to fetch orders placed by users on an
        ecommerce site.

        The API endpoint provides the ability to filter orders based on their status as
        well.

        To filter by status, the client can pass an `order` query parameter in the URL,
        which can have one of the following values: `PENDING`, `DELIVERED`, or
        `CANCELLED`. This allows the admin user to retrieve specific sets of orders
        based on their status.

        **NOTE:** This api returns data which is useful to show list view of the item.

        This api does not contain complete details of the products ordered instead the
        count of the ordered products as generally UI will show the product details in
        the list format.

        To get complete details of the order call `Get order by id` api.

        Args:
          status: PENDING | DELIVERED | CENCELLED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ecommerce/orders/list/admin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    admin_list_params.AdminListParams,
                ),
            ),
            cast_to=AdminListResponse,
        )


class AsyncAdminResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncAdminResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdminListResponse:
        """
        The API allows users with the `ADMIN` role to fetch orders placed by users on an
        ecommerce site.

        The API endpoint provides the ability to filter orders based on their status as
        well.

        To filter by status, the client can pass an `order` query parameter in the URL,
        which can have one of the following values: `PENDING`, `DELIVERED`, or
        `CANCELLED`. This allows the admin user to retrieve specific sets of orders
        based on their status.

        **NOTE:** This api returns data which is useful to show list view of the item.

        This api does not contain complete details of the products ordered instead the
        count of the ordered products as generally UI will show the product details in
        the list format.

        To get complete details of the order call `Get order by id` api.

        Args:
          status: PENDING | DELIVERED | CENCELLED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ecommerce/orders/list/admin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    admin_list_params.AdminListParams,
                ),
            ),
            cast_to=AdminListResponse,
        )


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.list = to_raw_response_wrapper(
            admin.list,
        )


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.list = async_to_raw_response_wrapper(
            admin.list,
        )


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.list = to_streamed_response_wrapper(
            admin.list,
        )


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.list = async_to_streamed_response_wrapper(
            admin.list,
        )
