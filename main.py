import json
from datetime import datetime as dt

with open("./vehicles_simple.json", "r") as json_file:
    vehicles_dict = json.load(json_file)
    # print(vehicles_dict)
    # print(vehicles_dict[0]["make_model"])
    line_no = 1
    for line in vehicles_dict:
        # print(f"This is line number: {line_no}.")
        line_no += 1
        

REQUIRED_SCHEMA_FIELDS = {"license_plate", "make_model", "year", "color", "registered_date", "registered_name" "registered_address", }

def check_schema(row, requried_fields=REQUIRED_SCHEMA_FIELDS):
    for field_name in requried_fields:
        if field_name not in row:
            return False
    return True

# check_schema(row)

# vehicles_dict[4]["license_plate"] = None

# print(vehicles_dict[4]["license_plate"])

def parse_date(value, dtfmt="%Y-%m-%d"):
    try:
        return dt.strptime(value, dtfmt).date()
    except:
        return None

parse_date("registered_date")