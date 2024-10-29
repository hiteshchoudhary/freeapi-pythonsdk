# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cats import (
    CatsResource,
    AsyncCatsResource,
    CatsResourceWithRawResponse,
    AsyncCatsResourceWithRawResponse,
    CatsResourceWithStreamingResponse,
    AsyncCatsResourceWithStreamingResponse,
)
from .dogs import (
    DogsResource,
    AsyncDogsResource,
    DogsResourceWithRawResponse,
    AsyncDogsResourceWithRawResponse,
    DogsResourceWithStreamingResponse,
    AsyncDogsResourceWithStreamingResponse,
)
from .books import (
    BooksResource,
    AsyncBooksResource,
    BooksResourceWithRawResponse,
    AsyncBooksResourceWithRawResponse,
    BooksResourceWithStreamingResponse,
    AsyncBooksResourceWithStreamingResponse,
)
from .meals import (
    MealsResource,
    AsyncMealsResource,
    MealsResourceWithRawResponse,
    AsyncMealsResourceWithRawResponse,
    MealsResourceWithStreamingResponse,
    AsyncMealsResourceWithStreamingResponse,
)
from .quotes import (
    QuotesResource,
    AsyncQuotesResource,
    QuotesResourceWithRawResponse,
    AsyncQuotesResourceWithRawResponse,
    QuotesResourceWithStreamingResponse,
    AsyncQuotesResourceWithStreamingResponse,
)
from .stocks import (
    StocksResource,
    AsyncStocksResource,
    StocksResourceWithRawResponse,
    AsyncStocksResourceWithRawResponse,
    StocksResourceWithStreamingResponse,
    AsyncStocksResourceWithStreamingResponse,
)
from .youtube import (
    YoutubeResource,
    AsyncYoutubeResource,
    YoutubeResourceWithRawResponse,
    AsyncYoutubeResourceWithRawResponse,
    YoutubeResourceWithStreamingResponse,
    AsyncYoutubeResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .cats.cats import CatsResource, AsyncCatsResource
from .dogs.dogs import DogsResource, AsyncDogsResource
from ..._resource import SyncAPIResource, AsyncAPIResource
from .meals.meals import MealsResource, AsyncMealsResource
from .random_jokes import (
    RandomJokesResource,
    AsyncRandomJokesResource,
    RandomJokesResourceWithRawResponse,
    AsyncRandomJokesResourceWithRawResponse,
    RandomJokesResourceWithStreamingResponse,
    AsyncRandomJokesResourceWithStreamingResponse,
)
from .random_users import (
    RandomUsersResource,
    AsyncRandomUsersResource,
    RandomUsersResourceWithRawResponse,
    AsyncRandomUsersResourceWithRawResponse,
    RandomUsersResourceWithStreamingResponse,
    AsyncRandomUsersResourceWithStreamingResponse,
)
from .random_products import (
    RandomProductsResource,
    AsyncRandomProductsResource,
    RandomProductsResourceWithRawResponse,
    AsyncRandomProductsResourceWithRawResponse,
    RandomProductsResourceWithStreamingResponse,
    AsyncRandomProductsResourceWithStreamingResponse,
)
from .youtube.youtube import YoutubeResource, AsyncYoutubeResource
from .random_jokes.random_jokes import RandomJokesResource, AsyncRandomJokesResource
from .random_users.random_users import RandomUsersResource, AsyncRandomUsersResource
from .random_products.random_products import RandomProductsResource, AsyncRandomProductsResource

__all__ = ["PublicResource", "AsyncPublicResource"]


class PublicResource(SyncAPIResource):
    @cached_property
    def random_users(self) -> RandomUsersResource:
        return RandomUsersResource(self._client)

    @cached_property
    def random_products(self) -> RandomProductsResource:
        return RandomProductsResource(self._client)

    @cached_property
    def random_jokes(self) -> RandomJokesResource:
        return RandomJokesResource(self._client)

    @cached_property
    def books(self) -> BooksResource:
        return BooksResource(self._client)

    @cached_property
    def stocks(self) -> StocksResource:
        return StocksResource(self._client)

    @cached_property
    def quotes(self) -> QuotesResource:
        return QuotesResource(self._client)

    @cached_property
    def meals(self) -> MealsResource:
        return MealsResource(self._client)

    @cached_property
    def dogs(self) -> DogsResource:
        return DogsResource(self._client)

    @cached_property
    def cats(self) -> CatsResource:
        return CatsResource(self._client)

    @cached_property
    def youtube(self) -> YoutubeResource:
        return YoutubeResource(self._client)

    @cached_property
    def with_raw_response(self) -> PublicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return PublicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return PublicResourceWithStreamingResponse(self)


class AsyncPublicResource(AsyncAPIResource):
    @cached_property
    def random_users(self) -> AsyncRandomUsersResource:
        return AsyncRandomUsersResource(self._client)

    @cached_property
    def random_products(self) -> AsyncRandomProductsResource:
        return AsyncRandomProductsResource(self._client)

    @cached_property
    def random_jokes(self) -> AsyncRandomJokesResource:
        return AsyncRandomJokesResource(self._client)

    @cached_property
    def books(self) -> AsyncBooksResource:
        return AsyncBooksResource(self._client)

    @cached_property
    def stocks(self) -> AsyncStocksResource:
        return AsyncStocksResource(self._client)

    @cached_property
    def quotes(self) -> AsyncQuotesResource:
        return AsyncQuotesResource(self._client)

    @cached_property
    def meals(self) -> AsyncMealsResource:
        return AsyncMealsResource(self._client)

    @cached_property
    def dogs(self) -> AsyncDogsResource:
        return AsyncDogsResource(self._client)

    @cached_property
    def cats(self) -> AsyncCatsResource:
        return AsyncCatsResource(self._client)

    @cached_property
    def youtube(self) -> AsyncYoutubeResource:
        return AsyncYoutubeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPublicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/freeapiapp-python#with_streaming_response
        """
        return AsyncPublicResourceWithStreamingResponse(self)


class PublicResourceWithRawResponse:
    def __init__(self, public: PublicResource) -> None:
        self._public = public

    @cached_property
    def random_users(self) -> RandomUsersResourceWithRawResponse:
        return RandomUsersResourceWithRawResponse(self._public.random_users)

    @cached_property
    def random_products(self) -> RandomProductsResourceWithRawResponse:
        return RandomProductsResourceWithRawResponse(self._public.random_products)

    @cached_property
    def random_jokes(self) -> RandomJokesResourceWithRawResponse:
        return RandomJokesResourceWithRawResponse(self._public.random_jokes)

    @cached_property
    def books(self) -> BooksResourceWithRawResponse:
        return BooksResourceWithRawResponse(self._public.books)

    @cached_property
    def stocks(self) -> StocksResourceWithRawResponse:
        return StocksResourceWithRawResponse(self._public.stocks)

    @cached_property
    def quotes(self) -> QuotesResourceWithRawResponse:
        return QuotesResourceWithRawResponse(self._public.quotes)

    @cached_property
    def meals(self) -> MealsResourceWithRawResponse:
        return MealsResourceWithRawResponse(self._public.meals)

    @cached_property
    def dogs(self) -> DogsResourceWithRawResponse:
        return DogsResourceWithRawResponse(self._public.dogs)

    @cached_property
    def cats(self) -> CatsResourceWithRawResponse:
        return CatsResourceWithRawResponse(self._public.cats)

    @cached_property
    def youtube(self) -> YoutubeResourceWithRawResponse:
        return YoutubeResourceWithRawResponse(self._public.youtube)


class AsyncPublicResourceWithRawResponse:
    def __init__(self, public: AsyncPublicResource) -> None:
        self._public = public

    @cached_property
    def random_users(self) -> AsyncRandomUsersResourceWithRawResponse:
        return AsyncRandomUsersResourceWithRawResponse(self._public.random_users)

    @cached_property
    def random_products(self) -> AsyncRandomProductsResourceWithRawResponse:
        return AsyncRandomProductsResourceWithRawResponse(self._public.random_products)

    @cached_property
    def random_jokes(self) -> AsyncRandomJokesResourceWithRawResponse:
        return AsyncRandomJokesResourceWithRawResponse(self._public.random_jokes)

    @cached_property
    def books(self) -> AsyncBooksResourceWithRawResponse:
        return AsyncBooksResourceWithRawResponse(self._public.books)

    @cached_property
    def stocks(self) -> AsyncStocksResourceWithRawResponse:
        return AsyncStocksResourceWithRawResponse(self._public.stocks)

    @cached_property
    def quotes(self) -> AsyncQuotesResourceWithRawResponse:
        return AsyncQuotesResourceWithRawResponse(self._public.quotes)

    @cached_property
    def meals(self) -> AsyncMealsResourceWithRawResponse:
        return AsyncMealsResourceWithRawResponse(self._public.meals)

    @cached_property
    def dogs(self) -> AsyncDogsResourceWithRawResponse:
        return AsyncDogsResourceWithRawResponse(self._public.dogs)

    @cached_property
    def cats(self) -> AsyncCatsResourceWithRawResponse:
        return AsyncCatsResourceWithRawResponse(self._public.cats)

    @cached_property
    def youtube(self) -> AsyncYoutubeResourceWithRawResponse:
        return AsyncYoutubeResourceWithRawResponse(self._public.youtube)


class PublicResourceWithStreamingResponse:
    def __init__(self, public: PublicResource) -> None:
        self._public = public

    @cached_property
    def random_users(self) -> RandomUsersResourceWithStreamingResponse:
        return RandomUsersResourceWithStreamingResponse(self._public.random_users)

    @cached_property
    def random_products(self) -> RandomProductsResourceWithStreamingResponse:
        return RandomProductsResourceWithStreamingResponse(self._public.random_products)

    @cached_property
    def random_jokes(self) -> RandomJokesResourceWithStreamingResponse:
        return RandomJokesResourceWithStreamingResponse(self._public.random_jokes)

    @cached_property
    def books(self) -> BooksResourceWithStreamingResponse:
        return BooksResourceWithStreamingResponse(self._public.books)

    @cached_property
    def stocks(self) -> StocksResourceWithStreamingResponse:
        return StocksResourceWithStreamingResponse(self._public.stocks)

    @cached_property
    def quotes(self) -> QuotesResourceWithStreamingResponse:
        return QuotesResourceWithStreamingResponse(self._public.quotes)

    @cached_property
    def meals(self) -> MealsResourceWithStreamingResponse:
        return MealsResourceWithStreamingResponse(self._public.meals)

    @cached_property
    def dogs(self) -> DogsResourceWithStreamingResponse:
        return DogsResourceWithStreamingResponse(self._public.dogs)

    @cached_property
    def cats(self) -> CatsResourceWithStreamingResponse:
        return CatsResourceWithStreamingResponse(self._public.cats)

    @cached_property
    def youtube(self) -> YoutubeResourceWithStreamingResponse:
        return YoutubeResourceWithStreamingResponse(self._public.youtube)


class AsyncPublicResourceWithStreamingResponse:
    def __init__(self, public: AsyncPublicResource) -> None:
        self._public = public

    @cached_property
    def random_users(self) -> AsyncRandomUsersResourceWithStreamingResponse:
        return AsyncRandomUsersResourceWithStreamingResponse(self._public.random_users)

    @cached_property
    def random_products(self) -> AsyncRandomProductsResourceWithStreamingResponse:
        return AsyncRandomProductsResourceWithStreamingResponse(self._public.random_products)

    @cached_property
    def random_jokes(self) -> AsyncRandomJokesResourceWithStreamingResponse:
        return AsyncRandomJokesResourceWithStreamingResponse(self._public.random_jokes)

    @cached_property
    def books(self) -> AsyncBooksResourceWithStreamingResponse:
        return AsyncBooksResourceWithStreamingResponse(self._public.books)

    @cached_property
    def stocks(self) -> AsyncStocksResourceWithStreamingResponse:
        return AsyncStocksResourceWithStreamingResponse(self._public.stocks)

    @cached_property
    def quotes(self) -> AsyncQuotesResourceWithStreamingResponse:
        return AsyncQuotesResourceWithStreamingResponse(self._public.quotes)

    @cached_property
    def meals(self) -> AsyncMealsResourceWithStreamingResponse:
        return AsyncMealsResourceWithStreamingResponse(self._public.meals)

    @cached_property
    def dogs(self) -> AsyncDogsResourceWithStreamingResponse:
        return AsyncDogsResourceWithStreamingResponse(self._public.dogs)

    @cached_property
    def cats(self) -> AsyncCatsResourceWithStreamingResponse:
        return AsyncCatsResourceWithStreamingResponse(self._public.cats)

    @cached_property
    def youtube(self) -> AsyncYoutubeResourceWithStreamingResponse:
        return AsyncYoutubeResourceWithStreamingResponse(self._public.youtube)
