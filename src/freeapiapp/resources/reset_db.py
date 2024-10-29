# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.reset_db_delete_response import ResetDBDeleteResponse

__all__ = ["ResetDBResource", "AsyncResetDBResource"]


class ResetDBResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResetDBResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return ResetDBResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResetDBResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return ResetDBResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResetDBDeleteResponse:
        """
        ⚠️ DANGER ⚠️

        This API endpoint is a potentially destructive operation designed to allow users
        to drop or delete an entire database associated with their account or
        application.

        _**It should be used with caution as it permanently deletes all data stored in
        the specified database.**_
        """
        return self._delete(
            "/reset-db",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResetDBDeleteResponse,
        )


class AsyncResetDBResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResetDBResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResetDBResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResetDBResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncResetDBResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResetDBDeleteResponse:
        """
        ⚠️ DANGER ⚠️

        This API endpoint is a potentially destructive operation designed to allow users
        to drop or delete an entire database associated with their account or
        application.

        _**It should be used with caution as it permanently deletes all data stored in
        the specified database.**_
        """
        return await self._delete(
            "/reset-db",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResetDBDeleteResponse,
        )


class ResetDBResourceWithRawResponse:
    def __init__(self, reset_db: ResetDBResource) -> None:
        self._reset_db = reset_db

        self.delete = to_raw_response_wrapper(
            reset_db.delete,
        )


class AsyncResetDBResourceWithRawResponse:
    def __init__(self, reset_db: AsyncResetDBResource) -> None:
        self._reset_db = reset_db

        self.delete = async_to_raw_response_wrapper(
            reset_db.delete,
        )


class ResetDBResourceWithStreamingResponse:
    def __init__(self, reset_db: ResetDBResource) -> None:
        self._reset_db = reset_db

        self.delete = to_streamed_response_wrapper(
            reset_db.delete,
        )


class AsyncResetDBResourceWithStreamingResponse:
    def __init__(self, reset_db: AsyncResetDBResource) -> None:
        self._reset_db = reset_db

        self.delete = async_to_streamed_response_wrapper(
            reset_db.delete,
        )
