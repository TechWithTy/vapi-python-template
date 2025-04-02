import os
import requests
from typing import Dict, Any

VAPI_API_KEY = os.getenv('VAPI_PRIVATE_KEY')  # Get API key from environment variable

def delete_phone_number_by_id(phone_number_id: str) -> Dict[str, Any]:
    """
    Delete a phone number by ID using the VAPI AI API.
    
    :param phone_number_id: The ID of the phone number to delete.
    :return: JSON response data from the API.
    """
    url = f"https://api.vapi.ai/phone-number/{phone_number_id}"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.delete(url, headers=headers)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f"Error deleting phone number: {error_text}")
            
        response_data = response.json()
        return response_data
        
    except Exception as err:
        print("Error:", err)
        raise err

# Example usage
# deleted_phone_number = delete_phone_number_by_id("phone-number-id-123")
# print("Deleted Phone Number:", deleted_phone_number)
