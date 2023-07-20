from cafeteria_helper import *

print(f"~~~~~~~~Welcome to {cafeteria.name}~~~~~~~~~")
while True:
    cafeteria.print_categories()
    while True:
        try:
            category_index = int(input("Enter the category number: ")) - 1
            if category_index < 0 or category_index >= len(cafeteria.categories):
                print("Invalid category...")
                continue
            break
        except:
            print("Invalid category...")


    cafeteria.print_products(category_index)
    while True:
        try:
            product_index = int(input("Enter the product number: ")) - 1
            if product_index < 0 or product_index >= len(cafeteria.categories[category_index].products):
                print("Invalid product...")
                continue
            break
        except:
            print("Invalid product...")

    product = cafeteria.categories[category_index].products[product_index]
    cafeteria.orders.append(product)
    print(f"{product.name} added to cart")
    choice = input("Do you want to continue shopping (yes / no): ")
    if choice.lower().startswith("n"):
        cafeteria.print_bill()
        cafeteria.print_payment_methods()
        break
