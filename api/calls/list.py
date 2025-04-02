import requests
import os


VAPI_API_KEY = os.getenv('VAPI_PRIVATE_KEY')  # Get API key from environment variable


def list_calls(params=None):
    """
    Fetch list of calls with query parameters.

    :param params: Optional query parameters to filter the call list.
    :return: The call list response data.
    """
    if not params:
        params = {}

    url = "https://api.vapi.ai/call"
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers, params=params)

    if not response.ok:
        error = response.text
        raise Exception(f"Error fetching call list: {error}")

    call_list_data = response.json()
    return call_list_data
