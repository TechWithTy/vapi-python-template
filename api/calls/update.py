from typing import Optional
from ..client import get_client


def update_call(call_id: str) -> Optional[dict]:
    """
    Update a call using the Vapi SDK.

    Args:
        call_id (str): The ID of the call to update.

    Returns:
        Optional[dict]: The response from the API if successful, None otherwise.
    """
    try:
        client = get_client()
        return client.calls.update(id=call_id)
    except Exception as e:
        print(f"Error updating call: {e}")
        return None
