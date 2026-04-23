import requests
import json
from bs4 import BeautifulSoup
from Extract.ollama_client import generate_filtered_list

# Target sitemaps
sitemaps = [
    "https://xn--frbanken-o4a.se/sitemap.xml?urlset=3",
    "https://xn--frbanken-o4a.se/sitemap.xml?urlset=4"
]

# Harvests the urls from the sitemaps
def harvest_urls(sitemaps, output_filename):
    # Ready file for writing
    with open(output_filename, "w", encoding="utf-8") as file:
        # Fetch the raw xml
        for sitemap in sitemaps:
            response = requests.get(sitemap)
            soup = BeautifulSoup(response.text, 'xml')

            # Format into urls and write to file
            for loc in soup.find_all('loc'):
                file.write(f"{loc.text}\n")
    print("[url_extractor] URLs harvested from sitemaps...")

def filter():
    return filter_unique_types(extract_bulk_urls_from_file("frobanken-raw-urls.txt"))

def extract_bulk_urls_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        raw_urls = file.read()

        bulk_urls = raw_urls.split("\n")

    return bulk_urls

def filter_unique_types(bulk_urls):
    types = []
    for url in bulk_urls:
        if url == "":
            continue
        name = url.replace(".html", "")
        split = name.split("/")
        slug = split[-1]
        split_slug = slug.split("-")
        type = split_slug[0]
        types.append(type)
    
    unique_types = set(types)
    sorted_types = sorted(unique_types)

    return sorted_types

def filter_raw_urls(bulk_urls, vegetables):
    vegetable_urls = []
    for url in bulk_urls:
        if url == "":
            continue

        slug = url.split("/")[-1]
        type = slug.split("-")[0].replace(".html", "")

        if type in vegetables:
            vegetable_urls.append(url)

    return vegetable_urls

def save_filtered_urls(filename, vegetable_urls):
    with open(filename, 'w', encoding = "utf-8") as file:
        for url in vegetable_urls:
            file.write(f"{url}\n")

test_vegetables = ['aubergine', 'broccoli', 'bifftomat', 'bondbona', 'sattpotatis']

def filter_and_save_clean_urls():
    save_filtered_urls("frobanken-veg-urls.txt", 
                       filter_raw_urls(extract_bulk_urls_from_file("frobanken-raw-urls.txt"), 
                                       test_vegetables))
        
def harvest_raw_urls():
    harvest_urls(sitemaps, "frobanken-raw-urls.txt")

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