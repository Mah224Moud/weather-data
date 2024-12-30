
def send_data(url, data, requests, headers=None):
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            print("Données ajoutées avec succès!")
            return response.json()
        elif response.status_code == 200:
            print("Requête réussie!")
            return response.json()
        else:
            print(f"Erreur {response.status_code}: {response.text}")
            return {"error": response.text}

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
        return {"error": str(e)}