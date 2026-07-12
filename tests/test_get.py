import requests


def test_get_positive(base_url, api_key):
    response = requests.get(base_url, headers={"x-api-key": api_key})
    assert response.status_code == 200
    assert response.json()["page"] == 1
    assert response.json()["data"][1]["id"] == 2
    assert response.json()["data"][0]["first_name"] == "George"


def test_get_negative_invalid_user_id(base_url, api_key):
    response = requests.get(f"{base_url}/999999", headers={"x-api-key": api_key})
    assert response.status_code == 404
      