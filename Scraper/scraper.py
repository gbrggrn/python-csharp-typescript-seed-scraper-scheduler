from Extract.frobanken_uid_extractor import fetch_uids
from Extract.frobanken_uid_extractor import cast_and_save_uids
from Extract.frobanken_content_extractor import request_veg_data
from Extract.frobanken_content_extractor import clean_response
from Transform.frobanken_transformer import transform
from Load.frobanken_loader import load

# Extract URLs
print("==========\nRetrieving URLs...\n==========")
raw_uids = fetch_uids()
cast_and_save_uids(raw_uids)

print("==========\nExtracting data...\n==========")
response = request_veg_data()
cleaned_response = clean_response(response)

# Transform
print("==========\nPackaging data...\n===========")
DTOs = transform(cleaned_response)

# Load
print("==========\nLoading data...\n===========")
load(DTOs)

print("==========\nETL SCRIPTING FINISHED...\n==========")
