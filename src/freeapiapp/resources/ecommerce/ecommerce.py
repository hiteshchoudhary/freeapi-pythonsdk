# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cart import (
    CartResource,
    AsyncCartResource,
    CartResourceWithRawResponse,
    AsyncCartResourceWithRawResponse,
    CartResourceWithStreamingResponse,
    AsyncCartResourceWithStreamingResponse,
)
from .orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
)
from .coupons import (
    CouponsResource,
    AsyncCouponsResource,
    CouponsResourceWithRawResponse,
    AsyncCouponsResourceWithRawResponse,
    CouponsResourceWithStreamingResponse,
    AsyncCouponsResourceWithStreamingResponse,
)
from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .addresses import (
    AddressesResource,
    AsyncAddressesResource,
    AddressesResourceWithRawResponse,
    AsyncAddressesResourceWithRawResponse,
    AddressesResourceWithStreamingResponse,
    AsyncAddressesResourceWithStreamingResponse,
)
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .orders.orders import OrdersResource, AsyncOrdersResource
from .coupons.coupons import CouponsResource, AsyncCouponsResource
from .profile.profile import ProfileResource, AsyncProfileResource

__all__ = ["EcommerceResource", "AsyncEcommerceResource"]


class EcommerceResource(SyncAPIResource):
    @cached_property
    def profile(self) -> ProfileResource:
        return ProfileResource(self._client)

    @cached_property
    def cart(self) -> CartResource:
        return CartResource(self._client)

    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def coupons(self) -> CouponsResource:
        return CouponsResource(self._client)

    @cached_property
    def addresses(self) -> AddressesResource:
        return AddressesResource(self._client)

    @cached_property
    def orders(self) -> OrdersResource:
        return OrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> EcommerceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return EcommerceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EcommerceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return EcommerceResourceWithStreamingResponse(self)


class AsyncEcommerceResource(AsyncAPIResource):
    @cached_property
    def profile(self) -> AsyncProfileResource:
        return AsyncProfileResource(self._client)

    @cached_property
    def cart(self) -> AsyncCartResource:
        return AsyncCartResource(self._client)

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def coupons(self) -> AsyncCouponsResource:
        return AsyncCouponsResource(self._client)

    @cached_property
    def addresses(self) -> AsyncAddressesResource:
        return AsyncAddressesResource(self._client)

    @cached_property
    def orders(self) -> AsyncOrdersResource:
        return AsyncOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEcommerceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEcommerceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEcommerceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncEcommerceResourceWithStreamingResponse(self)


class EcommerceResourceWithRawResponse:
    def __init__(self, ecommerce: EcommerceResource) -> None:
        self._ecommerce = ecommerce

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        return ProfileResourceWithRawResponse(self._ecommerce.profile)

    @cached_property
    def cart(self) -> CartResourceWithRawResponse:
        return CartResourceWithRawResponse(self._ecommerce.cart)

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._ecommerce.categories)

    @cached_property
    def coupons(self) -> CouponsResourceWithRawResponse:
        return CouponsResourceWithRawResponse(self._ecommerce.coupons)

    @cached_property
    def addresses(self) -> AddressesResourceWithRawResponse:
        return AddressesResourceWithRawResponse(self._ecommerce.addresses)

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        return OrdersResourceWithRawResponse(self._ecommerce.orders)


class AsyncEcommerceResourceWithRawResponse:
    def __init__(self, ecommerce: AsyncEcommerceResource) -> None:
        self._ecommerce = ecommerce

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        return AsyncProfileResourceWithRawResponse(self._ecommerce.profile)

    @cached_property
    def cart(self) -> AsyncCartResourceWithRawResponse:
        return AsyncCartResourceWithRawResponse(self._ecommerce.cart)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._ecommerce.categories)

    @cached_property
    def coupons(self) -> AsyncCouponsResourceWithRawResponse:
        return AsyncCouponsResourceWithRawResponse(self._ecommerce.coupons)

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithRawResponse:
        return AsyncAddressesResourceWithRawResponse(self._ecommerce.addresses)

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        return AsyncOrdersResourceWithRawResponse(self._ecommerce.orders)


class EcommerceResourceWithStreamingResponse:
    def __init__(self, ecommerce: EcommerceResource) -> None:
        self._ecommerce = ecommerce

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        return ProfileResourceWithStreamingResponse(self._ecommerce.profile)

    @cached_property
    def cart(self) -> CartResourceWithStreamingResponse:
        return CartResourceWithStreamingResponse(self._ecommerce.cart)

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._ecommerce.categories)

    @cached_property
    def coupons(self) -> CouponsResourceWithStreamingResponse:
        return CouponsResourceWithStreamingResponse(self._ecommerce.coupons)

    @cached_property
    def addresses(self) -> AddressesResourceWithStreamingResponse:
        return AddressesResourceWithStreamingResponse(self._ecommerce.addresses)

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        return OrdersResourceWithStreamingResponse(self._ecommerce.orders)


class AsyncEcommerceResourceWithStreamingResponse:
    def __init__(self, ecommerce: AsyncEcommerceResource) -> None:
        self._ecommerce = ecommerce

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        return AsyncProfileResourceWithStreamingResponse(self._ecommerce.profile)

    @cached_property
    def cart(self) -> AsyncCartResourceWithStreamingResponse:
        return AsyncCartResourceWithStreamingResponse(self._ecommerce.cart)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._ecommerce.categories)

    @cached_property
    def coupons(self) -> AsyncCouponsResourceWithStreamingResponse:
        return AsyncCouponsResourceWithStreamingResponse(self._ecommerce.coupons)

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithStreamingResponse:
        return AsyncAddressesResourceWithStreamingResponse(self._ecommerce.addresses)

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        return AsyncOrdersResourceWithStreamingResponse(self._ecommerce.orders)
