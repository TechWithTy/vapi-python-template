import os
import requests
from typing import Dict, Any

# Retrieve API key from environment variables
VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")

def delete_tool_by_id(tool_id: str) -> Dict[str, Any]:
    """
    Delete a tool by ID using the VAPI AI API.
    
    :param tool_id: The ID of the tool to delete.
    :return: JSON response data from the API.
    """
    url = f"https://api.vapi.ai/tool/{tool_id}"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.delete(url, headers=headers)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f"Error deleting tool: {error_text}")
            
        response_data = response.json()
        return response_data
        
    except Exception as err:
        print("Error:", err)
        raise err

