# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .avatar import (
    AvatarResource,
    AsyncAvatarResource,
    AvatarResourceWithRawResponse,
    AsyncAvatarResourceWithRawResponse,
    AvatarResourceWithStreamingResponse,
    AsyncAvatarResourceWithStreamingResponse,
)
from ...types import (
    user_assign_role_params,
    user_reset_password_params,
    user_change_password_params,
    user_forgot_password_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.user_assign_role_response import UserAssignRoleResponse
from ...types.user_refresh_token_response import UserRefreshTokenResponse
from ...types.user_reset_password_response import UserResetPasswordResponse
from ...types.user_change_password_response import UserChangePasswordResponse
from ...types.user_forgot_password_response import UserForgotPasswordResponse
from ...types.user_resend_email_verification_response import UserResendEmailVerificationResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def avatar(self) -> AvatarResource:
        return AvatarResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def assign_role(
        self,
        user_id: str,
        *,
        role: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAssignRoleResponse:
        """
        The API endpoint allows administrators to change the roles of users within the
        system.

        This functionality is restricted to users with the `ADMIN` role, ensuring that
        only authorized personnel can modify user roles.

        It provides an essential tool for managing user permissions and ensuring proper
        authorization levels within the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/users/assign-role/{user_id}",
            body=maybe_transform({"role": role}, user_assign_role_params.UserAssignRoleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAssignRoleResponse,
        )

    def change_password(
        self,
        *,
        new_password: str | NotGiven = NOT_GIVEN,
        old_password: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserChangePasswordResponse:
        """
        The Change Password API allows logged-in users to update their current password
        by providing the old password as a verification step.

        This API provides a secure mechanism for users to change their passwords within
        the application.

        By accessing this endpoint and providing the old password, users can initiate
        the password change process and set a new password of their choice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users/change-password",
            body=maybe_transform(
                {
                    "new_password": new_password,
                    "old_password": old_password,
                },
                user_change_password_params.UserChangePasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserChangePasswordResponse,
        )

    def forgot_password(
        self,
        *,
        email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserForgotPasswordResponse:
        """
        The API endpoint allows you to send a forgot password email by providing the
        user's email ID.

        When accessing this endpoint and providing the email ID as a parameter, the API
        initiates the process of sending a password reset email to the specified email
        address.

        This functionality is useful for implementing password recovery mechanisms
        within your application, allowing users to reset their passwords securely.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users/forgot-password",
            body=maybe_transform({"email": email}, user_forgot_password_params.UserForgotPasswordParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserForgotPasswordResponse,
        )

    def refresh_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRefreshTokenResponse:
        """
        The Refresh Access Token API is responsible for refreshing the access token when
        it expires.

        It allows you to make a request to this endpoint with the refresh token, which
        has a lengthy expiry time, to obtain a new access token.

        Simultaneously, the API sets the new access token in a cookie for future
        authentication purposes while replacing the expired one.

        This functionality ensures continuous access to protected resources by
        automatically renewing the access token **without requiring the user to
        reauthenticate manually**.

        By utilizing the refresh token, the API securely refreshes the access token and
        updates it in the cookie, ensuring seamless and uninterrupted access to
        authorized endpoints.
        """
        return self._post(
            "/users/refresh-token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRefreshTokenResponse,
        )

    def resend_email_verification(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResendEmailVerificationResponse:
        """
        The API endpoint allows the logged-in user to request a resend of the email
        verification mail.

        By accessing this endpoint, the user can trigger the system to send another
        email verification link to their registered email address.

        This functionality is useful in cases where the initial verification email may
        have been missed, expired, or encountered delivery issues.
        """
        return self._post(
            "/users/resend-email-verification",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResendEmailVerificationResponse,
        )

    def reset_password(
        self,
        reset_token: str,
        *,
        new_password: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResetPasswordResponse:
        """
        The API endpoint enables users to reset their password through the password
        reset email.

        By providing the new password and the password reset token obtained from the
        URL, users can securely reset their password and regain access to their account.

        This functionality ensures a secure and streamlined password reset process,
        allowing users to update their password conveniently and protect their account
        from unauthorized access.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reset_token:
            raise ValueError(f"Expected a non-empty value for `reset_token` but received {reset_token!r}")
        return self._post(
            f"/users/reset-password/{reset_token}",
            body=maybe_transform({"new_password": new_password}, user_reset_password_params.UserResetPasswordParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResetPasswordResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def avatar(self) -> AsyncAvatarResource:
        return AsyncAvatarResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def assign_role(
        self,
        user_id: str,
        *,
        role: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAssignRoleResponse:
        """
        The API endpoint allows administrators to change the roles of users within the
        system.

        This functionality is restricted to users with the `ADMIN` role, ensuring that
        only authorized personnel can modify user roles.

        It provides an essential tool for managing user permissions and ensuring proper
        authorization levels within the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/users/assign-role/{user_id}",
            body=await async_maybe_transform({"role": role}, user_assign_role_params.UserAssignRoleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAssignRoleResponse,
        )

    async def change_password(
        self,
        *,
        new_password: str | NotGiven = NOT_GIVEN,
        old_password: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserChangePasswordResponse:
        """
        The Change Password API allows logged-in users to update their current password
        by providing the old password as a verification step.

        This API provides a secure mechanism for users to change their passwords within
        the application.

        By accessing this endpoint and providing the old password, users can initiate
        the password change process and set a new password of their choice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users/change-password",
            body=await async_maybe_transform(
                {
                    "new_password": new_password,
                    "old_password": old_password,
                },
                user_change_password_params.UserChangePasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserChangePasswordResponse,
        )

    async def forgot_password(
        self,
        *,
        email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserForgotPasswordResponse:
        """
        The API endpoint allows you to send a forgot password email by providing the
        user's email ID.

        When accessing this endpoint and providing the email ID as a parameter, the API
        initiates the process of sending a password reset email to the specified email
        address.

        This functionality is useful for implementing password recovery mechanisms
        within your application, allowing users to reset their passwords securely.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users/forgot-password",
            body=await async_maybe_transform({"email": email}, user_forgot_password_params.UserForgotPasswordParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserForgotPasswordResponse,
        )

    async def refresh_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRefreshTokenResponse:
        """
        The Refresh Access Token API is responsible for refreshing the access token when
        it expires.

        It allows you to make a request to this endpoint with the refresh token, which
        has a lengthy expiry time, to obtain a new access token.

        Simultaneously, the API sets the new access token in a cookie for future
        authentication purposes while replacing the expired one.

        This functionality ensures continuous access to protected resources by
        automatically renewing the access token **without requiring the user to
        reauthenticate manually**.

        By utilizing the refresh token, the API securely refreshes the access token and
        updates it in the cookie, ensuring seamless and uninterrupted access to
        authorized endpoints.
        """
        return await self._post(
            "/users/refresh-token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRefreshTokenResponse,
        )

    async def resend_email_verification(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResendEmailVerificationResponse:
        """
        The API endpoint allows the logged-in user to request a resend of the email
        verification mail.

        By accessing this endpoint, the user can trigger the system to send another
        email verification link to their registered email address.

        This functionality is useful in cases where the initial verification email may
        have been missed, expired, or encountered delivery issues.
        """
        return await self._post(
            "/users/resend-email-verification",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResendEmailVerificationResponse,
        )

    async def reset_password(
        self,
        reset_token: str,
        *,
        new_password: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserResetPasswordResponse:
        """
        The API endpoint enables users to reset their password through the password
        reset email.

        By providing the new password and the password reset token obtained from the
        URL, users can securely reset their password and regain access to their account.

        This functionality ensures a secure and streamlined password reset process,
        allowing users to update their password conveniently and protect their account
        from unauthorized access.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reset_token:
            raise ValueError(f"Expected a non-empty value for `reset_token` but received {reset_token!r}")
        return await self._post(
            f"/users/reset-password/{reset_token}",
            body=await async_maybe_transform(
                {"new_password": new_password}, user_reset_password_params.UserResetPasswordParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResetPasswordResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.assign_role = to_raw_response_wrapper(
            users.assign_role,
        )
        self.change_password = to_raw_response_wrapper(
            users.change_password,
        )
        self.forgot_password = to_raw_response_wrapper(
            users.forgot_password,
        )
        self.refresh_token = to_raw_response_wrapper(
            users.refresh_token,
        )
        self.resend_email_verification = to_raw_response_wrapper(
            users.resend_email_verification,
        )
        self.reset_password = to_raw_response_wrapper(
            users.reset_password,
        )

    @cached_property
    def avatar(self) -> AvatarResourceWithRawResponse:
        return AvatarResourceWithRawResponse(self._users.avatar)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.assign_role = async_to_raw_response_wrapper(
            users.assign_role,
        )
        self.change_password = async_to_raw_response_wrapper(
            users.change_password,
        )
        self.forgot_password = async_to_raw_response_wrapper(
            users.forgot_password,
        )
        self.refresh_token = async_to_raw_response_wrapper(
            users.refresh_token,
        )
        self.resend_email_verification = async_to_raw_response_wrapper(
            users.resend_email_verification,
        )
        self.reset_password = async_to_raw_response_wrapper(
            users.reset_password,
        )

    @cached_property
    def avatar(self) -> AsyncAvatarResourceWithRawResponse:
        return AsyncAvatarResourceWithRawResponse(self._users.avatar)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.assign_role = to_streamed_response_wrapper(
            users.assign_role,
        )
        self.change_password = to_streamed_response_wrapper(
            users.change_password,
        )
        self.forgot_password = to_streamed_response_wrapper(
            users.forgot_password,
        )
        self.refresh_token = to_streamed_response_wrapper(
            users.refresh_token,
        )
        self.resend_email_verification = to_streamed_response_wrapper(
            users.resend_email_verification,
        )
        self.reset_password = to_streamed_response_wrapper(
            users.reset_password,
        )

    @cached_property
    def avatar(self) -> AvatarResourceWithStreamingResponse:
        return AvatarResourceWithStreamingResponse(self._users.avatar)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.assign_role = async_to_streamed_response_wrapper(
            users.assign_role,
        )
        self.change_password = async_to_streamed_response_wrapper(
            users.change_password,
        )
        self.forgot_password = async_to_streamed_response_wrapper(
            users.forgot_password,
        )
        self.refresh_token = async_to_streamed_response_wrapper(
            users.refresh_token,
        )
        self.resend_email_verification = async_to_streamed_response_wrapper(
            users.resend_email_verification,
        )
        self.reset_password = async_to_streamed_response_wrapper(
            users.reset_password,
        )

    @cached_property
    def avatar(self) -> AsyncAvatarResourceWithStreamingResponse:
        return AsyncAvatarResourceWithStreamingResponse(self._users.avatar)
