import requests
import pytest

URL = 'https://api.pokemonbattle.me'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers():
    """
    Get trainers test status code
    """
    response = requests.get(url=f'{URL}/v2/trainers', params={"trainer_id": 432}, headers=HEADER)
    assert response.status_code == 200, 'Unexpected status code'
