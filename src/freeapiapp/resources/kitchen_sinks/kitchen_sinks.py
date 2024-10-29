# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import kitchen_sink_redirect_to_params
from .cookies import (
    CookiesResource,
    AsyncCookiesResource,
    CookiesResourceWithRawResponse,
    AsyncCookiesResourceWithRawResponse,
    CookiesResourceWithStreamingResponse,
    AsyncCookiesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.kitchen_sink_response_gzip_response import KitchenSinkResponseGzipResponse
from ...types.kitchen_sink_response_brotli_response import KitchenSinkResponseBrotliResponse

__all__ = ["KitchenSinksResource", "AsyncKitchenSinksResource"]


class KitchenSinksResource(SyncAPIResource):
    @cached_property
    def cookies(self) -> CookiesResource:
        return CookiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> KitchenSinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return KitchenSinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KitchenSinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return KitchenSinksResourceWithStreamingResponse(self)

    def image_svg(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint sends an image response in SVG format.

        When accessing this endpoint, the client will receive an image file in SVG
        format as the response.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/kitchen-sink/image/svg",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def images_jpeg(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint sends an image response in JPEG format.

        When accessing this endpoint, the client will receive an image file in JPEG
        format as the response.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/kitchen-sink/image/jpeg",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def images_jpg(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint sends an image response in JPG format.

        When accessing this endpoint, the client will receive an image file in JPG
        format as the response.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/kitchen-sink/image/jpg",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def images_png(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint sends an image response in PNG format.

        When accessing this endpoint, the client will receive an image file in PNG
        format as the response.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/kitchen-sink/image/png",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def images_webp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint sends an image response in WEBP format.

        When accessing this endpoint, the client will receive an image file in WEBP
        format as the response.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/kitchen-sink/image/webp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def redirect_to(
        self,
        *,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint redirects the client to a URL specified in the query parameter.

        When accessing this endpoint, the client's browser will be automatically
        redirected to the URL extracted from the query parameter.

        This functionality is useful when you need to redirect clients to a different
        location or resource based on dynamic information included in the query
        parameter. It allows for flexible navigation and routing within your application
        or for redirecting to external resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/kitchen-sink/redirect/to",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, kitchen_sink_redirect_to_params.KitchenSinkRedirectToParams),
            ),
            cast_to=NoneType,
        )

    def response_brotli(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KitchenSinkResponseBrotliResponse:
        """
        _Brotli encoding is a modern compression algorithm specifically designed for web
        content compression. It provides advanced and efficient compression by utilizing
        a combination of various techniques, including LZ77, Huffman coding, and context
        modeling._

        The API endpoint returns a Brotli encoded response, which means the response
        data is compressed using the Brotli compression algorithm.

        Brotli compression offers superior compression ratios compared to traditional
        compression methods like GZIP, resulting in smaller file sizes and improved
        network efficiency.

        The client will receive the compressed response and can decompress it using
        Brotli decompression to obtain the original data.
        """
        return self._get(
            "/kitchen-sink/response/brotli",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KitchenSinkResponseBrotliResponse,
        )

    def response_gzip(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KitchenSinkResponseGzipResponse:
        """
        _GZIP encoding is a compression technique used to reduce the size of data
        transmitted over the network. It works by replacing repetitive or redundant
        sequences of data with references, resulting in a compressed representation._

        The API endpoint returns a GZIP encoded response, providing a compressed version
        of the requested resource.

        When accessing this endpoint, the response received will be encoded using the
        GZIP compression algorithm, resulting in a smaller response size for efficient
        transmission over the network.

        GZIP encoding reduces bandwidth usage and improves overall performance by
        compressing the response data on the server-side and decompressing it on the
        client-side.
        """
        return self._get(
            "/kitchen-sink/response/gzip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KitchenSinkResponseGzipResponse,
        )


class AsyncKitchenSinksResource(AsyncAPIResource):
    @cached_property
    def cookies(self) -> AsyncCookiesResource:
        return AsyncCookiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKitchenSinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncKitchenSinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKitchenSinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncKitchenSinksResourceWithStreamingResponse(self)

    async def image_svg(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint sends an image response in SVG format.

        When accessing this endpoint, the client will receive an image file in SVG
        format as the response.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/kitchen-sink/image/svg",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def images_jpeg(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint sends an image response in JPEG format.

        When accessing this endpoint, the client will receive an image file in JPEG
        format as the response.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/kitchen-sink/image/jpeg",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def images_jpg(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint sends an image response in JPG format.

        When accessing this endpoint, the client will receive an image file in JPG
        format as the response.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/kitchen-sink/image/jpg",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def images_png(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint sends an image response in PNG format.

        When accessing this endpoint, the client will receive an image file in PNG
        format as the response.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/kitchen-sink/image/png",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def images_webp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint sends an image response in WEBP format.

        When accessing this endpoint, the client will receive an image file in WEBP
        format as the response.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/kitchen-sink/image/webp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def redirect_to(
        self,
        *,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The API endpoint redirects the client to a URL specified in the query parameter.

        When accessing this endpoint, the client's browser will be automatically
        redirected to the URL extracted from the query parameter.

        This functionality is useful when you need to redirect clients to a different
        location or resource based on dynamic information included in the query
        parameter. It allows for flexible navigation and routing within your application
        or for redirecting to external resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/kitchen-sink/redirect/to",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"url": url}, kitchen_sink_redirect_to_params.KitchenSinkRedirectToParams
                ),
            ),
            cast_to=NoneType,
        )

    async def response_brotli(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KitchenSinkResponseBrotliResponse:
        """
        _Brotli encoding is a modern compression algorithm specifically designed for web
        content compression. It provides advanced and efficient compression by utilizing
        a combination of various techniques, including LZ77, Huffman coding, and context
        modeling._

        The API endpoint returns a Brotli encoded response, which means the response
        data is compressed using the Brotli compression algorithm.

        Brotli compression offers superior compression ratios compared to traditional
        compression methods like GZIP, resulting in smaller file sizes and improved
        network efficiency.

        The client will receive the compressed response and can decompress it using
        Brotli decompression to obtain the original data.
        """
        return await self._get(
            "/kitchen-sink/response/brotli",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KitchenSinkResponseBrotliResponse,
        )

    async def response_gzip(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KitchenSinkResponseGzipResponse:
        """
        _GZIP encoding is a compression technique used to reduce the size of data
        transmitted over the network. It works by replacing repetitive or redundant
        sequences of data with references, resulting in a compressed representation._

        The API endpoint returns a GZIP encoded response, providing a compressed version
        of the requested resource.

        When accessing this endpoint, the response received will be encoded using the
        GZIP compression algorithm, resulting in a smaller response size for efficient
        transmission over the network.

        GZIP encoding reduces bandwidth usage and improves overall performance by
        compressing the response data on the server-side and decompressing it on the
        client-side.
        """
        return await self._get(
            "/kitchen-sink/response/gzip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KitchenSinkResponseGzipResponse,
        )


class KitchenSinksResourceWithRawResponse:
    def __init__(self, kitchen_sinks: KitchenSinksResource) -> None:
        self._kitchen_sinks = kitchen_sinks

        self.image_svg = to_raw_response_wrapper(
            kitchen_sinks.image_svg,
        )
        self.images_jpeg = to_raw_response_wrapper(
            kitchen_sinks.images_jpeg,
        )
        self.images_jpg = to_raw_response_wrapper(
            kitchen_sinks.images_jpg,
        )
        self.images_png = to_raw_response_wrapper(
            kitchen_sinks.images_png,
        )
        self.images_webp = to_raw_response_wrapper(
            kitchen_sinks.images_webp,
        )
        self.redirect_to = to_raw_response_wrapper(
            kitchen_sinks.redirect_to,
        )
        self.response_brotli = to_raw_response_wrapper(
            kitchen_sinks.response_brotli,
        )
        self.response_gzip = to_raw_response_wrapper(
            kitchen_sinks.response_gzip,
        )

    @cached_property
    def cookies(self) -> CookiesResourceWithRawResponse:
        return CookiesResourceWithRawResponse(self._kitchen_sinks.cookies)


class AsyncKitchenSinksResourceWithRawResponse:
    def __init__(self, kitchen_sinks: AsyncKitchenSinksResource) -> None:
        self._kitchen_sinks = kitchen_sinks

        self.image_svg = async_to_raw_response_wrapper(
            kitchen_sinks.image_svg,
        )
        self.images_jpeg = async_to_raw_response_wrapper(
            kitchen_sinks.images_jpeg,
        )
        self.images_jpg = async_to_raw_response_wrapper(
            kitchen_sinks.images_jpg,
        )
        self.images_png = async_to_raw_response_wrapper(
            kitchen_sinks.images_png,
        )
        self.images_webp = async_to_raw_response_wrapper(
            kitchen_sinks.images_webp,
        )
        self.redirect_to = async_to_raw_response_wrapper(
            kitchen_sinks.redirect_to,
        )
        self.response_brotli = async_to_raw_response_wrapper(
            kitchen_sinks.response_brotli,
        )
        self.response_gzip = async_to_raw_response_wrapper(
            kitchen_sinks.response_gzip,
        )

    @cached_property
    def cookies(self) -> AsyncCookiesResourceWithRawResponse:
        return AsyncCookiesResourceWithRawResponse(self._kitchen_sinks.cookies)


class KitchenSinksResourceWithStreamingResponse:
    def __init__(self, kitchen_sinks: KitchenSinksResource) -> None:
        self._kitchen_sinks = kitchen_sinks

        self.image_svg = to_streamed_response_wrapper(
            kitchen_sinks.image_svg,
        )
        self.images_jpeg = to_streamed_response_wrapper(
            kitchen_sinks.images_jpeg,
        )
        self.images_jpg = to_streamed_response_wrapper(
            kitchen_sinks.images_jpg,
        )
        self.images_png = to_streamed_response_wrapper(
            kitchen_sinks.images_png,
        )
        self.images_webp = to_streamed_response_wrapper(
            kitchen_sinks.images_webp,
        )
        self.redirect_to = to_streamed_response_wrapper(
            kitchen_sinks.redirect_to,
        )
        self.response_brotli = to_streamed_response_wrapper(
            kitchen_sinks.response_brotli,
        )
        self.response_gzip = to_streamed_response_wrapper(
            kitchen_sinks.response_gzip,
        )

    @cached_property
    def cookies(self) -> CookiesResourceWithStreamingResponse:
        return CookiesResourceWithStreamingResponse(self._kitchen_sinks.cookies)


class AsyncKitchenSinksResourceWithStreamingResponse:
    def __init__(self, kitchen_sinks: AsyncKitchenSinksResource) -> None:
        self._kitchen_sinks = kitchen_sinks

        self.image_svg = async_to_streamed_response_wrapper(
            kitchen_sinks.image_svg,
        )
        self.images_jpeg = async_to_streamed_response_wrapper(
            kitchen_sinks.images_jpeg,
        )
        self.images_jpg = async_to_streamed_response_wrapper(
            kitchen_sinks.images_jpg,
        )
        self.images_png = async_to_streamed_response_wrapper(
            kitchen_sinks.images_png,
        )
        self.images_webp = async_to_streamed_response_wrapper(
            kitchen_sinks.images_webp,
        )
        self.redirect_to = async_to_streamed_response_wrapper(
            kitchen_sinks.redirect_to,
        )
        self.response_brotli = async_to_streamed_response_wrapper(
            kitchen_sinks.response_brotli,
        )
        self.response_gzip = async_to_streamed_response_wrapper(
            kitchen_sinks.response_gzip,
        )

    @cached_property
    def cookies(self) -> AsyncCookiesResourceWithStreamingResponse:
        return AsyncCookiesResourceWithStreamingResponse(self._kitchen_sinks.cookies)
