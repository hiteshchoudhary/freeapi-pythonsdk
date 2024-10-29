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
from ....types.social_media.posts import user_post_list_params
from ....types.social_media.posts.user_post_list_response import UserPostListResponse

__all__ = ["UserPostsResource", "AsyncUserPostsResource"]


class UserPostsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return UserPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return UserPostsResourceWithStreamingResponse(self)

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
    ) -> UserPostListResponse:
        """
        The API endpoint allows users to fetch posts of other users by passing the
        username as a path variable.

        When accessing this endpoint and providing a valid username as a parameter, you
        will receive a response containing the posts associated with the specified
        username.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/social-media/posts/get/u/{username}",
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
                    user_post_list_params.UserPostListParams,
                ),
            ),
            cast_to=UserPostListResponse,
        )


class AsyncUserPostsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUserPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncUserPostsResourceWithStreamingResponse(self)

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
    ) -> UserPostListResponse:
        """
        The API endpoint allows users to fetch posts of other users by passing the
        username as a path variable.

        When accessing this endpoint and providing a valid username as a parameter, you
        will receive a response containing the posts associated with the specified
        username.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/social-media/posts/get/u/{username}",
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
                    user_post_list_params.UserPostListParams,
                ),
            ),
            cast_to=UserPostListResponse,
        )


class UserPostsResourceWithRawResponse:
    def __init__(self, user_posts: UserPostsResource) -> None:
        self._user_posts = user_posts

        self.list = to_raw_response_wrapper(
            user_posts.list,
        )


class AsyncUserPostsResourceWithRawResponse:
    def __init__(self, user_posts: AsyncUserPostsResource) -> None:
        self._user_posts = user_posts

        self.list = async_to_raw_response_wrapper(
            user_posts.list,
        )


class UserPostsResourceWithStreamingResponse:
    def __init__(self, user_posts: UserPostsResource) -> None:
        self._user_posts = user_posts

        self.list = to_streamed_response_wrapper(
            user_posts.list,
        )


class AsyncUserPostsResourceWithStreamingResponse:
    def __init__(self, user_posts: AsyncUserPostsResource) -> None:
        self._user_posts = user_posts

        self.list = async_to_streamed_response_wrapper(
            user_posts.list,
        )
