# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .joke import (
    JokeResource,
    AsyncJokeResource,
    JokeResourceWithRawResponse,
    AsyncJokeResourceWithRawResponse,
    JokeResourceWithStreamingResponse,
    AsyncJokeResourceWithStreamingResponse,
)
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
from ....types.public import random_joke_list_params
from ....types.public.random_joke_list_response import RandomJokeListResponse
from ....types.public.random_joke_retrieve_response import RandomJokeRetrieveResponse

__all__ = ["RandomJokesResource", "AsyncRandomJokesResource"]


class RandomJokesResource(SyncAPIResource):
    @cached_property
    def joke(self) -> JokeResource:
        return JokeResource(self._client)

    @cached_property
    def with_raw_response(self) -> RandomJokesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return RandomJokesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RandomJokesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return RandomJokesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        joke_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RandomJokeRetrieveResponse:
        """
        The API endpoint allows you to retrieve a joke based on the specified joke ID.

        When accessing this endpoint and providing a valid joke ID as a parameter, you
        will receive a response containing the joke associated with the provided ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not joke_id:
            raise ValueError(f"Expected a non-empty value for `joke_id` but received {joke_id!r}")
        return self._get(
            f"/public/randomjokes/{joke_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RandomJokeRetrieveResponse,
        )

    def list(
        self,
        *,
        inc: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RandomJokeListResponse:
        """The API endpoint retrieves a list of jokes.


        When accessing this endpoint, you will receive a response containing a
        collection of jokes.

        This functionality is useful for retrieving multiple jokes at once, enabling you
        to incorporate humor and amusement into your application or provide
        entertainment to users.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/randomjokes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "inc": inc,
                        "limit": limit,
                        "page": page,
                        "query": query,
                    },
                    random_joke_list_params.RandomJokeListParams,
                ),
            ),
            cast_to=RandomJokeListResponse,
        )


class AsyncRandomJokesResource(AsyncAPIResource):
    @cached_property
    def joke(self) -> AsyncJokeResource:
        return AsyncJokeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRandomJokesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRandomJokesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRandomJokesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncRandomJokesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        joke_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RandomJokeRetrieveResponse:
        """
        The API endpoint allows you to retrieve a joke based on the specified joke ID.

        When accessing this endpoint and providing a valid joke ID as a parameter, you
        will receive a response containing the joke associated with the provided ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not joke_id:
            raise ValueError(f"Expected a non-empty value for `joke_id` but received {joke_id!r}")
        return await self._get(
            f"/public/randomjokes/{joke_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RandomJokeRetrieveResponse,
        )

    async def list(
        self,
        *,
        inc: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RandomJokeListResponse:
        """The API endpoint retrieves a list of jokes.


        When accessing this endpoint, you will receive a response containing a
        collection of jokes.

        This functionality is useful for retrieving multiple jokes at once, enabling you
        to incorporate humor and amusement into your application or provide
        entertainment to users.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/randomjokes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "inc": inc,
                        "limit": limit,
                        "page": page,
                        "query": query,
                    },
                    random_joke_list_params.RandomJokeListParams,
                ),
            ),
            cast_to=RandomJokeListResponse,
        )


class RandomJokesResourceWithRawResponse:
    def __init__(self, random_jokes: RandomJokesResource) -> None:
        self._random_jokes = random_jokes

        self.retrieve = to_raw_response_wrapper(
            random_jokes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            random_jokes.list,
        )

    @cached_property
    def joke(self) -> JokeResourceWithRawResponse:
        return JokeResourceWithRawResponse(self._random_jokes.joke)


class AsyncRandomJokesResourceWithRawResponse:
    def __init__(self, random_jokes: AsyncRandomJokesResource) -> None:
        self._random_jokes = random_jokes

        self.retrieve = async_to_raw_response_wrapper(
            random_jokes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            random_jokes.list,
        )

    @cached_property
    def joke(self) -> AsyncJokeResourceWithRawResponse:
        return AsyncJokeResourceWithRawResponse(self._random_jokes.joke)


class RandomJokesResourceWithStreamingResponse:
    def __init__(self, random_jokes: RandomJokesResource) -> None:
        self._random_jokes = random_jokes

        self.retrieve = to_streamed_response_wrapper(
            random_jokes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            random_jokes.list,
        )

    @cached_property
    def joke(self) -> JokeResourceWithStreamingResponse:
        return JokeResourceWithStreamingResponse(self._random_jokes.joke)


class AsyncRandomJokesResourceWithStreamingResponse:
    def __init__(self, random_jokes: AsyncRandomJokesResource) -> None:
        self._random_jokes = random_jokes

        self.retrieve = async_to_streamed_response_wrapper(
            random_jokes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            random_jokes.list,
        )

    @cached_property
    def joke(self) -> AsyncJokeResourceWithStreamingResponse:
        return AsyncJokeResourceWithStreamingResponse(self._random_jokes.joke)
