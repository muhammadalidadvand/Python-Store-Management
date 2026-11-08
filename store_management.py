products = []

i = input("Do you want to add a product? (yes/no) ")

while i == "yes":

    p_name = input("Enter product name: ")
    p_price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))

    product = {
        "p_name": p_name,
        "p_price": p_price,
        "stock": stock
    }

    products.append(product)

    i = input("Do you want to add another product? (yes/no) ")

print(products)

j = input("Do you want to search for a product? (yes/no) ")

while j == "yes":

    search_stock = input("Enter product name: ")

    for product in products:

        if search_stock == product["p_name"]:

            print("Product found!")
            print("Price:", product["p_price"])
            print("Stock:", product["stock"])
            break

    else:
        print("Product not found.")

    j = input("Do you want to search again? (yes/no) ")

print("End of work")
