# Task 2: Simple Expense Tracker

# Scenario: Help users track their daily expenses.

# Instructions:

# - Let user enter multiple expenses: description + amount

# - Store as a list of dictionaries e.g., {"item": "Transport", "amount": 150.0}

# - Allow menu options:

#  - Add expense

#  - View all expenses

#  - Total and average

#  - Exit

expenses = []

def add_expense():
    item = input("please input your item: ")
    amount = float(input("Please input the amount of the Item: "))  
    entry = {
        "item": item,
        "amount": amount
            }
    expenses.append(entry)
    print(f"{item} cost {amount} has been added to the tracker")
    
def display_expense():
    if not expenses:
        print("No expense available")
        return
    print("List of Expense")
    for expense in expenses:
        print("=======================")
        print(f"item:{expense['item']}")
        print(f"Amount:{expense['amount']}")
        print("=======================")
        print()
        
# def total_amount(amount):
#     return sum(amount)

# def average(amount):
#     return sum(amount)/len(amount)

def total_avg():
    if not expenses:
        print("No Expense Record")
        return
    
    total = sum(entry['amount'] for entry in expenses)  
    avg = total / len(expenses) 
    print("=======================")
    print(f"Total expenses: {total}")
    print(f"Average expense: {avg:.2f}")
    print("=======================")
    print()

def menu():
    while True:
        print("WELCOME TO ZAYNET EXPENSE TRACKER")
        print("1: Add Expense")
        print("2: View all Expense")
        print("3: Total and Average")
        print("4: Exit")
        try:
            choice = int(input("please input choice to continue: "))
            if choice == 1:
                add_expense()
            elif choice ==2:
                display_expense()
            elif choice==3:
                total_avg()
            elif choice ==4:
                print("THANK YOU FOR USING OUR EXPENSE TRACKER")
                break
            else:
                print("Invalid input")
            
        except ValueError as e:
            print(f" Error!! Invalid input {e} ")

menu()