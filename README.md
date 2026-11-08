# Python Store Management System

A simple store management system developed using Python.

This project is an introductory Python programming project focused on basic product registration, data storage, and product search functionality.

## Version

**Version 1.0 – Initial Release**

## Features

- Register multiple products.
- Store product information using dictionaries.
- Keep registered products in a list.
- Enter product name, price, and stock quantity.
- Search for products by name.
- Display product price and stock quantity.
- Search for multiple products during one program session.
- Display a message when a searched product is not found.

## Technologies and Concepts Used

This project was developed using Python and the following programming concepts:

- Variables
- Strings, integers, and floating-point numbers
- Lists
- Dictionaries
- User input with `input()`
- Type conversion with `int()` and `float()`
- `while` loops
- `for` loops
- `if` statements
- Conditional comparisons
- `append()` method
- `break` statement
- `for...else` statement

## How It Works

### 1. Product Registration

The program asks the user whether they want to add a product.

If the answer is `yes`, the user enters:

- Product name
- Product price
- Stock quantity

The information is stored in a dictionary, and each product dictionary is added to a list.

The registration process continues until the user chooses not to add another product.

### 2. Product Search

After registration, the program asks whether the user wants to search for a product.

The user enters a product name, and the program searches through the registered products.

If the product is found, the program displays its price and stock quantity.

If no matching product is found, the program displays a message indicating that the product was not found.

The user can perform multiple searches during the same session.

## Data Storage

Product information is stored temporarily in a Python list containing dictionaries.

The data is kept in the program's memory and is not saved permanently.

As a result, registered products will be lost when the program ends.

## Current Limitations

This is the initial version of the project. It has some limitations:

- Product information is not saved to a file or database.
- Invalid numeric inputs are not handled.
- Negative prices and stock quantities are not validated.
- Product searches are case-sensitive.
- Duplicate product names are not prevented.
- The program does not include product editing or deletion features.

## Future Improvements

Possible improvements for future versions include:

- Improving input validation.
- Making product searches more reliable.
- Adding product editing and deletion.
- Improving stock management.
- Saving product information permanently.
- Adding more advanced management features.

## Project Status

Version 1.0 – Basic product registration and search functionality.
