from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)

BASE = "/api/v1/fizzbuzz"
STATS = "/api/v1/stats/"


def test_stats_empty():
    response = client.get(STATS)
    assert response.status_code == 200
    assert response.json() == {}


def test_stats_after_request():
    client.get(
        BASE, params={"int1": 3, "int2": 5, "limit": 15, "str1": "Fizz", "str2": "Buzz"}
    )
    response = client.get(STATS)
    assert response.status_code == 200
    data = response.json()
    assert data["hits"] == 1
    assert len(data["requests"]) == 1


def test_stats_increments_hits():
    params = {"int1": 3, "int2": 5, "limit": 15, "str1": "Fizz", "str2": "Buzz"}
    client.get(BASE, params=params)
    client.get(BASE, params=params)
    response = client.get(STATS)
    assert response.json()["hits"] == 2


def test_stats_most_frequent():
    params_a = {"int1": 3, "int2": 5, "limit": 15, "str1": "Fizz", "str2": "Buzz"}
    params_b = {"int1": 2, "int2": 3, "limit": 10, "str1": "Foo", "str2": "Bar"}
    client.get(BASE, params=params_a)
    client.get(BASE, params=params_a)
    client.get(BASE, params=params_b)
    response = client.get(STATS)
    data = response.json()
    assert data["hits"] == 2
    assert len(data["requests"]) == 1
