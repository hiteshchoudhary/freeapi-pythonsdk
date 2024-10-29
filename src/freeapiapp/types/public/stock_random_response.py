# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StockRandomResponse", "Data"]


class Data(BaseModel):
    book_value: Optional[str] = FieldInfo(alias="BookValue", default=None)

    current_price: Optional[str] = FieldInfo(alias="CurrentPrice", default=None)

    dividend_yield: Optional[str] = FieldInfo(alias="DividendYield", default=None)

    face_value: Optional[str] = FieldInfo(alias="FaceValue", default=None)

    high_low: Optional[str] = FieldInfo(alias="HighLow", default=None)

    isin: Optional[str] = FieldInfo(alias="ISIN", default=None)

    listing_date: Optional[str] = FieldInfo(alias="ListingDate", default=None)

    market_cap: Optional[str] = FieldInfo(alias="MarketCap", default=None)

    name: Optional[str] = FieldInfo(alias="Name", default=None)

    roce: Optional[str] = FieldInfo(alias="ROCE", default=None)

    roe: Optional[str] = FieldInfo(alias="ROE", default=None)

    stock_pe: Optional[str] = FieldInfo(alias="StockPE", default=None)

    symbol: Optional[str] = FieldInfo(alias="Symbol", default=None)


class StockRandomResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
