from Transform.frobanken_transformer import transform
import json

def load():
    data = transform()

    for object in data:
        json.dumps({
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

        