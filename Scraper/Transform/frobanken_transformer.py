import re

def transform(data):
    DTOs = extract_DTOs_from_data(data)

    return DTOs

def extract_DTOs_from_data(data):
    extracted_DTOs = []
    
    for entry in data:

        dto = {
            "Name": entry['name'],
            "SowDepth": 0.0,
            "MinGerminationDays": 0.0, "MaxGerminationDays": 0.0,
            "MinHeight": 0.0, "MaxHeight": 0.0,
            "RowSpacing": 0.0,
            "PlantSpacing": 0.0,
            "MinSowMonth": 0.0, "MaxSowMonth": 0.0,
            "MinHarvestMonth": 0.0, "MaxHarvestMonth": 0.0
        }

        description = entry['description']

        for i, line in enumerate(description):
            key = line.strip().lower()

            if i + 1 >= len(description):
                break

            if "sådjup" in key:
                val = description[i+1]
                print(f"{val}")
                dto["SowDepth"], _ = parse_range(val)
            elif "grotid" in key:
                val = description[i+1]
                print(f"{val}")
                dto["MinGerminationDays"], dto["MaxGerminationDays"] = map(int, parse_range(val))
            elif "höjd" in key:
                val = description[i+1]
                print(f"{val}")
                dto["MinHeight"], dto["MaxHeight"] = map(int, parse_range(val))
            elif "radavstånd" in key:
                val = description[i+1]
                print(f"{val}")
                dto["RowSpacing"], _ = parse_range(val)
            elif "plantavstånd" in key:
                val = description[i+1]
                print(f"{val}")
                dto["PlantSpacing"], _ = parse_range(val)
            elif "såperiod" in key:
                val = description[i+1]
                print(f"{val}")
                if "–" in val: # !!! OBSERVE: Frobanken used EN-DASHES
                    parts = val.split("–")
                    dto["MinSowMonth"] = month_helper(parts[0])
                    dto["MaxSowMonth"] = month_helper(parts[1])
                else:
                    dto["MinSowMonth"] = month_helper(val)
                    dto["MaxSowMonth"] = dto["MinSowMonth"]
            elif "skördeperiod" in key:
                val = description[i+1]
                if "–" in val:
                    parts = val.split("–")
                    dto["MinHarvestMonth"] = month_helper(parts[0])
                    dto["MaxHarvestMonth"] = month_helper(parts[1])
                else:
                    dto["MinHarvestMonth"] = month_helper(val)
                    dto["MaxHarvestMonth"] = dto["MinHarvestMonth"]

        extracted_DTOs.append(dto)

    return extracted_DTOs

def month_helper(month):
    months_values = {
        "jan": 1.0,
        "feb": 2.0,
        "mars": 3.0,
        "april": 4.0,
        "maj": 5.0,
        "juni": 6.0,
        "juli": 7.0,
        "augusti": 8.0,
        "september": 9.0,
        "oktober": 10.0,
        "november": 11.0,
        "december": 12.0,
        "frost": 10.0
    }

    if month in months_values:
        return months_values[month]
    else:
        return 0
    
def parse_range(value_str):
    # Find all numbers replace commas with dots
    numbers = re.findall(r'\d+(?:[.,]\d+)?', value_str.replace(',', '.'))

    nums = [float(n) for n in numbers]

    if len(nums) >= 2:
        return nums[0], nums[1]
    elif len(nums) == 1:
        return nums[0], nums[0]
    return 0, 0
