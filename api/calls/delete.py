import os
import requests

VAPI_API_KEY = os.getenv('VAPI_PRIVATE_KEY')  # Get API key from environment variable

# Function to delete a call by ID
def delete_call_by_id(call_id: str) -> dict:
    url = f"https://api.vapi.ai/call/{call_id}"

    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.delete(url, headers=headers)

        if not response.ok:
            error = response.text
            raise Exception(f"Error deleting call: {error}")

        delete_call_data = response.json()
        return delete_call_data
    except Exception as err:
        print("Error:", err)
        raise err


example_delete_response = {
    "id": "call-id-123",
    "status": "ended",
    "endedReason": "manually-canceled",
    "type": "inboundPhoneCall",
    "phoneCallProvider": "twilio",
    "messages": [],
    "createdAt": "2023-09-07T12:00:00Z",
    "updatedAt": "2023-09-07T12:30:00Z"
}
