import requests
import json

model = "llama3.1"
prompt = "Filter this list and return ONLY the vegetables. Output as a JSON array of strings, nothing else."
stream = False
url = "http://192.168.39.179:11434/api/generate"

def generate_filtered_list(sorted_types):
    payload = {
        "model": model,
        "prompt": f"{prompt} List: {sorted_types}",
        "stream": False,
        "format": "json"
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        raw_text = response.json()['response']
        clean_list = json.loads(raw_text)

        print(f"Success!\n{clean_list}")
        return clean_list
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []
    except json.JSONDecodeError:
        print("Ollama ignored the JSON format command.")
        return []