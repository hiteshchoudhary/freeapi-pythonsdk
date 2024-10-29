# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["RazorpayCreateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    amount: Optional[float] = None

    amount_due: Optional[float] = None

    amount_paid: Optional[float] = None

    attempts: Optional[float] = None

    created_at: Optional[float] = None

    currency: Optional[str] = None

    entity: Optional[str] = None

    notes: Optional[List[object]] = None

    offer_id: Optional[object] = None

    receipt: Optional[str] = None

    status: Optional[str] = None


class RazorpayCreateResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
