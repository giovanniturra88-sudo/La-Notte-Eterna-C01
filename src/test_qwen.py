import requests

URL = "http://172.16.1.163:11434/api/generate"

response = requests.post(
    URL,
    json={
        "model": "qwen3.6:35b",
        "prompt": "Rispondi solo con: OK",
        "stream": False
    },
    timeout=300
)

print(response.json()["response"])