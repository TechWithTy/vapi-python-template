import requests
import os
import json
from typing import Dict, Any

# Retrieve API key from environment variables
VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")

def update_squad(squad_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update a squad by ID using the VAPI AI API.
    
    :param squad_id: The ID of the squad to update.
    :param update_data: Dictionary containing the squad update data.
    :return: JSON response data from the API.
    """
    url = f"https://api.vapi.ai/squad/{squad_id}"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.patch(url, headers=headers, json=update_data)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f"Error updating squad: {error_text}")
            
        updated_squad = response.json()
        return updated_squad
        
    except Exception as err:
        print("Error:", err)
        raise err


# Uncomment to run
# updated_squad = update_squad(squad_id, update_data)
# print("Updated Squad:", updated_squad)

