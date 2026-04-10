import requests
import json

model = "llama3.1"
prompt = "Filter this list for vegetables. Return ONLY a plain JSON array of strings. Example Output: ['carrot', 'potato'] List: [YOUR_DATA]"
stream = False
url = "http://192.168.39.179:11434/api/generate"

def generate_filtered_list(sorted_types):
    if len(sorted_types) > 50:
        print(f"[ollama_client] {len(sorted_types)} types in veg-list. Splitting...")
        batches = chunk_types(sorted_types, 50)
        print(f"[ollama_client] Split complete...")
        filtered_types = []
        test_counter = 0

        for batch in batches:
            filtered = request_filtering(batch)
            filtered_types.extend(filtered)
            test_counter = test_counter + 1

            if test_counter >= 2:
                break
        
        return filtered_types
    else:
        return request_filtering(sorted_types)
    
def request_filtering(types):
    payload = {
        "model": model,
        "prompt": f"{prompt} List: {types}",
        "stream": False,
        "format": "json"
    }

    try:
        print(f"[ollama_client] Awaiting llama3.1 response...")
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()

        raw_text = response.json()['response']
        clean_list = json.loads(raw_text)

        print(f"[ollama-client] Success!\n{clean_list}")
        return clean_list
    except requests.exceptions.RequestException as e:
        print(f"[ollama-client] Network error: {e}")
        return []
    except json.JSONDecodeError:
        print("[ollama-client] Ollama ignored the JSON format command.")
        return []
    
def chunk_types(types, n):
    for i in range(0, len(types), n):
        yield types[i:i + n]