#!/bin/bash

LOG_FILE="/opt/dossier_partage/donnees-meteo/cron_log.txt"
VENV_PATH="/opt/dossier_partage/donnees-meteo/venv/bin/activate"
JUPYTER_CMD="/opt/dossier_partage/donnees-meteo/venv/bin/jupyter nbconvert --to notebook --execute /opt/dossier_partage/donnees-meteo/main.ipynb"

HEURE_REELLE=$(date)
HEURE_DECALEE=$(date --date='2 hours ago' '+%H')

echo -e "Exécution du: $HEURE_REELLE - Recuperation des données de ${HEURE_DECALEE}H" >> "$LOG_FILE" 2>&1
source "$VENV_PATH"
$JUPYTER_CMD >> "$LOG_FILE" 2>&1

HEURE_FIN=$(date --date='2 hours ago')
echo -e "Fin de l'execution: $HEURE_FIN\n " >> "$LOG_FILE" 2>&1