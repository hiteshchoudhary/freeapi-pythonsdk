# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .posts import (
    PostsResource,
    AsyncPostsResource,
    PostsResourceWithRawResponse,
    AsyncPostsResourceWithRawResponse,
    PostsResourceWithStreamingResponse,
    AsyncPostsResourceWithStreamingResponse,
)
from .follow import (
    FollowResource,
    AsyncFollowResource,
    FollowResourceWithRawResponse,
    AsyncFollowResourceWithRawResponse,
    FollowResourceWithStreamingResponse,
    AsyncFollowResourceWithStreamingResponse,
)
from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from .comments import (
    CommentsResource,
    AsyncCommentsResource,
    CommentsResourceWithRawResponse,
    AsyncCommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
    AsyncCommentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .bookmarks import (
    BookmarksResource,
    AsyncBookmarksResource,
    BookmarksResourceWithRawResponse,
    AsyncBookmarksResourceWithRawResponse,
    BookmarksResourceWithStreamingResponse,
    AsyncBookmarksResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .posts.posts import PostsResource, AsyncPostsResource
from .follow.follow import FollowResource, AsyncFollowResource
from .profile.profile import ProfileResource, AsyncProfileResource

__all__ = ["SocialMediaResource", "AsyncSocialMediaResource"]


class SocialMediaResource(SyncAPIResource):
    @cached_property
    def profile(self) -> ProfileResource:
        return ProfileResource(self._client)

    @cached_property
    def posts(self) -> PostsResource:
        return PostsResource(self._client)

    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def bookmarks(self) -> BookmarksResource:
        return BookmarksResource(self._client)

    @cached_property
    def follow(self) -> FollowResource:
        return FollowResource(self._client)

    @cached_property
    def with_raw_response(self) -> SocialMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return SocialMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SocialMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return SocialMediaResourceWithStreamingResponse(self)


class AsyncSocialMediaResource(AsyncAPIResource):
    @cached_property
    def profile(self) -> AsyncProfileResource:
        return AsyncProfileResource(self._client)

    @cached_property
    def posts(self) -> AsyncPostsResource:
        return AsyncPostsResource(self._client)

    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResource:
        return AsyncBookmarksResource(self._client)

    @cached_property
    def follow(self) -> AsyncFollowResource:
        return AsyncFollowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSocialMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSocialMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSocialMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncSocialMediaResourceWithStreamingResponse(self)


class SocialMediaResourceWithRawResponse:
    def __init__(self, social_media: SocialMediaResource) -> None:
        self._social_media = social_media

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        return ProfileResourceWithRawResponse(self._social_media.profile)

    @cached_property
    def posts(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self._social_media.posts)

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._social_media.comments)

    @cached_property
    def bookmarks(self) -> BookmarksResourceWithRawResponse:
        return BookmarksResourceWithRawResponse(self._social_media.bookmarks)

    @cached_property
    def follow(self) -> FollowResourceWithRawResponse:
        return FollowResourceWithRawResponse(self._social_media.follow)


class AsyncSocialMediaResourceWithRawResponse:
    def __init__(self, social_media: AsyncSocialMediaResource) -> None:
        self._social_media = social_media

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        return AsyncProfileResourceWithRawResponse(self._social_media.profile)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self._social_media.posts)

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._social_media.comments)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResourceWithRawResponse:
        return AsyncBookmarksResourceWithRawResponse(self._social_media.bookmarks)

    @cached_property
    def follow(self) -> AsyncFollowResourceWithRawResponse:
        return AsyncFollowResourceWithRawResponse(self._social_media.follow)


class SocialMediaResourceWithStreamingResponse:
    def __init__(self, social_media: SocialMediaResource) -> None:
        self._social_media = social_media

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        return ProfileResourceWithStreamingResponse(self._social_media.profile)

    @cached_property
    def posts(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self._social_media.posts)

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._social_media.comments)

    @cached_property
    def bookmarks(self) -> BookmarksResourceWithStreamingResponse:
        return BookmarksResourceWithStreamingResponse(self._social_media.bookmarks)

    @cached_property
    def follow(self) -> FollowResourceWithStreamingResponse:
        return FollowResourceWithStreamingResponse(self._social_media.follow)


class AsyncSocialMediaResourceWithStreamingResponse:
    def __init__(self, social_media: AsyncSocialMediaResource) -> None:
        self._social_media = social_media

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        return AsyncProfileResourceWithStreamingResponse(self._social_media.profile)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self._social_media.posts)

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._social_media.comments)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResourceWithStreamingResponse:
        return AsyncBookmarksResourceWithStreamingResponse(self._social_media.bookmarks)

    @cached_property
    def follow(self) -> AsyncFollowResourceWithStreamingResponse:
        return AsyncFollowResourceWithStreamingResponse(self._social_media.follow)
