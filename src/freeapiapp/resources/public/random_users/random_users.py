# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
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
from ....types.public import random_user_list_params
from ....types.public.random_user_list_response import RandomUserListResponse
from ....types.public.random_user_retrieve_response import RandomUserRetrieveResponse

__all__ = ["RandomUsersResource", "AsyncRandomUsersResource"]


class RandomUsersResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def with_raw_response(self) -> RandomUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return RandomUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RandomUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return RandomUsersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RandomUserRetrieveResponse:
        """
        The API endpoint retrieves a user based on the specified ID.

        When accessing this endpoint and providing a valid user ID as a parameter, you
        will receive a response containing the details of the user matching the provided
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/public/randomusers/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RandomUserRetrieveResponse,
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
    ) -> RandomUserListResponse:
        """The API endpoint retrieves a random list of users.

        When accessing this endpoint,
        you will receive a response containing a randomly generated list of users.

        This functionality is useful for scenarios such as testing, demo data
        generation, or populating user interfaces with dummy data.

        It provides a convenient way to obtain randomized user information for various
        purposes within your application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/randomusers",
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
                    random_user_list_params.RandomUserListParams,
                ),
            ),
            cast_to=RandomUserListResponse,
        )


class AsyncRandomUsersResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRandomUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRandomUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRandomUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncRandomUsersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RandomUserRetrieveResponse:
        """
        The API endpoint retrieves a user based on the specified ID.

        When accessing this endpoint and providing a valid user ID as a parameter, you
        will receive a response containing the details of the user matching the provided
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/public/randomusers/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RandomUserRetrieveResponse,
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
    ) -> RandomUserListResponse:
        """The API endpoint retrieves a random list of users.

        When accessing this endpoint,
        you will receive a response containing a randomly generated list of users.

        This functionality is useful for scenarios such as testing, demo data
        generation, or populating user interfaces with dummy data.

        It provides a convenient way to obtain randomized user information for various
        purposes within your application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/randomusers",
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
                    random_user_list_params.RandomUserListParams,
                ),
            ),
            cast_to=RandomUserListResponse,
        )


class RandomUsersResourceWithRawResponse:
    def __init__(self, random_users: RandomUsersResource) -> None:
        self._random_users = random_users

        self.retrieve = to_raw_response_wrapper(
            random_users.retrieve,
        )
        self.list = to_raw_response_wrapper(
            random_users.list,
        )

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._random_users.user)


class AsyncRandomUsersResourceWithRawResponse:
    def __init__(self, random_users: AsyncRandomUsersResource) -> None:
        self._random_users = random_users

        self.retrieve = async_to_raw_response_wrapper(
            random_users.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            random_users.list,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._random_users.user)


class RandomUsersResourceWithStreamingResponse:
    def __init__(self, random_users: RandomUsersResource) -> None:
        self._random_users = random_users

        self.retrieve = to_streamed_response_wrapper(
            random_users.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            random_users.list,
        )

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._random_users.user)


class AsyncRandomUsersResourceWithStreamingResponse:
    def __init__(self, random_users: AsyncRandomUsersResource) -> None:
        self._random_users = random_users

        self.retrieve = async_to_streamed_response_wrapper(
            random_users.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            random_users.list,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._random_users.user)
