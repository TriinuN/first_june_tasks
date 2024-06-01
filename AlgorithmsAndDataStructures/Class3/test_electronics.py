import unittest
import json
import csv
import os


class TestJsonToCsvConversion(unittest.TestCase):

    def test_conversion(self):
        # Ensure the test JSON file exists
        self.assertTrue(os.path.exists('electronics_products.json'), "JSON file not found")

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
        with open('test_electronics_products.csv', 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['id', 'name', 'price', 'category', 'currency', 'stock', 'description',
                          'manufacturer', 'warranty', 'extra_field']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for product in cleaned_data:
                writer.writerow(product)

        # Check if the CSV file was created successfully
        self.assertTrue(os.path.exists('test_electronics_products.csv'), "CSV file not created")

        # Check if the CSV file contains expected headers
        with open('test_electronics_products.csv', 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            expected_headers = ['id', 'name', 'price', 'category', 'currency', 'stock', 'description',
                                'manufacturer', 'warranty', 'extra_field']
            self.assertEqual(reader.fieldnames, expected_headers, "Incorrect CSV headers")

        # Clean up: Delete the test CSV file
        os.remove('test_electronics_products.csv')


if __name__ == '__main__':
    unittest.main()
