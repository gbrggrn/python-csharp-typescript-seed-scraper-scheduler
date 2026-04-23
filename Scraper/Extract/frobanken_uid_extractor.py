import requests
import json

def fetch_uids():
    url = "https://xn--frbanken-o4a.se/backend/jsonrpc/v1?webshop=74924&auth=&session=&language=sv&vat_country=SE"
    headers = {
        "Content-Type": "text/plain;charset=UTF-8",
        "Referer": "https://xn--frbanken-o4a.se/sv/gronsaker.html",
        "X-Requested-With": "XMLHttpRequest"
    }

    payload = {
        "jsonrpc": "2.0",
        "id": 13,
        "method": "Article.elasticSearch",
        "params": ["sv", {
            "limit": "1000",
            "artgroups": [5509467],
            "sort": [{"name": "created", "direction": "desc"}]
        }]
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
        try:
            results = response.json()
            uids = results.get("result", {}).get("articles", [])
            print(f"[uid-extractor] Fetch succesful of {len(uids)} UIDs...")
            return uids
        except requests.exceptions.JSONDecodeError:
            print("[uid-extractor] Fetch succesful but response contained no JSON...")
    else:
        print(f"[uid-extractor] Fetch failed! Status: {response.status_code}")

def cast_and_save_uids(uids):
    int_uids = [int(uid) for uid in uids]

    with open("plant_uids.json", "w") as file:
        json.dump(int_uids, file)

    print(f"[uid-extractor] {len(int_uids)} UIDs saved to file...")

    return int_uids