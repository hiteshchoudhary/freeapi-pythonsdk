# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .videos import (
    VideosResource,
    AsyncVideosResource,
    VideosResourceWithRawResponse,
    AsyncVideosResourceWithRawResponse,
    VideosResourceWithStreamingResponse,
    AsyncVideosResourceWithStreamingResponse,
)
from .channel import (
    ChannelResource,
    AsyncChannelResource,
    ChannelResourceWithRawResponse,
    AsyncChannelResourceWithRawResponse,
    ChannelResourceWithStreamingResponse,
    AsyncChannelResourceWithStreamingResponse,
)
from .related import (
    RelatedResource,
    AsyncRelatedResource,
    RelatedResourceWithRawResponse,
    AsyncRelatedResourceWithRawResponse,
    RelatedResourceWithStreamingResponse,
    AsyncRelatedResourceWithStreamingResponse,
)
from .comments import (
    CommentsResource,
    AsyncCommentsResource,
    CommentsResourceWithRawResponse,
    AsyncCommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
    AsyncCommentsResourceWithStreamingResponse,
)
from .playlists import (
    PlaylistsResource,
    AsyncPlaylistsResource,
    PlaylistsResourceWithRawResponse,
    AsyncPlaylistsResourceWithRawResponse,
    PlaylistsResourceWithStreamingResponse,
    AsyncPlaylistsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["YoutubeResource", "AsyncYoutubeResource"]


class YoutubeResource(SyncAPIResource):
    @cached_property
    def channel(self) -> ChannelResource:
        return ChannelResource(self._client)

    @cached_property
    def videos(self) -> VideosResource:
        return VideosResource(self._client)

    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def related(self) -> RelatedResource:
        return RelatedResource(self._client)

    @cached_property
    def playlists(self) -> PlaylistsResource:
        return PlaylistsResource(self._client)

    @cached_property
    def with_raw_response(self) -> YoutubeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return YoutubeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> YoutubeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return YoutubeResourceWithStreamingResponse(self)


class AsyncYoutubeResource(AsyncAPIResource):
    @cached_property
    def channel(self) -> AsyncChannelResource:
        return AsyncChannelResource(self._client)

    @cached_property
    def videos(self) -> AsyncVideosResource:
        return AsyncVideosResource(self._client)

    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def related(self) -> AsyncRelatedResource:
        return AsyncRelatedResource(self._client)

    @cached_property
    def playlists(self) -> AsyncPlaylistsResource:
        return AsyncPlaylistsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncYoutubeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncYoutubeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncYoutubeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncYoutubeResourceWithStreamingResponse(self)


class YoutubeResourceWithRawResponse:
    def __init__(self, youtube: YoutubeResource) -> None:
        self._youtube = youtube

    @cached_property
    def channel(self) -> ChannelResourceWithRawResponse:
        return ChannelResourceWithRawResponse(self._youtube.channel)

    @cached_property
    def videos(self) -> VideosResourceWithRawResponse:
        return VideosResourceWithRawResponse(self._youtube.videos)

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._youtube.comments)

    @cached_property
    def related(self) -> RelatedResourceWithRawResponse:
        return RelatedResourceWithRawResponse(self._youtube.related)

    @cached_property
    def playlists(self) -> PlaylistsResourceWithRawResponse:
        return PlaylistsResourceWithRawResponse(self._youtube.playlists)


class AsyncYoutubeResourceWithRawResponse:
    def __init__(self, youtube: AsyncYoutubeResource) -> None:
        self._youtube = youtube

    @cached_property
    def channel(self) -> AsyncChannelResourceWithRawResponse:
        return AsyncChannelResourceWithRawResponse(self._youtube.channel)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithRawResponse:
        return AsyncVideosResourceWithRawResponse(self._youtube.videos)

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._youtube.comments)

    @cached_property
    def related(self) -> AsyncRelatedResourceWithRawResponse:
        return AsyncRelatedResourceWithRawResponse(self._youtube.related)

    @cached_property
    def playlists(self) -> AsyncPlaylistsResourceWithRawResponse:
        return AsyncPlaylistsResourceWithRawResponse(self._youtube.playlists)


class YoutubeResourceWithStreamingResponse:
    def __init__(self, youtube: YoutubeResource) -> None:
        self._youtube = youtube

    @cached_property
    def channel(self) -> ChannelResourceWithStreamingResponse:
        return ChannelResourceWithStreamingResponse(self._youtube.channel)

    @cached_property
    def videos(self) -> VideosResourceWithStreamingResponse:
        return VideosResourceWithStreamingResponse(self._youtube.videos)

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._youtube.comments)

    @cached_property
    def related(self) -> RelatedResourceWithStreamingResponse:
        return RelatedResourceWithStreamingResponse(self._youtube.related)

    @cached_property
    def playlists(self) -> PlaylistsResourceWithStreamingResponse:
        return PlaylistsResourceWithStreamingResponse(self._youtube.playlists)


class AsyncYoutubeResourceWithStreamingResponse:
    def __init__(self, youtube: AsyncYoutubeResource) -> None:
        self._youtube = youtube

    @cached_property
    def channel(self) -> AsyncChannelResourceWithStreamingResponse:
        return AsyncChannelResourceWithStreamingResponse(self._youtube.channel)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithStreamingResponse:
        return AsyncVideosResourceWithStreamingResponse(self._youtube.videos)

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._youtube.comments)

    @cached_property
    def related(self) -> AsyncRelatedResourceWithStreamingResponse:
        return AsyncRelatedResourceWithStreamingResponse(self._youtube.related)

    @cached_property
    def playlists(self) -> AsyncPlaylistsResourceWithStreamingResponse:
        return AsyncPlaylistsResourceWithStreamingResponse(self._youtube.playlists)
