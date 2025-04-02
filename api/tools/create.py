import requests
import json
import os

# Retrieve API key from environment variables
VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")
VAPI_URL = "https://api.vapi.ai/tool"

def create_tool(tool_data: dict) -> dict:
    """
    Creates a tool on the VAPI platform.

    :param tool_data: A dictionary containing the tool configuration.
    :return: JSON response data from the API or None if an error occurs.
    """
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(VAPI_URL, headers=headers, json=tool_data)
        response.raise_for_status()  # Raise error for non-200 responses
        
        response_data = response.json()
        print("Tool created successfully:", json.dumps(response_data, indent=4))
        return response_data

    except requests.exceptions.RequestException as error:
        print("Error creating tool:", error)
        raise error

