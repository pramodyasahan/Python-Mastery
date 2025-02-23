import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        print(pokemon_data)
    else:
        print("Failed to get pokemon data")


pokemon_name = "pikachu"
get_pokemon(pokemon_name)