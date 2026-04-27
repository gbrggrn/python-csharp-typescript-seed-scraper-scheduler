from Extract.frobanken_uid_extractor import extract_uids
from Extract.frobanken_uid_extractor import cast_and_save_uids
from Extract.frobanken_content_extractor import chunk_uids
from Extract.frobanken_content_extractor import run_content_extraction_pipeline
from Transform.frobanken_transformer import transform
from Load.frobanken_loader import load

# Extract URLs
print("==========\nRetrieving URLs...\n==========")
raw_uids = extract_uids()

if raw_uids:
    cast_and_save_uids(raw_uids)

print("==========\nExtracting data...\n==========")
uid_chunks = chunk_uids(25)
response = run_content_extraction_pipeline(uid_chunks)

# Transform
print("==========\nPackaging data...\n===========")
DTOs = transform(uid_chunks)

# Load
print("==========\nLoading data...\n===========")
load(DTOs)

print("==========\nETL SCRIPTING FINISHED...\n==========")
