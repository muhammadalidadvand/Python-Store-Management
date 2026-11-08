products = []

positive_answer = "yes"

i = input("Is there a product to register? (yes/no) ").lower()
   
while i == positive_answer:

    positive_answer = "yes"

    p_name = input("Enter the product name : ").lower()
    p_price = float(input("Enter the product price in usd : "))
    stock = int(input("Enter the number of product in stock : "))

    product = {"p_name" : p_name , "p_price" : p_price , "stock" : stock}
    print (product)

    products.append(product)
    
    endloop = input("Do you want to add another product? (yes/no) ").lower()
    if endloop != "yes":
        break

if len(products) == 0 :
    print("There is nothing in stock" )
else:   
    print(products)

j = input("Do you want to search between products? (yes/no) ").lower()
if j == "yes":
    while j == "yes":
        search_stock = input("Enter the product name for search: ").lower()
    
        found = False

        for product in products:

            if search_stock == product["p_name"] :
                found = True
                break

        if found and product["stock"] > 0 :
            print(f"Yes {product['p_name']} was in stock and price is {product['p_price']} usd and there is {product['stock']}. ")

        elif found and product["stock"] == 0 :
            print(f"{search_stock} was out stock. ")

        else:
            print(f"No {search_stock} was not in stock. ")

        j = input("Do you want to search between products? (yes/or) ").lower()

print("End of work")
