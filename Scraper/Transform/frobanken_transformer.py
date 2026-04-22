import re

def transform(data):
    DTOs = extract_DTOs_from_data(data)

    return DTOs

def extract_DTOs_from_data(data):
    extracted_DTOs = []
    
    for entry in data:

        dto = {
            "name": entry['name'],
            "sow_depth": 0.0,
            "min_germination_days": 0.0, "max_germination_days": 0.0,
            "min_height": 0.0, "max_height": 0.0,
            "row_spacing": 0.0,
            "plant_spacing": 0.0,
            "min_sow_month": 0.0, "max_sow_month": 0.0,
            "min_harvest": 0.0, "max_harvest": 0.0
        }

        description = entry['description']

        for i, line in enumerate(description):
            key = line.strip().lower()

            if i + 1 > len(description):
                break

            if "sådjup" in key:
                val = description[i+1]
                print(f"{val}")
                dto["sow_depth"], _ = parse_range(val)
            elif "grotid" in key:
                val = description[i+1]
                print(f"{val}")
                dto["min_germination_days"], dto["max_germination_days"] = map(int, parse_range(val))
            elif "höjd" in key:
                val = description[i+1]
                print(f"{val}")
                dto["min_height"], dto["max_height"] = map(int, parse_range(val))
            elif "radavstånd" in key:
                val = description[i+1]
                print(f"{val}")
                dto["row_spacing"], _ = parse_range(val)
            elif "plantavstånd" in key:
                val = description[i+1]
                print(f"{val}")
                dto["plant_spacing"], _ = parse_range(val)
            elif "såperiod" in key:
                val = description[i+1]
                print(f"{val}")
                if "-" in val:
                    parts = val.splt("–")
                    dto["min_sow_month"] = month_helper(parts[0])
                    dto["max_sow_month"] = month_helper(parts[1])
                else:
                    dto["min_sow_month"] = month_helper(val)
                    dto["max_sow_month"] = dto["min_sow_month"]
            elif "skördeperiod" in key:
                val = description[i+1]
                if "–" in val:
                    parts = val.split("–")
                    dto["min_harvest"] = month_helper(parts[0])
                    dto["max_harvest"] = month_helper(parts[1])
                else:
                    dto["min_harvest"] = month_helper(val)
                    dto["max_harvest"] = dto["min_harvest"]

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
