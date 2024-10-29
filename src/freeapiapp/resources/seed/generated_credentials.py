# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.seed.generated_credential_list_response import GeneratedCredentialListResponse

__all__ = ["GeneratedCredentialsResource", "AsyncGeneratedCredentialsResource"]


class GeneratedCredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GeneratedCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return GeneratedCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GeneratedCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return GeneratedCredentialsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GeneratedCredentialListResponse:
        """
        This API serves a JSON file containing a collection of dummy usernames and their
        corresponding raw passwords.

        It is primarily designed to assist developers during the database seeding
        process and provide a convenient way to access the raw passwords for testing or
        development purposes.
        """
        return self._get(
            "/seed/generated-credentials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GeneratedCredentialListResponse,
        )


class AsyncGeneratedCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGeneratedCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGeneratedCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGeneratedCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncGeneratedCredentialsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GeneratedCredentialListResponse:
        """
        This API serves a JSON file containing a collection of dummy usernames and their
        corresponding raw passwords.

        It is primarily designed to assist developers during the database seeding
        process and provide a convenient way to access the raw passwords for testing or
        development purposes.
        """
        return await self._get(
            "/seed/generated-credentials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GeneratedCredentialListResponse,
        )


class GeneratedCredentialsResourceWithRawResponse:
    def __init__(self, generated_credentials: GeneratedCredentialsResource) -> None:
        self._generated_credentials = generated_credentials

        self.list = to_raw_response_wrapper(
            generated_credentials.list,
        )


class AsyncGeneratedCredentialsResourceWithRawResponse:
    def __init__(self, generated_credentials: AsyncGeneratedCredentialsResource) -> None:
        self._generated_credentials = generated_credentials

        self.list = async_to_raw_response_wrapper(
            generated_credentials.list,
        )


class GeneratedCredentialsResourceWithStreamingResponse:
    def __init__(self, generated_credentials: GeneratedCredentialsResource) -> None:
        self._generated_credentials = generated_credentials

        self.list = to_streamed_response_wrapper(
            generated_credentials.list,
        )


class AsyncGeneratedCredentialsResourceWithStreamingResponse:
    def __init__(self, generated_credentials: AsyncGeneratedCredentialsResource) -> None:
        self._generated_credentials = generated_credentials

        self.list = async_to_streamed_response_wrapper(
            generated_credentials.list,
        )
