# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.kitchen_sink import StatusCodeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatusCodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        status_code = client.kitchen_sink.status_codes.retrieve(
            "429",
        )
        assert status_code is None

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.status_codes.with_raw_response.retrieve(
            "429",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status_code = response.parse()
        assert status_code is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.status_codes.with_streaming_response.retrieve(
            "429",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status_code = response.parse()
            assert status_code is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_code` but received ''"):
            client.kitchen_sink.status_codes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        status_code = client.kitchen_sink.status_codes.list()
        assert_matches_type(StatusCodeListResponse, status_code, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.kitchen_sink.status_codes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status_code = response.parse()
        assert_matches_type(StatusCodeListResponse, status_code, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.kitchen_sink.status_codes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status_code = response.parse()
            assert_matches_type(StatusCodeListResponse, status_code, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatusCodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        status_code = await async_client.kitchen_sink.status_codes.retrieve(
            "429",
        )
        assert status_code is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.status_codes.with_raw_response.retrieve(
            "429",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status_code = await response.parse()
        assert status_code is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.status_codes.with_streaming_response.retrieve(
            "429",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status_code = await response.parse()
            assert status_code is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `status_code` but received ''"):
            await async_client.kitchen_sink.status_codes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        status_code = await async_client.kitchen_sink.status_codes.list()
        assert_matches_type(StatusCodeListResponse, status_code, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.kitchen_sink.status_codes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status_code = await response.parse()
        assert_matches_type(StatusCodeListResponse, status_code, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.kitchen_sink.status_codes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status_code = await response.parse()
            assert_matches_type(StatusCodeListResponse, status_code, path=["response"])

        assert cast(Any, response.is_closed) is True
