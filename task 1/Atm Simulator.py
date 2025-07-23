initial_bal = 1000
print("=========ATM MENU========")
print("1: Check Balance")
print("2: Deposit")
print("3: Withdraw")
print("4: Exit")

while True:
    choice = input("Press a number to continue: ")
    if choice.isalpha():
        print("Enter numbers only")
        continue
    
    try:
        choice =int(choice)
        if choice==1:
            print("====ACCOUNT SUMMARY====")
            print(f"Balance: ${initial_bal:.2f}")
        elif choice ==2:
            deposit=float(input("Enter Amount to deposit: "))
            if deposit<0:
                continue
            initial_bal += deposit
            print("====ACCOUNT SUMMARY====")
            print(f"you have successfully deposited {deposit:.2f}")
            print(f"Your current balance: ${initial_bal:.2f}")
        elif choice ==3:
            withdraw_amt=float(input("Enter Amount to Withdraw: "))
            if withdraw_amt<0:
                print("Enter positive number")
                continue
            if withdraw_amt > initial_bal:
                print("SAPA NICE ONE, INSUFFICIENT FUNDS")
                continue
            initial_bal -= withdraw_amt
            print("====ACCOUNT SUMMARY====")
            print(f"You have successfully withdrawn {withdraw_amt}")
            print(f"Your current balance: ${initial_bal:.2f}")
        elif choice==4:
            print("THANK YOU FOR USING ZAYNETBANK GOODBYE!!")
            break
        else:
            print("INPUT ERROR!! TRY AGAIN")
                    
    except ValueError:
        print("Error")

# Task 5: Simple ATM Simulator

# Scenario: Simulate a basic ATM system that allows a user to perform multiple banking operations.

# Instructions:

# - Start with a fixed account balance (e.g., $1,000).

# - Show a menu in a loop:

#      1. Check Balance

#      2. Deposit

#      3. Withdraw

#      4. Exit

# - For each choice:

#      - If 1: Show current balance.

#      - If 2: Ask how much to deposit, add to balance (ensure amount is positive).

#      -  If 3: Ask how much to withdraw.

#            - If amount > balance, show error.

#            - Else, subtract from balance.

#      - If 4: Exit the loop.

# - After exit, display a goodbye message with the final balance.