from Extract.frobanken_url_extractor import harvest_filter_save_clean_urls
from Extract.frobanken_content_extractor import extract
from Transform.frobanken_transformer import transform
from Load.frobanken_loader import load
from pathlib import Path

# Extract URLs
print("==========\nRetrieving URLs...\n==========")
savefile = Path("C:\\Users\\gusta\\source\\repos\\Random\\python-csharp-typescript-seed-scraper-scheduler\\Scraper\\frobanken-raw-urls.txt")
if not savefile.exists():
    harvest_filter_save_clean_urls()
else:
    print(f"[scraper] RAW-URLs already extracted. Continuing...")

print("==========\nExtracting data...\n==========")
data = extract()

# Transform
print("==========\nPackaging data...\n===========")
DTOs = transform(data)

# Load
print("==========\nLoading data...\n===========")
load(DTOs)

print("==========\nETL SCRIPTING FINISHED...\n==========")