import requests
import os
from typing import Dict, Any, Optional

def get_phone_number_by_id(phone_number_id: str) -> Dict[str, Any]:
    """
    Fetch phone number details by ID using the VAPI AI API.
    
    :param phone_number_id: The ID of the phone number to fetch
    :return: JSON response data from the API
    """
    api_url = f'https://api.vapi.ai/phone-number/{phone_number_id}'
    api_key = os.getenv('VAPI_PRIVATE_KEY')
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f'Error fetching phone number: {error_text}')
            
        response_data = response.json()
        print('Phone number fetched successfully:', response_data)
        
        return response_data
        
    except Exception as error:
        print('Error:', error)
        raise error
