# Utilisez une image de python de base
FROM python:3.9-slim-buster

# Définissez le répertoire de travail
WORKDIR /app

RUN mkdir images
RUN mkdir templates

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 libgl1-mesa-dev xvfb -y

# Copier les fichiers du répertoire actuel vers le conteneur
COPY requirements.txt .
COPY main.py .
COPY ./templates/. ./templates

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt


# Démarrez l'application
CMD ["python", "-m", "main"]
