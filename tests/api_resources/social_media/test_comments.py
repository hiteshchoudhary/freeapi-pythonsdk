# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.social_media import (
    CommentLikeResponse,
    CommentListResponse,
    CommentCreateResponse,
    CommentDeleteResponse,
    CommentUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        comment = client.social_media.comments.create(
            post_id="649957f74662581ee44781ee",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        comment = client.social_media.comments.create(
            post_id="649957f74662581ee44781ee",
            content="My first comment",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.social_media.comments.with_raw_response.create(
            post_id="649957f74662581ee44781ee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.social_media.comments.with_streaming_response.create(
            post_id="649957f74662581ee44781ee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.social_media.comments.with_raw_response.create(
                post_id="",
            )

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        comment = client.social_media.comments.update(
            comment_id="64973f433acb0ae20a97a354",
        )
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        comment = client.social_media.comments.update(
            comment_id="64973f433acb0ae20a97a354",
            content="Updated content",
        )
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.social_media.comments.with_raw_response.update(
            comment_id="64973f433acb0ae20a97a354",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.social_media.comments.with_streaming_response.update(
            comment_id="64973f433acb0ae20a97a354",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentUpdateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            client.social_media.comments.with_raw_response.update(
                comment_id="",
            )

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        comment = client.social_media.comments.list(
            post_id="649957f74662581ee44781ee",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        comment = client.social_media.comments.list(
            post_id="649957f74662581ee44781ee",
            limit="5",
            page="1",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.social_media.comments.with_raw_response.list(
            post_id="649957f74662581ee44781ee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.social_media.comments.with_streaming_response.list(
            post_id="649957f74662581ee44781ee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.social_media.comments.with_raw_response.list(
                post_id="",
            )

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        comment = client.social_media.comments.delete(
            "64973f433acb0ae20a97a354",
        )
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.social_media.comments.with_raw_response.delete(
            "64973f433acb0ae20a97a354",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.social_media.comments.with_streaming_response.delete(
            "64973f433acb0ae20a97a354",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentDeleteResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            client.social_media.comments.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_like(self, client: Freeapiapp) -> None:
        comment = client.social_media.comments.like(
            "649769d2b883005dbdcc3292",
        )
        assert_matches_type(CommentLikeResponse, comment, path=["response"])

    @parametrize
    def test_raw_response_like(self, client: Freeapiapp) -> None:
        response = client.social_media.comments.with_raw_response.like(
            "649769d2b883005dbdcc3292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentLikeResponse, comment, path=["response"])

    @parametrize
    def test_streaming_response_like(self, client: Freeapiapp) -> None:
        with client.social_media.comments.with_streaming_response.like(
            "649769d2b883005dbdcc3292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentLikeResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_like(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            client.social_media.comments.with_raw_response.like(
                "",
            )


class TestAsyncComments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        comment = await async_client.social_media.comments.create(
            post_id="649957f74662581ee44781ee",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        comment = await async_client.social_media.comments.create(
            post_id="649957f74662581ee44781ee",
            content="My first comment",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.comments.with_raw_response.create(
            post_id="649957f74662581ee44781ee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.comments.with_streaming_response.create(
            post_id="649957f74662581ee44781ee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.social_media.comments.with_raw_response.create(
                post_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        comment = await async_client.social_media.comments.update(
            comment_id="64973f433acb0ae20a97a354",
        )
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        comment = await async_client.social_media.comments.update(
            comment_id="64973f433acb0ae20a97a354",
            content="Updated content",
        )
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.comments.with_raw_response.update(
            comment_id="64973f433acb0ae20a97a354",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.comments.with_streaming_response.update(
            comment_id="64973f433acb0ae20a97a354",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentUpdateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            await async_client.social_media.comments.with_raw_response.update(
                comment_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        comment = await async_client.social_media.comments.list(
            post_id="649957f74662581ee44781ee",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        comment = await async_client.social_media.comments.list(
            post_id="649957f74662581ee44781ee",
            limit="5",
            page="1",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.comments.with_raw_response.list(
            post_id="649957f74662581ee44781ee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.comments.with_streaming_response.list(
            post_id="649957f74662581ee44781ee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.social_media.comments.with_raw_response.list(
                post_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        comment = await async_client.social_media.comments.delete(
            "64973f433acb0ae20a97a354",
        )
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.comments.with_raw_response.delete(
            "64973f433acb0ae20a97a354",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.comments.with_streaming_response.delete(
            "64973f433acb0ae20a97a354",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentDeleteResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            await async_client.social_media.comments.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_like(self, async_client: AsyncFreeapiapp) -> None:
        comment = await async_client.social_media.comments.like(
            "649769d2b883005dbdcc3292",
        )
        assert_matches_type(CommentLikeResponse, comment, path=["response"])

    @parametrize
    async def test_raw_response_like(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.social_media.comments.with_raw_response.like(
            "649769d2b883005dbdcc3292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentLikeResponse, comment, path=["response"])

    @parametrize
    async def test_streaming_response_like(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.social_media.comments.with_streaming_response.like(
            "649769d2b883005dbdcc3292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentLikeResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_like(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
            await async_client.social_media.comments.with_raw_response.like(
                "",
            )
