import os
import requests

def update_file(file_id, update_data):
    api_key = os.getenv('VAPI_PRIVATE_KEY')
    url = f"https://api.vapi.ai/file/{file_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    response = requests.patch(url, headers=headers, json=update_data)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Example usage:
# file_id = "your_file_id"
# update_data = {"name": "new_file_name", "purpose": "new_purpose"}
# updated_file = update_file(file_id, update_data)
# print(updated_file)