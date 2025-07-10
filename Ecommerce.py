def add_product(product_name, price, quantity):
    return {
        "product_name": product_name,
        "price": price,
        "quantity": quantity
    }

def update_price(product, new_price):
    product["price"] = new_price
    return product

def update_quantity(product, quantity_change):
    product["quantity"] += quantity_change
    return product

name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter initial quantity: "))

product = add_product(name, price, quantity)

print("\nCurrent Product Details:")
print(product)

new_price = float(input("\nEnter new price to update: "))
updated_product = update_price(product, new_price)
print("Updated Price:", updated_product)

change = int(input("\nEnter quantity change (+/-): "))
updated_product = update_quantity(updated_product, change)
print("Updated Quantity:", updated_product)
