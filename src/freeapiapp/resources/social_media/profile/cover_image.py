# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
from ....types.social_media.profile import cover_image_update_params
from ....types.social_media.profile.cover_image_update_response import CoverImageUpdateResponse

__all__ = ["CoverImageResource", "AsyncCoverImageResource"]


class CoverImageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CoverImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return CoverImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CoverImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return CoverImageResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        cover_image: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CoverImageUpdateResponse:
        """
        The API endpoint allows users to update their social media profile's cover
        image.

        By accessing this endpoint, users can submit a new cover image file, which will
        be applied as their updated profile cover on the social media platform.

        Args:
          cover_image: File

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"cover_image": cover_image})
        files = extract_files(cast(Mapping[str, object], body), paths=[["coverImage"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._patch(
            "/social-media/profile/cover-image",
            body=maybe_transform(body, cover_image_update_params.CoverImageUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CoverImageUpdateResponse,
        )


class AsyncCoverImageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCoverImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCoverImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCoverImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncCoverImageResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        cover_image: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CoverImageUpdateResponse:
        """
        The API endpoint allows users to update their social media profile's cover
        image.

        By accessing this endpoint, users can submit a new cover image file, which will
        be applied as their updated profile cover on the social media platform.

        Args:
          cover_image: File

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"cover_image": cover_image})
        files = extract_files(cast(Mapping[str, object], body), paths=[["coverImage"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._patch(
            "/social-media/profile/cover-image",
            body=await async_maybe_transform(body, cover_image_update_params.CoverImageUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CoverImageUpdateResponse,
        )


class CoverImageResourceWithRawResponse:
    def __init__(self, cover_image: CoverImageResource) -> None:
        self._cover_image = cover_image

        self.update = to_raw_response_wrapper(
            cover_image.update,
        )


class AsyncCoverImageResourceWithRawResponse:
    def __init__(self, cover_image: AsyncCoverImageResource) -> None:
        self._cover_image = cover_image

        self.update = async_to_raw_response_wrapper(
            cover_image.update,
        )


class CoverImageResourceWithStreamingResponse:
    def __init__(self, cover_image: CoverImageResource) -> None:
        self._cover_image = cover_image

        self.update = to_streamed_response_wrapper(
            cover_image.update,
        )


class AsyncCoverImageResourceWithStreamingResponse:
    def __init__(self, cover_image: AsyncCoverImageResource) -> None:
        self._cover_image = cover_image

        self.update = async_to_streamed_response_wrapper(
            cover_image.update,
        )
