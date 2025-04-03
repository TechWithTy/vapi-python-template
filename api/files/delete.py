import os
import requests
from typing import Dict, Any

VAPI_API_KEY = os.getenv('VAPI_PRIVATE_KEY')

def delete_file(file_id: str) -> Dict[str, Any]:
    """
    Delete a file by ID using the VAPI AI API.
    
    :param file_id: The ID of the file to delete.
    :return: JSON response data from the API.
    """
    url = f"https://api.vapi.ai/file/{file_id}"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.delete(url, headers=headers)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f"Error deleting file: {error_text}")
            
        response_data = response.json()
        return response_data
        
    except Exception as err:
        print("Error:", err)
        raise err

# Example usage
if __name__ == "__main__":
    file_id = "your_file_id_here"
    result = delete_file(file_id)
    print(result)