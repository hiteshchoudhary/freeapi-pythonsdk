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
from ...types.public import stock_list_params
from ...types.public.stock_list_response import StockListResponse
from ...types.public.stock_random_response import StockRandomResponse
from ...types.public.stock_retrieve_response import StockRetrieveResponse

__all__ = ["StocksResource", "AsyncStocksResource"]


class StocksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return StocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return StocksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        stock_symbol: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StockRetrieveResponse:
        """
        The API endpoint retrieves a stock based on the Symbol as ID provided as a path
        variable.

        By accessing this endpoint and specifying a valid stock symbol, you will receive
        a response containing the details of the corresponding stock.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_symbol:
            raise ValueError(f"Expected a non-empty value for `stock_symbol` but received {stock_symbol!r}")
        return self._get(
            f"/public/stocks/{stock_symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StockRetrieveResponse,
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
    ) -> StockListResponse:
        """
        The API endpoint allows you to retrieve a list of stocks listed on NSE [National
        Stock Exchange of India]. The data you get is a snapshot taken on 28th Dec 2023
        & not live from stock exchange. Upon accessing this endpoint, you will receive a
        response containing a collection of randomly selected stocks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/stocks",
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
                    stock_list_params.StockListParams,
                ),
            ),
            cast_to=StockListResponse,
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
    ) -> StockRandomResponse:
        """
        The API endpoint returns a single random stock from a list of stocks.

        Upon accessing this endpoint, you will receive a response containing the details
        of a randomly selected stock.
        """
        return self._get(
            "/public/stocks/stock/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StockRandomResponse,
        )


class AsyncStocksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncStocksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        stock_symbol: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StockRetrieveResponse:
        """
        The API endpoint retrieves a stock based on the Symbol as ID provided as a path
        variable.

        By accessing this endpoint and specifying a valid stock symbol, you will receive
        a response containing the details of the corresponding stock.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_symbol:
            raise ValueError(f"Expected a non-empty value for `stock_symbol` but received {stock_symbol!r}")
        return await self._get(
            f"/public/stocks/{stock_symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StockRetrieveResponse,
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
    ) -> StockListResponse:
        """
        The API endpoint allows you to retrieve a list of stocks listed on NSE [National
        Stock Exchange of India]. The data you get is a snapshot taken on 28th Dec 2023
        & not live from stock exchange. Upon accessing this endpoint, you will receive a
        response containing a collection of randomly selected stocks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/stocks",
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
                    stock_list_params.StockListParams,
                ),
            ),
            cast_to=StockListResponse,
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
    ) -> StockRandomResponse:
        """
        The API endpoint returns a single random stock from a list of stocks.

        Upon accessing this endpoint, you will receive a response containing the details
        of a randomly selected stock.
        """
        return await self._get(
            "/public/stocks/stock/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StockRandomResponse,
        )


class StocksResourceWithRawResponse:
    def __init__(self, stocks: StocksResource) -> None:
        self._stocks = stocks

        self.retrieve = to_raw_response_wrapper(
            stocks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            stocks.list,
        )
        self.random = to_raw_response_wrapper(
            stocks.random,
        )


class AsyncStocksResourceWithRawResponse:
    def __init__(self, stocks: AsyncStocksResource) -> None:
        self._stocks = stocks

        self.retrieve = async_to_raw_response_wrapper(
            stocks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            stocks.list,
        )
        self.random = async_to_raw_response_wrapper(
            stocks.random,
        )


class StocksResourceWithStreamingResponse:
    def __init__(self, stocks: StocksResource) -> None:
        self._stocks = stocks

        self.retrieve = to_streamed_response_wrapper(
            stocks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            stocks.list,
        )
        self.random = to_streamed_response_wrapper(
            stocks.random,
        )


class AsyncStocksResourceWithStreamingResponse:
    def __init__(self, stocks: AsyncStocksResource) -> None:
        self._stocks = stocks

        self.retrieve = async_to_streamed_response_wrapper(
            stocks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            stocks.list,
        )
        self.random = async_to_streamed_response_wrapper(
            stocks.random,
        )
