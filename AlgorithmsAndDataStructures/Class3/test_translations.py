import unittest
import os
import json
import translations_task


class TestTBTExtraction(unittest.TestCase):

    def test_tbt_extraction(self):
        # Directory containing the JSON files
        directory = 'translations'
        expected_tbt_values = {}
        tbt_values = {}

        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    json_data = json.load(file)
                    translations_task.extract_tbt_values(json_data, tbt_values)

        self.assertEqual(tbt_values, expected_tbt_values, "TBT values extraction failed")


if __name__ == '__main__':
    unittest.main()
