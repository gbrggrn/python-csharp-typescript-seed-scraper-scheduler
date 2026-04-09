from Transform.frobanken_transformer import transform
import json
import requests

url = "http://localhost:5239/api/Plant"

def load():
    data = transform()
    successes = 0
    fails = 0

    for payload in data:
        response = requests.post(url, json = payload)

        if not response.ok:
            print(f"Something went wrong. Code: {response}")
            fails = fails + 1
        else:
            successes = successes + 1

    print(f"Loading finished.\nSuccesses: {successes}\nFails: {fails}")