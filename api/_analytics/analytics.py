import requests
import json
import os  

# Retrieve API token from environment variables
API_TOKEN = os.getenv("VAPI_PRIVATE_TOKEN")  
API_URL = "https://api.vapi.ai/analytics"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def fetch_analytics(payload: dict):
    """
    Fetch analytics data from the VAPI AI API with a given payload.
    
    :param payload: A dictionary containing the API request payload.
    :return: JSON response data or None if an error occurs.
    """
    if not API_TOKEN:
        print("Error: Missing API token. Set VAPI_PRIVATE_TOKEN in your environment variables.")
        return None

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()
        
        print(json.dumps(data, indent=4))  # Pretty print the response
        
        for query_result in data.get("data", []):
            print("Query Name:", query_result.get("name"))
            print("Time Range:", query_result.get("timeRange"))
            
            for result in query_result.get("result", []):
                print("Date:", result.get("date"))
                print("Assistant ID:", result.get("assistantId"))
                print("Ended Reason:", result.get("endedReason"))
                print("Sum Duration:", result.get("sumDuration"))
                print("Avg Cost:", result.get("avgCost"))
        
        return data

    except requests.exceptions.RequestException as err:
        print("Error:", err)
        return None


example_analytics_payload = {
        "queries": [
            {
                "table": "call",
                "groupBy": ["assistantId", "endedReason"],
                "name": "callAnalyticsQuery",
                "timeRange": {
                    "step": "day",
                    "start": "2023-01-01T00:00:00Z",
                    "end": "2023-01-31T23:59:59Z",
                    "timezone": "UTC"
                },
                "operations": [
                    {"operation": "sum", "column": "duration", "alias": "sumDuration"},
                    {"operation": "avg", "column": "cost", "alias": "avgCost"}
                ]
            }
        ]
    }