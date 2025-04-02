import requests
import os
from typing import Dict, Any, Optional

def update_phone_number(phone_number_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update a phone number using the VAPI AI API.
    
    :param phone_number_id: The ID of the phone number to update
    :param update_data: Dictionary containing the phone number update data
    :return: JSON response data from the API
    """
    api_url = f'https://api.vapi.ai/phone-number/{phone_number_id}'
    api_key = os.getenv('VAPI_PRIVATE_KEY')
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.patch(api_url, headers=headers, json=update_data)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f'Error updating phone number: {error_text}')
            
        response_data = response.json()
        print('Phone number updated successfully:', response_data)
        
        return response_data
        
    except Exception as error:
        print('Error:', error)
        raise error

# Example usage
update_data = {
    "fallbackDestination": {
        "type": "number",
        "numberE164CheckEnabled": True,
        "number": "+14155551234",
        "extension": "1234",
        "message": "Fallback message",
        "description": "Fallback description"
    },
    "provider": "byo_phone_number",
    "numberE164CheckEnabled": True,
    "name": "Updated Phone Number",
    "assistantId": "assistant-123",
    "squadId": "squad-123",
    "serverUrl": "https://updated-server-url.com",
    "serverUrlSecret": "updated-secret-key",
    "number": "+14155551234",
    "credentialId": "credential-123"
}

# Uncomment to run
# updated_phone_number = update_phone_number("phone-number-123", update_data)
# print("Updated Phone Number:", updated_phone_number)
