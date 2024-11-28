# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.ecommerce.orders.provider import razorpay_create_params, razorpay_verify_payment_params
from .....types.ecommerce.orders.provider.razorpay_create_response import RazorpayCreateResponse
from .....types.ecommerce.orders.provider.razorpay_verify_payment_response import RazorpayVerifyPaymentResponse

__all__ = ["RazorpayResource", "AsyncRazorpayResource"]


class RazorpayResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RazorpayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return RazorpayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RazorpayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return RazorpayResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RazorpayCreateResponse:
        """
        The API allows a user to generate a **Razorpay** order instance, facilitating
        the creation of an order and initiating the checkout flow before the payment.

        The API accepts the `addressId` of the user's address as input to associate it
        with the order.

        This functionality enables users to seamlessly generate an order and proceed to
        the checkout process, providing a smooth and efficient payment experience using
        Razorpay integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ecommerce/orders/provider/razorpay",
            body=maybe_transform({"address_id": address_id}, razorpay_create_params.RazorpayCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RazorpayCreateResponse,
        )

    def verify_payment(
        self,
        *,
        razorpay_order_id: str | NotGiven = NOT_GIVEN,
        razorpay_payment_id: str | NotGiven = NOT_GIVEN,
        razorpay_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RazorpayVerifyPaymentResponse:
        """
        The API handles the verification of a Razorpay payment.

        Once a user completes the payment, this API receives the Razorpay generated
        order credentials after payment (`razorpay_payment_id`, `razorpay_order_id`,
        `razorpay_signature`).

        It then verifies the payment using the provided credentials and marks the
        corresponding order as paid if the received credentials are valid.

        This API ensures secure and reliable payment processing, enabling the system to
        accurately track and manage paid orders.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ecommerce/orders/provider/razorpay/verify-payment",
            body=maybe_transform(
                {
                    "razorpay_order_id": razorpay_order_id,
                    "razorpay_payment_id": razorpay_payment_id,
                    "razorpay_signature": razorpay_signature,
                },
                razorpay_verify_payment_params.RazorpayVerifyPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RazorpayVerifyPaymentResponse,
        )


class AsyncRazorpayResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRazorpayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRazorpayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRazorpayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncRazorpayResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RazorpayCreateResponse:
        """
        The API allows a user to generate a **Razorpay** order instance, facilitating
        the creation of an order and initiating the checkout flow before the payment.

        The API accepts the `addressId` of the user's address as input to associate it
        with the order.

        This functionality enables users to seamlessly generate an order and proceed to
        the checkout process, providing a smooth and efficient payment experience using
        Razorpay integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ecommerce/orders/provider/razorpay",
            body=await async_maybe_transform({"address_id": address_id}, razorpay_create_params.RazorpayCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RazorpayCreateResponse,
        )

    async def verify_payment(
        self,
        *,
        razorpay_order_id: str | NotGiven = NOT_GIVEN,
        razorpay_payment_id: str | NotGiven = NOT_GIVEN,
        razorpay_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RazorpayVerifyPaymentResponse:
        """
        The API handles the verification of a Razorpay payment.

        Once a user completes the payment, this API receives the Razorpay generated
        order credentials after payment (`razorpay_payment_id`, `razorpay_order_id`,
        `razorpay_signature`).

        It then verifies the payment using the provided credentials and marks the
        corresponding order as paid if the received credentials are valid.

        This API ensures secure and reliable payment processing, enabling the system to
        accurately track and manage paid orders.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ecommerce/orders/provider/razorpay/verify-payment",
            body=await async_maybe_transform(
                {
                    "razorpay_order_id": razorpay_order_id,
                    "razorpay_payment_id": razorpay_payment_id,
                    "razorpay_signature": razorpay_signature,
                },
                razorpay_verify_payment_params.RazorpayVerifyPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RazorpayVerifyPaymentResponse,
        )


class RazorpayResourceWithRawResponse:
    def __init__(self, razorpay: RazorpayResource) -> None:
        self._razorpay = razorpay

        self.create = to_raw_response_wrapper(
            razorpay.create,
        )
        self.verify_payment = to_raw_response_wrapper(
            razorpay.verify_payment,
        )


class AsyncRazorpayResourceWithRawResponse:
    def __init__(self, razorpay: AsyncRazorpayResource) -> None:
        self._razorpay = razorpay

        self.create = async_to_raw_response_wrapper(
            razorpay.create,
        )
        self.verify_payment = async_to_raw_response_wrapper(
            razorpay.verify_payment,
        )


class RazorpayResourceWithStreamingResponse:
    def __init__(self, razorpay: RazorpayResource) -> None:
        self._razorpay = razorpay

        self.create = to_streamed_response_wrapper(
            razorpay.create,
        )
        self.verify_payment = to_streamed_response_wrapper(
            razorpay.verify_payment,
        )


class AsyncRazorpayResourceWithStreamingResponse:
    def __init__(self, razorpay: AsyncRazorpayResource) -> None:
        self._razorpay = razorpay

        self.create = async_to_streamed_response_wrapper(
            razorpay.create,
        )
        self.verify_payment = async_to_streamed_response_wrapper(
            razorpay.verify_payment,
        )
