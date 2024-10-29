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
from ....types.public.random_jokes.joke_random_response import JokeRandomResponse

__all__ = ["JokeResource", "AsyncJokeResource"]


class JokeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JokeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return JokeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JokeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return JokeResourceWithStreamingResponse(self)

    def random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JokeRandomResponse:
        """
        The API endpoint returns a random joke from a list of jokes.

        When accessing this endpoint, you will receive a response containing a randomly
        selected joke.
        """
        return self._get(
            "/public/randomjokes/joke/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JokeRandomResponse,
        )


class AsyncJokeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJokeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncJokeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJokeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncJokeResourceWithStreamingResponse(self)

    async def random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JokeRandomResponse:
        """
        The API endpoint returns a random joke from a list of jokes.

        When accessing this endpoint, you will receive a response containing a randomly
        selected joke.
        """
        return await self._get(
            "/public/randomjokes/joke/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JokeRandomResponse,
        )


class JokeResourceWithRawResponse:
    def __init__(self, joke: JokeResource) -> None:
        self._joke = joke

        self.random = to_raw_response_wrapper(
            joke.random,
        )


class AsyncJokeResourceWithRawResponse:
    def __init__(self, joke: AsyncJokeResource) -> None:
        self._joke = joke

        self.random = async_to_raw_response_wrapper(
            joke.random,
        )


class JokeResourceWithStreamingResponse:
    def __init__(self, joke: JokeResource) -> None:
        self._joke = joke

        self.random = to_streamed_response_wrapper(
            joke.random,
        )


class AsyncJokeResourceWithStreamingResponse:
    def __init__(self, joke: AsyncJokeResource) -> None:
        self._joke = joke

        self.random = async_to_streamed_response_wrapper(
            joke.random,
        )
