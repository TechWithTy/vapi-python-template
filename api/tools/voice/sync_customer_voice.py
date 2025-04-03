
from typing import List, Dict, Any
import os

VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")

# Import from the same directory
from . import sync_voice_with_vapi, fetch_customer_voices

def sync_customer_voice_with_vapi(customer_id: str, voice_id: str) -> None:
    """
    Sync the cloned voice with VAPI for the given customer
    
    Args:
        customer_id: The unique ID of the customer
        voice_id: The cloned voice ID from ElevenLabs
        
    Returns:
        None
        
    Raises: 
        Exception: If the sync operation fails
    """
    try:
        # Sync the cloned voice with VAPI
        sync_voice_with_vapi(customer_id, voice_id)
        print(f"Successfully synced voice {voice_id} for customer {customer_id}")
    except Exception as error:
        print(f"Error syncing voice {voice_id} for customer {customer_id}: {error}")
        raise Exception("Failed to sync voice with VAPI")

def get_customer_voices(customer_id: str) -> List[Dict[str, Any]]:
    """
    Fetch only the voices for the authenticated customer from VAPI
    
    Args:
        customer_id: The unique ID of the customer
        
    Returns:
        List of voice data for that customer
        
    Raises:
        Exception: If fetching voices fails
    """
    try:
        # Fetch voices for this customer from VAPI
        voices = fetch_customer_voices(customer_id)
        print(f"Fetched {len(voices)} voices for customer {customer_id}")
        return voices
    except Exception as error:
        print(f"Error fetching voices for customer {customer_id}: {error}")
        raise Exception("Failed to fetch customer voices")
