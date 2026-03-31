from bs4 import BeautifulSoup as BF
import requests

def retrieve_urls_from_file(filename):
    vegetable_urls = []
    with open(filename, 'r', encoding = "utf-8") as file:
        raw_urls = file.read()

        url_list = raw_urls.split("\n")

    return url_list