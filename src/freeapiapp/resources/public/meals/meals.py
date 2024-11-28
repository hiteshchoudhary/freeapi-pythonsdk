# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .meal import (
    MealResource,
    AsyncMealResource,
    MealResourceWithRawResponse,
    AsyncMealResourceWithRawResponse,
    MealResourceWithStreamingResponse,
    AsyncMealResourceWithStreamingResponse,
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
from ....types.public import meal_list_params
from ....types.public.meal_list_response import MealListResponse
from ....types.public.meal_retrieve_response import MealRetrieveResponse

__all__ = ["MealsResource", "AsyncMealsResource"]


class MealsResource(SyncAPIResource):
    @cached_property
    def meal(self) -> MealResource:
        return MealResource(self._client)

    @cached_property
    def with_raw_response(self) -> MealsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return MealsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MealsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return MealsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        meal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MealRetrieveResponse:
        """
        The API endpoint retrieves a meal based on the provided meal ID in the path
        variable.

        When accessing this endpoint and specifying a valid meal ID, you will receive a
        response containing the details and information about the specific meal.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not meal_id:
            raise ValueError(f"Expected a non-empty value for `meal_id` but received {meal_id!r}")
        return self._get(
            f"/public/meals/{meal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MealRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MealListResponse:
        """
        The API endpoint enables you to retrieve a list of meals.

        Upon accessing this endpoint, you will receive a response containing a
        collection of meals.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/meals",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "query": query,
                    },
                    meal_list_params.MealListParams,
                ),
            ),
            cast_to=MealListResponse,
        )


class AsyncMealsResource(AsyncAPIResource):
    @cached_property
    def meal(self) -> AsyncMealResource:
        return AsyncMealResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMealsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMealsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMealsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncMealsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        meal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MealRetrieveResponse:
        """
        The API endpoint retrieves a meal based on the provided meal ID in the path
        variable.

        When accessing this endpoint and specifying a valid meal ID, you will receive a
        response containing the details and information about the specific meal.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not meal_id:
            raise ValueError(f"Expected a non-empty value for `meal_id` but received {meal_id!r}")
        return await self._get(
            f"/public/meals/{meal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MealRetrieveResponse,
        )

    async def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MealListResponse:
        """
        The API endpoint enables you to retrieve a list of meals.

        Upon accessing this endpoint, you will receive a response containing a
        collection of meals.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/meals",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "query": query,
                    },
                    meal_list_params.MealListParams,
                ),
            ),
            cast_to=MealListResponse,
        )


class MealsResourceWithRawResponse:
    def __init__(self, meals: MealsResource) -> None:
        self._meals = meals

        self.retrieve = to_raw_response_wrapper(
            meals.retrieve,
        )
        self.list = to_raw_response_wrapper(
            meals.list,
        )

    @cached_property
    def meal(self) -> MealResourceWithRawResponse:
        return MealResourceWithRawResponse(self._meals.meal)


class AsyncMealsResourceWithRawResponse:
    def __init__(self, meals: AsyncMealsResource) -> None:
        self._meals = meals

        self.retrieve = async_to_raw_response_wrapper(
            meals.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            meals.list,
        )

    @cached_property
    def meal(self) -> AsyncMealResourceWithRawResponse:
        return AsyncMealResourceWithRawResponse(self._meals.meal)


class MealsResourceWithStreamingResponse:
    def __init__(self, meals: MealsResource) -> None:
        self._meals = meals

        self.retrieve = to_streamed_response_wrapper(
            meals.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            meals.list,
        )

    @cached_property
    def meal(self) -> MealResourceWithStreamingResponse:
        return MealResourceWithStreamingResponse(self._meals.meal)


class AsyncMealsResourceWithStreamingResponse:
    def __init__(self, meals: AsyncMealsResource) -> None:
        self._meals = meals

        self.retrieve = async_to_streamed_response_wrapper(
            meals.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            meals.list,
        )

    @cached_property
    def meal(self) -> AsyncMealResourceWithStreamingResponse:
        return AsyncMealResourceWithStreamingResponse(self._meals.meal)
