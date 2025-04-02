import aiohttp
import asyncio
import json
import os
# Function to get an assistant by ID
async def get_assistant_by_id(assistant_id: str):
    VAPI_URL = f'https://api.vapi.ai/assistant/{assistant_id}'
    VAPI_API_KEY = os.getenv("VAPI_PRIVATE_KEY")

    headers = {
        'Authorization': f'Bearer {VAPI_API_KEY}',
        'Content-Type': 'application/json'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(VAPI_URL, headers=headers) as response:
            if response.status != 200:
                error = await response.text()
                raise Exception(f'Error fetching assistant: {error}')
            
            assistant = await response.json()
            return assistant

