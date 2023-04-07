# python -m pytest -k test_square_root
# python -m pytest -v
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_square_root_get():
    response = client.get("/square_root/81")
    assert response.status_code == 200
    assert response.text == '9.0'

def test_square_root_post():
    response = client.post("/square_root/", json={'number': 9})
    assert response.status_code == 200
    assert response.text == '3.0'

def test_secret_func_1():
    response = client.post("/secret_func/", json={'first': 16, 'second': 0})
    assert response.status_code == 200
    assert response.json() == {'answer': 16}

def test_secret_func_2():
    response = client.post("/secret_func/", json={'first': 16, 'second': 1})
    assert response.status_code == 200
    assert response.json() == {'answer': 8}

def test_secret_func_3():
    response = client.post("/secret_func/", json={'first': 16, 'second': 3})
    assert response.status_code == 200
    assert response.json() == {'answer': 2}

def test_secret_func_4():
    response = client.post("/secret_func/", json={'first': 16, 'second': -1})
    assert response.status_code == 200
    assert response.json() == {'answer': 'Bad input'}
