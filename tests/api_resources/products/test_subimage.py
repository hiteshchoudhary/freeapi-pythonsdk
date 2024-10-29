# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.products import SubimageRemoveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubimage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_remove(self, client: Freeapiapp) -> None:
        subimage = client.products.subimage.remove(
            sub_image_id="647c69c1912544cbe9cf05a2",
            product_id="647c6059fe873dfa3c256fc3",
        )
        assert_matches_type(SubimageRemoveResponse, subimage, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Freeapiapp) -> None:
        response = client.products.subimage.with_raw_response.remove(
            sub_image_id="647c69c1912544cbe9cf05a2",
            product_id="647c6059fe873dfa3c256fc3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subimage = response.parse()
        assert_matches_type(SubimageRemoveResponse, subimage, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Freeapiapp) -> None:
        with client.products.subimage.with_streaming_response.remove(
            sub_image_id="647c69c1912544cbe9cf05a2",
            product_id="647c6059fe873dfa3c256fc3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subimage = response.parse()
            assert_matches_type(SubimageRemoveResponse, subimage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.subimage.with_raw_response.remove(
                sub_image_id="647c69c1912544cbe9cf05a2",
                product_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_image_id` but received ''"):
            client.products.subimage.with_raw_response.remove(
                sub_image_id="",
                product_id="647c6059fe873dfa3c256fc3",
            )


class TestAsyncSubimage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_remove(self, async_client: AsyncFreeapiapp) -> None:
        subimage = await async_client.products.subimage.remove(
            sub_image_id="647c69c1912544cbe9cf05a2",
            product_id="647c6059fe873dfa3c256fc3",
        )
        assert_matches_type(SubimageRemoveResponse, subimage, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.products.subimage.with_raw_response.remove(
            sub_image_id="647c69c1912544cbe9cf05a2",
            product_id="647c6059fe873dfa3c256fc3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subimage = await response.parse()
        assert_matches_type(SubimageRemoveResponse, subimage, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.products.subimage.with_streaming_response.remove(
            sub_image_id="647c69c1912544cbe9cf05a2",
            product_id="647c6059fe873dfa3c256fc3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subimage = await response.parse()
            assert_matches_type(SubimageRemoveResponse, subimage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.subimage.with_raw_response.remove(
                sub_image_id="647c69c1912544cbe9cf05a2",
                product_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_image_id` but received ''"):
            await async_client.products.subimage.with_raw_response.remove(
                sub_image_id="",
                product_id="647c6059fe873dfa3c256fc3",
            )
