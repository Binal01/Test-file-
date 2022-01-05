import json

sample_dict = {
    "Name":"John Doe",
    "Age": 35,
    "City":"Collingwood"
}
json_string = json.dumps(sample_dict, indent=4)
print(json_string)