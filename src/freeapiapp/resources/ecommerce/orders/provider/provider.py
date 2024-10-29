# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .paypal import (
    PaypalResource,
    AsyncPaypalResource,
    PaypalResourceWithRawResponse,
    AsyncPaypalResourceWithRawResponse,
    PaypalResourceWithStreamingResponse,
    AsyncPaypalResourceWithStreamingResponse,
)
from .razorpay import (
    RazorpayResource,
    AsyncRazorpayResource,
    RazorpayResourceWithRawResponse,
    AsyncRazorpayResourceWithRawResponse,
    RazorpayResourceWithStreamingResponse,
    AsyncRazorpayResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ProviderResource", "AsyncProviderResource"]


class ProviderResource(SyncAPIResource):
    @cached_property
    def razorpay(self) -> RazorpayResource:
        return RazorpayResource(self._client)

    @cached_property
    def paypal(self) -> PaypalResource:
        return PaypalResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return ProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return ProviderResourceWithStreamingResponse(self)


class AsyncProviderResource(AsyncAPIResource):
    @cached_property
    def razorpay(self) -> AsyncRazorpayResource:
        return AsyncRazorpayResource(self._client)

    @cached_property
    def paypal(self) -> AsyncPaypalResource:
        return AsyncPaypalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncProviderResourceWithStreamingResponse(self)


class ProviderResourceWithRawResponse:
    def __init__(self, provider: ProviderResource) -> None:
        self._provider = provider

    @cached_property
    def razorpay(self) -> RazorpayResourceWithRawResponse:
        return RazorpayResourceWithRawResponse(self._provider.razorpay)

    @cached_property
    def paypal(self) -> PaypalResourceWithRawResponse:
        return PaypalResourceWithRawResponse(self._provider.paypal)


class AsyncProviderResourceWithRawResponse:
    def __init__(self, provider: AsyncProviderResource) -> None:
        self._provider = provider

    @cached_property
    def razorpay(self) -> AsyncRazorpayResourceWithRawResponse:
        return AsyncRazorpayResourceWithRawResponse(self._provider.razorpay)

    @cached_property
    def paypal(self) -> AsyncPaypalResourceWithRawResponse:
        return AsyncPaypalResourceWithRawResponse(self._provider.paypal)


class ProviderResourceWithStreamingResponse:
    def __init__(self, provider: ProviderResource) -> None:
        self._provider = provider

    @cached_property
    def razorpay(self) -> RazorpayResourceWithStreamingResponse:
        return RazorpayResourceWithStreamingResponse(self._provider.razorpay)

    @cached_property
    def paypal(self) -> PaypalResourceWithStreamingResponse:
        return PaypalResourceWithStreamingResponse(self._provider.paypal)


class AsyncProviderResourceWithStreamingResponse:
    def __init__(self, provider: AsyncProviderResource) -> None:
        self._provider = provider

    @cached_property
    def razorpay(self) -> AsyncRazorpayResourceWithStreamingResponse:
        return AsyncRazorpayResourceWithStreamingResponse(self._provider.razorpay)

    @cached_property
    def paypal(self) -> AsyncPaypalResourceWithStreamingResponse:
        return AsyncPaypalResourceWithStreamingResponse(self._provider.paypal)
