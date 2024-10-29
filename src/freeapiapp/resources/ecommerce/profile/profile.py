# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .my_orders import (
    MyOrdersResource,
    AsyncMyOrdersResource,
    MyOrdersResourceWithRawResponse,
    AsyncMyOrdersResourceWithRawResponse,
    MyOrdersResourceWithStreamingResponse,
    AsyncMyOrdersResourceWithStreamingResponse,
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
from ....types.ecommerce import profile_update_params
from ....types.ecommerce.profile_update_response import ProfileUpdateResponse
from ....types.ecommerce.profile_retrieve_response import ProfileRetrieveResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    @cached_property
    def my_orders(self) -> MyOrdersResource:
        return MyOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileRetrieveResponse:
        """
        The API endpoint allows you to retrieve the e-commerce profile of the logged-in
        user.

        When accessing this endpoint, you will receive a response containing the basic
        details of the user's e-commerce profile.

        This includes information such as the user's name, email address, phone number,
        and other relevant details.
        """
        return self._get(
            "/ecommerce/profile",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    def update(
        self,
        *,
        country_code: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileUpdateResponse:
        """
        The API endpoint allows a logged-in user to update their e-commerce profile.

        With this endpoint, users can make changes and updates to their profile
        information, such as personal details, contact information, or any other
        relevant profile attributes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/ecommerce/profile",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )


class AsyncProfileResource(AsyncAPIResource):
    @cached_property
    def my_orders(self) -> AsyncMyOrdersResource:
        return AsyncMyOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileRetrieveResponse:
        """
        The API endpoint allows you to retrieve the e-commerce profile of the logged-in
        user.

        When accessing this endpoint, you will receive a response containing the basic
        details of the user's e-commerce profile.

        This includes information such as the user's name, email address, phone number,
        and other relevant details.
        """
        return await self._get(
            "/ecommerce/profile",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    async def update(
        self,
        *,
        country_code: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileUpdateResponse:
        """
        The API endpoint allows a logged-in user to update their e-commerce profile.

        With this endpoint, users can make changes and updates to their profile
        information, such as personal details, contact information, or any other
        relevant profile attributes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/ecommerce/profile",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_raw_response_wrapper(
            profile.retrieve,
        )
        self.update = to_raw_response_wrapper(
            profile.update,
        )

    @cached_property
    def my_orders(self) -> MyOrdersResourceWithRawResponse:
        return MyOrdersResourceWithRawResponse(self._profile.my_orders)


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_raw_response_wrapper(
            profile.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            profile.update,
        )

    @cached_property
    def my_orders(self) -> AsyncMyOrdersResourceWithRawResponse:
        return AsyncMyOrdersResourceWithRawResponse(self._profile.my_orders)


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            profile.update,
        )

    @cached_property
    def my_orders(self) -> MyOrdersResourceWithStreamingResponse:
        return MyOrdersResourceWithStreamingResponse(self._profile.my_orders)


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            profile.update,
        )

    @cached_property
    def my_orders(self) -> AsyncMyOrdersResourceWithStreamingResponse:
        return AsyncMyOrdersResourceWithStreamingResponse(self._profile.my_orders)
