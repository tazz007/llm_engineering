import os
from dotenv import load_dotenv
import requests

def chat_completion():
    load_dotenv(override=True)
    endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ.get("OPENAI_API_KEY"),
    }
    body = {
        "model": "gpt-5-nano",
        "messages": [
            {
                "role": "user",
                "content": "tell me a funny story"
            }
        ]
    }
    response = requests.post(endpoint, headers=headers, json=body)
    print(response.json())