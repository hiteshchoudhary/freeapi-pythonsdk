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
from ...types.public import book_list_params
from ...types.public.book_list_response import BookListResponse
from ...types.public.book_random_response import BookRandomResponse
from ...types.public.book_retrieve_response import BookRetrieveResponse

__all__ = ["BooksResource", "AsyncBooksResource"]


class BooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return BooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return BooksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        book_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookRetrieveResponse:
        """
        The API endpoint retrieves a book based on the book ID provided as a path
        variable.

        By accessing this endpoint and specifying a valid book ID, you will receive a
        response containing the details of the corresponding book.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not book_id:
            raise ValueError(f"Expected a non-empty value for `book_id` but received {book_id!r}")
        return self._get(
            f"/public/books/{book_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookRetrieveResponse,
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
    ) -> BookListResponse:
        """
        The API endpoint allows you to retrieve a list of random books.

        Upon accessing this endpoint, you will receive a response containing a
        collection of randomly selected books.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/books",
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
                    book_list_params.BookListParams,
                ),
            ),
            cast_to=BookListResponse,
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
    ) -> BookRandomResponse:
        """
        The API endpoint returns a single random book from a list of books.

        Upon accessing this endpoint, you will receive a response containing the details
        of a randomly selected book.
        """
        return self._get(
            "/public/books/book/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookRandomResponse,
        )


class AsyncBooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncBooksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        book_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookRetrieveResponse:
        """
        The API endpoint retrieves a book based on the book ID provided as a path
        variable.

        By accessing this endpoint and specifying a valid book ID, you will receive a
        response containing the details of the corresponding book.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not book_id:
            raise ValueError(f"Expected a non-empty value for `book_id` but received {book_id!r}")
        return await self._get(
            f"/public/books/{book_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookRetrieveResponse,
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
    ) -> BookListResponse:
        """
        The API endpoint allows you to retrieve a list of random books.

        Upon accessing this endpoint, you will receive a response containing a
        collection of randomly selected books.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/books",
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
                    book_list_params.BookListParams,
                ),
            ),
            cast_to=BookListResponse,
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
    ) -> BookRandomResponse:
        """
        The API endpoint returns a single random book from a list of books.

        Upon accessing this endpoint, you will receive a response containing the details
        of a randomly selected book.
        """
        return await self._get(
            "/public/books/book/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookRandomResponse,
        )


class BooksResourceWithRawResponse:
    def __init__(self, books: BooksResource) -> None:
        self._books = books

        self.retrieve = to_raw_response_wrapper(
            books.retrieve,
        )
        self.list = to_raw_response_wrapper(
            books.list,
        )
        self.random = to_raw_response_wrapper(
            books.random,
        )


class AsyncBooksResourceWithRawResponse:
    def __init__(self, books: AsyncBooksResource) -> None:
        self._books = books

        self.retrieve = async_to_raw_response_wrapper(
            books.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            books.list,
        )
        self.random = async_to_raw_response_wrapper(
            books.random,
        )


class BooksResourceWithStreamingResponse:
    def __init__(self, books: BooksResource) -> None:
        self._books = books

        self.retrieve = to_streamed_response_wrapper(
            books.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            books.list,
        )
        self.random = to_streamed_response_wrapper(
            books.random,
        )


class AsyncBooksResourceWithStreamingResponse:
    def __init__(self, books: AsyncBooksResource) -> None:
        self._books = books

        self.retrieve = async_to_streamed_response_wrapper(
            books.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            books.list,
        )
        self.random = async_to_streamed_response_wrapper(
            books.random,
        )
