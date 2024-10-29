# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RazorpayVerifyPaymentParams"]


class RazorpayVerifyPaymentParams(TypedDict, total=False):
    razorpay_order_id: str

    razorpay_payment_id: str

    razorpay_signature: str
