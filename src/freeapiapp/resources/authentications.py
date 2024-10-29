# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import authentication_login_params, authentication_register_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.authentication_login_response import AuthenticationLoginResponse
from ..types.authentication_logout_response import AuthenticationLogoutResponse
from ..types.authentication_register_response import AuthenticationRegisterResponse
from ..types.authentication_current_user_response import AuthenticationCurrentUserResponse
from ..types.authentication_verify_email_response import AuthenticationVerifyEmailResponse

__all__ = ["AuthenticationsResource", "AsyncAuthenticationsResource"]


class AuthenticationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthenticationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AuthenticationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AuthenticationsResourceWithStreamingResponse(self)

    def current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationCurrentUserResponse:
        """
        The API endpoint allows you to retrieve the details of the currently logged-in
        user based on their authentication token.

        When accessing this endpoint with a valid authentication token, you will receive
        a response containing the information of the user who is currently authenticated
        and logged in.
        """
        return self._get(
            "/users/current-user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationCurrentUserResponse,
        )

    def github_callback(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Github will send user details in JSON format once user successfully logs in.

        Backend will create an access and refresh token and will redirect user to the
        appropreate frontend url with access token and refresh token in the query
        parameter.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/users/github/callback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def github_redirect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Redirect user to this url when user clicks on the **`Login with Github`**
        button.

        This url will render the github concent screen where user can select the github
        account with which he/she wants to login with.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/users/github",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def google_callback(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Google will send user details in JSON format once user successfully logs in.

        Backend will create an access and refresh token and will redirect user to the
        appropreate frontend url with access token and refresh token in the query
        parameter.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/users/google/callback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def google_redirect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Redirect user to this url when user clicks on the **`Login with Google`**
        button.

        This url will render the google concent screen where user can select the google
        account with which he/she wants to login with.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/users/google",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def login(
        self,
        *,
        password: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationLoginResponse:
        """
        The API endpoint allows users to log into the application securely and also
        returns an access token.

        When accessing this endpoint with valid login credentials, users will receive an
        access token in the response.

        Additionally, the API endpoint securely sets the access token within the
        browser/client httpOnly cookies for future authentication and authorization
        purposes.

        This functionality ensures a secure and efficient login process for users,
        providing them with an access token that can be used to authenticate subsequent
        API requests.

        By securely storing the access token in browser cookies, the endpoint enables
        automatic inclusion of the access token in future API requests, eliminating the
        need for users to manually manage and provide the token with each request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users/login",
            body=maybe_transform(
                {
                    "password": password,
                    "username": username,
                },
                authentication_login_params.AuthenticationLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationLoginResponse,
        )

    def logout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationLogoutResponse:
        """
        The API endpoint is responsible for logging out users from the application and
        destroying the access token cookies stored on the client-side.

        When accessing this endpoint, it triggers the logout process, revoking the
        user's authentication and terminating their active session.

        Additionally, it ensures that any access token cookies associated with the
        user's session are removed from the client's browser, effectively logging them
        out from the application.
        """
        return self._post(
            "/users/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationLogoutResponse,
        )

    def register(
        self,
        *,
        email: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        role: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationRegisterResponse:
        """
        The API endpoint allows users to register or signup to create their accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users/register",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "role": role,
                    "username": username,
                },
                authentication_register_params.AuthenticationRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationRegisterResponse,
        )

    def verify_email(
        self,
        verification_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationVerifyEmailResponse:
        """
        The API endpoint is used to verify a user's email by accessing the verification
        token (**verificationToken**) included in the path variable.

        When the user clicks on the email verification link provided to them, this API
        is invoked to validate their email address.

        By including the verification token in the URL path, the endpoint confirms the
        authenticity of the token and marks the user's email as verified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_token:
            raise ValueError(f"Expected a non-empty value for `verification_token` but received {verification_token!r}")
        return self._get(
            f"/users/verify-email/{verification_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationVerifyEmailResponse,
        )


class AsyncAuthenticationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthenticationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncAuthenticationsResourceWithStreamingResponse(self)

    async def current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationCurrentUserResponse:
        """
        The API endpoint allows you to retrieve the details of the currently logged-in
        user based on their authentication token.

        When accessing this endpoint with a valid authentication token, you will receive
        a response containing the information of the user who is currently authenticated
        and logged in.
        """
        return await self._get(
            "/users/current-user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationCurrentUserResponse,
        )

    async def github_callback(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Github will send user details in JSON format once user successfully logs in.

        Backend will create an access and refresh token and will redirect user to the
        appropreate frontend url with access token and refresh token in the query
        parameter.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/users/github/callback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def github_redirect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Redirect user to this url when user clicks on the **`Login with Github`**
        button.

        This url will render the github concent screen where user can select the github
        account with which he/she wants to login with.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/users/github",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def google_callback(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Google will send user details in JSON format once user successfully logs in.

        Backend will create an access and refresh token and will redirect user to the
        appropreate frontend url with access token and refresh token in the query
        parameter.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/users/google/callback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def google_redirect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Redirect user to this url when user clicks on the **`Login with Google`**
        button.

        This url will render the google concent screen where user can select the google
        account with which he/she wants to login with.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/users/google",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def login(
        self,
        *,
        password: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationLoginResponse:
        """
        The API endpoint allows users to log into the application securely and also
        returns an access token.

        When accessing this endpoint with valid login credentials, users will receive an
        access token in the response.

        Additionally, the API endpoint securely sets the access token within the
        browser/client httpOnly cookies for future authentication and authorization
        purposes.

        This functionality ensures a secure and efficient login process for users,
        providing them with an access token that can be used to authenticate subsequent
        API requests.

        By securely storing the access token in browser cookies, the endpoint enables
        automatic inclusion of the access token in future API requests, eliminating the
        need for users to manually manage and provide the token with each request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users/login",
            body=await async_maybe_transform(
                {
                    "password": password,
                    "username": username,
                },
                authentication_login_params.AuthenticationLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationLoginResponse,
        )

    async def logout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationLogoutResponse:
        """
        The API endpoint is responsible for logging out users from the application and
        destroying the access token cookies stored on the client-side.

        When accessing this endpoint, it triggers the logout process, revoking the
        user's authentication and terminating their active session.

        Additionally, it ensures that any access token cookies associated with the
        user's session are removed from the client's browser, effectively logging them
        out from the application.
        """
        return await self._post(
            "/users/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationLogoutResponse,
        )

    async def register(
        self,
        *,
        email: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        role: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationRegisterResponse:
        """
        The API endpoint allows users to register or signup to create their accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users/register",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "role": role,
                    "username": username,
                },
                authentication_register_params.AuthenticationRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationRegisterResponse,
        )

    async def verify_email(
        self,
        verification_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationVerifyEmailResponse:
        """
        The API endpoint is used to verify a user's email by accessing the verification
        token (**verificationToken**) included in the path variable.

        When the user clicks on the email verification link provided to them, this API
        is invoked to validate their email address.

        By including the verification token in the URL path, the endpoint confirms the
        authenticity of the token and marks the user's email as verified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_token:
            raise ValueError(f"Expected a non-empty value for `verification_token` but received {verification_token!r}")
        return await self._get(
            f"/users/verify-email/{verification_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationVerifyEmailResponse,
        )


class AuthenticationsResourceWithRawResponse:
    def __init__(self, authentications: AuthenticationsResource) -> None:
        self._authentications = authentications

        self.current_user = to_raw_response_wrapper(
            authentications.current_user,
        )
        self.github_callback = to_raw_response_wrapper(
            authentications.github_callback,
        )
        self.github_redirect = to_raw_response_wrapper(
            authentications.github_redirect,
        )
        self.google_callback = to_raw_response_wrapper(
            authentications.google_callback,
        )
        self.google_redirect = to_raw_response_wrapper(
            authentications.google_redirect,
        )
        self.login = to_raw_response_wrapper(
            authentications.login,
        )
        self.logout = to_raw_response_wrapper(
            authentications.logout,
        )
        self.register = to_raw_response_wrapper(
            authentications.register,
        )
        self.verify_email = to_raw_response_wrapper(
            authentications.verify_email,
        )


class AsyncAuthenticationsResourceWithRawResponse:
    def __init__(self, authentications: AsyncAuthenticationsResource) -> None:
        self._authentications = authentications

        self.current_user = async_to_raw_response_wrapper(
            authentications.current_user,
        )
        self.github_callback = async_to_raw_response_wrapper(
            authentications.github_callback,
        )
        self.github_redirect = async_to_raw_response_wrapper(
            authentications.github_redirect,
        )
        self.google_callback = async_to_raw_response_wrapper(
            authentications.google_callback,
        )
        self.google_redirect = async_to_raw_response_wrapper(
            authentications.google_redirect,
        )
        self.login = async_to_raw_response_wrapper(
            authentications.login,
        )
        self.logout = async_to_raw_response_wrapper(
            authentications.logout,
        )
        self.register = async_to_raw_response_wrapper(
            authentications.register,
        )
        self.verify_email = async_to_raw_response_wrapper(
            authentications.verify_email,
        )


class AuthenticationsResourceWithStreamingResponse:
    def __init__(self, authentications: AuthenticationsResource) -> None:
        self._authentications = authentications

        self.current_user = to_streamed_response_wrapper(
            authentications.current_user,
        )
        self.github_callback = to_streamed_response_wrapper(
            authentications.github_callback,
        )
        self.github_redirect = to_streamed_response_wrapper(
            authentications.github_redirect,
        )
        self.google_callback = to_streamed_response_wrapper(
            authentications.google_callback,
        )
        self.google_redirect = to_streamed_response_wrapper(
            authentications.google_redirect,
        )
        self.login = to_streamed_response_wrapper(
            authentications.login,
        )
        self.logout = to_streamed_response_wrapper(
            authentications.logout,
        )
        self.register = to_streamed_response_wrapper(
            authentications.register,
        )
        self.verify_email = to_streamed_response_wrapper(
            authentications.verify_email,
        )


class AsyncAuthenticationsResourceWithStreamingResponse:
    def __init__(self, authentications: AsyncAuthenticationsResource) -> None:
        self._authentications = authentications

        self.current_user = async_to_streamed_response_wrapper(
            authentications.current_user,
        )
        self.github_callback = async_to_streamed_response_wrapper(
            authentications.github_callback,
        )
        self.github_redirect = async_to_streamed_response_wrapper(
            authentications.github_redirect,
        )
        self.google_callback = async_to_streamed_response_wrapper(
            authentications.google_callback,
        )
        self.google_redirect = async_to_streamed_response_wrapper(
            authentications.google_redirect,
        )
        self.login = async_to_streamed_response_wrapper(
            authentications.login,
        )
        self.logout = async_to_streamed_response_wrapper(
            authentications.logout,
        )
        self.register = async_to_streamed_response_wrapper(
            authentications.register,
        )
        self.verify_email = async_to_streamed_response_wrapper(
            authentications.verify_email,
        )
