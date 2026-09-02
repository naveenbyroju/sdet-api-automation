import requests

from config.config import BASE_URL


class APIClient:

    def get(self, endpoint):
        response = requests.get(f"{BASE_URL}{endpoint}")
        return response