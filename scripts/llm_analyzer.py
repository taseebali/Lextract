# ...existing code...
import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def analyze_contract_ollama(contract_text):
    # ...existing code...
    prompt = ("You are a contract analysis expert.\n"
        "Here's a legal contract. Summarize it in plain English. Then:\n"
        "1. List the major clauses and their meanings\n"
        "2. Point out any potentially risky or unclear language\n"
        "3. Suggest additional clauses to protect the individual\n\n"
        f"Contract:\n{contract_text}"
    )
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_API_URL, json = payload)
    response.raise_for_status()
    return response.json()["response"]
# ...existing code...
