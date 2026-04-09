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

    for url in url_list:
        if not url:
            continue

        print(f"Now scraping: {url}")

        response = requests.get(url)
        soup = BS(response.text, 'html.parser')

        name_element = soup.select_one('.tws-article-name h1')

        if not name_element:
            print(f"Name not found for: {url}")
            continue

        name = name_element.text.strip()
        print(f"Scraped veg: {name}")

        description_element = soup.select_one('.tws-article-description-text')

        if not description_element:
            print(f"Description not found for: {url}")
            continue

        print(f"Description scraped for: {name}")

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