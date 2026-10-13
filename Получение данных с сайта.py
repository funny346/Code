from http.client import responses

import requests
URL = "https://pokeapi.co/api/v2/"
def get_info(name):
    b_url = f"{URL}/pokemon/{name}"
    response = requests.get(b_url)
    if response.status_code == 200:
       print(f"Status code {response.status_code}")
       print(response.json())
       return response.json()
    else:
        print(f"Error code: {response.status_code}")


pokemon_name = "pikachu"

info = get_info(pokemon_name)
print()
if info:
    print(f"{info["name"]}")