import random
import json
from collections import deque
from multiprocessing import Process, Queue, current_process

# Define categories and products
categories = ["Fruits", "Vegetables", "Dairy", "Bakery", "Meat"]
products = {
    "Fruits": [("Apple", 1.0), ("Banana", 0.5), ("Orange", 0.8)],
    "Vegetables": [("Carrot", 0.3), ("Potato", 0.4), ("Tomato", 0.5)],
    "Dairy": [("Milk", 1.2), ("Cheese", 2.5), ("Yogurt", 1.0)],
    "Bakery": [("Bread", 1.5), ("Croissant", 1.0), ("Donut", 1.2)],
    "Meat": [("Chicken", 5.0), ("Beef", 7.0), ("Pork", 6.0)]
}

# Define discounts
discounts = {
    "Fruits": 0.1,  # 10% discount on all fruits
    "Bakery": 0.2,  # 20% discount on all bakery items
    "Milk": 0.15  # 15% discount on Milk specifically
}

# Define customer names
first_names = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah", "Ian", "Julia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]


def generate_random_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = round(price, 2)
        self.category = category


class Customer:
    def __init__(self, name, has_loyalty_card):
        self.name = name
        self.has_loyalty_card = has_loyalty_card
        self.products = []

    def pick_products(self, products, num_products=5):
        for _ in range(num_products):
            category = random.choice(list(products.keys()))
            product_name, price = random.choice(products[category])
            self.products.append(Product(product_name, price, category))


class Cashier:
    def __init__(self, name):
        self.name = name

    def calculate_total(self, customer):
        total_price = round(sum(p.price for p in customer.products), 2)
        total_price_with_discount = total_price
        products_with_discounts = []

        for p in customer.products:
            discount = discounts.get(p.category, 0) + discounts.get(p.name, 0)
            discounted_price = round(p.price * (1 - discount), 2)
            products_with_discounts.append({
                "name": p.name,
                "price": f"{p.price:.2f}€",
                "discounted_price": f"{discounted_price:.2f}€"
            })
            total_price_with_discount -= round(p.price * discount, 2)

        if customer.has_loyalty_card:
            total_price_with_discount = round(total_price_with_discount * 0.95,
                                              2)  # additional 5% discount for loyalty card holders

        return total_price, total_price_with_discount, products_with_discounts


class StoreQueue:
    def __init__(self):
        self.queue = deque()

    def add_customer(self, customer):
        self.queue.append(customer)

    def get_customer(self):
        return self.queue.popleft() if self.queue else None


def customer_shopping(queue, products):
    for i in range(150):
        customer_name = generate_random_name()
        customer = Customer(customer_name, random.choice([True, False]))
        customer.pick_products(products)
        queue.put(customer)


def cashier_process(queue, report_queue, cashier_name):
    cashier = Cashier(cashier_name)
    served_customers = 0

    while not queue.empty() and served_customers < 50:
        customer = queue.get()
        if customer:
            total_price, total_price_with_discount, products_with_discounts = cashier.calculate_total(customer)
            report_queue.put({
                "Customer name": customer.name,
                "Products": products_with_discounts,
                "Total price without discount": f"{total_price:.2f}€",
                "Total amount spent (with discount)": f"{total_price_with_discount:.2f}€",
                "Cashier that served them": cashier.name
            })
            served_customers += 1


def simulate_store_day():
    customer_queue = Queue()
    report_queue = Queue()

    customer_process = Process(target=customer_shopping, args=(customer_queue, products))
    customer_process.start()
    customer_process.join()

    cashier_names = ["Mari", "Liis"]
    cashier_processes = []

    for cashier_name in cashier_names:
        p = Process(target=cashier_process, args=(customer_queue, report_queue, cashier_name))
        cashier_processes.append(p)
        p.start()

    for p in cashier_processes:
        p.join()

    report = []
    while not report_queue.empty():
        report.append(report_queue.get())

    # Write report to a JSON file
    with open('store_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    return report


# Run simulation
if __name__ == "__main__":
    report = simulate_store_day()
    print(json.dumps(report, indent=4, ensure_ascii=False))
