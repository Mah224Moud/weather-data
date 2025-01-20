#!/bin/bash

# Répertoire de travail, vous pouvez le changer selon votre besoin
rep_travail="."

# Aller dans le répertoire de travail
cd "$rep_travail" || exit 1

# Boucle sur tous les fichiers .gz du répertoire
for fichier_gz in *.gz; do
    # Vérifie si c'est un fichier
    if [ -f "$fichier_gz" ]; then
        # Extraction du fichier CSV
        echo "Extraction de $fichier_gz ..."
        gunzip -c "$fichier_gz" > "${fichier_gz%.gz}"
        
        # Suppression du fichier .gz après extraction
        rm "$fichier_gz"
        
        echo "Fichier ${fichier_gz%.gz}.csv extrait et $fichier_gz supprimé."
    fi
done
