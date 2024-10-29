# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.kitchen_sink.request import PathVariableRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPathVariable:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        path_variable = client.kitchen_sink.request.path_variable.retrieve(
            "123",
        )
        assert_matches_type(PathVariableRetrieveResponse, path_variable, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.request.path_variable.with_raw_response.retrieve(
            "123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        path_variable = response.parse()
        assert_matches_type(PathVariableRetrieveResponse, path_variable, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.request.path_variable.with_streaming_response.retrieve(
            "123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            path_variable = response.parse()
            assert_matches_type(PathVariableRetrieveResponse, path_variable, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_variable` but received ''"):
            client.kitchen_sink.request.path_variable.with_raw_response.retrieve(
                "",
            )


class TestAsyncPathVariable:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        path_variable = await async_client.kitchen_sink.request.path_variable.retrieve(
            "123",
        )
        assert_matches_type(PathVariableRetrieveResponse, path_variable, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.request.path_variable.with_raw_response.retrieve(
            "123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        path_variable = await response.parse()
        assert_matches_type(PathVariableRetrieveResponse, path_variable, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.request.path_variable.with_streaming_response.retrieve(
            "123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            path_variable = await response.parse()
            assert_matches_type(PathVariableRetrieveResponse, path_variable, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_variable` but received ''"):
            await async_client.kitchen_sink.request.path_variable.with_raw_response.retrieve(
                "",
            )
