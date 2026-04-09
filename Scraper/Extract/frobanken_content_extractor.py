from bs4 import BeautifulSoup as BS
import requests
import random
import time

def retrieve_urls_from_file(filename):
    with open(filename, 'r', encoding = "utf-8") as file:
        url_list = file.read().splitlines()

    return url_list

def extract_content_from_urls(url_list):
    extracted_DTOs = []

    name = ""
    sow_depth = ""
    min_germination_days = ""
    max_germination_days = ""
    min_height = ""
    max_height = ""
    row_spacing = ""
    plant_spacing = ""
    min_sow_month = ""
    max_sow_month = ""
    min_harvest = ""
    max_harvest = ""
    
    for url in url_list:
        if not url:
            continue

        print(f"Now scraping: {url}")

        response = requests.get(url)
        soup = BS(response.text, 'html.parser')

        name = soup.select_one('.tws-article-name h1').text
        print(name)

        description_text = soup.select_one('.tws-article-description-text')

        clean_text = description_text.get_text(separator='\n')

        lines = clean_text.split('\n')

        for line in lines:
            if "Sådjup:" in line:
                sow_depth = line.split(":")[1].strip()
            if "Grotid:" in line:
                min_germination_days = line.split(":")[1].split("–")[0].strip()
                max_germination_days = line.split(":")[1].split("–")[1].split(" ")[0].strip()
            if "Höjd:" in line:
                min_height_split = line.split(":")[1]
                if "–" in min_height_split:
                    min_height = min_height_split.split("–")[0].strip()
                    max_height = min_height_split.split("–")[1].strip()
                else:
                    min_height = min_height_split.split(" ")[0].strip()
            if "Radavstånd:" in line:
                row_spacing = line.split(":")[1].split(" ")[0].strip()
            if "Plantavstånd:" in line:
                plant_spacing = line.split(":")[1].split(" ")[0].strip()
            if "Såperiod:" in line:
                min_month_str = line.split(":")[1].split("–")[0].strip()
                max_month_str = line.split(":")[1].split("–")[1].strip()

                min_sow_month = month_helper(min_month_str)
                max_sow_month = month_helper(max_month_str)
            if "Skördeperiod:" in line:
                min_harvest_str = line.split(":")[1].split("–")[0].strip()
                max_harvest_str = line.split(":")[1].split("–")[1].strip()

                min_harvest = month_helper(min_harvest_str)
                max_harvest = month_helper(max_harvest_str)

        DTO = {
            "name": name,
            "sow_depth": sow_depth,
            "min_germination_days": min_germination_days,
            "max_germination_days": max_germination_days,
            "min_height": min_height,
            "max_height": max_height,
            "row_spacing": row_spacing,
            "plant_spacing": plant_spacing,
            "min_sow_month": min_sow_month,
            "max_sow_month": max_sow_month,
            "min_harvest": min_harvest,
            "max_harvest": max_harvest
        }

        extracted_DTOs.append(DTO)
        
        time.sleep(random.uniform(1.5, 3.0))

    return extracted_DTOs

def month_helper(month):
    months_values = {
        "januari": 1,
        "februari": 2,
        "mars": 3,
        "april": 4,
        "maj": 5,
        "juni": 6,
        "juli": 7,
        "augusti": 8,
        "september": 9,
        "oktober": 10,
        "november": 11,
        "december": 12
    }

    if month in months_values:
        return months_values[month]
    else:
        return 0
    
def extract():
    return extract_content_from_urls(retrieve_urls_from_file("frobanken-veg-urls.txt"))