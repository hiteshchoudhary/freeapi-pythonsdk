# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.public.dogs.dog_random_response import DogRandomResponse

__all__ = ["DogResource", "AsyncDogResource"]


class DogResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return DogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return DogResourceWithStreamingResponse(self)

    def random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DogRandomResponse:
        """
        The API endpoint returns a randomly selected dog object from a list.

        When accessing this endpoint, you will receive a response containing a dog
        object randomly chosen from the available list.
        """
        return self._get(
            "/public/dogs/dog/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DogRandomResponse,
        )


class AsyncDogResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncDogResourceWithStreamingResponse(self)

    async def random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DogRandomResponse:
        """
        The API endpoint returns a randomly selected dog object from a list.

        When accessing this endpoint, you will receive a response containing a dog
        object randomly chosen from the available list.
        """
        return await self._get(
            "/public/dogs/dog/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DogRandomResponse,
        )


class DogResourceWithRawResponse:
    def __init__(self, dog: DogResource) -> None:
        self._dog = dog

        self.random = to_raw_response_wrapper(
            dog.random,
        )


class AsyncDogResourceWithRawResponse:
    def __init__(self, dog: AsyncDogResource) -> None:
        self._dog = dog

        self.random = async_to_raw_response_wrapper(
            dog.random,
        )


class DogResourceWithStreamingResponse:
    def __init__(self, dog: DogResource) -> None:
        self._dog = dog

        self.random = to_streamed_response_wrapper(
            dog.random,
        )


class AsyncDogResourceWithStreamingResponse:
    def __init__(self, dog: AsyncDogResource) -> None:
        self._dog = dog

        self.random = async_to_streamed_response_wrapper(
            dog.random,
        )
