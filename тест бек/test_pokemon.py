import requests
import pytest

URL= "https://api.pokemonbattle.me"
Header= {'Content-Type':'application/json','trainer_token':'token'}
def test_get_trainers():
 '''
 GET /trainers приходит с кодом 200 и имя твоего тренера
 '''
response = requests.get(url=f'{URL}/v2/trainers',params={'trainer_id': 2493},timeout=5)
assert response.status_code == 200,'Unexpected status code'