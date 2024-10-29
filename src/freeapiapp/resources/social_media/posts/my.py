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
from ....types.social_media.posts import my_list_params
from ....types.social_media.posts.my_list_response import MyListResponse

__all__ = ["MyResource", "AsyncMyResource"]


class MyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return MyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return MyResourceWithStreamingResponse(self)

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
    ) -> MyListResponse:
        """
        The API endpoint allows a logged-in user to fetch their own posts, which can be
        displayed on the "My Profile" page of the frontend.

        When accessing this endpoint, the logged-in user's accessToken is used to
        authenticate and retrieve their specific posts from the backend.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/social-media/posts/get/my",
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
                    my_list_params.MyListParams,
                ),
            ),
            cast_to=MyListResponse,
        )


class AsyncMyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncMyResourceWithStreamingResponse(self)

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
    ) -> MyListResponse:
        """
        The API endpoint allows a logged-in user to fetch their own posts, which can be
        displayed on the "My Profile" page of the frontend.

        When accessing this endpoint, the logged-in user's accessToken is used to
        authenticate and retrieve their specific posts from the backend.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/social-media/posts/get/my",
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
                    my_list_params.MyListParams,
                ),
            ),
            cast_to=MyListResponse,
        )


class MyResourceWithRawResponse:
    def __init__(self, my: MyResource) -> None:
        self._my = my

        self.list = to_raw_response_wrapper(
            my.list,
        )


class AsyncMyResourceWithRawResponse:
    def __init__(self, my: AsyncMyResource) -> None:
        self._my = my

        self.list = async_to_raw_response_wrapper(
            my.list,
        )


class MyResourceWithStreamingResponse:
    def __init__(self, my: MyResource) -> None:
        self._my = my

        self.list = to_streamed_response_wrapper(
            my.list,
        )


class AsyncMyResourceWithStreamingResponse:
    def __init__(self, my: AsyncMyResource) -> None:
        self._my = my

        self.list = async_to_streamed_response_wrapper(
            my.list,
        )
