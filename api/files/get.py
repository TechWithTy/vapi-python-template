import os
import requests

def get_file(file_id):
    api_key = os.getenv('VAPI_PRIVATE_KEY')
    url = f"https://api.vapi.ai/file/{file_id}"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()

# Example usage:
# file_data = get_file("your_file_id_here")
# print(file_data)