import requests
import os
from typing import Dict, Any

# Function to get a squad by ID
def get_squad_by_id(squad_id: str) -> Dict[str, Any]:
    """
    Fetch squad details by ID from the VAPI AI API.
    
    :param squad_id: The ID of the squad to fetch.
    :return: JSON response data from the API.
    """
    VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")
    url = f"https://api.vapi.ai/squad/{squad_id}"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f"Error fetching squad: {error_text}")
            
        squad_data = response.json()
        return squad_data
        
    except Exception as err:
        print("Error:", err)
        raise err
