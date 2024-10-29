# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.social_media import (
    PostLikeResponse,
    PostListResponse,
    PostCreateResponse,
    PostDeleteResponse,
    PostUpdateResponse,
    PostRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPosts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        post = client.social_media.posts.create()
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        post = client.social_media.posts.create(
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sapien libero, bibendum sed semper vel, cursus ut enim. Sed a lectus eu ligula varius tincidunt vel vitae odio. Phasellus vel massa odio. Donec in velit eu eros consequat ultrices nec eu nulla. Sed id molestie diam, sed suscipit enim. Ut auctor turpis dui, eu gravida elit molestie nec. Vestibulum posuere eros a dolor iaculis, sollicitudin ullamcorper nisl condimentum.",
            images=b"raw file contents",
            tags_0="first_post",
            tags_1="marketing",
            tags_2="digital",
        )
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.social_media.posts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.social_media.posts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostCreateResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        post = client.social_media.posts.retrieve(
            "6495426ed02af5a73904db67",
        )
        assert_matches_type(PostRetrieveResponse, post, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.social_media.posts.with_raw_response.retrieve(
            "6495426ed02af5a73904db67",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostRetrieveResponse, post, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.social_media.posts.with_streaming_response.retrieve(
            "6495426ed02af5a73904db67",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostRetrieveResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.social_media.posts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        post = client.social_media.posts.update(
            post_id="6495426ed02af5a73904db67",
        )
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        post = client.social_media.posts.update(
            post_id="6495426ed02af5a73904db67",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sapien libero, bibendum sed semper vel, cursus ut enim. Sed a lectus eu ligula varius tincidunt vel vitae odio. Phasellus vel massa odio. Donec in velit eu eros consequat ultrices nec eu nulla.",
            images=b"raw file contents",
            tags_0="updatedTag",
        )
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.social_media.posts.with_raw_response.update(
            post_id="6495426ed02af5a73904db67",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.social_media.posts.with_streaming_response.update(
            post_id="6495426ed02af5a73904db67",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostUpdateResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.social_media.posts.with_raw_response.update(
                post_id="",
            )

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        post = client.social_media.posts.list()
        assert_matches_type(PostListResponse, post, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        post = client.social_media.posts.list(
            limit="10",
            page="1",
        )
        assert_matches_type(PostListResponse, post, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.social_media.posts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostListResponse, post, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.social_media.posts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostListResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        post = client.social_media.posts.delete(
            "6495426ed02af5a73904db67",
        )
        assert_matches_type(PostDeleteResponse, post, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.social_media.posts.with_raw_response.delete(
            "6495426ed02af5a73904db67",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostDeleteResponse, post, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.social_media.posts.with_streaming_response.delete(
            "6495426ed02af5a73904db67",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostDeleteResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.social_media.posts.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_like(self, client: Freeapiapp) -> None:
        post = client.social_media.posts.like(
            "649736ac3e2615fb255a948b",
        )
        assert_matches_type(PostLikeResponse, post, path=["response"])

    @parametrize
    def test_raw_response_like(self, client: Freeapiapp) -> None:
        response = client.social_media.posts.with_raw_response.like(
            "649736ac3e2615fb255a948b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostLikeResponse, post, path=["response"])

    @parametrize
    def test_streaming_response_like(self, client: Freeapiapp) -> None:
        with client.social_media.posts.with_streaming_response.like(
            "649736ac3e2615fb255a948b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostLikeResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_like(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.social_media.posts.with_raw_response.like(
                "",
            )


class TestAsyncPosts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        post = await async_client.social_media.posts.create()
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        post = await async_client.social_media.posts.create(
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sapien libero, bibendum sed semper vel, cursus ut enim. Sed a lectus eu ligula varius tincidunt vel vitae odio. Phasellus vel massa odio. Donec in velit eu eros consequat ultrices nec eu nulla. Sed id molestie diam, sed suscipit enim. Ut auctor turpis dui, eu gravida elit molestie nec. Vestibulum posuere eros a dolor iaculis, sollicitudin ullamcorper nisl condimentum.",
            images=b"raw file contents",
            tags_0="first_post",
            tags_1="marketing",
            tags_2="digital",
        )
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.posts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.posts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostCreateResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        post = await async_client.social_media.posts.retrieve(
            "6495426ed02af5a73904db67",
        )
        assert_matches_type(PostRetrieveResponse, post, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.posts.with_raw_response.retrieve(
            "6495426ed02af5a73904db67",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostRetrieveResponse, post, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.posts.with_streaming_response.retrieve(
            "6495426ed02af5a73904db67",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostRetrieveResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.social_media.posts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        post = await async_client.social_media.posts.update(
            post_id="6495426ed02af5a73904db67",
        )
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        post = await async_client.social_media.posts.update(
            post_id="6495426ed02af5a73904db67",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sapien libero, bibendum sed semper vel, cursus ut enim. Sed a lectus eu ligula varius tincidunt vel vitae odio. Phasellus vel massa odio. Donec in velit eu eros consequat ultrices nec eu nulla.",
            images=b"raw file contents",
            tags_0="updatedTag",
        )
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.posts.with_raw_response.update(
            post_id="6495426ed02af5a73904db67",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostUpdateResponse, post, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.posts.with_streaming_response.update(
            post_id="6495426ed02af5a73904db67",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostUpdateResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.social_media.posts.with_raw_response.update(
                post_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        post = await async_client.social_media.posts.list()
        assert_matches_type(PostListResponse, post, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        post = await async_client.social_media.posts.list(
            limit="10",
            page="1",
        )
        assert_matches_type(PostListResponse, post, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.posts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostListResponse, post, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.posts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostListResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        post = await async_client.social_media.posts.delete(
            "6495426ed02af5a73904db67",
        )
        assert_matches_type(PostDeleteResponse, post, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.posts.with_raw_response.delete(
            "6495426ed02af5a73904db67",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostDeleteResponse, post, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.posts.with_streaming_response.delete(
            "6495426ed02af5a73904db67",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostDeleteResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.social_media.posts.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_like(self, async_client: AsyncFreeapiapp) -> None:
        post = await async_client.social_media.posts.like(
            "649736ac3e2615fb255a948b",
        )
        assert_matches_type(PostLikeResponse, post, path=["response"])

    @parametrize
    async def test_raw_response_like(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.posts.with_raw_response.like(
            "649736ac3e2615fb255a948b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostLikeResponse, post, path=["response"])

    @parametrize
    async def test_streaming_response_like(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.posts.with_streaming_response.like(
            "649736ac3e2615fb255a948b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostLikeResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_like(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.social_media.posts.with_raw_response.like(
                "",
            )
