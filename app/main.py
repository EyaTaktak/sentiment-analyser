import os

import gradio as gr
from dotenv import load_dotenv
from pydantic import ValidationError

from analyzer import BuyBuyAnalyzer
from dashboard import RetailAnalytics

load_dotenv()

# Initialisation des composants métier
analyzer = BuyBuyAnalyzer(
    api_key=os.getenv("NVIDIA_API_KEY")
)
analytics_engine = RetailAnalytics(analyzer)


def chat_interface(message, history):
    """Gradio chat interface for BuyBuy sentiment analysis."""
    try:
        response = analyzer.process_email(message)

        res_text = "### Analyse BuyBuy effectuée\n"
        res_text += (
            f"- **Catégorie** : {response.product_category}\n"
        )
        res_text += (
            f"- **Sentiment** : {response.sentiment}\n"
        )
        res_text += (
            f"- **Magasin** : {response.store_location}"
        )

        return res_text

    except ValidationError:
        return (
            "Je suis un assistant spécialisé pour la plateforme BuyBuy. 🛒\n\n"
            "Je traite uniquement les emails clients pour analyser les "
            "sentiments (Positive / Negative / Neutral) et extraire les "
            "catégories de produits.\n\n"
            "Veuillez me soumettre un message concernant un achat ou une "
            "expérience en magasin."
        )

    except Exception:
        return (
            "Je suis disponible pour traiter vos emails, mais j'ai "
            "rencontré une difficulté technique momentanée."
        )


demo = gr.ChatInterface(
    fn=chat_interface,
    title="BuyBuy Analytics - Customer Intelligence",
    description=(
        "Interface professionnelle d'analyse de sentiment client "
        "via NVIDIA Llama 3.1."
    ),
    theme="soft",
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
    )
