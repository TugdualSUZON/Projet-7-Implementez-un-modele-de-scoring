FROM python:3.13-slim
WORKDIR /app
COPY ./app # Model, requirement and main.py
RUN pip install -r requirements_main.txt


# Installer pyenv pour la virtualisation du model
CMD []

# Lancer l'API REST du model
CMD ["mlflow" "models" "serve" "-m" "./"] # ADD path to file

# Lancer l'iinterface graphique pour intéroger l'API
CMD ["streamlit", "run", "P7_dashboard.py"]