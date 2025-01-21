import shutil
import os
from datetime import datetime

def change_file_extension(download_directory: str) -> str:
    """
    Changes the file extension of the most recently modified .txt file 
    in the specified download directory to .csv.

    Parameters:
    download_directory (str): The path to the directory containing the files.

    Returns:
    str: The new file path with the .csv extension if a .txt file is found and renamed, 
    otherwise None.
    """

    files = [f for f in os.listdir(download_directory) if f.endswith('.txt')]

    if files:
        latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(download_directory, f)))
        
        old_file_path = os.path.join(download_directory, latest_file)
        new_file_path = os.path.splitext(old_file_path)[0] + '.csv'
        
        os.rename(old_file_path, new_file_path)
        print(f"Le fichier a été renommé : {old_file_path} -> {new_file_path}")

        return new_file_path
    else:
        print("Aucun fichier .txt trouvé.")
        return


def move_file(source_file: str, destination_folder: str):
    """
    Move a file from the source path to the destination folder.

    Parameters:
    source_file (str): The path to the file to be moved.
    destination_folder (str): The folder to move the file to.

    Returns:
    None
    """
    if os.path.exists(source_file):
        destination_path = os.path.join(destination_folder, os.path.basename(source_file))
        shutil.move(source_file, destination_path)
        print(f"Le fichier a été déplacé de {source_file} à {destination_path}")
    else:
        print("Le fichier n'existe pas.")

def get_oldest_csv_file(path: str) -> str:
    """
    Trouve et retourne le chemin complet du fichier CSV avec la date la plus ancienne 
    dans un répertoire donné, basé sur le format du nom de fichier : synop.anneemois.csv.

    Parameters:
    path (str): Le chemin vers le répertoire contenant les fichiers CSV.

    Returns:
    str: Le chemin complet du fichier le plus ancien si trouvé, sinon None.
    """
    try:
        csv_files = [f for f in os.listdir(path) if f.startswith("synop.") and f.endswith(".csv") and f.count('.') == 2]
        
        if not csv_files:
            print("Aucun fichier CSV correspondant trouvé dans le répertoire.")
            return None

        oldest_file = None
        oldest_date = None

        for file in csv_files:
            try:
                date_str = file.split('.')[1]  
                date_obj = datetime.strptime(date_str, "%Y%m")  
                
                if oldest_date is None or date_obj < oldest_date:
                    oldest_date = date_obj
                    oldest_file = file
            except ValueError:
                print(f"Format de date incorrect pour le fichier : {file}")
        
        if oldest_file:
            oldest_file_path = os.path.join(path, oldest_file)
            print(f"Le fichier le plus ancien est : {oldest_file_path}")
            return oldest_file_path
        else:
            print("Aucun fichier avec une date valide n'a été trouvé.")
            return None

    except Exception as e:
        print(f"Erreur lors du traitement : {e}")
        return None
