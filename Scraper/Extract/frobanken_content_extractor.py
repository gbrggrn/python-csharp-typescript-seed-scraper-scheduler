from bs4 import BeautifulSoup as BS
from pathlib import Path
import requests
import os
import json
    
def request_veg_data(uid_chunk):
    url = "https://xn--frbanken-o4a.se/backend/jsonrpc/v1?webshop=74924&auth=&session=&language=sv&vat_country=SE"
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://xn--frbanken-o4a.se/sv/bifftomat-pantano.html",
        "X-Requested-With": "XMLHttpRequest"
    }


    payload = {
        "jsonrpc": "2.0",
        "id": 12,
        "method": "Article.list",
        "params": [
            {
                "name": ["sv"],
                "description": "sv",
                "uid": True
            },
            {
                "filters": {
                    "/uid": {
                        "in": uid_chunk
                    }
                },
                "limit": len(uid_chunk)
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"[content-extractor] Fetch successful!")
        return response.json()
    else:
        print(f"[content-extractor] Fetch Failed! Response:\n{response.text}")
        return None
    
def chunk_uids(chunk_size):
    SCRIPT_DIR = Path(__file__).parent
    UIDS_PATH = SCRIPT_DIR / "plant_uids.json"

    if not UIDS_PATH.exists():
        print(f"[content-extractor] A UID save file could not be found at: {UIDS_PATH}. No extraction...")
        return []
    else:
        print(f"[content extractor] UID Save file found at: {UIDS_PATH}. Reading...")

        with open(UIDS_PATH, "r") as file:
            uids = json.load(file)

        print("[content-extractor] Chunking...")
        chunks = [uids[i:i + chunk_size] for i in range(0, len(uids), chunk_size)]
        print(f"[content-extractor] Chunking resulted in {len(chunks)} chunks.")
        return chunks
    
def run_content_extraction_pipeline(chunked_uids):
    if not chunked_uids:
        print("[content-extractor] No chunked UIDs to extract from. Quitting...")
        return
    
    print(f"[content-extractor] Initiating fetching from {len(chunked_uids)} chunks...")
    all_cleaned_data = []

    for chunk in chunked_uids:
        response = request_veg_data(chunk)
        if response:
            cleaned = clean_response(response)
            all_cleaned_data.extend(cleaned)
    
def clean_response(response_json):
    print("[content-extractor] Cleaning and formatting JSON response...")
    packaged_data = []

    for item in response_json.get('result', []):
        name = item.get('name', {}).get('sv', 'Unknown')

        uid = item.get('uid')

        raw_description = item.get('description', {}).get('sv', '')
        description_lines = clean_description(raw_description)

        object = {
            "name": name,
            "description": description_lines,
            "uid": uid
        }

        packaged_data.append(object)

    return packaged_data

def clean_description(raw_description):
    if not raw_description:
        return []
    
    soup = BS(raw_description, 'html.parser')
    clean_text = soup.get_text(separator='\n')

    return [line.strip() for line in clean_text.splitlines() if line.strip()]