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
from ....types.kitchen_sink.request.user_agent_retrieve_response import UserAgentRetrieveResponse

__all__ = ["UserAgentResource", "AsyncUserAgentResource"]


class UserAgentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return UserAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return UserAgentResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAgentRetrieveResponse:
        """
        This API endpoint is designed to provide information about the user agent string
        associated with the client making the request.

        It allows users to retrieve details about the user agent, which typically
        includes the name and version of the client's software or web browser.
        """
        return self._get(
            "/kitchen-sink/request/user-agent",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAgentRetrieveResponse,
        )


class AsyncUserAgentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncUserAgentResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAgentRetrieveResponse:
        """
        This API endpoint is designed to provide information about the user agent string
        associated with the client making the request.

        It allows users to retrieve details about the user agent, which typically
        includes the name and version of the client's software or web browser.
        """
        return await self._get(
            "/kitchen-sink/request/user-agent",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAgentRetrieveResponse,
        )


class UserAgentResourceWithRawResponse:
    def __init__(self, user_agent: UserAgentResource) -> None:
        self._user_agent = user_agent

        self.retrieve = to_raw_response_wrapper(
            user_agent.retrieve,
        )


class AsyncUserAgentResourceWithRawResponse:
    def __init__(self, user_agent: AsyncUserAgentResource) -> None:
        self._user_agent = user_agent

        self.retrieve = async_to_raw_response_wrapper(
            user_agent.retrieve,
        )


class UserAgentResourceWithStreamingResponse:
    def __init__(self, user_agent: UserAgentResource) -> None:
        self._user_agent = user_agent

        self.retrieve = to_streamed_response_wrapper(
            user_agent.retrieve,
        )


class AsyncUserAgentResourceWithStreamingResponse:
    def __init__(self, user_agent: AsyncUserAgentResource) -> None:
        self._user_agent = user_agent

        self.retrieve = async_to_streamed_response_wrapper(
            user_agent.retrieve,
        )
