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
from ...types.ecommerce import address_list_params, address_create_params, address_update_params
from ...types.ecommerce.address_list_response import AddressListResponse
from ...types.ecommerce.address_create_response import AddressCreateResponse
from ...types.ecommerce.address_delete_response import AddressDeleteResponse
from ...types.ecommerce.address_update_response import AddressUpdateResponse
from ...types.ecommerce.address_retrieve_response import AddressRetrieveResponse

__all__ = ["AddressesResource", "AsyncAddressesResource"]


class AddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AddressesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address_line1: str | NotGiven = NOT_GIVEN,
        address_line2: str | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        pincode: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressCreateResponse:
        """
        The API endpoint allows a logged-in user to create a new address in an
        e-commerce application.

        By accessing this endpoint and providing the necessary information, the user can
        add a new address to their profile for shipping or billing purposes.

        This functionality enables users to conveniently manage their address book
        within the e-commerce app, ensuring accurate and efficient order processing and
        delivery.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ecommerce/addresses",
            body=maybe_transform(
                {
                    "address_line1": address_line1,
                    "address_line2": address_line2,
                    "city": city,
                    "country": country,
                    "pincode": pincode,
                    "state": state,
                },
                address_create_params.AddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressCreateResponse,
        )

    def retrieve(
        self,
        address_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressRetrieveResponse:
        """
        The API endpoint allows users to fetch an address based on the `addressId`
        provided in the URL path variable.

        By accessing this endpoint and specifying a valid `addressId` in the URL, users
        will receive a response containing the details of the corresponding address.

        User can only be able to fetch addresses if they are logged in and the address
        that they are fetching is added by them.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address_id:
            raise ValueError(f"Expected a non-empty value for `address_id` but received {address_id!r}")
        return self._get(
            f"/ecommerce/addresses/{address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressRetrieveResponse,
        )

    def update(
        self,
        address_id: str,
        *,
        address_line1: str | NotGiven = NOT_GIVEN,
        address_line2: str | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        pincode: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressUpdateResponse:
        """
        The API endpoint allows a logged-in user to update their address based on the
        `addressId` provided.

        This functionality ensures that users can only update their own addresses within
        the context of an ecommerce application.

        By accessing this endpoint and providing the `addressId` of the address to be
        updated and necessary fields, the logged-in user can modify the address details
        such as street, city, state, or postal code etc.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address_id:
            raise ValueError(f"Expected a non-empty value for `address_id` but received {address_id!r}")
        return self._patch(
            f"/ecommerce/addresses/{address_id}",
            body=maybe_transform(
                {
                    "address_line1": address_line1,
                    "address_line2": address_line2,
                    "city": city,
                    "country": country,
                    "pincode": pincode,
                    "state": state,
                },
                address_update_params.AddressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressUpdateResponse,
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
    ) -> AddressListResponse:
        """
        The API endpoint allows a logged-in user to retrieve all the addresses saved in
        their profile within an e-commerce application.

        By accessing this endpoint, the user can retrieve a list of their saved
        addresses, that have been previously stored in their account.

        This functionality enables users to conveniently access and manage their saved
        addresses for a seamless checkout experience, eliminating the need to repeatedly
        enter address information for each transaction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ecommerce/addresses",
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
                    address_list_params.AddressListParams,
                ),
            ),
            cast_to=AddressListResponse,
        )

    def delete(
        self,
        address_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressDeleteResponse:
        """
        The API endpoint allows a logged-in user to delete their own address based on
        the provided `addressId` in the URL.

        When accessing this endpoint, the user can specify the `addressId` of the
        address they wish to delete.

        This functionality ensures that users can manage their address book by removing
        unwanted or outdated addresses from their profile within the ecommerce
        application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address_id:
            raise ValueError(f"Expected a non-empty value for `address_id` but received {address_id!r}")
        return self._delete(
            f"/ecommerce/addresses/{address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressDeleteResponse,
        )


class AsyncAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncAddressesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address_line1: str | NotGiven = NOT_GIVEN,
        address_line2: str | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        pincode: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressCreateResponse:
        """
        The API endpoint allows a logged-in user to create a new address in an
        e-commerce application.

        By accessing this endpoint and providing the necessary information, the user can
        add a new address to their profile for shipping or billing purposes.

        This functionality enables users to conveniently manage their address book
        within the e-commerce app, ensuring accurate and efficient order processing and
        delivery.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ecommerce/addresses",
            body=await async_maybe_transform(
                {
                    "address_line1": address_line1,
                    "address_line2": address_line2,
                    "city": city,
                    "country": country,
                    "pincode": pincode,
                    "state": state,
                },
                address_create_params.AddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressCreateResponse,
        )

    async def retrieve(
        self,
        address_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressRetrieveResponse:
        """
        The API endpoint allows users to fetch an address based on the `addressId`
        provided in the URL path variable.

        By accessing this endpoint and specifying a valid `addressId` in the URL, users
        will receive a response containing the details of the corresponding address.

        User can only be able to fetch addresses if they are logged in and the address
        that they are fetching is added by them.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address_id:
            raise ValueError(f"Expected a non-empty value for `address_id` but received {address_id!r}")
        return await self._get(
            f"/ecommerce/addresses/{address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressRetrieveResponse,
        )

    async def update(
        self,
        address_id: str,
        *,
        address_line1: str | NotGiven = NOT_GIVEN,
        address_line2: str | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        pincode: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressUpdateResponse:
        """
        The API endpoint allows a logged-in user to update their address based on the
        `addressId` provided.

        This functionality ensures that users can only update their own addresses within
        the context of an ecommerce application.

        By accessing this endpoint and providing the `addressId` of the address to be
        updated and necessary fields, the logged-in user can modify the address details
        such as street, city, state, or postal code etc.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address_id:
            raise ValueError(f"Expected a non-empty value for `address_id` but received {address_id!r}")
        return await self._patch(
            f"/ecommerce/addresses/{address_id}",
            body=await async_maybe_transform(
                {
                    "address_line1": address_line1,
                    "address_line2": address_line2,
                    "city": city,
                    "country": country,
                    "pincode": pincode,
                    "state": state,
                },
                address_update_params.AddressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressUpdateResponse,
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
    ) -> AddressListResponse:
        """
        The API endpoint allows a logged-in user to retrieve all the addresses saved in
        their profile within an e-commerce application.

        By accessing this endpoint, the user can retrieve a list of their saved
        addresses, that have been previously stored in their account.

        This functionality enables users to conveniently access and manage their saved
        addresses for a seamless checkout experience, eliminating the need to repeatedly
        enter address information for each transaction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ecommerce/addresses",
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
                    address_list_params.AddressListParams,
                ),
            ),
            cast_to=AddressListResponse,
        )

    async def delete(
        self,
        address_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressDeleteResponse:
        """
        The API endpoint allows a logged-in user to delete their own address based on
        the provided `addressId` in the URL.

        When accessing this endpoint, the user can specify the `addressId` of the
        address they wish to delete.

        This functionality ensures that users can manage their address book by removing
        unwanted or outdated addresses from their profile within the ecommerce
        application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address_id:
            raise ValueError(f"Expected a non-empty value for `address_id` but received {address_id!r}")
        return await self._delete(
            f"/ecommerce/addresses/{address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressDeleteResponse,
        )


class AddressesResourceWithRawResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.create = to_raw_response_wrapper(
            addresses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            addresses.retrieve,
        )
        self.update = to_raw_response_wrapper(
            addresses.update,
        )
        self.list = to_raw_response_wrapper(
            addresses.list,
        )
        self.delete = to_raw_response_wrapper(
            addresses.delete,
        )


class AsyncAddressesResourceWithRawResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.create = async_to_raw_response_wrapper(
            addresses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            addresses.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            addresses.update,
        )
        self.list = async_to_raw_response_wrapper(
            addresses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            addresses.delete,
        )


class AddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.create = to_streamed_response_wrapper(
            addresses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            addresses.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            addresses.update,
        )
        self.list = to_streamed_response_wrapper(
            addresses.list,
        )
        self.delete = to_streamed_response_wrapper(
            addresses.delete,
        )


class AsyncAddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.create = async_to_streamed_response_wrapper(
            addresses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            addresses.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            addresses.update,
        )
        self.list = async_to_streamed_response_wrapper(
            addresses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            addresses.delete,
        )
