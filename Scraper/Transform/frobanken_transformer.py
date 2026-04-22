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
            "min_germination_days": 0, "max_germination_days": 0,
            "min_height": 0.0, "max_height": 0.0,
            "row_spacing": 0,
            "plant_spacing": 0,
            "min_sow_month": 0, "max_sow_month": 0,
            "min_harvest": 0, "max_harvest": 0
        }

        description = entry['description']

        for i, line in enumerate(description):
            key = line.strip().lower()

            if i + 1 > len(description):
                break

            if "sådjup" in key:
                val = description[i+1]
                dto["sow_depth"], _ = parse_range(val)
            elif "grotid" in key:
                val = description[i+1]
                dto["min_germination_days"], dto["max_germination_days"] = map(int, parse_range(val))
            elif "höjd" in key:
                val = description[i+1]
                dto["min_height"], dto["max_height"] = map(int, parse_range(val))
            elif "radavstånd" in key:
                val = description[i+1]
                dto["row_spacing"], _ = parse_range(val)
            elif "plantavstånd" in key:
                val = description[i+1]
                dto["plant_spacing"], _ = parse_range(val)
            elif "såperiod" in key:
                val = description[i+1]
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
    
def parse_range(value_str):
    # Find all numbers replace commas with dots
    numbers = re.findall(r'\d+(?:[.,]\d+)?', value_str.replace(',', '.'))

    nums = [float(n) for n in numbers]

    if len(nums) >= 2:
        return nums[0], nums[1]
    elif len(nums) == 1:
        return nums[0], nums[0]
    return 0, 0
