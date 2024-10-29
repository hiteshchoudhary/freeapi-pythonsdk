# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .followers import (
    FollowersResource,
    AsyncFollowersResource,
    FollowersResourceWithRawResponse,
    AsyncFollowersResourceWithRawResponse,
    FollowersResourceWithStreamingResponse,
    AsyncFollowersResourceWithStreamingResponse,
)
from .following import (
    FollowingResource,
    AsyncFollowingResource,
    FollowingResourceWithRawResponse,
    AsyncFollowingResourceWithRawResponse,
    FollowingResourceWithStreamingResponse,
    AsyncFollowingResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FollowResource", "AsyncFollowResource"]


class FollowResource(SyncAPIResource):
    @cached_property
    def followers(self) -> FollowersResource:
        return FollowersResource(self._client)

    @cached_property
    def following(self) -> FollowingResource:
        return FollowingResource(self._client)

    @cached_property
    def with_raw_response(self) -> FollowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return FollowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FollowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return FollowResourceWithStreamingResponse(self)


class AsyncFollowResource(AsyncAPIResource):
    @cached_property
    def followers(self) -> AsyncFollowersResource:
        return AsyncFollowersResource(self._client)

    @cached_property
    def following(self) -> AsyncFollowingResource:
        return AsyncFollowingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFollowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFollowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFollowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncFollowResourceWithStreamingResponse(self)


class FollowResourceWithRawResponse:
    def __init__(self, follow: FollowResource) -> None:
        self._follow = follow

    @cached_property
    def followers(self) -> FollowersResourceWithRawResponse:
        return FollowersResourceWithRawResponse(self._follow.followers)

    @cached_property
    def following(self) -> FollowingResourceWithRawResponse:
        return FollowingResourceWithRawResponse(self._follow.following)


class AsyncFollowResourceWithRawResponse:
    def __init__(self, follow: AsyncFollowResource) -> None:
        self._follow = follow

    @cached_property
    def followers(self) -> AsyncFollowersResourceWithRawResponse:
        return AsyncFollowersResourceWithRawResponse(self._follow.followers)

    @cached_property
    def following(self) -> AsyncFollowingResourceWithRawResponse:
        return AsyncFollowingResourceWithRawResponse(self._follow.following)


class FollowResourceWithStreamingResponse:
    def __init__(self, follow: FollowResource) -> None:
        self._follow = follow

    @cached_property
    def followers(self) -> FollowersResourceWithStreamingResponse:
        return FollowersResourceWithStreamingResponse(self._follow.followers)

    @cached_property
    def following(self) -> FollowingResourceWithStreamingResponse:
        return FollowingResourceWithStreamingResponse(self._follow.following)


class AsyncFollowResourceWithStreamingResponse:
    def __init__(self, follow: AsyncFollowResource) -> None:
        self._follow = follow

    @cached_property
    def followers(self) -> AsyncFollowersResourceWithStreamingResponse:
        return AsyncFollowersResourceWithStreamingResponse(self._follow.followers)

    @cached_property
    def following(self) -> AsyncFollowingResourceWithStreamingResponse:
        return AsyncFollowingResourceWithStreamingResponse(self._follow.following)
