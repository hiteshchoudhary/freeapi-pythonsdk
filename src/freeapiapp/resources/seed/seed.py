# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .todos import (
    TodosResource,
    AsyncTodosResource,
    TodosResourceWithRawResponse,
    AsyncTodosResourceWithRawResponse,
    TodosResourceWithStreamingResponse,
    AsyncTodosResourceWithStreamingResponse,
)
from .chat_app import (
    ChatAppResource,
    AsyncChatAppResource,
    ChatAppResourceWithRawResponse,
    AsyncChatAppResourceWithRawResponse,
    ChatAppResourceWithStreamingResponse,
    AsyncChatAppResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .ecommerce import (
    EcommerceResource,
    AsyncEcommerceResource,
    EcommerceResourceWithRawResponse,
    AsyncEcommerceResourceWithRawResponse,
    EcommerceResourceWithStreamingResponse,
    AsyncEcommerceResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .social_media import (
    SocialMediaResource,
    AsyncSocialMediaResource,
    SocialMediaResourceWithRawResponse,
    AsyncSocialMediaResourceWithRawResponse,
    SocialMediaResourceWithStreamingResponse,
    AsyncSocialMediaResourceWithStreamingResponse,
)
from .generated_credentials import (
    GeneratedCredentialsResource,
    AsyncGeneratedCredentialsResource,
    GeneratedCredentialsResourceWithRawResponse,
    AsyncGeneratedCredentialsResourceWithRawResponse,
    GeneratedCredentialsResourceWithStreamingResponse,
    AsyncGeneratedCredentialsResourceWithStreamingResponse,
)

__all__ = ["SeedResource", "AsyncSeedResource"]


class SeedResource(SyncAPIResource):
    @cached_property
    def generated_credentials(self) -> GeneratedCredentialsResource:
        return GeneratedCredentialsResource(self._client)

    @cached_property
    def todos(self) -> TodosResource:
        return TodosResource(self._client)

    @cached_property
    def ecommerce(self) -> EcommerceResource:
        return EcommerceResource(self._client)

    @cached_property
    def social_media(self) -> SocialMediaResource:
        return SocialMediaResource(self._client)

    @cached_property
    def chat_app(self) -> ChatAppResource:
        return ChatAppResource(self._client)

    @cached_property
    def with_raw_response(self) -> SeedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return SeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return SeedResourceWithStreamingResponse(self)


class AsyncSeedResource(AsyncAPIResource):
    @cached_property
    def generated_credentials(self) -> AsyncGeneratedCredentialsResource:
        return AsyncGeneratedCredentialsResource(self._client)

    @cached_property
    def todos(self) -> AsyncTodosResource:
        return AsyncTodosResource(self._client)

    @cached_property
    def ecommerce(self) -> AsyncEcommerceResource:
        return AsyncEcommerceResource(self._client)

    @cached_property
    def social_media(self) -> AsyncSocialMediaResource:
        return AsyncSocialMediaResource(self._client)

    @cached_property
    def chat_app(self) -> AsyncChatAppResource:
        return AsyncChatAppResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSeedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncSeedResourceWithStreamingResponse(self)


class SeedResourceWithRawResponse:
    def __init__(self, seed: SeedResource) -> None:
        self._seed = seed

    @cached_property
    def generated_credentials(self) -> GeneratedCredentialsResourceWithRawResponse:
        return GeneratedCredentialsResourceWithRawResponse(self._seed.generated_credentials)

    @cached_property
    def todos(self) -> TodosResourceWithRawResponse:
        return TodosResourceWithRawResponse(self._seed.todos)

    @cached_property
    def ecommerce(self) -> EcommerceResourceWithRawResponse:
        return EcommerceResourceWithRawResponse(self._seed.ecommerce)

    @cached_property
    def social_media(self) -> SocialMediaResourceWithRawResponse:
        return SocialMediaResourceWithRawResponse(self._seed.social_media)

    @cached_property
    def chat_app(self) -> ChatAppResourceWithRawResponse:
        return ChatAppResourceWithRawResponse(self._seed.chat_app)


class AsyncSeedResourceWithRawResponse:
    def __init__(self, seed: AsyncSeedResource) -> None:
        self._seed = seed

    @cached_property
    def generated_credentials(self) -> AsyncGeneratedCredentialsResourceWithRawResponse:
        return AsyncGeneratedCredentialsResourceWithRawResponse(self._seed.generated_credentials)

    @cached_property
    def todos(self) -> AsyncTodosResourceWithRawResponse:
        return AsyncTodosResourceWithRawResponse(self._seed.todos)

    @cached_property
    def ecommerce(self) -> AsyncEcommerceResourceWithRawResponse:
        return AsyncEcommerceResourceWithRawResponse(self._seed.ecommerce)

    @cached_property
    def social_media(self) -> AsyncSocialMediaResourceWithRawResponse:
        return AsyncSocialMediaResourceWithRawResponse(self._seed.social_media)

    @cached_property
    def chat_app(self) -> AsyncChatAppResourceWithRawResponse:
        return AsyncChatAppResourceWithRawResponse(self._seed.chat_app)


class SeedResourceWithStreamingResponse:
    def __init__(self, seed: SeedResource) -> None:
        self._seed = seed

    @cached_property
    def generated_credentials(self) -> GeneratedCredentialsResourceWithStreamingResponse:
        return GeneratedCredentialsResourceWithStreamingResponse(self._seed.generated_credentials)

    @cached_property
    def todos(self) -> TodosResourceWithStreamingResponse:
        return TodosResourceWithStreamingResponse(self._seed.todos)

    @cached_property
    def ecommerce(self) -> EcommerceResourceWithStreamingResponse:
        return EcommerceResourceWithStreamingResponse(self._seed.ecommerce)

    @cached_property
    def social_media(self) -> SocialMediaResourceWithStreamingResponse:
        return SocialMediaResourceWithStreamingResponse(self._seed.social_media)

    @cached_property
    def chat_app(self) -> ChatAppResourceWithStreamingResponse:
        return ChatAppResourceWithStreamingResponse(self._seed.chat_app)


class AsyncSeedResourceWithStreamingResponse:
    def __init__(self, seed: AsyncSeedResource) -> None:
        self._seed = seed

    @cached_property
    def generated_credentials(self) -> AsyncGeneratedCredentialsResourceWithStreamingResponse:
        return AsyncGeneratedCredentialsResourceWithStreamingResponse(self._seed.generated_credentials)

    @cached_property
    def todos(self) -> AsyncTodosResourceWithStreamingResponse:
        return AsyncTodosResourceWithStreamingResponse(self._seed.todos)

    @cached_property
    def ecommerce(self) -> AsyncEcommerceResourceWithStreamingResponse:
        return AsyncEcommerceResourceWithStreamingResponse(self._seed.ecommerce)

    @cached_property
    def social_media(self) -> AsyncSocialMediaResourceWithStreamingResponse:
        return AsyncSocialMediaResourceWithStreamingResponse(self._seed.social_media)

    @cached_property
    def chat_app(self) -> AsyncChatAppResourceWithStreamingResponse:
        return AsyncChatAppResourceWithStreamingResponse(self._seed.chat_app)
