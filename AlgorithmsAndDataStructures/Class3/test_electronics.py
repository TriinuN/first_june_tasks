import unittest
import json
import csv
import os


class TestJsonToCsvConversion(unittest.TestCase):

    def test_conversion(self):
        self.assertTrue(os.path.exists('electronics_products.json'), "JSON file not found")

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

        with open('test_electronics_products.csv', 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['id', 'name', 'price', 'category', 'currency', 'stock', 'description',
                          'manufacturer', 'warranty', 'extra_field']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for product in cleaned_data:
                writer.writerow(product)

        self.assertTrue(os.path.exists('test_electronics_products.csv'), "CSV file not created")

        with open('test_electronics_products.csv', 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            expected_headers = ['id', 'name', 'price', 'category', 'currency', 'stock', 'description',
                                'manufacturer', 'warranty', 'extra_field']
            self.assertEqual(reader.fieldnames, expected_headers, "Incorrect CSV headers")

        os.remove('test_electronics_products.csv')


if __name__ == '__main__':
    unittest.main()
