import logging
import requests

from config.config import BASE_URL


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIClient:

    def get(self, endpoint):
        logger.info(f"GET request: {endpoint}")
        return requests.get(f"{BASE_URL}{endpoint}")

    def post(self, endpoint, payload):
        logger.info(f"POST request: {endpoint}")
        return requests.post(f"{BASE_URL}{endpoint}", json=payload)

    def put(self, endpoint, payload):
        logger.info(f"PUT request: {endpoint}")
        return requests.put(f"{BASE_URL}{endpoint}", json=payload)

    def delete(self, endpoint):
        logger.info(f"DELETE request: {endpoint}")
        return requests.delete(f"{BASE_URL}{endpoint}")