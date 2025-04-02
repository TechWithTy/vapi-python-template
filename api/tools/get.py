import os
import requests
from typing import Dict, Any

# Retrieve API key from environment variables
VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")

def get_tool_by_id(tool_id: str) -> Dict[str, Any]:
    """
    Fetch tool details by ID from the VAPI AI API.
    
    :param tool_id: The ID of the tool to fetch.
    :return: JSON response data from the API.
    """
    url = f"https://api.vapi.ai/tool/{tool_id}"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f"Error fetching tool: {error_text}")
            
        tool_data = response.json()
        print("Tool fetched successfully:", tool_data)
        return tool_data
        
    except Exception as err:
        print("Error:", err)
        raise err

