# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Freeapiapp",
    "AsyncFreeapiapp",
    "Client",
    "AsyncClient",
]


class Freeapiapp(SyncAPIClient):
    public: resources.PublicResource
    kitchen_sink: resources.KitchenSinkResource
    kitchen_sinks: resources.KitchenSinksResource
    authentications: resources.AuthenticationsResource
    users: resources.UsersResource
    ecommerce: resources.EcommerceResource
    products: resources.ProductsResource
    cart: resources.CartResource
    todos: resources.TodosResource
    social_media: resources.SocialMediaResource
    chat_app: resources.ChatAppResource
    chats: resources.ChatsResource
    messages: resources.MessagesResource
    seed: resources.SeedResource
    reset_db: resources.ResetDBResource
    healthcheck: resources.HealthcheckResource
    with_raw_response: FreeapiappWithRawResponse
    with_streaming_response: FreeapiappWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous freeapiapp client instance."""
        if base_url is None:
            base_url = os.environ.get("FREEAPIAPP_BASE_URL")
        if base_url is None:
            base_url = f"https://api.freeapi.app/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.public = resources.PublicResource(self)
        self.kitchen_sink = resources.KitchenSinkResource(self)
        self.kitchen_sinks = resources.KitchenSinksResource(self)
        self.authentications = resources.AuthenticationsResource(self)
        self.users = resources.UsersResource(self)
        self.ecommerce = resources.EcommerceResource(self)
        self.products = resources.ProductsResource(self)
        self.cart = resources.CartResource(self)
        self.todos = resources.TodosResource(self)
        self.social_media = resources.SocialMediaResource(self)
        self.chat_app = resources.ChatAppResource(self)
        self.chats = resources.ChatsResource(self)
        self.messages = resources.MessagesResource(self)
        self.seed = resources.SeedResource(self)
        self.reset_db = resources.ResetDBResource(self)
        self.healthcheck = resources.HealthcheckResource(self)
        self.with_raw_response = FreeapiappWithRawResponse(self)
        self.with_streaming_response = FreeapiappWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncFreeapiapp(AsyncAPIClient):
    public: resources.AsyncPublicResource
    kitchen_sink: resources.AsyncKitchenSinkResource
    kitchen_sinks: resources.AsyncKitchenSinksResource
    authentications: resources.AsyncAuthenticationsResource
    users: resources.AsyncUsersResource
    ecommerce: resources.AsyncEcommerceResource
    products: resources.AsyncProductsResource
    cart: resources.AsyncCartResource
    todos: resources.AsyncTodosResource
    social_media: resources.AsyncSocialMediaResource
    chat_app: resources.AsyncChatAppResource
    chats: resources.AsyncChatsResource
    messages: resources.AsyncMessagesResource
    seed: resources.AsyncSeedResource
    reset_db: resources.AsyncResetDBResource
    healthcheck: resources.AsyncHealthcheckResource
    with_raw_response: AsyncFreeapiappWithRawResponse
    with_streaming_response: AsyncFreeapiappWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async freeapiapp client instance."""
        if base_url is None:
            base_url = os.environ.get("FREEAPIAPP_BASE_URL")
        if base_url is None:
            base_url = f"https://api.freeapi.app/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.public = resources.AsyncPublicResource(self)
        self.kitchen_sink = resources.AsyncKitchenSinkResource(self)
        self.kitchen_sinks = resources.AsyncKitchenSinksResource(self)
        self.authentications = resources.AsyncAuthenticationsResource(self)
        self.users = resources.AsyncUsersResource(self)
        self.ecommerce = resources.AsyncEcommerceResource(self)
        self.products = resources.AsyncProductsResource(self)
        self.cart = resources.AsyncCartResource(self)
        self.todos = resources.AsyncTodosResource(self)
        self.social_media = resources.AsyncSocialMediaResource(self)
        self.chat_app = resources.AsyncChatAppResource(self)
        self.chats = resources.AsyncChatsResource(self)
        self.messages = resources.AsyncMessagesResource(self)
        self.seed = resources.AsyncSeedResource(self)
        self.reset_db = resources.AsyncResetDBResource(self)
        self.healthcheck = resources.AsyncHealthcheckResource(self)
        self.with_raw_response = AsyncFreeapiappWithRawResponse(self)
        self.with_streaming_response = AsyncFreeapiappWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class FreeapiappWithRawResponse:
    def __init__(self, client: Freeapiapp) -> None:
        self.public = resources.PublicResourceWithRawResponse(client.public)
        self.kitchen_sink = resources.KitchenSinkResourceWithRawResponse(client.kitchen_sink)
        self.kitchen_sinks = resources.KitchenSinksResourceWithRawResponse(client.kitchen_sinks)
        self.authentications = resources.AuthenticationsResourceWithRawResponse(client.authentications)
        self.users = resources.UsersResourceWithRawResponse(client.users)
        self.ecommerce = resources.EcommerceResourceWithRawResponse(client.ecommerce)
        self.products = resources.ProductsResourceWithRawResponse(client.products)
        self.cart = resources.CartResourceWithRawResponse(client.cart)
        self.todos = resources.TodosResourceWithRawResponse(client.todos)
        self.social_media = resources.SocialMediaResourceWithRawResponse(client.social_media)
        self.chat_app = resources.ChatAppResourceWithRawResponse(client.chat_app)
        self.chats = resources.ChatsResourceWithRawResponse(client.chats)
        self.messages = resources.MessagesResourceWithRawResponse(client.messages)
        self.seed = resources.SeedResourceWithRawResponse(client.seed)
        self.reset_db = resources.ResetDBResourceWithRawResponse(client.reset_db)
        self.healthcheck = resources.HealthcheckResourceWithRawResponse(client.healthcheck)


