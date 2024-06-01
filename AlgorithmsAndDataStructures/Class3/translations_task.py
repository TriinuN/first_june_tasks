import json
import os


# Kaust, mis sisaldab JSON faile
directory = 'translations'  # Muuda see reaalseks kausta teeks

# Listi, et hoida kõiki ekstrakteeritud TBT väärtusi
tbt_values = []


def extract_tbt_values(data):
    """Rekursiivselt ekstrakteeri TBT väärtused JSON andmetest."""
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str) and value.startswith("TBT:"):
                tbt_values.append(value.split("TBT:")[1].strip())
            else:
                extract_tbt_values(value)
    elif isinstance(data, list):
        for item in data:
            extract_tbt_values(item)


# Loe kõik JSON failid kaustast
for filename in os.listdir(directory):  # Loeb kausta sisu
    if filename.endswith(".json"):  # Eeldame, et failid on JSON formaadis
        file_path = os.path.join(directory, filename)  # Koostab täieliku failitee
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            extract_tbt_values(data)

# Koosta uus fail
with open('result_file.txt', 'w', encoding='utf-8') as result_file:
    for value in tbt_values:
        result_file.write(value + "\n")