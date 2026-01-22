from typing import Literal

from pydantic import BaseModel, Field


class CustomerFeedback(BaseModel):
    """Schema de sortie pour l'analyse IA client."""

    product_category: str = Field(
        description="Ex: Electronics, Household, Food"
    )
    sentiment: Literal[
        "Positive",
        "Negative",
        "Neutral",
    ] = Field(description="Global sentiment")
    store_location: str = Field(
        description="Store city or name"
    )
    is_complaint: bool = Field(
        description="True if sentiment is Negative"
    )
