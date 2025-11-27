# File_name set_launch_mlflow_server.py
# Author Tugdual SUZON 27/11/2025
# Created 27/11/2025

# Packages
import mlflow
import subprocess
import time

# Lancer le processus (ex : serveur MLflow)
process = subprocess.Popen([
    "mlflow", "server",
    "--backend-store-uri", "sqlite:///data/mlflow.db",
    #"--default-artifact-root", "file:///chemin/absolu/vers/data/mlruns",
    "--host", "0.0.0.0",
    "--port", "5000"
])

print("Serveur MLflow démarré.")
