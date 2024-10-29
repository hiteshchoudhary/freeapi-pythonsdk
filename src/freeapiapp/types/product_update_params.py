# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ProductUpdateParams"]


class ProductUpdateParams(TypedDict, total=False):
    category: str

    description: str

    main_image: Annotated[FileTypes, PropertyInfo(alias="mainImage")]
    """File"""

    name: str

    price: str

    stock: str

    sub_images: Annotated[FileTypes, PropertyInfo(alias="subImages")]
    """
    subImages is a multiple images field having 4 as a maximum number of images
    limit
    """
