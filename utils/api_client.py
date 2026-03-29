"""
Cliente HTTP con logging
"""

import requests
from utils.logger import logger

BASE_URL = "https://jsonplaceholder.typicode.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}


def get(endpoint, headers=None):
    final_headers = HEADERS.copy()
    if headers:
        final_headers.update(headers)

    url = f"{BASE_URL}{endpoint}"

    logger.info(f"GET Request: {url}")

    response = requests.get(url, headers=final_headers)

    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

    return response


def post(endpoint, data=None, headers=None):
    final_headers = HEADERS.copy()
    if headers:
        final_headers.update(headers)

    url = f"{BASE_URL}{endpoint}"

    logger.info(f"POST Request: {url}")
    logger.info(f"Payload: {data}")

    response = requests.post(url, json=data, headers=final_headers)

    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")

    return response