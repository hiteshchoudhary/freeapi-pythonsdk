# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from .my import (
    MyResource,
    AsyncMyResource,
    MyResourceWithRawResponse,
    AsyncMyResourceWithRawResponse,
    MyResourceWithStreamingResponse,
    AsyncMyResourceWithStreamingResponse,
)
from .tag import (
    TagResource,
    AsyncTagResource,
    TagResourceWithRawResponse,
    AsyncTagResourceWithRawResponse,
    TagResourceWithStreamingResponse,
    AsyncTagResourceWithStreamingResponse,
)
from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from ...._compat import cached_property
from .user_posts import (
    UserPostsResource,
    AsyncUserPostsResource,
    UserPostsResourceWithRawResponse,
    AsyncUserPostsResourceWithRawResponse,
    UserPostsResourceWithStreamingResponse,
    AsyncUserPostsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.social_media import post_list_params, post_create_params, post_update_params
from ....types.social_media.post_like_response import PostLikeResponse
from ....types.social_media.post_list_response import PostListResponse
from ....types.social_media.post_create_response import PostCreateResponse
from ....types.social_media.post_delete_response import PostDeleteResponse
from ....types.social_media.post_update_response import PostUpdateResponse
from ....types.social_media.post_retrieve_response import PostRetrieveResponse

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    @cached_property
    def my(self) -> MyResource:
        return MyResource(self._client)

    @cached_property
    def user_posts(self) -> UserPostsResource:
        return UserPostsResource(self._client)

    @cached_property
    def tag(self) -> TagResource:
        return TagResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return PostsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content: str | NotGiven = NOT_GIVEN,
        images: FileTypes | NotGiven = NOT_GIVEN,
        tags_0: str | NotGiven = NOT_GIVEN,
        tags_1: str | NotGiven = NOT_GIVEN,
        tags_2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostCreateResponse:
        """
        The API allows a logged-in user to create a social media post by providing the
        necessary details in the request body.

        The user can include the content of the post, relevant tags, and attach images
        (upto 6) as part of the request.

        NOTE: As this api requires formData to be used, to send multiple tags client
        must send them with the respective index.

        e.g. if you are passing 4 tags the keys in the, following is onw of the ways to
        send them:

        ```javascript
        const formData = new FromData()
        // ... other form data appends
        tags.forEach((tag, ind) => {
            formData.append(`tag[${ind}]`: tag)
        })

        ```

        Args:
          images: Upto 6 images per post are allowed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "content": content,
                "images": images,
                "tags_0": tags_0,
                "tags_1": tags_1,
                "tags_2": tags_2,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["images"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/social-media/posts",
            body=maybe_transform(body, post_create_params.PostCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostCreateResponse,
        )

    def retrieve(
        self,
        post_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostRetrieveResponse:
        """
        The API endpoint allows users to fetch a post by providing the post ID as a path
        variable.

        By accessing this endpoint and providing a valid post ID, users will receive a
        response containing the details of the post corresponding to the provided ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._get(
            f"/social-media/posts/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostRetrieveResponse,
        )

    def update(
        self,
        post_id: str,
        *,
        content: str | NotGiven = NOT_GIVEN,
        images: FileTypes | NotGiven = NOT_GIVEN,
        tags_0: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostUpdateResponse:
        """
        The API endpoint allows users to update a post by passing relevant data, along
        with the post ID as a path variable.

        By accessing this endpoint and providing the necessary data and post ID, users
        can modify and update the content of a specific post.

        **NOTE:** All the fields in the body and optional but must not be empty if
        passed in the body.

        Args:
          images: Upto 6 total images are allowed per post

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        body = deepcopy_minimal(
            {
                "content": content,
                "images": images,
                "tags_0": tags_0,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["images"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._patch(
            f"/social-media/posts/{post_id}",
            body=maybe_transform(body, post_update_params.PostUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostUpdateResponse,
        )

    def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostListResponse:
        """
        The API endpoint allows users to fetch all posts posted by themselves or other
        users within the social media application.

        By accessing this endpoint, users can retrieve a collection of posts containing
        relevant information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/social-media/posts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=PostListResponse,
        )

    def delete(
        self,
        post_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostDeleteResponse:
        """
        The API endpoint allows users to delete a post by passing the post ID as a path
        variable.

        By accessing this endpoint and providing the specific post ID in the URL, users
        can initiate the deletion of the corresponding post.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._delete(
            f"/social-media/posts/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostDeleteResponse,
        )

    def like(
        self,
        post_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostLikeResponse:
        """
        The API endpoint enables users to like or unlike a social media post.

        By accessing this endpoint, users can interact with the post by either liking or
        unliking it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return self._post(
            f"/social-media/like/post/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostLikeResponse,
        )


class AsyncPostsResource(AsyncAPIResource):
    @cached_property
    def my(self) -> AsyncMyResource:
        return AsyncMyResource(self._client)

    @cached_property
    def user_posts(self) -> AsyncUserPostsResource:
        return AsyncUserPostsResource(self._client)

    @cached_property
    def tag(self) -> AsyncTagResource:
        return AsyncTagResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncPostsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content: str | NotGiven = NOT_GIVEN,
        images: FileTypes | NotGiven = NOT_GIVEN,
        tags_0: str | NotGiven = NOT_GIVEN,
        tags_1: str | NotGiven = NOT_GIVEN,
        tags_2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostCreateResponse:
        """
        The API allows a logged-in user to create a social media post by providing the
        necessary details in the request body.

        The user can include the content of the post, relevant tags, and attach images
        (upto 6) as part of the request.

        NOTE: As this api requires formData to be used, to send multiple tags client
        must send them with the respective index.

        e.g. if you are passing 4 tags the keys in the, following is onw of the ways to
        send them:

        ```javascript
        const formData = new FromData()
        // ... other form data appends
        tags.forEach((tag, ind) => {
            formData.append(`tag[${ind}]`: tag)
        })

        ```

        Args:
          images: Upto 6 images per post are allowed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "content": content,
                "images": images,
                "tags_0": tags_0,
                "tags_1": tags_1,
                "tags_2": tags_2,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["images"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/social-media/posts",
            body=await async_maybe_transform(body, post_create_params.PostCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostCreateResponse,
        )

    async def retrieve(
        self,
        post_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostRetrieveResponse:
        """
        The API endpoint allows users to fetch a post by providing the post ID as a path
        variable.

        By accessing this endpoint and providing a valid post ID, users will receive a
        response containing the details of the post corresponding to the provided ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._get(
            f"/social-media/posts/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostRetrieveResponse,
        )

    async def update(
        self,
        post_id: str,
        *,
        content: str | NotGiven = NOT_GIVEN,
        images: FileTypes | NotGiven = NOT_GIVEN,
        tags_0: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostUpdateResponse:
        """
        The API endpoint allows users to update a post by passing relevant data, along
        with the post ID as a path variable.

        By accessing this endpoint and providing the necessary data and post ID, users
        can modify and update the content of a specific post.

        **NOTE:** All the fields in the body and optional but must not be empty if
        passed in the body.

        Args:
          images: Upto 6 total images are allowed per post

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        body = deepcopy_minimal(
            {
                "content": content,
                "images": images,
                "tags_0": tags_0,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["images"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._patch(
            f"/social-media/posts/{post_id}",
            body=await async_maybe_transform(body, post_update_params.PostUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostUpdateResponse,
        )

    async def list(
        self,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostListResponse:
        """
        The API endpoint allows users to fetch all posts posted by themselves or other
        users within the social media application.

        By accessing this endpoint, users can retrieve a collection of posts containing
        relevant information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/social-media/posts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=PostListResponse,
        )

    async def delete(
        self,
        post_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostDeleteResponse:
        """
        The API endpoint allows users to delete a post by passing the post ID as a path
        variable.

        By accessing this endpoint and providing the specific post ID in the URL, users
        can initiate the deletion of the corresponding post.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._delete(
            f"/social-media/posts/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostDeleteResponse,
        )

    async def like(
        self,
        post_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostLikeResponse:
        """
        The API endpoint enables users to like or unlike a social media post.

        By accessing this endpoint, users can interact with the post by either liking or
        unliking it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not post_id:
            raise ValueError(f"Expected a non-empty value for `post_id` but received {post_id!r}")
        return await self._post(
            f"/social-media/like/post/{post_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostLikeResponse,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_raw_response_wrapper(
            posts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            posts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            posts.update,
        )
        self.list = to_raw_response_wrapper(
            posts.list,
        )
        self.delete = to_raw_response_wrapper(
            posts.delete,
        )
        self.like = to_raw_response_wrapper(
            posts.like,
        )

    @cached_property
    def my(self) -> MyResourceWithRawResponse:
        return MyResourceWithRawResponse(self._posts.my)

    @cached_property
    def user_posts(self) -> UserPostsResourceWithRawResponse:
        return UserPostsResourceWithRawResponse(self._posts.user_posts)

    @cached_property
    def tag(self) -> TagResourceWithRawResponse:
        return TagResourceWithRawResponse(self._posts.tag)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._posts.images)


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_raw_response_wrapper(
            posts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            posts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            posts.update,
        )
        self.list = async_to_raw_response_wrapper(
            posts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            posts.delete,
        )
        self.like = async_to_raw_response_wrapper(
            posts.like,
        )

    @cached_property
    def my(self) -> AsyncMyResourceWithRawResponse:
        return AsyncMyResourceWithRawResponse(self._posts.my)

    @cached_property
    def user_posts(self) -> AsyncUserPostsResourceWithRawResponse:
        return AsyncUserPostsResourceWithRawResponse(self._posts.user_posts)

    @cached_property
    def tag(self) -> AsyncTagResourceWithRawResponse:
        return AsyncTagResourceWithRawResponse(self._posts.tag)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._posts.images)


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_streamed_response_wrapper(
            posts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            posts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            posts.update,
        )
        self.list = to_streamed_response_wrapper(
            posts.list,
        )
        self.delete = to_streamed_response_wrapper(
            posts.delete,
        )
        self.like = to_streamed_response_wrapper(
            posts.like,
        )

    @cached_property
    def my(self) -> MyResourceWithStreamingResponse:
        return MyResourceWithStreamingResponse(self._posts.my)

    @cached_property
    def user_posts(self) -> UserPostsResourceWithStreamingResponse:
        return UserPostsResourceWithStreamingResponse(self._posts.user_posts)

    @cached_property
    def tag(self) -> TagResourceWithStreamingResponse:
        return TagResourceWithStreamingResponse(self._posts.tag)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._posts.images)


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_streamed_response_wrapper(
            posts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            posts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            posts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            posts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            posts.delete,
        )
        self.like = async_to_streamed_response_wrapper(
            posts.like,
        )

    @cached_property
    def my(self) -> AsyncMyResourceWithStreamingResponse:
        return AsyncMyResourceWithStreamingResponse(self._posts.my)

    @cached_property
    def user_posts(self) -> AsyncUserPostsResourceWithStreamingResponse:
        return AsyncUserPostsResourceWithStreamingResponse(self._posts.user_posts)

    @cached_property
    def tag(self) -> AsyncTagResourceWithStreamingResponse:
        return AsyncTagResourceWithStreamingResponse(self._posts.tag)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._posts.images)
