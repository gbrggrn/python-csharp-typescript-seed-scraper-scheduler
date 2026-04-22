# from Extract.frobanken_url_extractor import filter_and_save_clean_urls
#from Extract.frobanken_url_extractor import harvest_raw_urls
from Extract.frobanken_content_extractor import request_veg_data
from Extract.frobanken_content_extractor import clean_response
from Transform.frobanken_transformer import transform
#from Load.frobanken_loader import load
#from pathlib import Path
"""
# Extract URLs
print("==========\nRetrieving URLs...\n==========")
savefile = Path("C:\\Users\\gusta\\source\\repos\\Random\\python-csharp-typescript-seed-scraper-scheduler\\Scraper\\frobanken-raw-urls.txt")
if not savefile.exists():
    print("[scraper] No previous raw url save file. Harvesting...")
    harvest_raw_urls()
    print("[scraper] Filtering raw urls...")
    filter_and_save_clean_urls()
    print("[scraper] Harvesting and filtering done. Continuing...")
else:
    print("[scraper] RAW-URLs already extracted. Filtering...")
    filter_and_save_clean_urls()
    print("[scraper] Filtering done. Continuing...")
"""
print("==========\nExtracting data...\n==========")
response = request_veg_data()
clean_response = package_response(response)

# Transform
print("==========\nPackaging data...\n===========")
DTOs = transform(clean_response)

# Load
print("==========\nLoading data...\n===========")
# load(DTOs)

print("==========\nETL SCRIPTING FINISHED...\n==========")
