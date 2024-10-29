# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.seed.social_media_create_response import SocialMediaCreateResponse

__all__ = ["SocialMediaResource", "AsyncSocialMediaResource"]


class SocialMediaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SocialMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return SocialMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SocialMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return SocialMediaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SocialMediaCreateResponse:
        """
        This API endpoint is responsible for populating all the essential entities
        required for a social media app service in the database.

        It provides a convenient way for developers to initialize the social media app
        with dummy or sample data for testing or development purposes.
        """
        return self._post(
            "/seed/social-media",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaCreateResponse,
        )


class AsyncSocialMediaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSocialMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSocialMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSocialMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncSocialMediaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SocialMediaCreateResponse:
        """
        This API endpoint is responsible for populating all the essential entities
        required for a social media app service in the database.

        It provides a convenient way for developers to initialize the social media app
        with dummy or sample data for testing or development purposes.
        """
        return await self._post(
            "/seed/social-media",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaCreateResponse,
        )


class SocialMediaResourceWithRawResponse:
    def __init__(self, social_media: SocialMediaResource) -> None:
        self._social_media = social_media

        self.create = to_raw_response_wrapper(
            social_media.create,
        )


class AsyncSocialMediaResourceWithRawResponse:
    def __init__(self, social_media: AsyncSocialMediaResource) -> None:
        self._social_media = social_media

        self.create = async_to_raw_response_wrapper(
            social_media.create,
        )


class SocialMediaResourceWithStreamingResponse:
    def __init__(self, social_media: SocialMediaResource) -> None:
        self._social_media = social_media

        self.create = to_streamed_response_wrapper(
            social_media.create,
        )


class AsyncSocialMediaResourceWithStreamingResponse:
    def __init__(self, social_media: AsyncSocialMediaResource) -> None:
        self._social_media = social_media

        self.create = async_to_streamed_response_wrapper(
            social_media.create,
        )
