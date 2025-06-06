from typing import Optional, List
from ..client import get_client

def list_phone_numbers() -> Optional[List[dict]]:
    """
    List phone numbers using the Vapi SDK.

    Returns:
        Optional[List[dict]]: The response from the API if successful, None otherwise.
    """
    try:
        client = get_client()
        return client.phone_numbers.list()
    except Exception as e:
        print(f"Error listing phone numbers: {e}")
        return None
