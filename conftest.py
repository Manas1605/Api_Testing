import os
import pytest

@pytest.fixture
def base_url():
    return "https://reqres.in/api/users"
@pytest.fixture
def api_key():
    
    return os.getenv("key","free_user_3G1lwUrEAQ09JFT1RnnAYbffByF")

@pytest.fixture
def login_url():
    return "https://reqres.in/api/login"