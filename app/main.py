import gradio as gr
import os
from dotenv import load_dotenv
from analyzer import BuyBuyAnalyzer
from dashboard import RetailAnalytics

load_dotenv()

# Initialisation des composants métier
analyzer = BuyBuyAnalyzer(api_key=os.getenv("NVIDIA_API_KEY"))
analytics_engine = RetailAnalytics(analyzer)

from pydantic import ValidationError

def chat_interface(message, history):
    try:
        # Tentative d'analyse avec la chaîne LangChain
        response = analyzer.process_email(message)
        
        # Si ça réussit, on affiche le résultat pro
        res_text = f"###  Analyse BuyBuy effectuée\n"
        res_text += f"- **Catégorie** : {response.product_category}\n"
        res_text += f"- **Sentiment** : {response.sentiment}\n"
        res_text += f"- **Magasin** : {response.store_location}"
        return res_text

    except ValidationError:
        # C'est ici qu'on gère le cas où le sentiment n'est pas reconnu
        return (
            "Je suis un assistant spécialisé pour la plateforme BuyBuy. 🛒\n\n"
            "Je traite uniquement les emails clients pour analyser les sentiments "
            "(Positive/Negative) et extraire les catégories de produits. "
            "Veuillez me soumettre un message concernant un achat ou une expérience en magasin."
        )
    except Exception as e:
        # Pour les autres erreurs (connexion API, etc.)
        return "Je suis disponible pour traiter vos emails, mais j'ai rencontré une difficulté technique momentanée."
# Création de l'interface de Chat
demo = gr.ChatInterface(
    fn=chat_interface,
    title="BuyBuy Analytics - Customer Intelligence",
    description="Interface professionnelle d'analyse de sentiment client via NVIDIA Llama 3.1.",
    theme="soft"
)

if __name__ == "__main__":
    # On lance sur 0.0.0.0 pour permettre l'accès via Docker
    demo.launch(server_name="0.0.0.0", server_port=7860)