# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp._utils import parse_datetime
from freeapiapp.types.ecommerce import (
    CouponListResponse,
    CouponApplyResponse,
    CouponCreateResponse,
    CouponDeleteResponse,
    CouponRemoveResponse,
    CouponUpdateResponse,
    CouponRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCoupons:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.create()
        assert_matches_type(CouponCreateResponse, coupon, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.create(
            coupon_code="GET600",
            discount_value=600,
            expiry_date=parse_datetime("2024-06-13T11:07:10.693Z"),
            minimum_cart_value=700,
            name="Season sale",
            start_date=parse_datetime("2023-02-13T11:07:10.693Z"),
            type="FLAT",
        )
        assert_matches_type(CouponCreateResponse, coupon, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.ecommerce.coupons.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(CouponCreateResponse, coupon, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.ecommerce.coupons.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(CouponCreateResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.retrieve(
            "648850c3718cdeb85439aefc",
        )
        assert_matches_type(CouponRetrieveResponse, coupon, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.ecommerce.coupons.with_raw_response.retrieve(
            "648850c3718cdeb85439aefc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(CouponRetrieveResponse, coupon, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.ecommerce.coupons.with_streaming_response.retrieve(
            "648850c3718cdeb85439aefc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(CouponRetrieveResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            client.ecommerce.coupons.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.update(
            coupon_id="648850c3718cdeb85439aefc",
        )
        assert_matches_type(CouponUpdateResponse, coupon, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.update(
            coupon_id="648850c3718cdeb85439aefc",
            coupon_code="First350",
            discount_value=350,
            name="First 350 code",
        )
        assert_matches_type(CouponUpdateResponse, coupon, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.ecommerce.coupons.with_raw_response.update(
            coupon_id="648850c3718cdeb85439aefc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(CouponUpdateResponse, coupon, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.ecommerce.coupons.with_streaming_response.update(
            coupon_id="648850c3718cdeb85439aefc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(CouponUpdateResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            client.ecommerce.coupons.with_raw_response.update(
                coupon_id="",
            )

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.list()
        assert_matches_type(CouponListResponse, coupon, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.list(
            limit="5",
            page="1",
        )
        assert_matches_type(CouponListResponse, coupon, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.ecommerce.coupons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(CouponListResponse, coupon, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.ecommerce.coupons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(CouponListResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.delete(
            "648850c3718cdeb85439aefc",
        )
        assert_matches_type(CouponDeleteResponse, coupon, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.ecommerce.coupons.with_raw_response.delete(
            "648850c3718cdeb85439aefc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(CouponDeleteResponse, coupon, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.ecommerce.coupons.with_streaming_response.delete(
            "648850c3718cdeb85439aefc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(CouponDeleteResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            client.ecommerce.coupons.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_apply(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.apply()
        assert_matches_type(CouponApplyResponse, coupon, path=["response"])

    @parametrize
    def test_method_apply_with_all_params(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.apply(
            coupon_code="CORRUPTI845",
        )
        assert_matches_type(CouponApplyResponse, coupon, path=["response"])

    @parametrize
    def test_raw_response_apply(self, client: Freeapiapp) -> None:
        response = client.ecommerce.coupons.with_raw_response.apply()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(CouponApplyResponse, coupon, path=["response"])

    @parametrize
    def test_streaming_response_apply(self, client: Freeapiapp) -> None:
        with client.ecommerce.coupons.with_streaming_response.apply() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(CouponApplyResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.remove()
        assert_matches_type(CouponRemoveResponse, coupon, path=["response"])

    @parametrize
    def test_method_remove_with_all_params(self, client: Freeapiapp) -> None:
        coupon = client.ecommerce.coupons.remove(
            coupon_code="CORRUPTI845",
        )
        assert_matches_type(CouponRemoveResponse, coupon, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Freeapiapp) -> None:
        response = client.ecommerce.coupons.with_raw_response.remove()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(CouponRemoveResponse, coupon, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Freeapiapp) -> None:
        with client.ecommerce.coupons.with_streaming_response.remove() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(CouponRemoveResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCoupons:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.create()
        assert_matches_type(CouponCreateResponse, coupon, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.create(
            coupon_code="GET600",
            discount_value=600,
            expiry_date=parse_datetime("2024-06-13T11:07:10.693Z"),
            minimum_cart_value=700,
            name="Season sale",
            start_date=parse_datetime("2023-02-13T11:07:10.693Z"),
            type="FLAT",
        )
        assert_matches_type(CouponCreateResponse, coupon, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.coupons.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(CouponCreateResponse, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.coupons.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(CouponCreateResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.retrieve(
            "648850c3718cdeb85439aefc",
        )
        assert_matches_type(CouponRetrieveResponse, coupon, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.coupons.with_raw_response.retrieve(
            "648850c3718cdeb85439aefc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(CouponRetrieveResponse, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.coupons.with_streaming_response.retrieve(
            "648850c3718cdeb85439aefc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(CouponRetrieveResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            await async_client.ecommerce.coupons.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.update(
            coupon_id="648850c3718cdeb85439aefc",
        )
        assert_matches_type(CouponUpdateResponse, coupon, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.update(
            coupon_id="648850c3718cdeb85439aefc",
            coupon_code="First350",
            discount_value=350,
            name="First 350 code",
        )
        assert_matches_type(CouponUpdateResponse, coupon, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.coupons.with_raw_response.update(
            coupon_id="648850c3718cdeb85439aefc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(CouponUpdateResponse, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.coupons.with_streaming_response.update(
            coupon_id="648850c3718cdeb85439aefc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(CouponUpdateResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            await async_client.ecommerce.coupons.with_raw_response.update(
                coupon_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.list()
        assert_matches_type(CouponListResponse, coupon, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.list(
            limit="5",
            page="1",
        )
        assert_matches_type(CouponListResponse, coupon, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.coupons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(CouponListResponse, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.coupons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(CouponListResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.delete(
            "648850c3718cdeb85439aefc",
        )
        assert_matches_type(CouponDeleteResponse, coupon, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.coupons.with_raw_response.delete(
            "648850c3718cdeb85439aefc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(CouponDeleteResponse, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.coupons.with_streaming_response.delete(
            "648850c3718cdeb85439aefc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(CouponDeleteResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            await async_client.ecommerce.coupons.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_apply(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.apply()
        assert_matches_type(CouponApplyResponse, coupon, path=["response"])

    @parametrize
    async def test_method_apply_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.apply(
            coupon_code="CORRUPTI845",
        )
        assert_matches_type(CouponApplyResponse, coupon, path=["response"])

    @parametrize
    async def test_raw_response_apply(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.coupons.with_raw_response.apply()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(CouponApplyResponse, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_apply(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.coupons.with_streaming_response.apply() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(CouponApplyResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.remove()
        assert_matches_type(CouponRemoveResponse, coupon, path=["response"])

    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        coupon = await async_client.ecommerce.coupons.remove(
            coupon_code="CORRUPTI845",
        )
        assert_matches_type(CouponRemoveResponse, coupon, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.coupons.with_raw_response.remove()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(CouponRemoveResponse, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.coupons.with_streaming_response.remove() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(CouponRemoveResponse, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True
