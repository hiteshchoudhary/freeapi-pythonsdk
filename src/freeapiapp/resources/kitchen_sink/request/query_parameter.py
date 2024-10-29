# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ....types.kitchen_sink.request import query_parameter_retrieve_params
from ....types.kitchen_sink.request.query_parameter_retrieve_response import QueryParameterRetrieveResponse

__all__ = ["QueryParameterResource", "AsyncQueryParameterResource"]


class QueryParameterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryParameterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return QueryParameterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryParameterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return QueryParameterResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        query1: str | NotGiven = NOT_GIVEN,
        query2: str | NotGiven = NOT_GIVEN,
        query3: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryParameterRetrieveResponse:
        """
        The API endpoint provides the capability to retrieve the query parameters being
        supplied in the URL.

        When accessing this endpoint, you can retrieve and access the values of the
        query parameters included in the URL.

        This functionality allows you to extract and utilize the information provided as
        query parameters for further processing or customization within your
        application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/kitchen-sink/request/query-parameter",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query1": query1,
                        "query2": query2,
                        "query3": query3,
                    },
                    query_parameter_retrieve_params.QueryParameterRetrieveParams,
                ),
            ),
            cast_to=QueryParameterRetrieveResponse,
        )


class AsyncQueryParameterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryParameterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryParameterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryParameterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncQueryParameterResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        query1: str | NotGiven = NOT_GIVEN,
        query2: str | NotGiven = NOT_GIVEN,
        query3: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryParameterRetrieveResponse:
        """
        The API endpoint provides the capability to retrieve the query parameters being
        supplied in the URL.

        When accessing this endpoint, you can retrieve and access the values of the
        query parameters included in the URL.

        This functionality allows you to extract and utilize the information provided as
        query parameters for further processing or customization within your
        application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/kitchen-sink/request/query-parameter",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query1": query1,
                        "query2": query2,
                        "query3": query3,
                    },
                    query_parameter_retrieve_params.QueryParameterRetrieveParams,
                ),
            ),
            cast_to=QueryParameterRetrieveResponse,
        )


class QueryParameterResourceWithRawResponse:
    def __init__(self, query_parameter: QueryParameterResource) -> None:
        self._query_parameter = query_parameter

        self.retrieve = to_raw_response_wrapper(
            query_parameter.retrieve,
        )


class AsyncQueryParameterResourceWithRawResponse:
    def __init__(self, query_parameter: AsyncQueryParameterResource) -> None:
        self._query_parameter = query_parameter

        self.retrieve = async_to_raw_response_wrapper(
            query_parameter.retrieve,
        )


class QueryParameterResourceWithStreamingResponse:
    def __init__(self, query_parameter: QueryParameterResource) -> None:
        self._query_parameter = query_parameter

        self.retrieve = to_streamed_response_wrapper(
            query_parameter.retrieve,
        )


class AsyncQueryParameterResourceWithStreamingResponse:
    def __init__(self, query_parameter: AsyncQueryParameterResource) -> None:
        self._query_parameter = query_parameter

        self.retrieve = async_to_streamed_response_wrapper(
            query_parameter.retrieve,
        )
