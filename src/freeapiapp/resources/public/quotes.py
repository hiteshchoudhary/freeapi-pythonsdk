# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.public import quote_list_params
from ...types.public.quote_list_response import QuoteListResponse
from ...types.public.quote_random_response import QuoteRandomResponse
from ...types.public.quote_retrieve_response import QuoteRetrieveResponse

__all__ = ["QuotesResource", "AsyncQuotesResource"]


class QuotesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return QuotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return QuotesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        quote_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuoteRetrieveResponse:
        """
        The API endpoint enables you to retrieve a specific quote based on the quote ID
        provided in the path variable.

        When accessing this endpoint and providing a valid quote ID, you will receive a
        response containing the quote corresponding to that ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        return self._get(
            f"/public/quotes/{quote_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuoteRetrieveResponse,
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
    ) -> QuoteListResponse:
        """
        The API endpoint allows you to retrieve a list of quotes.

        When accessing this endpoint, you will receive a response containing a
        collection of quotes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/quotes",
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
                    quote_list_params.QuoteListParams,
                ),
            ),
            cast_to=QuoteListResponse,
        )

    def random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuoteRandomResponse:
        """
        The API endpoint returns a random quote from a list of quotes.

        When accessing this endpoint, you will receive a response containing a randomly
        selected quote.
        """
        return self._get(
            "/public/quotes/quote/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuoteRandomResponse,
        )


class AsyncQuotesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncQuotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncQuotesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        quote_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuoteRetrieveResponse:
        """
        The API endpoint enables you to retrieve a specific quote based on the quote ID
        provided in the path variable.

        When accessing this endpoint and providing a valid quote ID, you will receive a
        response containing the quote corresponding to that ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        return await self._get(
            f"/public/quotes/{quote_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuoteRetrieveResponse,
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
    ) -> QuoteListResponse:
        """
        The API endpoint allows you to retrieve a list of quotes.

        When accessing this endpoint, you will receive a response containing a
        collection of quotes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/quotes",
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
                    quote_list_params.QuoteListParams,
                ),
            ),
            cast_to=QuoteListResponse,
        )

    async def random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuoteRandomResponse:
        """
        The API endpoint returns a random quote from a list of quotes.

        When accessing this endpoint, you will receive a response containing a randomly
        selected quote.
        """
        return await self._get(
            "/public/quotes/quote/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuoteRandomResponse,
        )


class QuotesResourceWithRawResponse:
    def __init__(self, quotes: QuotesResource) -> None:
        self._quotes = quotes

        self.retrieve = to_raw_response_wrapper(
            quotes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            quotes.list,
        )
        self.random = to_raw_response_wrapper(
            quotes.random,
        )


class AsyncQuotesResourceWithRawResponse:
    def __init__(self, quotes: AsyncQuotesResource) -> None:
        self._quotes = quotes

        self.retrieve = async_to_raw_response_wrapper(
            quotes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            quotes.list,
        )
        self.random = async_to_raw_response_wrapper(
            quotes.random,
        )


class QuotesResourceWithStreamingResponse:
    def __init__(self, quotes: QuotesResource) -> None:
        self._quotes = quotes

        self.retrieve = to_streamed_response_wrapper(
            quotes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            quotes.list,
        )
        self.random = to_streamed_response_wrapper(
            quotes.random,
        )


class AsyncQuotesResourceWithStreamingResponse:
    def __init__(self, quotes: AsyncQuotesResource) -> None:
        self._quotes = quotes

        self.retrieve = async_to_streamed_response_wrapper(
            quotes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            quotes.list,
        )
        self.random = async_to_streamed_response_wrapper(
            quotes.random,
        )
