# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.public.random_jokes import JokeRandomResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJoke:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_random(self, client: Freeapiapp) -> None:
        joke = client.public.random_jokes.joke.random()
        assert_matches_type(JokeRandomResponse, joke, path=["response"])

    @parametrize
    def test_raw_response_random(self, client: Freeapiapp) -> None:
        response = client.public.random_jokes.joke.with_raw_response.random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        joke = response.parse()
        assert_matches_type(JokeRandomResponse, joke, path=["response"])

    @parametrize
    def test_streaming_response_random(self, client: Freeapiapp) -> None:
        with client.public.random_jokes.joke.with_streaming_response.random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            joke = response.parse()
            assert_matches_type(JokeRandomResponse, joke, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJoke:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_random(self, async_client: AsyncFreeapiapp) -> None:
        joke = await async_client.public.random_jokes.joke.random()
        assert_matches_type(JokeRandomResponse, joke, path=["response"])

    @parametrize
    async def test_raw_response_random(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.public.random_jokes.joke.with_raw_response.random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        joke = await response.parse()
        assert_matches_type(JokeRandomResponse, joke, path=["response"])

    @parametrize
    async def test_streaming_response_random(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.public.random_jokes.joke.with_streaming_response.random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            joke = await response.parse()
            assert_matches_type(JokeRandomResponse, joke, path=["response"])

        assert cast(Any, response.is_closed) is True
