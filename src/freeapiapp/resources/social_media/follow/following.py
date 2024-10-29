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
from ....types.social_media.follow import following_list_params
from ....types.social_media.follow.following_list_response import FollowingListResponse

__all__ = ["FollowingResource", "AsyncFollowingResource"]


class FollowingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FollowingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return FollowingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FollowingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return FollowingResourceWithStreamingResponse(self)

    def list(
        self,
        username: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FollowingListResponse:
        """
        The API endpoint allows you to retrieve the list of users which are being
        followed by a specific user based on their username passed as a path variable.

        When accessing this endpoint, you will receive a response containing the users'
        information followed by the specified user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/social-media/follow/list/following/{username}",
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
                    following_list_params.FollowingListParams,
                ),
            ),
            cast_to=FollowingListResponse,
        )


class AsyncFollowingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFollowingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFollowingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFollowingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncFollowingResourceWithStreamingResponse(self)

    async def list(
        self,
        username: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FollowingListResponse:
        """
        The API endpoint allows you to retrieve the list of users which are being
        followed by a specific user based on their username passed as a path variable.

        When accessing this endpoint, you will receive a response containing the users'
        information followed by the specified user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/social-media/follow/list/following/{username}",
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
                    following_list_params.FollowingListParams,
                ),
            ),
            cast_to=FollowingListResponse,
        )


class FollowingResourceWithRawResponse:
    def __init__(self, following: FollowingResource) -> None:
        self._following = following

        self.list = to_raw_response_wrapper(
            following.list,
        )


class AsyncFollowingResourceWithRawResponse:
    def __init__(self, following: AsyncFollowingResource) -> None:
        self._following = following

        self.list = async_to_raw_response_wrapper(
            following.list,
        )


class FollowingResourceWithStreamingResponse:
    def __init__(self, following: FollowingResource) -> None:
        self._following = following

        self.list = to_streamed_response_wrapper(
            following.list,
        )


class AsyncFollowingResourceWithStreamingResponse:
    def __init__(self, following: AsyncFollowingResource) -> None:
        self._following = following

        self.list = async_to_streamed_response_wrapper(
            following.list,
        )
