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
from ....types.public.youtube import related_list_params
from ....types.public.youtube.related_list_response import RelatedListResponse

__all__ = ["RelatedResource", "AsyncRelatedResource"]


class RelatedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelatedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return RelatedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelatedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return RelatedResourceWithStreamingResponse(self)

    def list(
        self,
        video_id: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelatedListResponse:
        """
        The API endpoint returns a list of recommended YouTube videos based on the
        `videoId` provided in the path variable.

        When accessing this endpoint and passing a valid video ID, you will receive a
        response containing a list of videos that are related to the current video.

        These recommended videos can be displayed in a list view on the right side of
        the user interface, providing users with relevant and engaging content that
        complements the video they are currently viewing.

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
            f"/public/youtube/related/{video_id}",
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
                    related_list_params.RelatedListParams,
                ),
            ),
            cast_to=RelatedListResponse,
        )


class AsyncRelatedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelatedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRelatedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelatedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncRelatedResourceWithStreamingResponse(self)

    async def list(
        self,
        video_id: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelatedListResponse:
        """
        The API endpoint returns a list of recommended YouTube videos based on the
        `videoId` provided in the path variable.

        When accessing this endpoint and passing a valid video ID, you will receive a
        response containing a list of videos that are related to the current video.

        These recommended videos can be displayed in a list view on the right side of
        the user interface, providing users with relevant and engaging content that
        complements the video they are currently viewing.

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
            f"/public/youtube/related/{video_id}",
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
                    related_list_params.RelatedListParams,
                ),
            ),
            cast_to=RelatedListResponse,
        )


class RelatedResourceWithRawResponse:
    def __init__(self, related: RelatedResource) -> None:
        self._related = related

        self.list = to_raw_response_wrapper(
            related.list,
        )


class AsyncRelatedResourceWithRawResponse:
    def __init__(self, related: AsyncRelatedResource) -> None:
        self._related = related

        self.list = async_to_raw_response_wrapper(
            related.list,
        )


class RelatedResourceWithStreamingResponse:
    def __init__(self, related: RelatedResource) -> None:
        self._related = related

        self.list = to_streamed_response_wrapper(
            related.list,
        )


class AsyncRelatedResourceWithStreamingResponse:
    def __init__(self, related: AsyncRelatedResource) -> None:
        self._related = related

        self.list = async_to_streamed_response_wrapper(
            related.list,
        )
