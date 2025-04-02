import os
import requests

VAPI_API_KEY = os.getenv('VAPI_PRIVATE_KEY')  # Get API key from environment variable

def get_call_by_id(call_id: str) -> dict:
    """
    Fetch call details by ID from the VAPI AI API.

    :param call_id: The ID of the call to fetch.
    :return: JSON response data from the API or None if an error occurs.
    """
    if not VAPI_API_KEY:
        print("Error: Missing API key. Set VAPI_PRIVATE_KEY in your environment variables.")
        return None

    url = f"https://api.vapi.ai/call/{call_id}"
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for non-200 responses

        call_data = response.json()
        return call_data

    except requests.exceptions.RequestException as err:
        print("Error:", err)
        return None
