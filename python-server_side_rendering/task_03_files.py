#!/usr/bin/python3
"""A Flask application that displays product data read from either a
JSON or a CSV file, selected by a query parameter and optionally
filtered by product id."""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(path):
    """Read a list of product dictionaries from a JSON file.

    Args:
        path: the path to the JSON file.

    Returns:
        list: the products stored in the file.
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv(path):
    """Read a list of product dictionaries from a CSV file.

    Args:
        path: the path to the CSV file.

    Returns:
        list: the products stored in the file, with id and price
            converted to numeric types.
    """
    products = []
    with open(path, 'r', encoding='utf-8', newline='') as file:
        for row in csv.DictReader(file):
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def products():
    """Display products from the requested source, optionally filtered
    by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json('products.json')
        elif source == 'csv':
            data = read_csv('products.csv')
        else:
            return render_template('product_display.html',
                                   error='Wrong source')
    except (FileNotFoundError, json.JSONDecodeError, ValueError, KeyError):
        return render_template('product_display.html',
                               error='Error reading the data source')

    if product_id is not None:
        data = [item for item in data if str(item['id']) == str(product_id)]
        if not data:
            return render_template('product_display.html',
                                   error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
