from bs4 import BeautifulSoup as BS
import requests
    
def request_veg_data():
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
                        "in": [178276989]
                    }
                }
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