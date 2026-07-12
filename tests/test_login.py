import requests


def test_login_positive(login_url, api_key):
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(login_url, json=payload, headers={"x-api-key": api_key})
    assert response.status_code == 200
    assert "token" in response.json()


def test_login_negative_wrong_email(login_url, api_key):
    payload = {"email": "wrong@example.com", "password": "cityslicka"}
    response = requests.post(login_url, headers={"x-api-key": api_key}, json=payload)
    assert response.status_code == 400
    assert "error" in response.json()


def test_login_negative_missing_password(login_url, api_key):
    payload = {"email": "eve.holt@reqres.in"}
    response = requests.post(login_url, headers={"x-api-key": api_key}, json=payload)
    assert response.status_code == 400
    assert "error" in response.json()