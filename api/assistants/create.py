import requests
import json
import os

# Retrieve API key from environment variables
VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")
VAPI_URL = "https://api.vapi.ai/assistant"

HEADERS = {
    "Authorization": f"Bearer {VAPI_API_KEY}",
    "Content-Type": "application/json",
}


def create_assistant(payload: dict) -> dict:
    """
    Creates an assistant on the VAPI platform.

    :param payload: A dictionary containing the assistant configuration.
    :return: JSON response data from the API or None if an error occurs.
    """
    if not VAPI_API_KEY:
        print("Error: Missing API key. Set VAPI_API_KEY in your environment variables.")
        return None

    try:
        response = requests.post(VAPI_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise error for non-200 responses
        data = response.json()

        print("Assistant Created:", json.dumps(data, indent=4))
        return data

    except requests.exceptions.RequestException as err:
        print("Error:", err)
        return None

example_payload = {
        "transcriber": {
            "provider": "deepgram",
            "model": "nova-2",
            "language": "en",
            "smartFormat": False,
            "keywords": ["example", "test"],
            "endpointing": 255,
        },
        "model": {
            "messages": [
                {"content": "Hello, how may I assist you today?", "role": "assistant"}
            ],
            "tools": [
                {
                    "async": False,
                    "messages": [
                        {
                            "type": "request-start",
                            "content": "Starting tool...",
                            "role": "assistant",
                            "conditions": [
                                {"value": "start", "operator": "eq", "param": "status"}
                            ],
                        }
                    ],
                    "type": "dtmf",
                    "function": {
                        "name": "ProcessPayment",
                        "description": "This function processes payments.",
                        "parameters": {
                            "type": "object",
                            "properties": {},
                            "required": ["amount"],
                        },
                    },
                    "server": {
                        "timeoutSeconds": 20,
                        "url": "https://example.com/process-payment",
                        "secret": "my-secret",
                    },
                }
            ],
            "toolIds": ["tool-123"],
            "provider": "anyscale",
            "model": "gpt-3",
            "temperature": 1,
            "knowledgeBase": {
                "provider": "canonical",
                "topK": 5,
                "fileIds": ["file-123"],
            },
            "maxTokens": 500,
            "emotionRecognitionEnabled": True,
            "numFastTurns": 1,
        },
        "voice": {
            "fillerInjectionEnabled": False,
            "provider": "azure",
            "voiceId": "andrew",
            "speed": 1.25,
            "chunkPlan": {
                "enabled": True,
                "minCharacters": 30,
                "punctuationBoundaries": [".", "!", "?"],
                "formatPlan": {"enabled": True, "numberToDigitsCutoff": 2025},
            },
        },
        "firstMessageMode": "assistant-speaks-first",
        "recordingEnabled": True,
        "hipaaEnabled": False,
        "clientMessages": ["conversation-update", "function-call"],
        "serverMessages": ["conversation-update", "end-of-call-report"],
        "silenceTimeoutSeconds": 30,
        "maxDurationSeconds": 600,
        "backgroundSound": "office",
        "backchannelingEnabled": False,
        "backgroundDenoisingEnabled": False,
        "modelOutputInMessagesEnabled": False,
        "transportConfigurations": [
            {
                "provider": "twilio",
                "timeout": 60,
                "record": False,
                "recordingChannels": "mono",
            }
        ],
        "name": "Test Assistant",
        "firstMessage": "Hello! How can I assist you today?",
        "voicemailDetection": {
            "provider": "twilio",
            "voicemailDetectionTypes": ["machine_end_beep"],
            "enabled": True,
            "machineDetectionTimeout": 31,
            "machineDetectionSpeechThreshold": 3500,
            "machineDetectionSpeechEndThreshold": 2750,
            "machineDetectionSilenceTimeout": 6000,
        },
        "voicemailMessage": "Please leave a message after the beep.",
        "endCallMessage": "Thank you for calling, goodbye!",
        "endCallPhrases": ["goodbye", "bye"],
        "metadata": {},
        "serverUrl": "https://example.com/server-url",
        "serverUrlSecret": "my-server-secret",
        "analysisPlan": {
            "summaryPrompt": "Summarize the conversation.",
            "summaryRequestTimeoutSeconds": 10,
            "structuredDataRequestTimeoutSeconds": 10,
            "successEvaluationPrompt": "Was this successful?",
            "successEvaluationRubric": "NumericScale",
            "successEvaluationRequestTimeoutSeconds": 10,
            "structuredDataPrompt": "Provide structured data.",
            "structuredDataSchema": {
                "type": "string",
                "items": {},
                "properties": {},
                "description": "Schema description",
                "required": ["requiredField"],
            },
        },
        "artifactPlan": {
            "videoRecordingEnabled": True,
            "recordingS3PathPrefix": "s3://my-recordings/",
        },
        "messagePlan": {
            "idleMessages": ["Please hold."],
            "idleMessageMaxSpokenCount": 5,
            "idleTimeoutSeconds": 20,
        },
        "startSpeakingPlan": {
            "waitSeconds": 0.4,
            "smartEndpointingEnabled": False,
            "transcriptionEndpointingPlan": {
                "onPunctuationSeconds": 0.1,
                "onNoPunctuationSeconds": 1.5,
                "onNumberSeconds": 0.5,
            },
        },
        "stopSpeakingPlan": {"numWords": 0, "voiceSeconds": 0.2, "backoffSeconds": 1},
        "credentialIds": ["credential-123"],
    }
