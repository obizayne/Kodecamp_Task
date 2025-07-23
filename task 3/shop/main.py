# main.py

from billing import Cart, load_previous_transactions

def main():
    cart = Cart()

    while True:
        print("\n--- Small Shop Billing System ---")
        print("1. Add product to cart")
        print("2. View cart and total")
        print("3. Save bill to file")
        print("4. View previous transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Product name: ").strip()
            price = input("Price: ").strip()
            quantity = input("Quantity: ").strip()
            cart.add_product(name, price, quantity)

        elif choice == '2':
            cart.show_cart()

        elif choice == '3':
            cart.show_cart()
            confirm = input("Save this bill? (y/n): ").lower()
            if confirm == 'y':
                cart.save_bill()

        elif choice == '4':
            transactions = load_previous_transactions()
            if not transactions:
                print("No previous transactions found.")
            else:
                for tx in transactions:
                    print(f"\nDate: {tx['timestamp']}")
                    for item in tx['items']:
                        print(f"  {item['name']} - ₦{item['price']} x {item['quantity']} = ₦{item['total']:,.2f}")
                    print(f"Subtotal: ₦{tx['subtotal']:,.2f}")
                    print(f"Total (with discount): ₦{tx['total_with_discount']:,.2f}")
                    print("-" * 40)

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
