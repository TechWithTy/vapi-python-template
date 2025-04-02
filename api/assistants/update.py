import requests
import json
import os

# Function to update an assistant by ID
def update_assistant_by_id(assistant_id: str, update_data: dict) -> None:
    VAPI_URL = f'https://api.vapi.ai/assistant/{assistant_id}'
    VAPI_API_KEY = os.getenv('VAPI_PRIVATE_KEY')  # Get API key from environment variable

    headers = {
        'Authorization': f'Bearer {VAPI_API_KEY}',
        'Content-Type': 'application/json'
    }

    # Send PATCH request with JSON body
    response = requests.patch(VAPI_URL, headers=headers, data=json.dumps(update_data))

    if response.status_code != 200:
        error = response.text
        raise Exception(f'Error updating assistant: {error}')

    # Parse the response JSON if the update was successful
    updated_assistant = response.json()
    print('Assistant updated successfully:', updated_assistant)

