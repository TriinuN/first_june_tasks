import json
import csv

# Read the JSON file
with open('electronics_products.json', 'r') as json_file:
    data = json.load(json_file)

cleaned_data = []

for product in data['data']:
    cleaned_product = {
        'id': product.get('id', None),
        'name': product.get('name', None),
        'category': product.get('category', None),
        'price': product.get('price', None),
        'currency': product.get('currency', None),
        'stock': product.get('stock', None),
        'description': product.get('description', None),
        'manufacturer': product.get('manufacturer', None),
        'warranty': product.get('warranty', None),
        'extra_field': product.get('extra_field', None),
    }
    cleaned_data.append(cleaned_product)

# Write the cleaned data to a CSV file
with open('electronics_products.csv', 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['id', 'name', 'price', 'category', 'currency', 'stock', 'description',
                  'manufacturer', 'warranty', 'extra_field']  # Define field names based on cleaned data keys
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for product in cleaned_data:
        writer.writerow(product)

print("CSV file created successfully.")