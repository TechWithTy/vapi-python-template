import aiohttp
import os
from typing import Optional

# Function to list assistants with optional query parameters
async def list_assistants(
    limit: int = 100,  # Default limit
    created_at_gt: Optional[str] = None,  # Optional: created after this date
    created_at_lt: Optional[str] = None,  # Optional: created before this date
    updated_at_gt: Optional[str] = None,  # Optional: updated after this date
    updated_at_lt: Optional[str] = None   # Optional: updated before this date
):
    VAPI_URL = 'https://api.vapi.ai/assistant'
    VAPI_API_KEY = os.getenv('VAPI_PRIVATE_KEY')  # Get API key from environment variable

    # Construct query parameters
    params = {
        'limit': str(limit),
        'createdAtGt': created_at_gt,
        'createdAtLt': created_at_lt,
        'updatedAtGt': updated_at_gt,
        'updatedAtLt': updated_at_lt
    }
    # Remove any parameters that are None
    params = {key: value for key, value in params.items() if value is not None}

    # Construct the full URL with query parameters
    async with aiohttp.ClientSession() as session:
        async with session.get(VAPI_URL, headers={
            'Authorization': f'Bearer {VAPI_API_KEY}',
            'Content-Type': 'application/json'
        }, params=params) as response:
            if response.status != 200:
                error = await response.text()
                raise Exception(f'Error listing assistants: {error}')
            
            assistants_list = await response.json()
            return assistants_list

