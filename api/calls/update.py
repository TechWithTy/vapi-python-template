import os
import requests
import json

VAPI_API_KEY = os.getenv('VAPI_PRIVATE_KEY')  # Get API key from environment variable

def update_call(call_id: str, request_body: dict) -> dict:
    """
    Update a call by ID using the VAPI AI API.
    
    :param call_id: The ID of the call to update.
    :param request_body: Dictionary containing the fields to update.
    :return: JSON response data from the API.
    """
    url = f"https://api.vapi.ai/call/{call_id}"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.patch(url, headers=headers, json=request_body)
        
        if not response.ok:
            error = response.text
            raise Exception(f"Error updating call: {error}")
            
        updated_call_data = response.json()
        return updated_call_data
    
    except Exception as err:
        print("Error:", err)
        raise err

# Example usage
# request_body = {
#     "name": "Updated Call Name"  # Updating the name of the call
# }
# 
# updated_call = update_call("call-id-123", request_body)
# print("Updated call:", updated_call)

