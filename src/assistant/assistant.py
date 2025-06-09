import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
HF_TOKEN = os.getenv("HF_TOKEN")

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def ask_assistant(user_input):
    payload = {"inputs": user_input}
    response = requests.post(API_URL, headers=headers, json=payload)
    print("Status:", response.status_code)
    print("Response:", response.text)
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()
        else:
            return "Sorry, I couldn't understand the response."
    else:
        return "Sorry, the AI assistant is currently unavailable."