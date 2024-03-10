class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"ID: {self.product_id} - {self.name} - ${self.price} - Stock: {self.stock_quantity}"

class ShoppingCart:
    def __init__(self):
        self.items = {}  

    def add_product(self, product, quantity=1):
        if product.stock_quantity < quantity:
            print("Insufficient stock!")
            return False
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity
        product.stock_quantity -= quantity  
        return True

    def remove_product(self, product_id, quantity=1):
        if product_id in self.items:
            if self.items[product_id] <= quantity:
                del self.items[product_id]
            else:
                self.items[product_id] -= quantity
            print("Product removed successfully.")
            products[product_id].stock_quantity += quantity
        else:
            print("Product not found in cart.")

    def total_cost(self, products):
        total = 0
        for product_id, quantity in self.items.items():
            total += quantity * products[product_id].price
        return total

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.order_history = []

    def add_to_order_history(self, order):
        self.order_history.append(order)

    def display_order_history(self, products):
        if not self.order_history:
            print("No order history available.")
            return
        print("\nOrder History:")
        for order in self.order_history:
            print("Order ID:", order["order_id"])
            for product_id, quantity in order["products"].items():
                print(f"{products[product_id].name} - Quantity: {quantity}")
            print("Total Cost:", order["total_cost"])
            print("--------------------")

def display_menu():
    print("\nMenu:")
    print("1. Add product to cart")
    print("2. Remove product from cart")
    print("3. View shopping cart")
    print("4. Checkout")
    print("5. Display order history")
    print("6. Exit")

def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username].password == password:
        return users[username]
    else:
        print("Invalid username or password.")
        return None

if __name__ == "__main__":
    products = {
        1: Product(1, "SmartWatch", 5000, 10),
        2: Product(2, "Earpods", 2000, 20)  }
    users = {"sanjeevi": User("sanjeevi", "123456")}
    logged_in_user = None
    while not logged_in_user:
        print("\n1. Sign In")
        print("2. Login")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            if username in users:
                print("User already exists. Please login.")
            else:
                password = input("Enter password: ")
                users[username] = User(username, password)
                print("User created successfully. Please login.")
        elif choice == "2":
            logged_in_user = login(users)
        else:
            print("Invalid choice.")
    cart = ShoppingCart()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Available Products:")
            for product_id, product in products.items():
                print(product)
            product_id = int(input("Enter the product ID to add to cart: "))
            if product_id in products:
                quantity = int(input("Enter the quantity: "))
                if cart.add_product(products[product_id], quantity):
                    print("Product added to cart successfully.")
            else:
                print("Item not found.")

        elif choice == "2":
            if not cart.items:
                print("No items added to cart.")
                continue
            print("Shopping Cart:")
            for product_id, quantity in cart.items.items():
                print(f"{products[product_id]} - Quantity: {quantity}")
            product_id = int(input("Enter the product ID to remove from cart: "))
            quantity = int(input("Enter the quantity: "))
            cart.remove_product(product_id, quantity)

        elif choice == "3":
            if not cart.items:
                print("No items added to cart.")
            else:
                print("Shopping Cart:")
                for product_id, quantity in cart.items.items():
                    print(f"{products[product_id]} - Quantity: {quantity}")

        elif choice == "4":
            if not cart.items:
                print("Cart is empty. No items are available to place order.")
                continue              
            print("Checking out...")
            order = {
                "order_id": len(logged_in_user.order_history) + 1,
                "products": cart.items,
                "total_cost": cart.total_cost(products)
            }
            logged_in_user.add_to_order_history(order)
            cart = ShoppingCart()  
            print("Order placed successfully!")

        elif choice == "5":
            logged_in_user.display_order_history(products)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")