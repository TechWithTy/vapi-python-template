import os
import requests

def list_files():
    api_key = os.getenv('VAPI_PRIVATE_KEY')
    url = "https://api.vapi.ai/file"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    files = list_files()
    for file in files:
        print(f"File ID: {file['id']}")
        print(f"Name: {file['name']}")
        print(f"Status: {file['status']}")
        print("---")
