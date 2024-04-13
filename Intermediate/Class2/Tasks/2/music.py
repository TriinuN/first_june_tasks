import json
import csv

with open('music.csv', 'r') as file:
    data_m = csv.DictReader(file)
    data = []
    for row in data_m:
        cleaned_row = {key.strip(): int(value.strip()) if value.strip().isdigit() else value.strip() for key, value in
                       row.items()}
        data.append(cleaned_row)

with open('music_convert.json', 'w') as file:
    json.dump(data, file, indent=4)
