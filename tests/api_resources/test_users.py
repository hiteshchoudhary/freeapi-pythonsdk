# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from freeapiapp import Freeapiapp, AsyncFreeapiapp
from tests.utils import assert_matches_type
from freeapiapp.types import (
    UserAssignRoleResponse,
    UserRefreshTokenResponse,
    UserResetPasswordResponse,
    UserChangePasswordResponse,
    UserForgotPasswordResponse,
    UserResendEmailVerificationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_assign_role(self, client: Freeapiapp) -> None:
        user = client.users.assign_role(
            user_id="6489626dc265f0aa2dbb73a4",
        )
        assert_matches_type(UserAssignRoleResponse, user, path=["response"])

    @parametrize
    def test_method_assign_role_with_all_params(self, client: Freeapiapp) -> None:
        user = client.users.assign_role(
            user_id="6489626dc265f0aa2dbb73a4",
            role="ADMIN",
        )
        assert_matches_type(UserAssignRoleResponse, user, path=["response"])

    @parametrize
    def test_raw_response_assign_role(self, client: Freeapiapp) -> None:
        response = client.users.with_raw_response.assign_role(
            user_id="6489626dc265f0aa2dbb73a4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserAssignRoleResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_assign_role(self, client: Freeapiapp) -> None:
        with client.users.with_streaming_response.assign_role(
            user_id="6489626dc265f0aa2dbb73a4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserAssignRoleResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_assign_role(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.assign_role(
                user_id="",
            )

    @parametrize
    def test_method_change_password(self, client: Freeapiapp) -> None:
        user = client.users.change_password()
        assert_matches_type(UserChangePasswordResponse, user, path=["response"])

    @parametrize
    def test_method_change_password_with_all_params(self, client: Freeapiapp) -> None:
        user = client.users.change_password(
            new_password="test@123",
            old_password="new@123",
        )
        assert_matches_type(UserChangePasswordResponse, user, path=["response"])

    @parametrize
    def test_raw_response_change_password(self, client: Freeapiapp) -> None:
        response = client.users.with_raw_response.change_password()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserChangePasswordResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_change_password(self, client: Freeapiapp) -> None:
        with client.users.with_streaming_response.change_password() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserChangePasswordResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_forgot_password(self, client: Freeapiapp) -> None:
        user = client.users.forgot_password()
        assert_matches_type(UserForgotPasswordResponse, user, path=["response"])

    @parametrize
    def test_method_forgot_password_with_all_params(self, client: Freeapiapp) -> None:
        user = client.users.forgot_password(
            email="user.email@domain.com",
        )
        assert_matches_type(UserForgotPasswordResponse, user, path=["response"])

    @parametrize
    def test_raw_response_forgot_password(self, client: Freeapiapp) -> None:
        response = client.users.with_raw_response.forgot_password()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserForgotPasswordResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_forgot_password(self, client: Freeapiapp) -> None:
        with client.users.with_streaming_response.forgot_password() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserForgotPasswordResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_refresh_token(self, client: Freeapiapp) -> None:
        user = client.users.refresh_token()
        assert_matches_type(UserRefreshTokenResponse, user, path=["response"])

    @parametrize
    def test_raw_response_refresh_token(self, client: Freeapiapp) -> None:
        response = client.users.with_raw_response.refresh_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRefreshTokenResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_refresh_token(self, client: Freeapiapp) -> None:
        with client.users.with_streaming_response.refresh_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRefreshTokenResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_resend_email_verification(self, client: Freeapiapp) -> None:
        user = client.users.resend_email_verification()
        assert_matches_type(UserResendEmailVerificationResponse, user, path=["response"])

    @parametrize
    def test_raw_response_resend_email_verification(self, client: Freeapiapp) -> None:
        response = client.users.with_raw_response.resend_email_verification()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserResendEmailVerificationResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_resend_email_verification(self, client: Freeapiapp) -> None:
        with client.users.with_streaming_response.resend_email_verification() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserResendEmailVerificationResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reset_password(self, client: Freeapiapp) -> None:
        user = client.users.reset_password(
            reset_token="",
        )
        assert_matches_type(UserResetPasswordResponse, user, path=["response"])

    @parametrize
    def test_method_reset_password_with_all_params(self, client: Freeapiapp) -> None:
        user = client.users.reset_password(
            reset_token="",
            new_password="test@123",
        )
        assert_matches_type(UserResetPasswordResponse, user, path=["response"])

    @parametrize
    def test_raw_response_reset_password(self, client: Freeapiapp) -> None:
        response = client.users.with_raw_response.reset_password(
            reset_token="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserResetPasswordResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_reset_password(self, client: Freeapiapp) -> None:
        with client.users.with_streaming_response.reset_password(
            reset_token="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserResetPasswordResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset_password(self, client: Freeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reset_token` but received ''"):
            client.users.with_raw_response.reset_password(
                reset_token="",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_assign_role(self, async_client: AsyncFreeapiapp) -> None:
        user = await async_client.users.assign_role(
            user_id="6489626dc265f0aa2dbb73a4",
        )
        assert_matches_type(UserAssignRoleResponse, user, path=["response"])

    @parametrize
    async def test_method_assign_role_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        user = await async_client.users.assign_role(
            user_id="6489626dc265f0aa2dbb73a4",
            role="ADMIN",
        )
        assert_matches_type(UserAssignRoleResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_assign_role(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.users.with_raw_response.assign_role(
            user_id="6489626dc265f0aa2dbb73a4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserAssignRoleResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_assign_role(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.users.with_streaming_response.assign_role(
            user_id="6489626dc265f0aa2dbb73a4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserAssignRoleResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_assign_role(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.assign_role(
                user_id="",
            )

    @parametrize
    async def test_method_change_password(self, async_client: AsyncFreeapiapp) -> None:
        user = await async_client.users.change_password()
        assert_matches_type(UserChangePasswordResponse, user, path=["response"])

    @parametrize
    async def test_method_change_password_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        user = await async_client.users.change_password(
            new_password="test@123",
            old_password="new@123",
        )
        assert_matches_type(UserChangePasswordResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_change_password(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.users.with_raw_response.change_password()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserChangePasswordResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_change_password(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.users.with_streaming_response.change_password() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserChangePasswordResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_forgot_password(self, async_client: AsyncFreeapiapp) -> None:
        user = await async_client.users.forgot_password()
        assert_matches_type(UserForgotPasswordResponse, user, path=["response"])

    @parametrize
    async def test_method_forgot_password_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        user = await async_client.users.forgot_password(
            email="user.email@domain.com",
        )
        assert_matches_type(UserForgotPasswordResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_forgot_password(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.users.with_raw_response.forgot_password()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserForgotPasswordResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_forgot_password(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.users.with_streaming_response.forgot_password() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserForgotPasswordResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_refresh_token(self, async_client: AsyncFreeapiapp) -> None:
        user = await async_client.users.refresh_token()
        assert_matches_type(UserRefreshTokenResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_refresh_token(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.users.with_raw_response.refresh_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRefreshTokenResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_refresh_token(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.users.with_streaming_response.refresh_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRefreshTokenResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_resend_email_verification(self, async_client: AsyncFreeapiapp) -> None:
        user = await async_client.users.resend_email_verification()
        assert_matches_type(UserResendEmailVerificationResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_resend_email_verification(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.users.with_raw_response.resend_email_verification()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserResendEmailVerificationResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_resend_email_verification(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.users.with_streaming_response.resend_email_verification() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserResendEmailVerificationResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reset_password(self, async_client: AsyncFreeapiapp) -> None:
        user = await async_client.users.reset_password(
            reset_token="",
        )
        assert_matches_type(UserResetPasswordResponse, user, path=["response"])

    @parametrize
    async def test_method_reset_password_with_all_params(self, async_client: AsyncFreeapiapp) -> None:
        user = await async_client.users.reset_password(
            reset_token="",
            new_password="test@123",
        )
        assert_matches_type(UserResetPasswordResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_reset_password(self, async_client: AsyncFreeapiapp) -> None:
        response = await async_client.users.with_raw_response.reset_password(
            reset_token="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserResetPasswordResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_reset_password(self, async_client: AsyncFreeapiapp) -> None:
        async with async_client.users.with_streaming_response.reset_password(
            reset_token="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserResetPasswordResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset_password(self, async_client: AsyncFreeapiapp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reset_token` but received ''"):
            await async_client.users.with_raw_response.reset_password(
                reset_token="",
            )
