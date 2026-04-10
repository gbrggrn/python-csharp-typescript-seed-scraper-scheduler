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

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}
        response = requests.get(url, headers=headers)
        print(f"Status: {response.status_code} | Length: {len(response.text)}")
        
        soup = BS(response.text, 'lxml')
        if soup.body:
            print(f"DEBUG BODY: {soup.body.text[:1000].strip()}")
        print(f"Page Title: {soup.title.string if soup.title else 'No Title'}")
        print(f"H1 Count: {len(soup.find_all('h1'))}")

        name_element = soup.find('h1')

        if not name_element:
            print(f"Name not found for: {url}")
            continue

        name = name_element.text.strip()
        print(f"Scraped veg: {name}")

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