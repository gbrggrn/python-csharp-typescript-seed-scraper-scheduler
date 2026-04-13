from bs4 import BeautifulSoup as BS
import requests
import random
import time

def extract():
    return extract_content(retrieve_urls_from_file("frobanken-veg-urls.txt"))

def retrieve_urls_from_file(filename):
    with open(filename, 'r', encoding = "utf-8") as file:
        url_list = file.read().splitlines()

    return url_list

def extract_content(url_list):
    data = []
    test_counter = 0

    for url in url_list:
        test_counter += 1
        if not url:
            continue

        if test_counter >= 2:
            break

        print(f"[content-extractor] Now scraping: {url}")

        name = extract_name_from_url(url)
        if len(name) < 1:
            print(f"[content-extractor] Name could not be extracted for {url}")
        else:
            print(f"[content-extractor] Name: {name}")

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}
        response = requests.get(url, headers=headers)
        print(f"Status: {response.status_code} | Length: {len(response.text)}")
        
        soup = BS(response.text, 'lxml')

        description_element = soup.select_one('.tws-article-description-text')

        if not description_element:
            print(f"[content-extractor] Description not found for: {url}")
            continue

        print(f"[content-extractor] Description scraped for: {name}")

        clean_text = description_element.get_text(separator='\n')

        lines = clean_text.split('\n')
        lines.append(f"\nName: {name}")

        object = {
            "name": name,
            "lines": lines
        }

        data.append(object)

        time.sleep(random.uniform(1.5, 3.0))
    
    return data

def extract_name_from_url(url):
    name_half = url.split('sv/')[1]
    raw_name = name_half.split('.html')[0]
    species_name = url.split('-')[0]
    type_chunk = raw_name.split('-')[1]
    if "-" in type_chunk:
        type_name = type_chunk.split('-')
    else:
        type_name = type_chunk

    name = ' '.join([species_name, type_name])
    
    return name