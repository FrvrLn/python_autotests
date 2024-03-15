"""
Pokemons API tests
"""
import requests

URL = 'https://api.pokemonbattle.me'

HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': '7595c81f42731deb07123f48d5890be0'
    }

body1 = {
    "name": "Marafa",
    "photo": "https://dolnikov.ru/pokemons/albums/095.png"
}

body2 = {
    "pokemon_id": "14095",
    "name": "Kuka",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body3 = {
    "pokemon_id": "14095"
}

response = requests.post(url=f'{URL}/v2/pokemons', json=body1, headers=HEADER)
print(f'message:{response.json()["message"]}')

response = requests.put(url=f'{URL}/v2/pokemons', json=body2, headers=HEADER)
print(f'message:{response.json()["message"]}')

response = requests.post(url=f'{URL}/v2/trainers/add_pokeball', json=body3, headers=HEADER)
print(f'message:{response.json()["message"]}')