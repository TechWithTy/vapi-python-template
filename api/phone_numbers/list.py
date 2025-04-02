import requests
import os
from typing import Dict, Any, List, Optional

# Function to list phone numbers with optional query parameters
def list_phone_numbers(
    limit: int = 100,
    created_at_gt: Optional[str] = None,
    created_at_lt: Optional[str] = None,
    updated_at_gt: Optional[str] = None,
    updated_at_lt: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Fetch a list of phone numbers with optional filtering parameters.
    
    :param limit: Maximum number of phone numbers to return
    :param created_at_gt: Filter for phone numbers created after this timestamp
    :param created_at_lt: Filter for phone numbers created before this timestamp
    :param updated_at_gt: Filter for phone numbers updated after this timestamp
    :param updated_at_lt: Filter for phone numbers updated before this timestamp
    :return: List of phone number objects
    """
    api_key = os.getenv('VAPI_PRIVATE_KEY')
    url = "https://api.vapi.ai/phone-number"
    
    # Add query parameters if provided
    params = {'limit': limit}
    if created_at_gt:
        params['createdAtGt'] = created_at_gt
    if created_at_lt:
        params['createdAtLt'] = created_at_lt
    if updated_at_gt:
        params['updatedAtGt'] = updated_at_gt
    if updated_at_lt:
        params['updatedAtLt'] = updated_at_lt
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f"Error listing phone numbers: {error_text}")
        
        response_data = response.json()
        return response_data
        
    except Exception as err:
        print("Error:", err)
        raise err

# Example usage
# phone_numbers = list_phone_numbers(
#     limit=50,
#     created_at_gt="2023-01-01T00:00:00Z",
#     updated_at_gt="2023-12-31T23:59:59Z"
# )
# print("Phone Numbers:", phone_numbers)

# Example response structure
