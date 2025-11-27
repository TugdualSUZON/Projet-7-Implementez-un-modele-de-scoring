# File_name set_mlflow_tracking.py
# Author Tugdual SUZON 27/11/2025
# Created 27/11/2025

# Scpécifier et le cas échéant créer le ficher database pour le suivie des entrainement
# dans le dossier data du projet

# Packages
import mlflow
import os

# Fonctions
def my_mkdir(directory_name):
    # Vérifie si le répertoire existe déjà
    if not os.path.exists(directory_name):
        # Crée le répertoire
        os.makedirs(directory_name)
        print(f"Le répertoire '{directory_name}' a été créé.")
    else:
        print(f"Le répertoire '{directory_name}' existe déjà.")

# Vérifier la présence du dossier data ou le créer
my_mkdir("data")

# 
if os.path.exists(f"data/mlflow.db") :
    
    print("Le fichier database mlflow.db pour le suivie de modèle existe déjà")

    os.environ["MLFLOW_ARTIFACT_URI"] = "file:///data/mlruns" # Spécifier le chemin pour le dossier de stokage des artéfact et modèles
    mlflow.set_tracking_uri("sqlite:///data/mlflow.db") # Spécifier le chemin pour la base de données des métadonnées
    
else :
    
    print("Le fichier database mlflow.db pour le suivie de modèle n'existe pas")
    
    os.environ["MLFLOW_ARTIFACT_URI"] = "file:///data/mlruns" # Spécifier le chemin pour le dossier de stokage des artéfact et modèles
    mlflow.set_tracking_uri("sqlite:///data/mlflow.db") # Spécifier le chemin pour la base de données des métadonnées
    
    # Pour le fichier soit créer il faut initialiser une premier expérience et log une valeurs
    mlflow.set_experiment("Dummy-experiment")
    
    with mlflow.start_run():
        mlflow.log_param("param_test", 1)

    
    # Vérifier la présence du fichier db
    if os.path.exists(f"data/mlflow.db") :
        print("Fichier mlflow.db pour le suivie de modèle à été créer avec succèe dans le dossier data du repertoire courant")
    else :
        print("Une erreur c'est produite le fichier mlflow.db pour le suivie de modèle n'a pas été crée")

    # Vérifier la présence du dossier mlrun
    if os.path.exists(f"data/mlruns") :
        print("Le dossier /mlrun pour le stockage des artéfacte et modèle à été créer avec succèes dans le dossier data du repertoire courant")
    else :
        print("Une erreur c'est produite Le dossier /mlrun pour le stockage des artéfacte et modèle n'a pas été crée")
