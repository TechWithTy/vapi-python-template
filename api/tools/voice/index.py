import requests
import os

# Base URL for VAPI API (replace with actual URL from VAPI docs)
VAPI_BASE_URL = 'https://api.vapi.ai'

# API key or token for VAPI API (replace with your actual API key/token)
VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")

def sync_voice_with_vapi(customer_id: str, voice_id: str) -> None:
    """
    Sync a cloned voice with VAPI.
    
    Args:
        customer_id: The unique ID of the customer
        voice_id: The cloned voice ID from ElevenLabs
        
    Returns:
        None
    
    Raises:
        Exception: If the sync operation fails
    """
    url = f"{VAPI_BASE_URL}/vapi/voices/sync"
    
    payload = {
        "customerId": customer_id,
        "voiceId": voice_id
    }
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            print(f"Voice ID {voice_id} synced successfully for customer {customer_id}")
        else:
            print(f"Failed to sync voice for customer {customer_id}: {response.reason}")
            raise Exception(f"Failed to sync voice: {response.reason}")
    except Exception as error:
        print(f"Error syncing voice with VAPI: {error}")
        raise Exception("Sync with VAPI failed.")

def fetch_customer_voices(customer_id: str) -> list:
    """
    Fetch all cloned voices for a specific customer from VAPI.
    
    Args:
        customer_id: The unique ID of the customer
        
    Returns:
        A list of voices for the customer
        
    Raises:
        Exception: If fetching voices fails
    """
    url = f"{VAPI_BASE_URL}/vapi/voices/customer/{customer_id}"
    
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            voices = response.json().get("voices", [])
            print(f"Fetched {len(voices)} voices for customer {customer_id}")
            return voices
        else:
            print(f"Failed to fetch voices for customer {customer_id}: {response.reason}")
            raise Exception(f"Failed to fetch voices: {response.reason}")
    except Exception as error:
        print(f"Error fetching customer voices from VAPI: {error}")
        raise Exception("Fetch customer voices failed.")
