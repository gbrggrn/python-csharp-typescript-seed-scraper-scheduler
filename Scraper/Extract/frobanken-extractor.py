import requests
from bs4 import BeautifulSoup

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
harvest_urls(sitemaps, "frobanken-urls.txt")
