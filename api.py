
def send_data(url, data, requests, headers=None):
    """
    Sends a POST request with JSON data to a specified URL.

    Parameters:
    url (str): The URL to which the request is sent.
    data (dict): The data to be sent in JSON format.
    requests (module): The requests module used to make HTTP requests.
    headers (dict, optional): Optional headers to include in the request.

    Returns:
    dict: The JSON response from the server if the request is successful,
          or an error message if there is a request error or a non-200/201 status code.

    Prints:
    Success or error message based on the response status code or connection error.
    """

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