import requests
import os
import json
from typing import Dict, Any, Optional

# API call to create a phone number
def create_phone_number(
    api_url: str, 
    phone_number_request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Create a phone number using the VAPI AI API.
    
    :param api_url: The API URL endpoint for creating phone numbers
    :param phone_number_request_data: Dictionary containing the phone number configuration
    :return: JSON response data from the API
    """
    api_key = os.getenv('VAPI_PRIVATE_KEY')
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=phone_number_request_data)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f'Error creating phone number: {error_text}')
            
        response_data = response.json()
        print('Phone number created successfully:', response_data)
        
        return response_data
        
    except Exception as error:
        print('Error:', error)
        raise error

# Example usage of the create_phone_number function
api_url = 'https://api.vapi.ai/phone-number'

phone_number_request_data = {
    "fallbackDestination": {
        "type": "number",
        "numberE164CheckEnabled": True,
        "number": "+14155551234",
        "extension": "123",
        "message": "This is a fallback message.",
        "description": "Fallback description."
    },
    "provider": "byo_phone_number",
    "numberE164CheckEnabled": True,
    "number": "+14155551234",
    "credentialId": "credential-id-123",
    "name": "Test Phone Number",
    "assistantId": "assistant-id-123",
    "squadId": "squad-id-123",
    "serverUrl": "https://server.url",
    "serverUrlSecret": "server-secret-123"
}
