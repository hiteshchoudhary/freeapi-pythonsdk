# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.kitchen_sink.http_method_get_response import HTTPMethodGetResponse
from ...types.kitchen_sink.http_method_put_response import HTTPMethodPutResponse
from ...types.kitchen_sink.http_method_create_response import HTTPMethodCreateResponse
from ...types.kitchen_sink.http_method_delete_response import HTTPMethodDeleteResponse
from ...types.kitchen_sink.http_method_update_response import HTTPMethodUpdateResponse

__all__ = ["HTTPMethodsResource", "AsyncHTTPMethodsResource"]


class HTTPMethodsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HTTPMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return HTTPMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTPMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return HTTPMethodsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPMethodCreateResponse:
        """
        The `POST` method is used to submit data to be processed by the server.

        It typically results in the creation of a new resource on the server.

        `POST` requests are **not idempotent** as each request creates a new resource,
        and subsequent identical requests may result in multiple resources being
        created.

        **Typical Usage:**

        `POST` requests are commonly used for operations that create new resources or
        trigger specific actions on the server.

        _**For example,**_

        creating a new user account, submitting a form, or making a purchase.
        """
        return self._post(
            "/kitchen-sink/http-methods/post",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPMethodCreateResponse,
        )

    def update(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPMethodUpdateResponse:
        """
        The `PATCH` method is used to partially update an existing resource on the
        server.

        Unlike `PUT`, `PATCH` only includes the changes that need to be made, rather
        than sending the entire resource representation.

        It allows for modifying specific fields or properties of a resource.

        **Typical Usage:**

        PATCH requests are commonly used to make partial updates to a resource.

        _**For example,**_

        updating only the email address of a user, modifying specific attributes of an
        object, or applying incremental changes to a document.
        """
        return self._patch(
            "/kitchen-sink/http-methods/patch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPMethodUpdateResponse,
        )

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPMethodDeleteResponse:
        """
        The `DELETE` method is used to remove or delete a specific resource on the
        server.

        It instructs the server to remove the identified resource, resulting in its
        permanent deletion.

        **Typical Usage:**

        `DELETE` requests are commonly used to delete a resource from the server.

        _**For example,**_

        deleting a user account, removing an item from a cart, or deleting a specific
        record from a database.
        """
        return self._delete(
            "/kitchen-sink/http-methods/delete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPMethodDeleteResponse,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPMethodGetResponse:
        """
        The `GET` method is used to retrieve or fetch a representation of a resource
        from a server.

        It is a **safe** and **idempotent** operation, meaning it should not have any
        side effects on the server's data.

        `GET` requests are read-only and should not modify the state of the server or
        its resources.

        **Typical Usage:** `GET` requests are commonly used to retrieve data from a
        server.

        _**For example,**_

        fetching a user's profile information, retrieving a list of products, or
        fetching specific data based on query parameters.
        """
        return self._get(
            "/kitchen-sink/http-methods/get",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPMethodGetResponse,
        )

    def put(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPMethodPutResponse:
        """
        The `PUT` method is used to update or replace an existing resource on the
        server.

        It sends the entire representation of the resource in the request payload,
        replacing the existing resource entirely.

        If the resource does not exist, `PUT` can also be used to create a new resource
        with a specific identifier.

        **Typical Usage:** `PUT` requests are commonly used to update or replace an
        entire resource on the server.

        _**For example,**_

        updating a user's profile information, replacing a document, or modifying an
        existing record.
        """
        return self._put(
            "/kitchen-sink/http-methods/put",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPMethodPutResponse,
        )


class AsyncHTTPMethodsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHTTPMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncHTTPMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTPMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncHTTPMethodsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPMethodCreateResponse:
        """
        The `POST` method is used to submit data to be processed by the server.

        It typically results in the creation of a new resource on the server.

        `POST` requests are **not idempotent** as each request creates a new resource,
        and subsequent identical requests may result in multiple resources being
        created.

        **Typical Usage:**

        `POST` requests are commonly used for operations that create new resources or
        trigger specific actions on the server.

        _**For example,**_

        creating a new user account, submitting a form, or making a purchase.
        """
        return await self._post(
            "/kitchen-sink/http-methods/post",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPMethodCreateResponse,
        )

    async def update(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPMethodUpdateResponse:
        """
        The `PATCH` method is used to partially update an existing resource on the
        server.

        Unlike `PUT`, `PATCH` only includes the changes that need to be made, rather
        than sending the entire resource representation.

        It allows for modifying specific fields or properties of a resource.

        **Typical Usage:**

        PATCH requests are commonly used to make partial updates to a resource.

        _**For example,**_

        updating only the email address of a user, modifying specific attributes of an
        object, or applying incremental changes to a document.
        """
        return await self._patch(
            "/kitchen-sink/http-methods/patch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPMethodUpdateResponse,
        )

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPMethodDeleteResponse:
        """
        The `DELETE` method is used to remove or delete a specific resource on the
        server.

        It instructs the server to remove the identified resource, resulting in its
        permanent deletion.

        **Typical Usage:**

        `DELETE` requests are commonly used to delete a resource from the server.

        _**For example,**_

        deleting a user account, removing an item from a cart, or deleting a specific
        record from a database.
        """
        return await self._delete(
            "/kitchen-sink/http-methods/delete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPMethodDeleteResponse,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPMethodGetResponse:
        """
        The `GET` method is used to retrieve or fetch a representation of a resource
        from a server.

        It is a **safe** and **idempotent** operation, meaning it should not have any
        side effects on the server's data.

        `GET` requests are read-only and should not modify the state of the server or
        its resources.

        **Typical Usage:** `GET` requests are commonly used to retrieve data from a
        server.

        _**For example,**_

        fetching a user's profile information, retrieving a list of products, or
        fetching specific data based on query parameters.
        """
        return await self._get(
            "/kitchen-sink/http-methods/get",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPMethodGetResponse,
        )

    async def put(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HTTPMethodPutResponse:
        """
        The `PUT` method is used to update or replace an existing resource on the
        server.

        It sends the entire representation of the resource in the request payload,
        replacing the existing resource entirely.

        If the resource does not exist, `PUT` can also be used to create a new resource
        with a specific identifier.

        **Typical Usage:** `PUT` requests are commonly used to update or replace an
        entire resource on the server.

        _**For example,**_

        updating a user's profile information, replacing a document, or modifying an
        existing record.
        """
        return await self._put(
            "/kitchen-sink/http-methods/put",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HTTPMethodPutResponse,
        )


class HTTPMethodsResourceWithRawResponse:
    def __init__(self, http_methods: HTTPMethodsResource) -> None:
        self._http_methods = http_methods

        self.create = to_raw_response_wrapper(
            http_methods.create,
        )
        self.update = to_raw_response_wrapper(
            http_methods.update,
        )
        self.delete = to_raw_response_wrapper(
            http_methods.delete,
        )
        self.get = to_raw_response_wrapper(
            http_methods.get,
        )
        self.put = to_raw_response_wrapper(
            http_methods.put,
        )


class AsyncHTTPMethodsResourceWithRawResponse:
    def __init__(self, http_methods: AsyncHTTPMethodsResource) -> None:
        self._http_methods = http_methods

        self.create = async_to_raw_response_wrapper(
            http_methods.create,
        )
        self.update = async_to_raw_response_wrapper(
            http_methods.update,
        )
        self.delete = async_to_raw_response_wrapper(
            http_methods.delete,
        )
        self.get = async_to_raw_response_wrapper(
            http_methods.get,
        )
        self.put = async_to_raw_response_wrapper(
            http_methods.put,
        )


class HTTPMethodsResourceWithStreamingResponse:
    def __init__(self, http_methods: HTTPMethodsResource) -> None:
        self._http_methods = http_methods

        self.create = to_streamed_response_wrapper(
            http_methods.create,
        )
        self.update = to_streamed_response_wrapper(
            http_methods.update,
        )
        self.delete = to_streamed_response_wrapper(
            http_methods.delete,
        )
        self.get = to_streamed_response_wrapper(
            http_methods.get,
        )
        self.put = to_streamed_response_wrapper(
            http_methods.put,
        )


class AsyncHTTPMethodsResourceWithStreamingResponse:
    def __init__(self, http_methods: AsyncHTTPMethodsResource) -> None:
        self._http_methods = http_methods

        self.create = async_to_streamed_response_wrapper(
            http_methods.create,
        )
        self.update = async_to_streamed_response_wrapper(
            http_methods.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            http_methods.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            http_methods.get,
        )
        self.put = async_to_streamed_response_wrapper(
            http_methods.put,
        )
