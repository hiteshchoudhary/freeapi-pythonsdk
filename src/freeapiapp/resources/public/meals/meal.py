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
from ....types.public.meals.meal_random_response import MealRandomResponse

__all__ = ["MealResource", "AsyncMealResource"]


class MealResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MealResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return MealResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MealResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return MealResourceWithStreamingResponse(self)

    def random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MealRandomResponse:
        """
        The API endpoint returns a random meal object from a given list of meals.

        When accessing this endpoint, you will receive a response containing a randomly
        selected meal.
        """
        return self._get(
            "/public/meals/meal/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MealRandomResponse,
        )


class AsyncMealResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMealResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMealResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMealResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncMealResourceWithStreamingResponse(self)

    async def random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MealRandomResponse:
        """
        The API endpoint returns a random meal object from a given list of meals.

        When accessing this endpoint, you will receive a response containing a randomly
        selected meal.
        """
        return await self._get(
            "/public/meals/meal/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MealRandomResponse,
        )


class MealResourceWithRawResponse:
    def __init__(self, meal: MealResource) -> None:
        self._meal = meal

        self.random = to_raw_response_wrapper(
            meal.random,
        )


class AsyncMealResourceWithRawResponse:
    def __init__(self, meal: AsyncMealResource) -> None:
        self._meal = meal

        self.random = async_to_raw_response_wrapper(
            meal.random,
        )


class MealResourceWithStreamingResponse:
    def __init__(self, meal: MealResource) -> None:
        self._meal = meal

        self.random = to_streamed_response_wrapper(
            meal.random,
        )


class AsyncMealResourceWithStreamingResponse:
    def __init__(self, meal: AsyncMealResource) -> None:
        self._meal = meal

        self.random = async_to_streamed_response_wrapper(
            meal.random,
        )
