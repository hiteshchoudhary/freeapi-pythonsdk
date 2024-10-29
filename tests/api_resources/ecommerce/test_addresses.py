# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types.ecommerce import (
    AddressListResponse,
    AddressCreateResponse,
    AddressDeleteResponse,
    AddressUpdateResponse,
    AddressRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Freeapiapp) -> None:
        address = client.ecommerce.addresses.create()
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Freeapiapp) -> None:
        address = client.ecommerce.addresses.create(
            address_line1="New lane central, D-203",
            address_line2="Opposite to central park",
            city="Mumbai",
            country="India",
            pincode="pincode",
            state="Maharashtra",
        )
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Freeapiapp) -> None:
        response = client.ecommerce.addresses.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Freeapiapp) -> None:
        with client.ecommerce.addresses.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressCreateResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Freeapiapp) -> None:
        address = client.ecommerce.addresses.retrieve(
            "647af1707396af90865b0edd",
        )
        assert_matches_type(AddressRetrieveResponse, address, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Freeapiapp) -> None:
        response = client.ecommerce.addresses.with_raw_response.retrieve(
            "647af1707396af90865b0edd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressRetrieveResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Freeapiapp) -> None:
        with client.ecommerce.addresses.with_streaming_response.retrieve(
            "647af1707396af90865b0edd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressRetrieveResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_id` but received ''"):
            client.ecommerce.addresses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Freeapiapp) -> None:
        address = client.ecommerce.addresses.update(
            address_id="647af1707396af90865b0edd",
        )
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Freeapiapp) -> None:
        address = client.ecommerce.addresses.update(
            address_id="647af1707396af90865b0edd",
            address_line1="New lane central, D-203",
            address_line2="Opposite to central park",
            city="Mumbai",
            country="India",
            pincode="pincode",
            state="Maharashtra",
        )
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Freeapiapp) -> None:
        response = client.ecommerce.addresses.with_raw_response.update(
            address_id="647af1707396af90865b0edd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Freeapiapp) -> None:
        with client.ecommerce.addresses.with_streaming_response.update(
            address_id="647af1707396af90865b0edd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressUpdateResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_id` but received ''"):
            client.ecommerce.addresses.with_raw_response.update(
                address_id="",
            )

    @parametrize
    def test_method_list(self, client: Freeapiapp) -> None:
        address = client.ecommerce.addresses.list()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Freeapiapp) -> None:
        address = client.ecommerce.addresses.list(
            limit="10",
            page="1",
        )
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Freeapiapp) -> None:
        response = client.ecommerce.addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Freeapiapp) -> None:
        with client.ecommerce.addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressListResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Freeapiapp) -> None:
        address = client.ecommerce.addresses.delete(
            "647af1707396af90865b0edd",
        )
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Freeapiapp) -> None:
        response = client.ecommerce.addresses.with_raw_response.delete(
            "647af1707396af90865b0edd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Freeapiapp) -> None:
        with client.ecommerce.addresses.with_streaming_response.delete(
            "647af1707396af90865b0edd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressDeleteResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_id` but received ''"):
            client.ecommerce.addresses.with_raw_response.delete(
                "",
            )


class TestAsyncAddresses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFreeapiapp) -> None:
        address = await async_client.ecommerce.addresses.create()
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        address = await async_client.ecommerce.addresses.create(
            address_line1="New lane central, D-203",
            address_line2="Opposite to central park",
            city="Mumbai",
            country="India",
            pincode="pincode",
            state="Maharashtra",
        )
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.addresses.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.addresses.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressCreateResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        address = await async_client.ecommerce.addresses.retrieve(
            "647af1707396af90865b0edd",
        )
        assert_matches_type(AddressRetrieveResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.addresses.with_raw_response.retrieve(
            "647af1707396af90865b0edd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressRetrieveResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.addresses.with_streaming_response.retrieve(
            "647af1707396af90865b0edd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressRetrieveResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_id` but received ''"):
            await async_client.ecommerce.addresses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncFreeapiapp) -> None:
        address = await async_client.ecommerce.addresses.update(
            address_id="647af1707396af90865b0edd",
        )
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        address = await async_client.ecommerce.addresses.update(
            address_id="647af1707396af90865b0edd",
            address_line1="New lane central, D-203",
            address_line2="Opposite to central park",
            city="Mumbai",
            country="India",
            pincode="pincode",
            state="Maharashtra",
        )
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.addresses.with_raw_response.update(
            address_id="647af1707396af90865b0edd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.addresses.with_streaming_response.update(
            address_id="647af1707396af90865b0edd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressUpdateResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_id` but received ''"):
            await async_client.ecommerce.addresses.with_raw_response.update(
                address_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFreeapiapp) -> None:
        address = await async_client.ecommerce.addresses.list()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        address = await async_client.ecommerce.addresses.list(
            limit="10",
            page="1",
        )
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressListResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncFreeapiapp) -> None:
        address = await async_client.ecommerce.addresses.delete(
            "647af1707396af90865b0edd",
        )
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.ecommerce.addresses.with_raw_response.delete(
            "647af1707396af90865b0edd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.ecommerce.addresses.with_streaming_response.delete(
            "647af1707396af90865b0edd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressDeleteResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_id` but received ''"):
            await async_client.ecommerce.addresses.with_raw_response.delete(
                "",
            )
