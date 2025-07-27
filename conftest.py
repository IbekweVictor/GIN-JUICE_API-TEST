import pytest
import requests
from utils.config import BASE_URL

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def session():
    return requests.Session()
