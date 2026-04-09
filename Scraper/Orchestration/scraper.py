from Extract.frobanken_url_extractor import filter_and_save_clean_urls
from Extract.frobanken_content_extractor import extract
from Transform.frobanken_transformer import transform
from Load.frobanken_loader import load

# Extract URLs
print("==========\nRetrieving URLs...\n==========")
filter_and_save_clean_urls()
print("==========\nExtracting data...\n==========")
data = extract()

# Transform
print("==========\nPackaging data...\n===========")
DTOs = transform(data)

# Load
print("==========\nLoading data...\n===========")
load(DTOs)

print("==========\nETL SCRIPTING FINISHED...\n==========")