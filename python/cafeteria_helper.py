from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int
    def __str__(self):
        return f"{self.name} - RS {self.price}"

@dataclass
class Category:
    title: str
    products: list[Product]
    def print_products(self):
        for (i, product) in enumerate(self.products):
            print(f"\t{i + 1}. {product}")

@dataclass
class Cafeteria:
    name: str
    categories: list[Category]
    orders: list[Product]

    def print_categories(self):
        print("=====================================")
        for (i, category) in enumerate(self.categories):
            print(f"\t{i + 1}. {category.title}")

    def print_products(self, category_index: int):
        print("=====================================")
        print(f"Products in {self.categories[category_index].title}:")
        print("=====================================")

        category = self.categories[category_index]
        category.print_products()

    def print_bill(self):
        if len(self.orders) == 0:
            print("No orders found...")
            return
        total = 0
        choice = input("Are you a student or faculty member (yes / no): ")
        if choice.lower().startswith("y"):
            total = total * 0.9
        print("=====================================")
        print("Your Bill:")
        print("=====================================")
        for (i, order) in enumerate(self.orders):
            total += order.price
            print(f"\t{i + 1}. {order}")
        tax = total * 0.05
        print(f"GST (5%) : {tax}")
        print(f"Total Bill: {total + tax}")

    def print_payment_methods(self):
        print("=====================================")
        print("Payment methods:")
        print("=====================================")
        print("\t1. Cash")
        print("\t2. Card")
        print("\t3. Sodexo")
        print("\t4. credit card")
        while True:
            try:
                payment_method = int(input("Enter the payment method: "))
                while payment_method < 1 or payment_method > 4:
                    payment_method = int(input("Enter valid payment method: "))
                break
            except:
                print("Invalid Input")
        if payment_method == 4 or payment_method == 2:
            card_number = input("Enter the card number: ")
            while card_number != "111111111111":
                card_number = input("Enter valid card number: ")
            pin = input("Enter the 4 digit pin: ")
            while pin != "1111":
                pin = input("Enter valid pin: ")
        if payment_method == 3:
            sodexo_number = input("Enter the sodexo number: ")
            while len(sodexo_number) != 12:
                sodexo_number = input("Enter valid sodexo number: ")
        print("Payment successfull... have a nice day")

cafeteria = Cafeteria("Cafeteria", [
    Category("Coffee", [
        Product("Espresso Coffee", 30),
        Product("Cappuccino Coffee", 50),
        Product("Latte Coffee", 70),
    ]),
    Category("Soups", [
        Product("Hot and Sour Soup", 50),
        Product("Veg Corn Soup", 60),
        Product("Tomato Soup", 50),
        Product("Spicy Tomato Soup", 70),
    ]),
    Category("Tea", [
        Product("Plain Tea", 30),
        Product("Assam Tea", 40),
        Product("Ginger Tea", 50),
        Product("Cardamom Tea", 70),
        Product("Masala Tea", 80),
        Product("Lemon Tea", 80),
        Product("Green Tea", 90),
        Product("Organic Darjeeling Tea", 120),
    ]),
    Category("Beverages", [
        Product("Hot Chocolate Drink", 70),
        Product("Badam Drink", 80),
        Product("Badam-Pista Drink", 90),
    ]),
], [ ])

