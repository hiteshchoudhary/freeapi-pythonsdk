# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from .....types.ecommerce.orders.provider import paypal_create_params, paypal_verify_payment_params
from .....types.ecommerce.orders.provider.paypal_create_response import PaypalCreateResponse

__all__ = ["PaypalResource", "AsyncPaypalResource"]


class PaypalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaypalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return PaypalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaypalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return PaypalResourceWithStreamingResponse(self)

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
    ) -> PaypalCreateResponse:
        """
        The API allows a user to generate a **PayPal** order instance, facilitating the
        creation of an order and initiating the checkout flow before the payment.

        The API accepts the `addressId` of the user's address as input to associate it
        with the order.

        This functionality enables users to seamlessly generate an order and proceed to
        the checkout process, providing a smooth and efficient payment experience using
        PayPal integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ecommerce/orders/provider/paypal",
            body=maybe_transform({"address_id": address_id}, paypal_create_params.PaypalCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaypalCreateResponse,
        )

    def verify_payment(
        self,
        *,
        order_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API handles the verification of a **PayPal** payment by integrating with
        PayPal's order capture API.

        Once a user completes a payment on PayPal, this API receives the
        PayPal-generated order ID which will be passed by the client on payment success.

        It then makes an API call to PayPal's order capture API to retrieve the payment
        status.

        The backend utilizes this payment status information to verify the payment and
        mark the corresponding order as paid in the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ecommerce/orders/provider/paypal/verify-payment",
            body=maybe_transform({"order_id": order_id}, paypal_verify_payment_params.PaypalVerifyPaymentParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPaypalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaypalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPaypalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaypalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncPaypalResourceWithStreamingResponse(self)

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
    ) -> PaypalCreateResponse:
        """
        The API allows a user to generate a **PayPal** order instance, facilitating the
        creation of an order and initiating the checkout flow before the payment.

        The API accepts the `addressId` of the user's address as input to associate it
        with the order.

        This functionality enables users to seamlessly generate an order and proceed to
        the checkout process, providing a smooth and efficient payment experience using
        PayPal integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ecommerce/orders/provider/paypal",
            body=await async_maybe_transform({"address_id": address_id}, paypal_create_params.PaypalCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaypalCreateResponse,
        )

    async def verify_payment(
        self,
        *,
        order_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API handles the verification of a **PayPal** payment by integrating with
        PayPal's order capture API.

        Once a user completes a payment on PayPal, this API receives the
        PayPal-generated order ID which will be passed by the client on payment success.

        It then makes an API call to PayPal's order capture API to retrieve the payment
        status.

        The backend utilizes this payment status information to verify the payment and
        mark the corresponding order as paid in the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ecommerce/orders/provider/paypal/verify-payment",
            body=await async_maybe_transform(
                {"order_id": order_id}, paypal_verify_payment_params.PaypalVerifyPaymentParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PaypalResourceWithRawResponse:
    def __init__(self, paypal: PaypalResource) -> None:
        self._paypal = paypal

        self.create = to_raw_response_wrapper(
            paypal.create,
        )
        self.verify_payment = to_raw_response_wrapper(
            paypal.verify_payment,
        )


class AsyncPaypalResourceWithRawResponse:
    def __init__(self, paypal: AsyncPaypalResource) -> None:
        self._paypal = paypal

        self.create = async_to_raw_response_wrapper(
            paypal.create,
        )
        self.verify_payment = async_to_raw_response_wrapper(
            paypal.verify_payment,
        )


class PaypalResourceWithStreamingResponse:
    def __init__(self, paypal: PaypalResource) -> None:
        self._paypal = paypal

        self.create = to_streamed_response_wrapper(
            paypal.create,
        )
        self.verify_payment = to_streamed_response_wrapper(
            paypal.verify_payment,
        )


class AsyncPaypalResourceWithStreamingResponse:
    def __init__(self, paypal: AsyncPaypalResource) -> None:
        self._paypal = paypal

        self.create = async_to_streamed_response_wrapper(
            paypal.create,
        )
        self.verify_payment = async_to_streamed_response_wrapper(
            paypal.verify_payment,
        )
