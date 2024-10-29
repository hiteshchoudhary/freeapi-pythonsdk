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
from ....types.public.youtube import video_list_params
from ....types.public.youtube.video_list_response import VideoListResponse
from ....types.public.youtube.video_retrieve_response import VideoRetrieveResponse

__all__ = ["VideosResource", "AsyncVideosResource"]


class VideosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return VideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return VideosResourceWithStreamingResponse(self)

    def retrieve(
        self,
        video_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VideoRetrieveResponse:
        """
        This API endpoint allows you to retrieve a YouTube video's complete details by
        passing the `videoId` as a path variable.

        When accessing this endpoint with a valid video ID, you will receive a response
        containing comprehensive information about the specified video.

        This includes video statistics such as the number of likes, dislikes, views, and
        the video's duration, as well as other relevant details like the video title,
        description, channel name, and publication date.

        This functionality enables you to access and display detailed information about
        specific YouTube videos within your application.

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
        if not video_id:
            raise ValueError(f"Expected a non-empty value for `video_id` but received {video_id!r}")
        return self._get(
            f"/public/youtube/videos/{video_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        sort_by: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VideoListResponse:
        """
        This API endpoint enables you to retrieve all YouTube videos from a JSON file
        with a structure similar to YouTube's public API.

        Upon accessing this endpoint, you will receive a response containing a list of
        YouTube videos, just like you would from YouTube's official API.

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
        return self._get(
            "/public/youtube/videos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "query": query,
                        "sort_by": sort_by,
                    },
                    video_list_params.VideoListParams,
                ),
            ),
            cast_to=VideoListResponse,
        )


class AsyncVideosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncVideosResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        video_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VideoRetrieveResponse:
        """
        This API endpoint allows you to retrieve a YouTube video's complete details by
        passing the `videoId` as a path variable.

        When accessing this endpoint with a valid video ID, you will receive a response
        containing comprehensive information about the specified video.

        This includes video statistics such as the number of likes, dislikes, views, and
        the video's duration, as well as other relevant details like the video title,
        description, channel name, and publication date.

        This functionality enables you to access and display detailed information about
        specific YouTube videos within your application.

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
        if not video_id:
            raise ValueError(f"Expected a non-empty value for `video_id` but received {video_id!r}")
        return await self._get(
            f"/public/youtube/videos/{video_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoRetrieveResponse,
        )

    async def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        sort_by: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VideoListResponse:
        """
        This API endpoint enables you to retrieve all YouTube videos from a JSON file
        with a structure similar to YouTube's public API.

        Upon accessing this endpoint, you will receive a response containing a list of
        YouTube videos, just like you would from YouTube's official API.

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
        return await self._get(
            "/public/youtube/videos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "query": query,
                        "sort_by": sort_by,
                    },
                    video_list_params.VideoListParams,
                ),
            ),
            cast_to=VideoListResponse,
        )


class VideosResourceWithRawResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

        self.retrieve = to_raw_response_wrapper(
            videos.retrieve,
        )
        self.list = to_raw_response_wrapper(
            videos.list,
        )


class AsyncVideosResourceWithRawResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

        self.retrieve = async_to_raw_response_wrapper(
            videos.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            videos.list,
        )


class VideosResourceWithStreamingResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

        self.retrieve = to_streamed_response_wrapper(
            videos.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            videos.list,
        )


class AsyncVideosResourceWithStreamingResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

        self.retrieve = async_to_streamed_response_wrapper(
            videos.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            videos.list,
        )
