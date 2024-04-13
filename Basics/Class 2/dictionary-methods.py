import json

sample_dict = {
    "name": "Triinu",   # Name is key and Triinu is value
    "age": "27",
    "city": "Tartu",
    "cats": ["Sammy", "Mustu"],
    "family": [
        {
            "name": "Marken",
            "age": 7
         },
        {
            "name": "Mariliis",
            "age": 1
        },
    ],
    "married": True
}
print(sample_dict)
# Add new Key, Value pair
sample_dict['favorite_color'] = "Blue"
# Adjust existing key, value pairs
sample_dict['age'] = 28
sample_dict['cats'].append("Maasikas")
print(sample_dict)

# Get specific data from dictionary
print(sample_dict['family'])
print(sample_dict.get('city'))
print(sample_dict.get('food', 'DefaultValue'))

# Deleting values from dictionary
del sample_dict['favorite_color']
deleted_value = sample_dict.pop('family')
print(deleted_value)


print(json.dumps(sample_dict, indent= 2))  # Indent is how many spaces
