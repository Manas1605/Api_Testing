import requests


def test_delete_positive(base_url, api_key):
    response = requests.delete(f"{base_url}/1", headers={"x-api-key": api_key})
    assert response.status_code == 204


def test_delete_negative_missing_header(base_url):
    response = requests.delete(f"{base_url}/1")
    assert response.status_code == 401