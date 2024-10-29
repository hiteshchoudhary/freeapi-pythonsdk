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
from ....types.ecommerce.coupons import status_update_params
from ....types.ecommerce.coupons.status_update_response import StatusUpdateResponse

__all__ = ["StatusResource", "AsyncStatusResource"]


class StatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return StatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return StatusResourceWithStreamingResponse(self)

    def update(
        self,
        coupon_id: str,
        *,
        is_active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusUpdateResponse:
        """
        The API endpoint allows an administrator role user to update the activity status
        of a coupon.

        It expects a request with a path variable `couponId` indicating the specific
        coupon to update. In the request body, there should be a `isActive` key, which
        is a boolean value indicating the desired status of the coupon.

        When this API is called, it toggles the active status of the coupon. This
        functionality allows the administrator to enable or disable the use of certain
        coupon codes in the application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coupon_id:
            raise ValueError(f"Expected a non-empty value for `coupon_id` but received {coupon_id!r}")
        return self._patch(
            f"/ecommerce/coupons/status/{coupon_id}",
            body=maybe_transform({"is_active": is_active}, status_update_params.StatusUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatusUpdateResponse,
        )


class AsyncStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncStatusResourceWithStreamingResponse(self)

    async def update(
        self,
        coupon_id: str,
        *,
        is_active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusUpdateResponse:
        """
        The API endpoint allows an administrator role user to update the activity status
        of a coupon.

        It expects a request with a path variable `couponId` indicating the specific
        coupon to update. In the request body, there should be a `isActive` key, which
        is a boolean value indicating the desired status of the coupon.

        When this API is called, it toggles the active status of the coupon. This
        functionality allows the administrator to enable or disable the use of certain
        coupon codes in the application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coupon_id:
            raise ValueError(f"Expected a non-empty value for `coupon_id` but received {coupon_id!r}")
        return await self._patch(
            f"/ecommerce/coupons/status/{coupon_id}",
            body=await async_maybe_transform({"is_active": is_active}, status_update_params.StatusUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatusUpdateResponse,
        )


class StatusResourceWithRawResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

        self.update = to_raw_response_wrapper(
            status.update,
        )


class AsyncStatusResourceWithRawResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

        self.update = async_to_raw_response_wrapper(
            status.update,
        )


class StatusResourceWithStreamingResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

        self.update = to_streamed_response_wrapper(
            status.update,
        )


class AsyncStatusResourceWithStreamingResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

        self.update = async_to_streamed_response_wrapper(
            status.update,
        )
