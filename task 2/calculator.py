# Task 3: Calculator with History

# Scenario: A basic calculator that remembers past results.

# Instructions:

# - Show options: Add, Subtract, Multiply, Divide, View History, Exit

# - Use input to take two numbers and perform operation

# - Store each operation and result in a list

# - Show history with index numbers

# - Use functions for operations and error handling for divide-by-zero
history = []

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 0.0
    
def get_numbers():
    while True:
        try:
            num1 = float(input("please input the first number:"))
            num2 = float(input("please input the second number:"))
            return num1, num2
        except ValueError as e:
            print("Invalid input. Please enter numeric values.")

def menu():
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Exit")
    print("Please select an option (1-6):")
def app():
    while True:
        menu()
        try:
            choice = int(input())
            if choice == 1:
                print("performing addition")
                num1, num2 = get_numbers()
                result = add(num1, num2)
                history.append(f"Addition: {num1} + {num2} = {result}")
                print(f"Result: {result}")
            elif choice == 2:
                print("performing subtraction")
                num1, num2 = get_numbers()
                result = sub(num1, num2)
                history.append(f"Subtraction: {num1} - {num2} = {result}")
                print(f"Result: {result}")
            elif choice == 3:
                print("performing multiplication")
                num1, num2 = get_numbers()
                result = mul(num1, num2)
                history.append(f"Multiplication: {num1} * {num2} = {result}")
                print(f"Result: {result}")
            elif choice == 4:
                print("performing division")
                num1, num2 = get_numbers()
                result = div(num1, num2)
                history.append(f"Division: {num1} / {num2} = {result}")
                print(f"Result: {result}")
            elif choice == 5:
                if not history:
                    print("No history available.")
                else:
                    print("History of operations:")
                    for index, entry in enumerate(history):
                        print(f"{index + 1}: {entry}")
            elif choice == 6:
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError as e:
            print("Invalid input. Please enter a number between 1 and 6.")
        
app()