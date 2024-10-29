# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.public.meals import MealRandomResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMeal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_random(self, client: Freeapiapp) -> None:
        meal = client.public.meals.meal.random()
        assert_matches_type(MealRandomResponse, meal, path=["response"])

    @parametrize
    def test_raw_response_random(self, client: Freeapiapp) -> None:
        response = client.public.meals.meal.with_raw_response.random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meal = response.parse()
        assert_matches_type(MealRandomResponse, meal, path=["response"])

    @parametrize
    def test_streaming_response_random(self, client: Freeapiapp) -> None:
        with client.public.meals.meal.with_streaming_response.random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meal = response.parse()
            assert_matches_type(MealRandomResponse, meal, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMeal:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_random(self, async_client: AsyncFreeapiapp) -> None:
        meal = await async_client.public.meals.meal.random()
        assert_matches_type(MealRandomResponse, meal, path=["response"])

    @parametrize
    async def test_raw_response_random(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.public.meals.meal.with_raw_response.random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meal = await response.parse()
        assert_matches_type(MealRandomResponse, meal, path=["response"])

    @parametrize
    async def test_streaming_response_random(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.public.meals.meal.with_streaming_response.random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meal = await response.parse()
            assert_matches_type(MealRandomResponse, meal, path=["response"])

        assert cast(Any, response.is_closed) is True
