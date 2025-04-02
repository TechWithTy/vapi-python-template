import requests
import json
import os

VAPI_API_KEY = os.getenv('VAPI_PRIVATE_KEY')  # Get API key from environment variable

# Function to create a call
def create_call(api_url: str, call_request_data: dict) -> dict:
    headers = {
        'Authorization': f'Bearer {VAPI_API_KEY}',
        'Content-Type': 'application/json'
    }

    # Send POST request with the request body
    try:
        response = requests.post(api_url, headers=headers, json=call_request_data)

        if response.status_code != 200:
            # Handle non-200 responses
            error_text = response.text
            raise Exception(f'Error creating call: {error_text}')

        # Parse the JSON response if the call was successful
        response_data = response.json()
        print('Call created successfully:', response_data)

        return response_data  # Return the response data if needed

    except Exception as error:
        print('Error:', error)
        raise error  # Re-throw the error if needed for further handling

  