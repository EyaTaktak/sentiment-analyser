from pydantic import BaseModel, Field
from typing import Literal

class CustomerFeedback(BaseModel):
    """Schéma de sortie pour l'extraction par IA"""
    product_category: str = Field(description="Ex: Electronics, Household, Food")
    # Ajout de Neutral et forçage des termes anglais
    sentiment: Literal["Positive", "Negative", "Neutral"] = Field(description="Global sentiment")
    store_location: str = Field(description="Store city or name")
    is_complaint: bool = Field(description="True if sentiment is Negative")