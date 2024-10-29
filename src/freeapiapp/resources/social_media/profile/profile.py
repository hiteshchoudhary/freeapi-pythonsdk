# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .cover_image import (
    CoverImageResource,
    AsyncCoverImageResource,
    CoverImageResourceWithRawResponse,
    AsyncCoverImageResourceWithRawResponse,
    CoverImageResourceWithStreamingResponse,
    AsyncCoverImageResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.social_media import profile_update_params
from ....types.social_media.profile_update_response import ProfileUpdateResponse
from ....types.social_media.profile_retrieve_response import ProfileRetrieveResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    @cached_property
    def cover_image(self) -> CoverImageResource:
        return CoverImageResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def retrieve(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileRetrieveResponse:
        """
        The API endpoint allows users to fetch another user's social media profile based
        on the username provided as a path variable.

        By accessing this endpoint and providing the username as a parameter, you will
        receive a response containing the social media profile information of the
        specified user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/social-media/profile/u/{username}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    def update(
        self,
        *,
        bio: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        dob: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileUpdateResponse:
        """
        The API endpoint allows users to update their social media profiles.

        By accessing this endpoint, users can make changes to their profile information
        such as name, bio, contact details, dob, basic details or any other relevant
        fields.

        _**NOTE:**_ _To update avatar or cover image we have separate endpoints._

        _**Update avatar:**_ _Apps > Authentication > Update avatar_

        _**Update cover image:**_ _Apps > Social Media > Update cover image_

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/social-media/profile",
            body=maybe_transform(
                {
                    "bio": bio,
                    "country_code": country_code,
                    "dob": dob,
                    "first_name": first_name,
                    "last_name": last_name,
                    "location": location,
                    "phone_number": phone_number,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )


class AsyncProfileResource(AsyncAPIResource):
    @cached_property
    def cover_image(self) -> AsyncCoverImageResource:
        return AsyncCoverImageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileRetrieveResponse:
        """
        The API endpoint allows users to fetch another user's social media profile based
        on the username provided as a path variable.

        By accessing this endpoint and providing the username as a parameter, you will
        receive a response containing the social media profile information of the
        specified user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/social-media/profile/u/{username}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    async def update(
        self,
        *,
        bio: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        dob: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileUpdateResponse:
        """
        The API endpoint allows users to update their social media profiles.

        By accessing this endpoint, users can make changes to their profile information
        such as name, bio, contact details, dob, basic details or any other relevant
        fields.

        _**NOTE:**_ _To update avatar or cover image we have separate endpoints._

        _**Update avatar:**_ _Apps > Authentication > Update avatar_

        _**Update cover image:**_ _Apps > Social Media > Update cover image_

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/social-media/profile",
            body=await async_maybe_transform(
                {
                    "bio": bio,
                    "country_code": country_code,
                    "dob": dob,
                    "first_name": first_name,
                    "last_name": last_name,
                    "location": location,
                    "phone_number": phone_number,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_raw_response_wrapper(
            profile.retrieve,
        )
        self.update = to_raw_response_wrapper(
            profile.update,
        )

    @cached_property
    def cover_image(self) -> CoverImageResourceWithRawResponse:
        return CoverImageResourceWithRawResponse(self._profile.cover_image)


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_raw_response_wrapper(
            profile.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            profile.update,
        )

    @cached_property
    def cover_image(self) -> AsyncCoverImageResourceWithRawResponse:
        return AsyncCoverImageResourceWithRawResponse(self._profile.cover_image)


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            profile.update,
        )

    @cached_property
    def cover_image(self) -> CoverImageResourceWithStreamingResponse:
        return CoverImageResourceWithStreamingResponse(self._profile.cover_image)


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            profile.update,
        )

    @cached_property
    def cover_image(self) -> AsyncCoverImageResourceWithStreamingResponse:
        return AsyncCoverImageResourceWithStreamingResponse(self._profile.cover_image)
