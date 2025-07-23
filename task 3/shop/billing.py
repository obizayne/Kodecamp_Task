# billing.py

import json
import os
import math
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bills.json')

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total_price(self):
        return self.price * self.quantity

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "total": self.total_price()
        }

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        try:
            product = Product(name, price, quantity)
            self.products.append(product)
            print(f"Added {quantity} x {name} to cart.")
        except ValueError:
            print("Invalid price or quantity.")

    def get_total(self):
        return sum(p.total_price() for p in self.products)

    def apply_discount(self):
        total = self.get_total()
        if total > 10000:
            discount = total * 0.1  # 10% discount
            return total - discount, discount
        return total, 0

    def show_cart(self):
        if not self.products:
            print("Cart is empty.")
            return

        for product in self.products:
            print(f"{product.name} - ₦{product.price} x {product.quantity} = ₦{product.total_price():,.2f}")

        total, discount = self.apply_discount()
        print(f"\nSubtotal: ₦{self.get_total():,.2f}")
        if discount:
            print(f"Discount: -₦{discount:,.2f}")
        print(f"Total: ₦{math.ceil(total):,.2f}")

    def save_bill(self):
        bill_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": [p.to_dict() for p in self.products],
            "subtotal": self.get_total(),
            "total_with_discount": math.ceil(self.apply_discount()[0])
        }

        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r') as file:
                    existing = json.load(file)
            else:
                existing = []

            existing.append(bill_data)

            with open(DATA_FILE, 'w') as file:
                json.dump(existing, file, indent=4)
            print("Bill saved successfully.")
        except Exception as e:
            print(f"Error saving bill: {e}")

def load_previous_transactions():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading past transactions.")
    return []
