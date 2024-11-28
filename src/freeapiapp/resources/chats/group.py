# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

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
from ...types.chats import group_create_params, group_update_params
from ..._base_client import make_request_options
from ...types.chats.group_leave_response import GroupLeaveResponse
from ...types.chats.group_create_response import GroupCreateResponse
from ...types.chats.group_delete_response import GroupDeleteResponse
from ...types.chats.group_update_response import GroupUpdateResponse
from ...types.chats.group_retrieve_response import GroupRetrieveResponse
from ...types.chats.group_participant_add_response import GroupParticipantAddResponse
from ...types.chats.group_participant_remove_response import GroupParticipantRemoveResponse

__all__ = ["GroupResource", "AsyncGroupResource"]


class GroupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return GroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return GroupResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        participants: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupCreateResponse:
        """
        This API endpoint enables a logged-in user to initiate the creation of a group
        chat, bringing together multiple participants to engage in collaborative
        discussions.

        To establish a group, a minimum of three participants is required.

        This endpoint streamlines the process of forming dynamic group conversations,
        fostering enriched interactions among users within the chat application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat-app/chats/group",
            body=maybe_transform(
                {
                    "name": name,
                    "participants": participants,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    def retrieve(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupRetrieveResponse:
        """
        This API endpoint allows developers to retrieve comprehensive information about
        a specific group chat.

        This includes essential details such as the group's name, the total number of
        participants, and a detailed list of member profiles, providing a holistic
        overview of the group's composition.

        By utilizing this endpoint, developers can seamlessly access and display key
        insights into group interactions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            f"/chat-app/chats/group/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupRetrieveResponse,
        )

    def update(
        self,
        chat_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateResponse:
        """
        This API endpoint empowers group administrators to seamlessly update the name of
        a group chat.

        Group administrators can utilize this endpoint to enhance the clarity and
        context of their group conversations by modifying the group's name as needed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._patch(
            f"/chat-app/chats/group/{chat_id}",
            body=maybe_transform({"name": name}, group_update_params.GroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateResponse,
        )

    def delete(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupDeleteResponse:
        """
        This API endpoint empowers group administrators to seamlessly delete a specific
        group chat identified by its unique `chatId`.

        By accessing this endpoint, group admins can initiate the removal process,
        ensuring efficient management of group interactions and maintaining a
        streamlined chat environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._delete(
            f"/chat-app/chats/group/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupDeleteResponse,
        )

    def leave(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupLeaveResponse:
        """
        This API endpoint enables logged in user to leave a specific group by passing
        the `chatId` as a path variable.

        This endpoint gives user privilege to decide whether to be a part of a specific
        group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._delete(
            f"/chat-app/chats/leave/group/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupLeaveResponse,
        )

    def participant_add(
        self,
        participant_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupParticipantAddResponse:
        """
        This API endpoint enables group administrators to effortlessly expand the
        participant roster of a specific group chat.

        With this endpoint, administrators can seamlessly add new members to the group,
        fostering inclusivity and enabling enriched collaborative discussions among
        participants.

        This functionality streamlines group management, empowering administrators to
        create vibrant and engaging group dynamics within the chat application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return self._post(
            f"/chat-app/chats/group/{chat_id}/{participant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupParticipantAddResponse,
        )

    def participant_remove(
        self,
        participant_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupParticipantRemoveResponse:
        """
        This API endpoint enables group administrators to efficiently manage group
        dynamics by removing participants from a specific group chat.

        This endpoint empowers administrators to maintain the composition and relevance
        of the group by seamlessly detaching selected participants, ensuring a
        streamlined and controlled group conversation environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return self._delete(
            f"/chat-app/chats/group/{chat_id}/{participant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupParticipantRemoveResponse,
        )


class AsyncGroupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiteshchoudhary/freeapi-pythonsdk#with_streaming_response
        """
        return AsyncGroupResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        participants: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupCreateResponse:
        """
        This API endpoint enables a logged-in user to initiate the creation of a group
        chat, bringing together multiple participants to engage in collaborative
        discussions.

        To establish a group, a minimum of three participants is required.

        This endpoint streamlines the process of forming dynamic group conversations,
        fostering enriched interactions among users within the chat application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat-app/chats/group",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "participants": participants,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    async def retrieve(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupRetrieveResponse:
        """
        This API endpoint allows developers to retrieve comprehensive information about
        a specific group chat.

        This includes essential details such as the group's name, the total number of
        participants, and a detailed list of member profiles, providing a holistic
        overview of the group's composition.

        By utilizing this endpoint, developers can seamlessly access and display key
        insights into group interactions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            f"/chat-app/chats/group/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupRetrieveResponse,
        )

    async def update(
        self,
        chat_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateResponse:
        """
        This API endpoint empowers group administrators to seamlessly update the name of
        a group chat.

        Group administrators can utilize this endpoint to enhance the clarity and
        context of their group conversations by modifying the group's name as needed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._patch(
            f"/chat-app/chats/group/{chat_id}",
            body=await async_maybe_transform({"name": name}, group_update_params.GroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateResponse,
        )

    async def delete(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupDeleteResponse:
        """
        This API endpoint empowers group administrators to seamlessly delete a specific
        group chat identified by its unique `chatId`.

        By accessing this endpoint, group admins can initiate the removal process,
        ensuring efficient management of group interactions and maintaining a
        streamlined chat environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._delete(
            f"/chat-app/chats/group/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupDeleteResponse,
        )

    async def leave(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupLeaveResponse:
        """
        This API endpoint enables logged in user to leave a specific group by passing
        the `chatId` as a path variable.

        This endpoint gives user privilege to decide whether to be a part of a specific
        group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._delete(
            f"/chat-app/chats/leave/group/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupLeaveResponse,
        )

    async def participant_add(
        self,
        participant_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupParticipantAddResponse:
        """
        This API endpoint enables group administrators to effortlessly expand the
        participant roster of a specific group chat.

        With this endpoint, administrators can seamlessly add new members to the group,
        fostering inclusivity and enabling enriched collaborative discussions among
        participants.

        This functionality streamlines group management, empowering administrators to
        create vibrant and engaging group dynamics within the chat application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return await self._post(
            f"/chat-app/chats/group/{chat_id}/{participant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupParticipantAddResponse,
        )

    async def participant_remove(
        self,
        participant_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupParticipantRemoveResponse:
        """
        This API endpoint enables group administrators to efficiently manage group
        dynamics by removing participants from a specific group chat.

        This endpoint empowers administrators to maintain the composition and relevance
        of the group by seamlessly detaching selected participants, ensuring a
        streamlined and controlled group conversation environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        return await self._delete(
            f"/chat-app/chats/group/{chat_id}/{participant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupParticipantRemoveResponse,
        )


class GroupResourceWithRawResponse:
    def __init__(self, group: GroupResource) -> None:
        self._group = group

        self.create = to_raw_response_wrapper(
            group.create,
        )
        self.retrieve = to_raw_response_wrapper(
            group.retrieve,
        )
        self.update = to_raw_response_wrapper(
            group.update,
        )
        self.delete = to_raw_response_wrapper(
            group.delete,
        )
        self.leave = to_raw_response_wrapper(
            group.leave,
        )
        self.participant_add = to_raw_response_wrapper(
            group.participant_add,
        )
        self.participant_remove = to_raw_response_wrapper(
            group.participant_remove,
        )


class AsyncGroupResourceWithRawResponse:
    def __init__(self, group: AsyncGroupResource) -> None:
        self._group = group

        self.create = async_to_raw_response_wrapper(
            group.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            group.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            group.update,
        )
        self.delete = async_to_raw_response_wrapper(
            group.delete,
        )
        self.leave = async_to_raw_response_wrapper(
            group.leave,
        )
        self.participant_add = async_to_raw_response_wrapper(
            group.participant_add,
        )
        self.participant_remove = async_to_raw_response_wrapper(
            group.participant_remove,
        )


class GroupResourceWithStreamingResponse:
    def __init__(self, group: GroupResource) -> None:
        self._group = group

        self.create = to_streamed_response_wrapper(
            group.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            group.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            group.update,
        )
        self.delete = to_streamed_response_wrapper(
            group.delete,
        )
        self.leave = to_streamed_response_wrapper(
            group.leave,
        )
        self.participant_add = to_streamed_response_wrapper(
            group.participant_add,
        )
        self.participant_remove = to_streamed_response_wrapper(
            group.participant_remove,
        )


class AsyncGroupResourceWithStreamingResponse:
    def __init__(self, group: AsyncGroupResource) -> None:
        self._group = group

        self.create = async_to_streamed_response_wrapper(
            group.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            group.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            group.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            group.delete,
        )
        self.leave = async_to_streamed_response_wrapper(
            group.leave,
        )
        self.participant_add = async_to_streamed_response_wrapper(
            group.participant_add,
        )
        self.participant_remove = async_to_streamed_response_wrapper(
            group.participant_remove,
        )
