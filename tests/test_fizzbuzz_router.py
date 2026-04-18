from fastapi.testclient import TestClient
from fizzbuzz.main import app

client = TestClient(app)

BASE = "/api/v1/fizzbuzz"


def test_valid_request():
    response = client.get(
        BASE, params={"int1": 3, "int2": 5, "limit": 15, "str1": "Fizz", "str2": "Buzz"}
    )
    assert response.status_code == 200
    data = response.json()["result"]
    assert data[2] == "Fizz"
    assert data[4] == "Buzz"
    assert data[14] == "FizzBuzz"
    assert data[0] == "1"


def test_result_length():
    response = client.get(
        BASE,
        params={"int1": 3, "int2": 5, "limit": 100, "str1": "Fizz", "str2": "Buzz"},
    )
    assert response.status_code == 200
    assert len(response.json()["result"]) == 100


def test_missing_param():
    response = client.get(
        BASE, params={"int1": 3, "int2": 5, "limit": 10, "str1": "Fizz"}
    )
    assert response.status_code == 422


def test_int1_zero():
    response = client.get(
        BASE, params={"int1": 0, "int2": 5, "limit": 10, "str1": "Fizz", "str2": "Buzz"}
    )
    assert response.status_code == 422


def test_int2_zero():
    response = client.get(
        BASE, params={"int1": 3, "int2": 0, "limit": 10, "str1": "Fizz", "str2": "Buzz"}
    )
    assert response.status_code == 422


def test_limit_zero():
    response = client.get(
        BASE, params={"int1": 3, "int2": 5, "limit": 0, "str1": "Fizz", "str2": "Buzz"}
    )
    assert response.status_code == 422


def test_limit_exceeds_max():
    response = client.get(
        BASE,
        params={"int1": 3, "int2": 5, "limit": 10001, "str1": "Fizz", "str2": "Buzz"},
    )
    assert response.status_code == 422


def test_limit_at_max():
    response = client.get(
        BASE,
        params={"int1": 3, "int2": 5, "limit": 10000, "str1": "Fizz", "str2": "Buzz"},
    )
    assert response.status_code == 200
    assert len(response.json()["result"]) == 10000


def test_custom_strings():
    response = client.get(
        BASE, params={"int1": 2, "int2": 3, "limit": 6, "str1": "Foo", "str2": "Bar"}
    )
    assert response.status_code == 200
    assert response.json()["result"] == ["1", "Foo", "Bar", "Foo", "5", "FooBar"]
