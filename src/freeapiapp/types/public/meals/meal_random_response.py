# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MealRandomResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    date_modified: Optional[object] = FieldInfo(alias="dateModified", default=None)

    id_meal: Optional[str] = FieldInfo(alias="idMeal", default=None)

    str_area: Optional[str] = FieldInfo(alias="strArea", default=None)

    str_category: Optional[str] = FieldInfo(alias="strCategory", default=None)

    str_creative_commons_confirmed: Optional[object] = FieldInfo(alias="strCreativeCommonsConfirmed", default=None)

    str_drink_alternate: Optional[object] = FieldInfo(alias="strDrinkAlternate", default=None)

    str_image_source: Optional[object] = FieldInfo(alias="strImageSource", default=None)

    str_ingredient1: Optional[str] = FieldInfo(alias="strIngredient1", default=None)

    str_ingredient10: Optional[str] = FieldInfo(alias="strIngredient10", default=None)

    str_ingredient11: Optional[str] = FieldInfo(alias="strIngredient11", default=None)

    str_ingredient12: Optional[str] = FieldInfo(alias="strIngredient12", default=None)

    str_ingredient13: Optional[str] = FieldInfo(alias="strIngredient13", default=None)

    str_ingredient14: Optional[str] = FieldInfo(alias="strIngredient14", default=None)

    str_ingredient15: Optional[str] = FieldInfo(alias="strIngredient15", default=None)

    str_ingredient16: Optional[str] = FieldInfo(alias="strIngredient16", default=None)

    str_ingredient17: Optional[str] = FieldInfo(alias="strIngredient17", default=None)

    str_ingredient18: Optional[str] = FieldInfo(alias="strIngredient18", default=None)

    str_ingredient19: Optional[str] = FieldInfo(alias="strIngredient19", default=None)

    str_ingredient2: Optional[str] = FieldInfo(alias="strIngredient2", default=None)

    str_ingredient20: Optional[str] = FieldInfo(alias="strIngredient20", default=None)

    str_ingredient3: Optional[str] = FieldInfo(alias="strIngredient3", default=None)

    str_ingredient4: Optional[str] = FieldInfo(alias="strIngredient4", default=None)

    str_ingredient5: Optional[str] = FieldInfo(alias="strIngredient5", default=None)

    str_ingredient6: Optional[str] = FieldInfo(alias="strIngredient6", default=None)

    str_ingredient7: Optional[str] = FieldInfo(alias="strIngredient7", default=None)

    str_ingredient8: Optional[str] = FieldInfo(alias="strIngredient8", default=None)

    str_ingredient9: Optional[str] = FieldInfo(alias="strIngredient9", default=None)

    str_instructions: Optional[str] = FieldInfo(alias="strInstructions", default=None)

    str_meal: Optional[str] = FieldInfo(alias="strMeal", default=None)

    str_meal_thumb: Optional[str] = FieldInfo(alias="strMealThumb", default=None)

    str_measure1: Optional[str] = FieldInfo(alias="strMeasure1", default=None)

    str_measure10: Optional[str] = FieldInfo(alias="strMeasure10", default=None)

    str_measure11: Optional[str] = FieldInfo(alias="strMeasure11", default=None)

    str_measure12: Optional[str] = FieldInfo(alias="strMeasure12", default=None)

    str_measure13: Optional[str] = FieldInfo(alias="strMeasure13", default=None)

    str_measure14: Optional[str] = FieldInfo(alias="strMeasure14", default=None)

    str_measure15: Optional[str] = FieldInfo(alias="strMeasure15", default=None)

    str_measure16: Optional[str] = FieldInfo(alias="strMeasure16", default=None)

    str_measure17: Optional[str] = FieldInfo(alias="strMeasure17", default=None)

    str_measure18: Optional[str] = FieldInfo(alias="strMeasure18", default=None)

    str_measure19: Optional[str] = FieldInfo(alias="strMeasure19", default=None)

    str_measure2: Optional[str] = FieldInfo(alias="strMeasure2", default=None)

    str_measure20: Optional[str] = FieldInfo(alias="strMeasure20", default=None)

    str_measure3: Optional[str] = FieldInfo(alias="strMeasure3", default=None)

    str_measure4: Optional[str] = FieldInfo(alias="strMeasure4", default=None)

    str_measure5: Optional[str] = FieldInfo(alias="strMeasure5", default=None)

    str_measure6: Optional[str] = FieldInfo(alias="strMeasure6", default=None)

    str_measure7: Optional[str] = FieldInfo(alias="strMeasure7", default=None)

    str_measure8: Optional[str] = FieldInfo(alias="strMeasure8", default=None)

    str_measure9: Optional[str] = FieldInfo(alias="strMeasure9", default=None)

    str_source: Optional[str] = FieldInfo(alias="strSource", default=None)

    str_tags: Optional[object] = FieldInfo(alias="strTags", default=None)

    str_youtube: Optional[str] = FieldInfo(alias="strYoutube", default=None)


class MealRandomResponse(BaseModel):
    data: Optional[Data] = None

    message: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None
