import requests

from config.config import BASE_URL


class APIClient:

    def get(self, endpoint):
        response = requests.get(f"{BASE_URL}{endpoint}")
        return response

    def post(self, endpoint, payload):
        response = requests.post(
            f"{BASE_URL}{endpoint}",
            json=payload
        )
        return response