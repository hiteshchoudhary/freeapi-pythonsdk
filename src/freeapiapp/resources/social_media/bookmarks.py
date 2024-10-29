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
from ...types.social_media import bookmark_retrieve_params
from ...types.social_media.bookmark_create_response import BookmarkCreateResponse
from ...types.social_media.bookmark_retrieve_response import BookmarkRetrieveResponse

__all__ = ["BookmarksResource", "AsyncBookmarksResource"]


class BookmarksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BookmarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return BookmarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BookmarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return BookmarksResourceWithStreamingResponse(self)

    def create(
        self,
        post_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookmarkCreateResponse:
        """
        The API endpoint allows users to add or remove posts from their bookmarks.

        By accessing this endpoint, users can add a post to their bookmarks or remove a
        post from their bookmarks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._post(
            f"/social-media/bookmarks/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkCreateResponse,
        )

    def retrieve(
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
    ) -> BookmarkRetrieveResponse:
        """
        The API endpoint allows you to retrieve the bookmarked posts of the currently
        logged-in user.

        Upon accessing this endpoint, you will receive a response containing the posts
        that the user has bookmarked or saved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/social-media/bookmarks",
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
                    bookmark_retrieve_params.BookmarkRetrieveParams,
                ),
            ),
            cast_to=BookmarkRetrieveResponse,
        )


class AsyncBookmarksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBookmarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBookmarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBookmarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncBookmarksResourceWithStreamingResponse(self)

    async def create(
        self,
        post_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookmarkCreateResponse:
        """
        The API endpoint allows users to add or remove posts from their bookmarks.

        By accessing this endpoint, users can add a post to their bookmarks or remove a
        post from their bookmarks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._post(
            f"/social-media/bookmarks/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkCreateResponse,
        )

    async def retrieve(
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
    ) -> BookmarkRetrieveResponse:
        """
        The API endpoint allows you to retrieve the bookmarked posts of the currently
        logged-in user.

        Upon accessing this endpoint, you will receive a response containing the posts
        that the user has bookmarked or saved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/social-media/bookmarks",
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
                    bookmark_retrieve_params.BookmarkRetrieveParams,
                ),
            ),
            cast_to=BookmarkRetrieveResponse,
        )


class BookmarksResourceWithRawResponse:
    def __init__(self, bookmarks: BookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.create = to_raw_response_wrapper(
            bookmarks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bookmarks.retrieve,
        )


class AsyncBookmarksResourceWithRawResponse:
    def __init__(self, bookmarks: AsyncBookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.create = async_to_raw_response_wrapper(
            bookmarks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bookmarks.retrieve,
        )


class BookmarksResourceWithStreamingResponse:
    def __init__(self, bookmarks: BookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.create = to_streamed_response_wrapper(
            bookmarks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bookmarks.retrieve,
        )


class AsyncBookmarksResourceWithStreamingResponse:
    def __init__(self, bookmarks: AsyncBookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.create = async_to_streamed_response_wrapper(
            bookmarks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bookmarks.retrieve,
        )
