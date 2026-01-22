FROM python:3.11-slim

WORKDIR /app

# Dépendances système
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Installation des librairies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gradio  # Ajout de gradio

COPY . .

# Exposer le port Gradio
EXPOSE 7860

# Lancer l'application
CMD ["python", "app/main.py"]