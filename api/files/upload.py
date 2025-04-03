import os
import requests

def upload_file(file_path):
    api_key = os.getenv('VAPI_PRIVATE_KEY')
    url = 'https://api.vapi.ai/file'
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, headers=headers, files=files)
    
    if response.status_code == 201:
        return response.json()
    else:
        response.raise_for_status()