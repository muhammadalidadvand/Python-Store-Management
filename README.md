# Python Store Management System

A simple store management system developed using Python.

This project demonstrates basic Python programming concepts through product registration, data storage, and product search functionality.

## Version History

- **Version 1.0:** Initial implementation of basic product registration and search functionality.
- **Version 2.0:** Improved search logic, case-insensitive product matching, and separate handling of out-of-stock products.

## Version 2.0 Features

- Register multiple products.
- Store product information using lists and dictionaries.
- Enter product names, prices, and stock quantities.
- Search for products by name.
- Support case-insensitive product name searches using `lower()`.
- Use a `found` variable to identify matching products.
- Check whether a product is available in stock.
- Identify products with zero stock.
- Display product prices and stock quantities.
- Support multiple product searches.

## Technologies and Concepts Used

- Python
- Variables and data types
- Lists
- Dictionaries
- `input()`
- `int()` and `float()`
- `lower()`
- `while` loops
- `for` loops
- Conditional statements
- Boolean variables
- `append()`
- `break`

## How It Works

### 1. Product Registration

Users can register multiple products by entering the product name, price, and stock quantity.

Each product is stored in a dictionary, and all product dictionaries are added to a list.

### 2. Product Storage

Product information is temporarily stored in the program's memory using a list of dictionaries.

### 3. Product Search

Users can search for products by entering their names.

The program converts product names and search inputs to lowercase to make searching case-insensitive.

A Boolean variable called `found` is used to determine whether a matching product exists.

### 4. Stock Availability

If a product is found and its stock quantity is greater than zero, the program displays its price and available quantity.

If the stock quantity is zero, the program displays an out-of-stock message.

If no matching product is found, the program displays a product-not-found message.

## Current Limitations

- Product information is not saved permanently.
- Invalid numeric inputs are not handled.
- Negative prices and stock quantities are not validated.
- Duplicate product names are not prevented.
- Product editing and deletion are not supported.
- The program does not use a database.
- Product searches return only the first matching product.

## Project Status

**Version 2.0 – Improved Product Registration and Search System**
