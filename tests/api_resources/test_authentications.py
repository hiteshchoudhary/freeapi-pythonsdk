# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types import (
    AuthenticationLoginResponse,
    AuthenticationLogoutResponse,
    AuthenticationRegisterResponse,
    AuthenticationCurrentUserResponse,
    AuthenticationVerifyEmailResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthentications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_current_user(self, client: Freeapiapp) -> None:
        authentication = client.authentications.current_user()
        assert_matches_type(AuthenticationCurrentUserResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_current_user(self, client: Freeapiapp) -> None:
        response = client.authentications.with_raw_response.current_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationCurrentUserResponse, authentication, path=["response"])

    @parametrize
    def test_streaming_response_current_user(self, client: Freeapiapp) -> None:
        with client.authentications.with_streaming_response.current_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert_matches_type(AuthenticationCurrentUserResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_github_callback(self, client: Freeapiapp) -> None:
        authentication = client.authentications.github_callback()
        assert authentication is None

    @parametrize
    def test_raw_response_github_callback(self, client: Freeapiapp) -> None:
        response = client.authentications.with_raw_response.github_callback()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert authentication is None

    @parametrize
    def test_streaming_response_github_callback(self, client: Freeapiapp) -> None:
        with client.authentications.with_streaming_response.github_callback() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert authentication is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_github_redirect(self, client: Freeapiapp) -> None:
        authentication = client.authentications.github_redirect()
        assert authentication is None

    @parametrize
    def test_raw_response_github_redirect(self, client: Freeapiapp) -> None:
        response = client.authentications.with_raw_response.github_redirect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert authentication is None

    @parametrize
    def test_streaming_response_github_redirect(self, client: Freeapiapp) -> None:
        with client.authentications.with_streaming_response.github_redirect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert authentication is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_callback(self, client: Freeapiapp) -> None:
        authentication = client.authentications.google_callback()
        assert authentication is None

    @parametrize
    def test_raw_response_google_callback(self, client: Freeapiapp) -> None:
        response = client.authentications.with_raw_response.google_callback()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert authentication is None

    @parametrize
    def test_streaming_response_google_callback(self, client: Freeapiapp) -> None:
        with client.authentications.with_streaming_response.google_callback() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert authentication is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_redirect(self, client: Freeapiapp) -> None:
        authentication = client.authentications.google_redirect()
        assert authentication is None

    @parametrize
    def test_raw_response_google_redirect(self, client: Freeapiapp) -> None:
        response = client.authentications.with_raw_response.google_redirect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert authentication is None

    @parametrize
    def test_streaming_response_google_redirect(self, client: Freeapiapp) -> None:
        with client.authentications.with_streaming_response.google_redirect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert authentication is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_login(self, client: Freeapiapp) -> None:
        authentication = client.authentications.login()
        assert_matches_type(AuthenticationLoginResponse, authentication, path=["response"])

    @parametrize
    def test_method_login_with_all_params(self, client: Freeapiapp) -> None:
        authentication = client.authentications.login(
            password="test@123",
            username="doejohn",
        )
        assert_matches_type(AuthenticationLoginResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_login(self, client: Freeapiapp) -> None:
        response = client.authentications.with_raw_response.login()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationLoginResponse, authentication, path=["response"])

    @parametrize
    def test_streaming_response_login(self, client: Freeapiapp) -> None:
        with client.authentications.with_streaming_response.login() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert_matches_type(AuthenticationLoginResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_logout(self, client: Freeapiapp) -> None:
        authentication = client.authentications.logout()
        assert_matches_type(AuthenticationLogoutResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_logout(self, client: Freeapiapp) -> None:
        response = client.authentications.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationLogoutResponse, authentication, path=["response"])

    @parametrize
    def test_streaming_response_logout(self, client: Freeapiapp) -> None:
        with client.authentications.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert_matches_type(AuthenticationLogoutResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: Freeapiapp) -> None:
        authentication = client.authentications.register()
        assert_matches_type(AuthenticationRegisterResponse, authentication, path=["response"])

    @parametrize
    def test_method_register_with_all_params(self, client: Freeapiapp) -> None:
        authentication = client.authentications.register(
            email="user.email@domain.com",
            password="test@123",
            role="ADMIN",
            username="doejohn",
        )
        assert_matches_type(AuthenticationRegisterResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_register(self, client: Freeapiapp) -> None:
        response = client.authentications.with_raw_response.register()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationRegisterResponse, authentication, path=["response"])

    @parametrize
    def test_streaming_response_register(self, client: Freeapiapp) -> None:
        with client.authentications.with_streaming_response.register() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert_matches_type(AuthenticationRegisterResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_verify_email(self, client: Freeapiapp) -> None:
        authentication = client.authentications.verify_email(
            "ffff8c2d25725516cf34c8cfa9c5f4d8f1f1f407",
        )
        assert_matches_type(AuthenticationVerifyEmailResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_verify_email(self, client: Freeapiapp) -> None:
        response = client.authentications.with_raw_response.verify_email(
            "ffff8c2d25725516cf34c8cfa9c5f4d8f1f1f407",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationVerifyEmailResponse, authentication, path=["response"])

    @parametrize
    def test_streaming_response_verify_email(self, client: Freeapiapp) -> None:
        with client.authentications.with_streaming_response.verify_email(
            "ffff8c2d25725516cf34c8cfa9c5f4d8f1f1f407",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert_matches_type(AuthenticationVerifyEmailResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_verify_email(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_token` but received ''"):
            client.authentications.with_raw_response.verify_email(
                "",
            )


class TestAsyncAuthentications:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_current_user(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.current_user()
        assert_matches_type(AuthenticationCurrentUserResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_current_user(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.authentications.with_raw_response.current_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert_matches_type(AuthenticationCurrentUserResponse, authentication, path=["response"])

    @parametrize
    async def test_streaming_response_current_user(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.authentications.with_streaming_response.current_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert_matches_type(AuthenticationCurrentUserResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_github_callback(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.github_callback()
        assert authentication is None

    @parametrize
    async def test_raw_response_github_callback(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.authentications.with_raw_response.github_callback()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert authentication is None

    @parametrize
    async def test_streaming_response_github_callback(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.authentications.with_streaming_response.github_callback() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert authentication is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_github_redirect(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.github_redirect()
        assert authentication is None

    @parametrize
    async def test_raw_response_github_redirect(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.authentications.with_raw_response.github_redirect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert authentication is None

    @parametrize
    async def test_streaming_response_github_redirect(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.authentications.with_streaming_response.github_redirect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert authentication is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_callback(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.google_callback()
        assert authentication is None

    @parametrize
    async def test_raw_response_google_callback(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.authentications.with_raw_response.google_callback()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert authentication is None

    @parametrize
    async def test_streaming_response_google_callback(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.authentications.with_streaming_response.google_callback() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert authentication is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_redirect(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.google_redirect()
        assert authentication is None

    @parametrize
    async def test_raw_response_google_redirect(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.authentications.with_raw_response.google_redirect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert authentication is None

    @parametrize
    async def test_streaming_response_google_redirect(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.authentications.with_streaming_response.google_redirect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert authentication is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_login(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.login()
        assert_matches_type(AuthenticationLoginResponse, authentication, path=["response"])

    @parametrize
    async def test_method_login_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.login(
            password="test@123",
            username="doejohn",
        )
        assert_matches_type(AuthenticationLoginResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_login(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.authentications.with_raw_response.login()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert_matches_type(AuthenticationLoginResponse, authentication, path=["response"])

    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.authentications.with_streaming_response.login() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert_matches_type(AuthenticationLoginResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_logout(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.logout()
        assert_matches_type(AuthenticationLogoutResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.authentications.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert_matches_type(AuthenticationLogoutResponse, authentication, path=["response"])

    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.authentications.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert_matches_type(AuthenticationLogoutResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.register()
        assert_matches_type(AuthenticationRegisterResponse, authentication, path=["response"])

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.register(
            email="user.email@domain.com",
            password="test@123",
            role="ADMIN",
            username="doejohn",
        )
        assert_matches_type(AuthenticationRegisterResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.authentications.with_raw_response.register()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert_matches_type(AuthenticationRegisterResponse, authentication, path=["response"])

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.authentications.with_streaming_response.register() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert_matches_type(AuthenticationRegisterResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_verify_email(self, async_client: AsyncFreeapiapp) -> None:
        authentication = await async_client.authentications.verify_email(
            "ffff8c2d25725516cf34c8cfa9c5f4d8f1f1f407",
        )
        assert_matches_type(AuthenticationVerifyEmailResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_verify_email(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.authentications.with_raw_response.verify_email(
            "ffff8c2d25725516cf34c8cfa9c5f4d8f1f1f407",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert_matches_type(AuthenticationVerifyEmailResponse, authentication, path=["response"])

    @parametrize
    async def test_streaming_response_verify_email(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.authentications.with_streaming_response.verify_email(
            "ffff8c2d25725516cf34c8cfa9c5f4d8f1f1f407",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert_matches_type(AuthenticationVerifyEmailResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_verify_email(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_token` but received ''"):
            await async_client.authentications.with_raw_response.verify_email(
                "",
            )