class AsyncFreeapiappWithRawResponse:
    def __init__(self, client: AsyncFreeapiapp) -> None:
        self.public = resources.AsyncPublicResourceWithRawResponse(client.public)
        self.kitchen_sink = resources.AsyncKitchenSinkResourceWithRawResponse(client.kitchen_sink)
        self.kitchen_sinks = resources.AsyncKitchenSinksResourceWithRawResponse(client.kitchen_sinks)
        self.authentications = resources.AsyncAuthenticationsResourceWithRawResponse(client.authentications)
        self.users = resources.AsyncUsersResourceWithRawResponse(client.users)
        self.ecommerce = resources.AsyncEcommerceResourceWithRawResponse(client.ecommerce)
        self.products = resources.AsyncProductsResourceWithRawResponse(client.products)
        self.cart = resources.AsyncCartResourceWithRawResponse(client.cart)
        self.todos = resources.AsyncTodosResourceWithRawResponse(client.todos)
        self.social_media = resources.AsyncSocialMediaResourceWithRawResponse(client.social_media)
        self.chat_app = resources.AsyncChatAppResourceWithRawResponse(client.chat_app)
        self.chats = resources.AsyncChatsResourceWithRawResponse(client.chats)
        self.messages = resources.AsyncMessagesResourceWithRawResponse(client.messages)
        self.seed = resources.AsyncSeedResourceWithRawResponse(client.seed)
        self.reset_db = resources.AsyncResetDBResourceWithRawResponse(client.reset_db)
        self.healthcheck = resources.AsyncHealthcheckResourceWithRawResponse(client.healthcheck)


class FreeapiappWithStreamedResponse:
    def __init__(self, client: Freeapiapp) -> None:
        self.public = resources.PublicResourceWithStreamingResponse(client.public)
        self.kitchen_sink = resources.KitchenSinkResourceWithStreamingResponse(client.kitchen_sink)
        self.kitchen_sinks = resources.KitchenSinksResourceWithStreamingResponse(client.kitchen_sinks)
        self.authentications = resources.AuthenticationsResourceWithStreamingResponse(client.authentications)
        self.users = resources.UsersResourceWithStreamingResponse(client.users)
        self.ecommerce = resources.EcommerceResourceWithStreamingResponse(client.ecommerce)
        self.products = resources.ProductsResourceWithStreamingResponse(client.products)
        self.cart = resources.CartResourceWithStreamingResponse(client.cart)
        self.todos = resources.TodosResourceWithStreamingResponse(client.todos)
        self.social_media = resources.SocialMediaResourceWithStreamingResponse(client.social_media)
        self.chat_app = resources.ChatAppResourceWithStreamingResponse(client.chat_app)
        self.chats = resources.ChatsResourceWithStreamingResponse(client.chats)
        self.messages = resources.MessagesResourceWithStreamingResponse(client.messages)
        self.seed = resources.SeedResourceWithStreamingResponse(client.seed)
        self.reset_db = resources.ResetDBResourceWithStreamingResponse(client.reset_db)
        self.healthcheck = resources.HealthcheckResourceWithStreamingResponse(client.healthcheck)


class AsyncFreeapiappWithStreamedResponse:
    def __init__(self, client: AsyncFreeapiapp) -> None:
        self.public = resources.AsyncPublicResourceWithStreamingResponse(client.public)
        self.kitchen_sink = resources.AsyncKitchenSinkResourceWithStreamingResponse(client.kitchen_sink)
        self.kitchen_sinks = resources.AsyncKitchenSinksResourceWithStreamingResponse(client.kitchen_sinks)
        self.authentications = resources.AsyncAuthenticationsResourceWithStreamingResponse(client.authentications)
        self.users = resources.AsyncUsersResourceWithStreamingResponse(client.users)
        self.ecommerce = resources.AsyncEcommerceResourceWithStreamingResponse(client.ecommerce)
        self.products = resources.AsyncProductsResourceWithStreamingResponse(client.products)
        self.cart = resources.AsyncCartResourceWithStreamingResponse(client.cart)
        self.todos = resources.AsyncTodosResourceWithStreamingResponse(client.todos)
        self.social_media = resources.AsyncSocialMediaResourceWithStreamingResponse(client.social_media)
        self.chat_app = resources.AsyncChatAppResourceWithStreamingResponse(client.chat_app)
        self.chats = resources.AsyncChatsResourceWithStreamingResponse(client.chats)
        self.messages = resources.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.seed = resources.AsyncSeedResourceWithStreamingResponse(client.seed)
        self.reset_db = resources.AsyncResetDBResourceWithStreamingResponse(client.reset_db)
        self.healthcheck = resources.AsyncHealthcheckResourceWithStreamingResponse(client.healthcheck)


Client = Freeapiapp

AsyncClient = AsyncFreeapiapp
