"""
Создание покемона POST 
"""
import requests

URL= "https://api.pokemonbattle.me"
Header= {'Content-Type':'application/json','trainer_token':'token'}

body= {
    "pokemon_id": "22144"
}

response = requests.post(url=f'{URL}/v2/pokemons',json=body,headers=Header,timeout=5)
print(f'статус код:{response.status_code}.сообщение:{response.text}')

response=requests.put(url=f'{URL}/v2/pokemons',headers=Header,json=body)
print(f'статус код:{response.status_code}.')

response=requests.post(url=f'{URL}/v2/trainers/add_pokeball',headers=Header,json=body)
print(f'статус код:{response.status_code}.')