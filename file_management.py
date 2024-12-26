import shutil
import os

def change_file_extension(download_directory: str) -> str:
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
    if os.path.exists(source_file):
        destination_path = os.path.join(destination_folder, os.path.basename(source_file))
        shutil.move(source_file, destination_path)
        print(f"Le fichier a été déplacé de {source_file} à {destination_path}")
    else:
        print("Le fichier n'existe pas.")