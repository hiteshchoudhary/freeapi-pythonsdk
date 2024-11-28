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
from ....types.public.youtube import playlist_list_params
from ....types.public.youtube.playlist_list_response import PlaylistListResponse
from ....types.public.youtube.playlist_retrieve_response import PlaylistRetrieveResponse

__all__ = ["PlaylistsResource", "AsyncPlaylistsResource"]


class PlaylistsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlaylistsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return PlaylistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlaylistsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return PlaylistsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        playlist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlaylistRetrieveResponse:
        """
        This API endpoint provides the details of a playlist, including playlist
        metadata and the videos included in the playlist, based on the specified
        playlist ID.

        When accessing this endpoint and providing a valid playlist ID as a parameter,
        you will receive a response containing comprehensive information about the
        playlist, such as its title, description, and other metadata.

        Additionally, the response will include a list of videos that are part of the
        playlist, enabling you to access the video details.

        **Disclaimer:**

        Data provided by the API is static and not real-time.

        This simplifies the process of developing a **YouTube clone**, allowing
        developers to solely focus on UI design and creativity, without worrying about
        complex API key configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not playlist_id:
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return self._get(
            f"/public/youtube/playlists/{playlist_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaylistRetrieveResponse,
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
    ) -> PlaylistListResponse:
        """
        This API endpoint allows users to retrieve playlists associated with the
        channel.

        By accessing this endpoint, users can obtain a collection of playlists that
        belong to the channel.

        This functionality is particularly useful for implementing a "Playlists" tab in
        the channel page UI design, where users can view the playlists conveniently.

        **Disclaimer:**

        Data provided by the API is static and not real-time.

        This simplifies the process of developing a **YouTube clone**, allowing
        developers to solely focus on UI design and creativity, without worrying about
        complex API key configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/youtube/playlists",
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
                    playlist_list_params.PlaylistListParams,
                ),
            ),
            cast_to=PlaylistListResponse,
        )


class AsyncPlaylistsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlaylistsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPlaylistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlaylistsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncPlaylistsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        playlist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlaylistRetrieveResponse:
        """
        This API endpoint provides the details of a playlist, including playlist
        metadata and the videos included in the playlist, based on the specified
        playlist ID.

        When accessing this endpoint and providing a valid playlist ID as a parameter,
        you will receive a response containing comprehensive information about the
        playlist, such as its title, description, and other metadata.

        Additionally, the response will include a list of videos that are part of the
        playlist, enabling you to access the video details.

        **Disclaimer:**

        Data provided by the API is static and not real-time.

        This simplifies the process of developing a **YouTube clone**, allowing
        developers to solely focus on UI design and creativity, without worrying about
        complex API key configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not playlist_id:
            raise ValueError(f"Expected a non-empty value for `playlist_id` but received {playlist_id!r}")
        return await self._get(
            f"/public/youtube/playlists/{playlist_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlaylistRetrieveResponse,
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
    ) -> PlaylistListResponse:
        """
        This API endpoint allows users to retrieve playlists associated with the
        channel.

        By accessing this endpoint, users can obtain a collection of playlists that
        belong to the channel.

        This functionality is particularly useful for implementing a "Playlists" tab in
        the channel page UI design, where users can view the playlists conveniently.

        **Disclaimer:**

        Data provided by the API is static and not real-time.

        This simplifies the process of developing a **YouTube clone**, allowing
        developers to solely focus on UI design and creativity, without worrying about
        complex API key configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/youtube/playlists",
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
                    playlist_list_params.PlaylistListParams,
                ),
            ),
            cast_to=PlaylistListResponse,
        )


class PlaylistsResourceWithRawResponse:
    def __init__(self, playlists: PlaylistsResource) -> None:
        self._playlists = playlists

        self.retrieve = to_raw_response_wrapper(
            playlists.retrieve,
        )
        self.list = to_raw_response_wrapper(
            playlists.list,
        )


class AsyncPlaylistsResourceWithRawResponse:
    def __init__(self, playlists: AsyncPlaylistsResource) -> None:
        self._playlists = playlists

        self.retrieve = async_to_raw_response_wrapper(
            playlists.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            playlists.list,
        )


class PlaylistsResourceWithStreamingResponse:
    def __init__(self, playlists: PlaylistsResource) -> None:
        self._playlists = playlists

        self.retrieve = to_streamed_response_wrapper(
            playlists.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            playlists.list,
        )


class AsyncPlaylistsResourceWithStreamingResponse:
    def __init__(self, playlists: AsyncPlaylistsResource) -> None:
        self._playlists = playlists

        self.retrieve = async_to_streamed_response_wrapper(
            playlists.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            playlists.list,
        )
