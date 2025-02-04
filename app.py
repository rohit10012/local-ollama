import requests
import json

# Define the Ollama API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

# Define the payload
payload = {
    "model": "deepseek-r1:1.5b",
    "prompt": input("Enter your prompt: "),
    "stream": False
}

# Send the request
response = requests.post(OLLAMA_URL, json=payload)

# Parse and print the response
if response.status_code == 200:
    data = response.json()
    print(data["response"])
else:
    print("Error:", response.status_code, response.text)
