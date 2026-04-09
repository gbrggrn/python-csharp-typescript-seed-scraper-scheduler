from Transform.frobanken_transformer import transform
import json
import requests

url = "http://localhost:5239"

def load():
    data = transform()
    successes = 0;
    fails = 0;

    for object in data:
        payload = json.dumps({
            "name": object.name,
            "sow_depth": object.sow_depth,
            "min_germination_days": object.min_germination_days,
            "max_germination_days": object.max_germination_days,
            "min_height": object.min_height,
            "max_height": object.max_height,
            "row_spacing": object.row_spacing,
            "plant_spacing": object.plant_spacing,
            "min_sow_month": object.min_sow_month,
            "max_sow_month": object.max_sow_month,
            "min_harvest": object.min_harvest,
            "max_harvest": object.max_harvest
        })

        response = requests.post(url, json = payload)

        if response != 200:
            print(f"Something went wrong. Code: {response}")
            fails = fails + 1
        
        successes = successes + 1

    print(f"Loading finished.\nSuccesses: {successes}\nFails: {fails}")