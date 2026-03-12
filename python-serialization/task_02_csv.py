#!/usr/bin/env python3
"""Module that converts CSV data to JSON"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON file (data.json)"""
    try:
        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except Exception:
        return False
