import requests
from bs4 import BeautifulSoup
import re

url_one = "https://xn--frbanken-o4a.se/sitemap.xml?urlset=3"
url_two = "https://xn--frbanken-o4a.se/sitemap.xml?urlset=4"

reqs_one = requests.get(url_one)
reqs_two = requests.get(url_two)

soup_one = BeautifulSoup(reqs_one.text, 'xml')
soup_two = BeautifulSoup(reqs_two.text, 'xml')

with open("frobanken-urls.txt", "w", encoding="utf-8") as file:

    for url in soup_one.find_all('loc'):
        data = url.text
        file.write(data)
        file.write("\n")

    for url in soup_two.find_all('loc'):
        data = url.text
        file.write(data)
        file.write("\n")