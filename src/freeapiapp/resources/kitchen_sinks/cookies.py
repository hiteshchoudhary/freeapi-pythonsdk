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
from ...types.kitchen_sinks import cookie_create_params, cookie_remove_params
from ...types.kitchen_sinks.cookie_create_response import CookieCreateResponse
from ...types.kitchen_sinks.cookie_remove_response import CookieRemoveResponse
from ...types.kitchen_sinks.cookie_retrieve_response import CookieRetrieveResponse

__all__ = ["CookiesResource", "AsyncCookiesResource"]


class CookiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CookiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return CookiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CookiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return CookiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        foo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CookieCreateResponse:
        """
        The API endpoint allows you to set cookies on the client's browser as part of
        the response.

        When accessing this endpoint, you can include specific cookie information in the
        response headers, which will be stored by the client's browser for future
        requests.

        This functionality enables you to set and manage cookies on the client side,
        which can be used for various purposes such as session management, user
        authentication, personalization, or tracking user preferences within your
        application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/kitchen-sink/cookies/set",
            body=maybe_transform({"foo": foo}, cookie_create_params.CookieCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CookieCreateResponse,
        )

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CookieRetrieveResponse:
        """
        The API endpoint allows you to retrieve the cookies sent by the client as part
        of the request.

        When accessing this endpoint, you will receive the cookies that were included in
        the request headers from the client.

        This functionality enables you to access and utilize the cookie data sent by the
        client for various purposes, such as session management, authentication, or
        personalization within your application.
        """
        return self._get(
            "/kitchen-sink/cookies/get",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CookieRetrieveResponse,
        )

    def remove(
        self,
        *,
        cookie_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CookieRemoveResponse:
        """
        The API endpoint facilitates the deletion of cookies from the client's browser.

        By accessing this endpoint, you can send a response that instructs the client's
        browser to remove specific cookies associated with your application.

        This functionality allows you to manage and revoke cookies on the client side,
        enabling tasks such as clearing session data, implementing logouts, or removing
        user preferences stored in cookies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/kitchen-sink/cookies/remove",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cookie_key": cookie_key}, cookie_remove_params.CookieRemoveParams),
            ),
            cast_to=CookieRemoveResponse,
        )


class AsyncCookiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCookiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCookiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCookiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncCookiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        foo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CookieCreateResponse:
        """
        The API endpoint allows you to set cookies on the client's browser as part of
        the response.

        When accessing this endpoint, you can include specific cookie information in the
        response headers, which will be stored by the client's browser for future
        requests.

        This functionality enables you to set and manage cookies on the client side,
        which can be used for various purposes such as session management, user
        authentication, personalization, or tracking user preferences within your
        application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/kitchen-sink/cookies/set",
            body=await async_maybe_transform({"foo": foo}, cookie_create_params.CookieCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CookieCreateResponse,
        )

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CookieRetrieveResponse:
        """
        The API endpoint allows you to retrieve the cookies sent by the client as part
        of the request.

        When accessing this endpoint, you will receive the cookies that were included in
        the request headers from the client.

        This functionality enables you to access and utilize the cookie data sent by the
        client for various purposes, such as session management, authentication, or
        personalization within your application.
        """
        return await self._get(
            "/kitchen-sink/cookies/get",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CookieRetrieveResponse,
        )

    async def remove(
        self,
        *,
        cookie_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CookieRemoveResponse:
        """
        The API endpoint facilitates the deletion of cookies from the client's browser.

        By accessing this endpoint, you can send a response that instructs the client's
        browser to remove specific cookies associated with your application.

        This functionality allows you to manage and revoke cookies on the client side,
        enabling tasks such as clearing session data, implementing logouts, or removing
        user preferences stored in cookies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/kitchen-sink/cookies/remove",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cookie_key": cookie_key}, cookie_remove_params.CookieRemoveParams),
            ),
            cast_to=CookieRemoveResponse,
        )


class CookiesResourceWithRawResponse:
    def __init__(self, cookies: CookiesResource) -> None:
        self._cookies = cookies

        self.create = to_raw_response_wrapper(
            cookies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            cookies.retrieve,
        )
        self.remove = to_raw_response_wrapper(
            cookies.remove,
        )


class AsyncCookiesResourceWithRawResponse:
    def __init__(self, cookies: AsyncCookiesResource) -> None:
        self._cookies = cookies

        self.create = async_to_raw_response_wrapper(
            cookies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            cookies.retrieve,
        )
        self.remove = async_to_raw_response_wrapper(
            cookies.remove,
        )


class CookiesResourceWithStreamingResponse:
    def __init__(self, cookies: CookiesResource) -> None:
        self._cookies = cookies

        self.create = to_streamed_response_wrapper(
            cookies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            cookies.retrieve,
        )
        self.remove = to_streamed_response_wrapper(
            cookies.remove,
        )


class AsyncCookiesResourceWithStreamingResponse:
    def __init__(self, cookies: AsyncCookiesResource) -> None:
        self._cookies = cookies

        self.create = async_to_streamed_response_wrapper(
            cookies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            cookies.retrieve,
        )
        self.remove = async_to_streamed_response_wrapper(
            cookies.remove,
        )
