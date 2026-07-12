import requests


def test_put_positive(base_url, api_key):
    payload = {"id": "1", "first_name": "manas"}
    api = {"x-api-key": api_key}
    response = requests.put(f"{base_url}/1", headers=api, json=payload)
    assert response.status_code == 200
    assert response.json()["first_name"] == "manas"


def test_put_negative_missing_header(base_url):
    payload = {"id": "1", "first_name": "manas"}
    response = requests.put(f"{base_url}/1", json=payload)
    assert response.status_code == 401