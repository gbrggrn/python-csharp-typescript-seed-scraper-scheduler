import requests
from bs4 import BeautifulSoup
from ollama_client import generate_filtered_list

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

# Initiate harvesting
harvest_urls(sitemaps, "frobanken-raw-urls.txt")

def filter():
    return filter_unique_types(extract_bulk_urls_from_file("frobanken-raw-urls.txt"))

def extract_bulk_urls_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        raw_urls = file.read()

        bulk_urls = raw_urls.split("\n")

    return bulk_urls

def filter_unique_types(bulk_urls):
    types = []
    urls = bulk_urls.split("\n")
    for url in urls:
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
        if (url.contains(vegetables)):
            vegetable_urls.append(url)

    return vegetable_urls

def save_filtered_urls(filename, vegetable_urls):
    with open(filename, 'w', encoding = "utf-8") as file:
        file.write(vegetable_urls)

def filter_and_save_clean_urls():
    save_filtered_urls("frobanken-veg-urls.txt", 
                       filter_raw_urls(extract_bulk_urls_from_file("frobanken-raw-urls.txt"), 
                                       generate_filtered_list(filter())))

filter_and_save_clean_urls()