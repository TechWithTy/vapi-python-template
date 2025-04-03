import requests  # Make sure to import the requests library
import os

# Function to delete an assistant by ID
def delete_assistant_by_id(assistant_id: str) -> None:
    VAPI_URL = f'https://api.vapi.ai/assistant/{assistant_id}'  # Corrected URL
    VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")

    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    # Example query parameters (if needed)
    params = {
        'force': 'true'  # Example: Force deletion if applicable
    }

    response = requests.delete(VAPI_URL, headers=headers, params=params)

    if response.status_code != 200:
        error = response.text
        raise Exception(f'Error deleting assistant: {error}')

    print(f'Assistant with ID {assistant_id} deleted successfully.')


