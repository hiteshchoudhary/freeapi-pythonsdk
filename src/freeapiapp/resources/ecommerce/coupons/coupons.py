# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
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
from ....types.ecommerce import (
    coupon_list_params,
    coupon_apply_params,
    coupon_create_params,
    coupon_remove_params,
    coupon_update_params,
)
from .customer_available import (
    CustomerAvailableResource,
    AsyncCustomerAvailableResource,
    CustomerAvailableResourceWithRawResponse,
    AsyncCustomerAvailableResourceWithRawResponse,
    CustomerAvailableResourceWithStreamingResponse,
    AsyncCustomerAvailableResourceWithStreamingResponse,
)
from ....types.ecommerce.coupon_list_response import CouponListResponse
from ....types.ecommerce.coupon_apply_response import CouponApplyResponse
from ....types.ecommerce.coupon_create_response import CouponCreateResponse
from ....types.ecommerce.coupon_delete_response import CouponDeleteResponse
from ....types.ecommerce.coupon_remove_response import CouponRemoveResponse
from ....types.ecommerce.coupon_update_response import CouponUpdateResponse
from ....types.ecommerce.coupon_retrieve_response import CouponRetrieveResponse

__all__ = ["CouponsResource", "AsyncCouponsResource"]


class CouponsResource(SyncAPIResource):
    @cached_property
    def customer_available(self) -> CustomerAvailableResource:
        return CustomerAvailableResource(self._client)

    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> CouponsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return CouponsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CouponsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return CouponsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        coupon_code: str | NotGiven = NOT_GIVEN,
        discount_value: float | NotGiven = NOT_GIVEN,
        expiry_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        minimum_cart_value: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        type: Literal["FLAT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponCreateResponse:
        """
        The API allows users with an `ADMIN` role to create a coupon.

        This API endpoint accepts the necessary information for creating a coupon, such
        as the coupon code, discount amount, expiration date, and any additional
        conditions.

        The endpoint performs authentication and authorization checks to ensure that
        only users with the `ADMIN` role can access it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ecommerce/coupons",
            body=maybe_transform(
                {
                    "coupon_code": coupon_code,
                    "discount_value": discount_value,
                    "expiry_date": expiry_date,
                    "minimum_cart_value": minimum_cart_value,
                    "name": name,
                    "start_date": start_date,
                    "type": type,
                },
                coupon_create_params.CouponCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponCreateResponse,
        )

    def retrieve(
        self,
        coupon_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponRetrieveResponse:
        """
        The API endpoint allows a logged-in user to retrieve a coupon by providing the
        `couponId` as a path variable.

        By making a request to the API with the appropriate `couponId`, the server will
        return the corresponding coupon details, such as its code, discount amount,
        expiration date, or any other relevant information associated with that specific
        coupon.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coupon_id:
            raise ValueError(f"Expected a non-empty value for `coupon_id` but received {coupon_id!r}")
        return self._get(
            f"/ecommerce/coupons/{coupon_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponRetrieveResponse,
        )

    def update(
        self,
        coupon_id: str,
        *,
        coupon_code: str | NotGiven = NOT_GIVEN,
        discount_value: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponUpdateResponse:
        """
        The API allows an `ADMIN` role user to update a coupon by sending the required
        data in the request body and specifying the `couponId` in the path variable.

        This endpoint grants authorized users the ability to modify existing coupon
        details, such as its code, discount amount, expiration date, or any other
        relevant attributes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coupon_id:
            raise ValueError(f"Expected a non-empty value for `coupon_id` but received {coupon_id!r}")
        return self._patch(
            f"/ecommerce/coupons/{coupon_id}",
            body=maybe_transform(
                {
                    "coupon_code": coupon_code,
                    "discount_value": discount_value,
                    "name": name,
                },
                coupon_update_params.CouponUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponUpdateResponse,
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
    ) -> CouponListResponse:
        """
        The API endpoint allows a logged-in user to retrieve all the available coupons
        in an ecommerce app before proceeding with the checkout process.

        This API provides a list of coupons that users can apply to their purchase,
        potentially offering discounts or special offers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ecommerce/coupons",
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
                    coupon_list_params.CouponListParams,
                ),
            ),
            cast_to=CouponListResponse,
        )

    def delete(
        self,
        coupon_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponDeleteResponse:
        """
        The API allows users with an `ADMIN` role to delete a coupon by providing the
        `couponId` as a path variable.

        The API verifies the user's role before processing the request and deletes the
        coupon associated with the provided `couponId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coupon_id:
            raise ValueError(f"Expected a non-empty value for `coupon_id` but received {coupon_id!r}")
        return self._delete(
            f"/ecommerce/coupons/{coupon_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponDeleteResponse,
        )

    def apply(
        self,
        *,
        coupon_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponApplyResponse:
        """
        The API allows a logged-in user to apply a coupon before proceeding to checkout.
        It performs the following tasks:

        1. **Verification of eligibility:** The API checks if the user is eligible to
           apply the coupon based on certain criteria, such as the total amount in the
           user's shopping cart.
        2. **Calculation of discounted cart value:** If the user is eligible, the API
           calculates the updated cart value by applying the discount offered by the
           coupon. This involves reducing the total cart amount by an amount based on
           the coupon details.
        3. **Return of updated cart:** Finally, the API returns the updated cart to the
           user, reflecting the applied discount. The user can then proceed to checkout
           with the discounted cart value.

        In summary, this API provides a mechanism for users to apply coupons, verifies
        their eligibility, calculates the discounted cart value, and returns the updated
        cart for a seamless checkout experience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ecommerce/coupons/c/apply",
            body=maybe_transform({"coupon_code": coupon_code}, coupon_apply_params.CouponApplyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponApplyResponse,
        )

    def remove(
        self,
        *,
        coupon_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponRemoveResponse:
        """
        The API for removing an applied coupon allows a logged-in user to remove a
        coupon code that was previously applied to their cart.

        Once the coupon is removed, the API recalculates the total value of the cart
        without considering the discount amount, resulting in a non-discounted cart
        value.

        This API essentially resets the cart to its original value before the coupon was
        applied, removing any discounts that were previously applied.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ecommerce/coupons/c/remove",
            body=maybe_transform({"coupon_code": coupon_code}, coupon_remove_params.CouponRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponRemoveResponse,
        )


class AsyncCouponsResource(AsyncAPIResource):
    @cached_property
    def customer_available(self) -> AsyncCustomerAvailableResource:
        return AsyncCustomerAvailableResource(self._client)

    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCouponsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCouponsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCouponsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncCouponsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        coupon_code: str | NotGiven = NOT_GIVEN,
        discount_value: float | NotGiven = NOT_GIVEN,
        expiry_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        minimum_cart_value: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        type: Literal["FLAT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponCreateResponse:
        """
        The API allows users with an `ADMIN` role to create a coupon.

        This API endpoint accepts the necessary information for creating a coupon, such
        as the coupon code, discount amount, expiration date, and any additional
        conditions.

        The endpoint performs authentication and authorization checks to ensure that
        only users with the `ADMIN` role can access it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ecommerce/coupons",
            body=await async_maybe_transform(
                {
                    "coupon_code": coupon_code,
                    "discount_value": discount_value,
                    "expiry_date": expiry_date,
                    "minimum_cart_value": minimum_cart_value,
                    "name": name,
                    "start_date": start_date,
                    "type": type,
                },
                coupon_create_params.CouponCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponCreateResponse,
        )

    async def retrieve(
        self,
        coupon_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponRetrieveResponse:
        """
        The API endpoint allows a logged-in user to retrieve a coupon by providing the
        `couponId` as a path variable.

        By making a request to the API with the appropriate `couponId`, the server will
        return the corresponding coupon details, such as its code, discount amount,
        expiration date, or any other relevant information associated with that specific
        coupon.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coupon_id:
            raise ValueError(f"Expected a non-empty value for `coupon_id` but received {coupon_id!r}")
        return await self._get(
            f"/ecommerce/coupons/{coupon_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponRetrieveResponse,
        )

    async def update(
        self,
        coupon_id: str,
        *,
        coupon_code: str | NotGiven = NOT_GIVEN,
        discount_value: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponUpdateResponse:
        """
        The API allows an `ADMIN` role user to update a coupon by sending the required
        data in the request body and specifying the `couponId` in the path variable.

        This endpoint grants authorized users the ability to modify existing coupon
        details, such as its code, discount amount, expiration date, or any other
        relevant attributes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coupon_id:
            raise ValueError(f"Expected a non-empty value for `coupon_id` but received {coupon_id!r}")
        return await self._patch(
            f"/ecommerce/coupons/{coupon_id}",
            body=await async_maybe_transform(
                {
                    "coupon_code": coupon_code,
                    "discount_value": discount_value,
                    "name": name,
                },
                coupon_update_params.CouponUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponUpdateResponse,
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
    ) -> CouponListResponse:
        """
        The API endpoint allows a logged-in user to retrieve all the available coupons
        in an ecommerce app before proceeding with the checkout process.

        This API provides a list of coupons that users can apply to their purchase,
        potentially offering discounts or special offers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ecommerce/coupons",
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
                    coupon_list_params.CouponListParams,
                ),
            ),
            cast_to=CouponListResponse,
        )

    async def delete(
        self,
        coupon_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponDeleteResponse:
        """
        The API allows users with an `ADMIN` role to delete a coupon by providing the
        `couponId` as a path variable.

        The API verifies the user's role before processing the request and deletes the
        coupon associated with the provided `couponId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coupon_id:
            raise ValueError(f"Expected a non-empty value for `coupon_id` but received {coupon_id!r}")
        return await self._delete(
            f"/ecommerce/coupons/{coupon_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponDeleteResponse,
        )

    async def apply(
        self,
        *,
        coupon_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponApplyResponse:
        """
        The API allows a logged-in user to apply a coupon before proceeding to checkout.
        It performs the following tasks:

        1. **Verification of eligibility:** The API checks if the user is eligible to
           apply the coupon based on certain criteria, such as the total amount in the
           user's shopping cart.
        2. **Calculation of discounted cart value:** If the user is eligible, the API
           calculates the updated cart value by applying the discount offered by the
           coupon. This involves reducing the total cart amount by an amount based on
           the coupon details.
        3. **Return of updated cart:** Finally, the API returns the updated cart to the
           user, reflecting the applied discount. The user can then proceed to checkout
           with the discounted cart value.

        In summary, this API provides a mechanism for users to apply coupons, verifies
        their eligibility, calculates the discounted cart value, and returns the updated
        cart for a seamless checkout experience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ecommerce/coupons/c/apply",
            body=await async_maybe_transform({"coupon_code": coupon_code}, coupon_apply_params.CouponApplyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponApplyResponse,
        )

    async def remove(
        self,
        *,
        coupon_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CouponRemoveResponse:
        """
        The API for removing an applied coupon allows a logged-in user to remove a
        coupon code that was previously applied to their cart.

        Once the coupon is removed, the API recalculates the total value of the cart
        without considering the discount amount, resulting in a non-discounted cart
        value.

        This API essentially resets the cart to its original value before the coupon was
        applied, removing any discounts that were previously applied.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ecommerce/coupons/c/remove",
            body=await async_maybe_transform({"coupon_code": coupon_code}, coupon_remove_params.CouponRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponRemoveResponse,
        )


class CouponsResourceWithRawResponse:
    def __init__(self, coupons: CouponsResource) -> None:
        self._coupons = coupons

        self.create = to_raw_response_wrapper(
            coupons.create,
        )
        self.retrieve = to_raw_response_wrapper(
            coupons.retrieve,
        )
        self.update = to_raw_response_wrapper(
            coupons.update,
        )
        self.list = to_raw_response_wrapper(
            coupons.list,
        )
        self.delete = to_raw_response_wrapper(
            coupons.delete,
        )
        self.apply = to_raw_response_wrapper(
            coupons.apply,
        )
        self.remove = to_raw_response_wrapper(
            coupons.remove,
        )

    @cached_property
    def customer_available(self) -> CustomerAvailableResourceWithRawResponse:
        return CustomerAvailableResourceWithRawResponse(self._coupons.customer_available)

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._coupons.status)


class AsyncCouponsResourceWithRawResponse:
    def __init__(self, coupons: AsyncCouponsResource) -> None:
        self._coupons = coupons

        self.create = async_to_raw_response_wrapper(
            coupons.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            coupons.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            coupons.update,
        )
        self.list = async_to_raw_response_wrapper(
            coupons.list,
        )
        self.delete = async_to_raw_response_wrapper(
            coupons.delete,
        )
        self.apply = async_to_raw_response_wrapper(
            coupons.apply,
        )
        self.remove = async_to_raw_response_wrapper(
            coupons.remove,
        )

    @cached_property
    def customer_available(self) -> AsyncCustomerAvailableResourceWithRawResponse:
        return AsyncCustomerAvailableResourceWithRawResponse(self._coupons.customer_available)

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._coupons.status)


class CouponsResourceWithStreamingResponse:
    def __init__(self, coupons: CouponsResource) -> None:
        self._coupons = coupons

        self.create = to_streamed_response_wrapper(
            coupons.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            coupons.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            coupons.update,
        )
        self.list = to_streamed_response_wrapper(
            coupons.list,
        )
        self.delete = to_streamed_response_wrapper(
            coupons.delete,
        )
        self.apply = to_streamed_response_wrapper(
            coupons.apply,
        )
        self.remove = to_streamed_response_wrapper(
            coupons.remove,
        )

    @cached_property
    def customer_available(self) -> CustomerAvailableResourceWithStreamingResponse:
        return CustomerAvailableResourceWithStreamingResponse(self._coupons.customer_available)

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._coupons.status)


class AsyncCouponsResourceWithStreamingResponse:
    def __init__(self, coupons: AsyncCouponsResource) -> None:
        self._coupons = coupons

        self.create = async_to_streamed_response_wrapper(
            coupons.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            coupons.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            coupons.update,
        )
        self.list = async_to_streamed_response_wrapper(
            coupons.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            coupons.delete,
        )
        self.apply = async_to_streamed_response_wrapper(
            coupons.apply,
        )
        self.remove = async_to_streamed_response_wrapper(
            coupons.remove,
        )

    @cached_property
    def customer_available(self) -> AsyncCustomerAvailableResourceWithStreamingResponse:
        return AsyncCustomerAvailableResourceWithStreamingResponse(self._coupons.customer_available)

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._coupons.status)
