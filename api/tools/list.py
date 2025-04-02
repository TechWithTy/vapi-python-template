import requests
import os
from typing import Dict, Any, Optional

# Retrieve API key from environment variables
VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")

def list_tools(
    limit: int = 100,
    created_at_gt: Optional[str] = None,
    created_at_lt: Optional[str] = None,
    updated_at_gt: Optional[str] = None,
    updated_at_lt: Optional[str] = None
) -> Dict[str, Any]:
    """
    Fetch a list of tools with optional filtering parameters.
    
    :param limit: Maximum number of tools to return
    :param created_at_gt: Filter for tools created after this timestamp
    :param created_at_lt: Filter for tools created before this timestamp
    :param updated_at_gt: Filter for tools updated after this timestamp
    :param updated_at_lt: Filter for tools updated before this timestamp
    :return: Dictionary containing tool list
    """
    url = "https://api.vapi.ai/tool"
    
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
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        if not response.ok:
            error_text = response.text
            raise Exception(f"Error listing tools: {error_text}")
        
        return response.json()
        
    except Exception as err:
        print("Error:", err)
        raise err

# Example usage
# tools = list_tools(
#     limit=50,
#     created_at_gt="2023-01-01T00:00:00Z"
# )
# print("Tools:", tools)
