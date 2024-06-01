import os
import json

directory = 'translations'
tbt_values = {}


def extract_tbt_values(data, parent_key=None):
    """Recursively extract TBT values from the JSON data."""
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, str) and value.startswith("TBT:"):
                tbt_values.setdefault(file_name, {}).setdefault(full_key, value.split("TBT:")[1].strip())
            else:
                extract_tbt_values(value, full_key)
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_key = f"{parent_key}[{idx}]" if parent_key else str(idx)
            extract_tbt_values(item, full_key)


for filename in os.listdir(directory):
    if filename.endswith(".json"):
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            file_name = filename.split('.')[0]
            data = json.load(file)
            extract_tbt_values(data)


with open('result_file.txt', 'w', encoding='utf-8') as result_file:
    for file_name, values in tbt_values.items():
        result_file.write(f'"{file_name}.json": {{\n')
        for key, value in values.items():
            keys = key.split('.')
            result_file.write('    ')
            for i, part in enumerate(keys):
                if i == len(keys) - 1:
                    result_file.write(f'"{part}": "TBT:{value}"\n')
                else:
                    result_file.write(f'"{part}": ')
            result_file.write('},\n')

print("Result file created successfully with all TBT values.")