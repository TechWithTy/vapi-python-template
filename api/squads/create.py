import requests
import json
import os

# Retrieve API key from environment variables
VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")
VAPI_URL = "https://api.vapi.ai/squad"

def create_squad(payload: dict) -> dict:
    """
    Creates a squad on the VAPI platform.

    :param payload: A dictionary containing the squad configuration.
    :return: JSON response data from the API or None if an error occurs.
    """
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(VAPI_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise error for non-200 responses
        data = response.json()

        print("Squad Created:", json.dumps(data, indent=4))
        return data

    except requests.exceptions.RequestException as err:
        print("Error:", err)
        raise err


