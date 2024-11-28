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
from ....types.public.cats.cat_random_response import CatRandomResponse

__all__ = ["CatResource", "AsyncCatResource"]


class CatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return CatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return CatResourceWithStreamingResponse(self)

    def random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatRandomResponse:
        """
        The API endpoint returns a randomly selected cat object from a list.

        When accessing this endpoint, you will receive a response containing a cat
        object randomly chosen from the available list.
        """
        return self._get(
            "/public/cats/cat/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatRandomResponse,
        )


class AsyncCatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncCatResourceWithStreamingResponse(self)

    async def random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatRandomResponse:
        """
        The API endpoint returns a randomly selected cat object from a list.

        When accessing this endpoint, you will receive a response containing a cat
        object randomly chosen from the available list.
        """
        return await self._get(
            "/public/cats/cat/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatRandomResponse,
        )


class CatResourceWithRawResponse:
    def __init__(self, cat: CatResource) -> None:
        self._cat = cat

        self.random = to_raw_response_wrapper(
            cat.random,
        )


class AsyncCatResourceWithRawResponse:
    def __init__(self, cat: AsyncCatResource) -> None:
        self._cat = cat

        self.random = async_to_raw_response_wrapper(
            cat.random,
        )


class CatResourceWithStreamingResponse:
    def __init__(self, cat: CatResource) -> None:
        self._cat = cat

        self.random = to_streamed_response_wrapper(
            cat.random,
        )


class AsyncCatResourceWithStreamingResponse:
    def __init__(self, cat: AsyncCatResource) -> None:
        self._cat = cat

        self.random = async_to_streamed_response_wrapper(
            cat.random,
        )
