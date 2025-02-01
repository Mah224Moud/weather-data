for i in {1..2}
do
    echo -e "Début de l'exécution du fichier $i."
    jupyter nbconvert --to notebook --execute archive.ipynb
    echo -e "Fin de l'exécution du fichier $i. \n"
done
