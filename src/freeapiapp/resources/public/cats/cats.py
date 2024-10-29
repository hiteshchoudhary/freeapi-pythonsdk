# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .cat import (
    CatResource,
    AsyncCatResource,
    CatResourceWithRawResponse,
    AsyncCatResourceWithRawResponse,
    CatResourceWithStreamingResponse,
    AsyncCatResourceWithStreamingResponse,
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
from ....types.public import cat_list_params
from ....types.public.cat_list_response import CatListResponse
from ....types.public.cat_retrieve_response import CatRetrieveResponse

__all__ = ["CatsResource", "AsyncCatsResource"]


class CatsResource(SyncAPIResource):
    @cached_property
    def cat(self) -> CatResource:
        return CatResource(self._client)

    @cached_property
    def with_raw_response(self) -> CatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return CatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return CatsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        cat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatRetrieveResponse:
        """
        The API endpoint retrieves a cat object based on the provided cat ID in the path
        variable.

        By accessing this endpoint with a valid cat ID, you will receive a response
        containing the details and information specific to the cat with the
        corresponding ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not cat_id:
            raise ValueError(f"Expected a non-empty value for `cat_id` but received {cat_id!r}")
        return self._get(
            f"/public/cats/{cat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatRetrieveResponse,
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
    ) -> CatListResponse:
        """
        The API endpoint retrieves a list of cat objects.

        When accessing this endpoint, you will receive a response containing a
        collection of cat objects.

        Each dog object represents a specific cat breed and includes relevant details
        such as name, characteristics, temperament, and images.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/cats",
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
                    cat_list_params.CatListParams,
                ),
            ),
            cast_to=CatListResponse,
        )


class AsyncCatsResource(AsyncAPIResource):
    @cached_property
    def cat(self) -> AsyncCatResource:
        return AsyncCatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncCatsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        cat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatRetrieveResponse:
        """
        The API endpoint retrieves a cat object based on the provided cat ID in the path
        variable.

        By accessing this endpoint with a valid cat ID, you will receive a response
        containing the details and information specific to the cat with the
        corresponding ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not cat_id:
            raise ValueError(f"Expected a non-empty value for `cat_id` but received {cat_id!r}")
        return await self._get(
            f"/public/cats/{cat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatRetrieveResponse,
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
    ) -> CatListResponse:
        """
        The API endpoint retrieves a list of cat objects.

        When accessing this endpoint, you will receive a response containing a
        collection of cat objects.

        Each dog object represents a specific cat breed and includes relevant details
        such as name, characteristics, temperament, and images.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/cats",
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
                    cat_list_params.CatListParams,
                ),
            ),
            cast_to=CatListResponse,
        )


class CatsResourceWithRawResponse:
    def __init__(self, cats: CatsResource) -> None:
        self._cats = cats

        self.retrieve = to_raw_response_wrapper(
            cats.retrieve,
        )
        self.list = to_raw_response_wrapper(
            cats.list,
        )

    @cached_property
    def cat(self) -> CatResourceWithRawResponse:
        return CatResourceWithRawResponse(self._cats.cat)


class AsyncCatsResourceWithRawResponse:
    def __init__(self, cats: AsyncCatsResource) -> None:
        self._cats = cats

        self.retrieve = async_to_raw_response_wrapper(
            cats.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            cats.list,
        )

    @cached_property
    def cat(self) -> AsyncCatResourceWithRawResponse:
        return AsyncCatResourceWithRawResponse(self._cats.cat)


class CatsResourceWithStreamingResponse:
    def __init__(self, cats: CatsResource) -> None:
        self._cats = cats

        self.retrieve = to_streamed_response_wrapper(
            cats.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            cats.list,
        )

    @cached_property
    def cat(self) -> CatResourceWithStreamingResponse:
        return CatResourceWithStreamingResponse(self._cats.cat)


class AsyncCatsResourceWithStreamingResponse:
    def __init__(self, cats: AsyncCatsResource) -> None:
        self._cats = cats

        self.retrieve = async_to_streamed_response_wrapper(
            cats.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            cats.list,
        )

    @cached_property
    def cat(self) -> AsyncCatResourceWithStreamingResponse:
        return AsyncCatResourceWithStreamingResponse(self._cats.cat)
