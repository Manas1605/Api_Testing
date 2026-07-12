import requests


def test_post_positive(base_url, api_key):
    payload = {"name": "manas", "job": "unemployed"}
    api = {"x-api-key": api_key}
    response = requests.post(base_url, headers=api, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "manas"


def test_post_negative_missing_header(base_url):
    payload = {"name": "manas", "job": "unemployed"}
    response = requests.post(base_url, json=payload)
    assert response.status_code == 401