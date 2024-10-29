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
from ....types.social_media.posts import tag_list_params
from ....types.social_media.posts.tag_list_response import TagListResponse

__all__ = ["TagResource", "AsyncTagResource"]


class TagResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return TagResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return TagResourceWithStreamingResponse(self)

    def list(
        self,
        tag: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TagListResponse:
        """
        The API endpoint allows users to retrieve posts by passing a tag name as a path
        variable.

        When accessing this endpoint and providing a valid tag name as part of the URL,
        the API will return a response containing posts that are associated with the
        specified tag.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag:
            raise ValueError(f"Expected a non-empty value for `tag` but received {tag!r}")
        return self._get(
            f"/social-media/posts/get/t/{tag}",
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
                    tag_list_params.TagListParams,
                ),
            ),
            cast_to=TagListResponse,
        )


class AsyncTagResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncTagResourceWithStreamingResponse(self)

    async def list(
        self,
        tag: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TagListResponse:
        """
        The API endpoint allows users to retrieve posts by passing a tag name as a path
        variable.

        When accessing this endpoint and providing a valid tag name as part of the URL,
        the API will return a response containing posts that are associated with the
        specified tag.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tag:
            raise ValueError(f"Expected a non-empty value for `tag` but received {tag!r}")
        return await self._get(
            f"/social-media/posts/get/t/{tag}",
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
                    tag_list_params.TagListParams,
                ),
            ),
            cast_to=TagListResponse,
        )


class TagResourceWithRawResponse:
    def __init__(self, tag: TagResource) -> None:
        self._tag = tag

        self.list = to_raw_response_wrapper(
            tag.list,
        )


class AsyncTagResourceWithRawResponse:
    def __init__(self, tag: AsyncTagResource) -> None:
        self._tag = tag

        self.list = async_to_raw_response_wrapper(
            tag.list,
        )


class TagResourceWithStreamingResponse:
    def __init__(self, tag: TagResource) -> None:
        self._tag = tag

        self.list = to_streamed_response_wrapper(
            tag.list,
        )


class AsyncTagResourceWithStreamingResponse:
    def __init__(self, tag: AsyncTagResource) -> None:
        self._tag = tag

        self.list = async_to_streamed_response_wrapper(
            tag.list,
        )
