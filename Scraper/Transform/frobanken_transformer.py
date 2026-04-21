def transform(data):
    DTOs = extract_DTOs_from_data(data)

    return DTOs

def extract_DTOs_from_data(data):
    extracted_DTOs = []
    
    for entry in data:

        for line in entry["lines"]:

            sow_depth = ""
            min_germination_days = ""
            max_germination_days = ""
            min_height = ""
            max_height = ""
            row_spacing = ""
            plant_spacing = ""
            min_sow_month = ""
            max_sow_month = ""
            min_harvest = ""
            max_harvest = ""

            if "Sådjup:" in line:
                sow_depth = line.split(":")[1].strip()
            if "Grotid:" in line:
                min_germination_days = line.split(":")[1].split("–")[0].strip()
                max_germination_days = line.split(":")[1].split("–")[1].split(" ")[0].strip()
            if "Höjd:" in line:
                min_height_split = line.split(":")[1]
                if "–" in min_height_split:
                    min_height = min_height_split.split("–")[0].strip()
                    max_height = min_height_split.split("–")[1].strip()
                else:
                    min_height = min_height_split.split(" ")[0].strip()
            if "Radavstånd:" in line:
                row_spacing = line.split(":")[1].split(" ")[0].strip()
            if "Plantavstånd:" in line:
                plant_spacing = line.split(":")[1].split(" ")[0].strip()
            if "Såperiod:" in line:
                min_month_str = line.split(":")[1].split("–")[0].strip()
                max_month_str = line.split(":")[1].split("–")[1].strip()

                min_sow_month = month_helper(min_month_str)
                max_sow_month = month_helper(max_month_str)
            if "Skördeperiod:" in line:
                min_harvest_str = line.split(":")[1].split("–")[0].strip()
                max_harvest_str = line.split(":")[1].split("–")[1].strip()

                min_harvest = month_helper(min_harvest_str)
                max_harvest = month_helper(max_harvest_str)

            print(f"[transformer] PLANT CONTENT:\nSådjup:{sow_depth}\nGrotid:{min_germination_days}-{max_germination_days}\nHöjd:{min_height}-{max_height}\nRadavstånd:{row_spacing}\nPlantavstånd:{plant_spacing}\nSåperiod: {min_sow_month}-{max_sow_month}\nSkördeperiod: {min_sow_month}-{max_sow_month}")

            DTO = {
                "name": entry["name"],
                "sow_depth": sow_depth,
                "min_germination_days": min_germination_days,
                "max_germination_days": max_germination_days,
                "min_height": min_height,
                "max_height": max_height,
                "row_spacing": row_spacing,
                "plant_spacing": plant_spacing,
                "min_sow_month": min_sow_month,
                "max_sow_month": max_sow_month,
                "min_harvest": min_harvest,
                "max_harvest": max_harvest
            }

            extracted_DTOs.append(DTO)

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