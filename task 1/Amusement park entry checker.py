while True:
    # check users name or exit
    name = input("Please input users name or Type 'done' to Exit: ")
    if name.lower() == "done":
        break
    try:
        # get price base on age
        age = int(input("Input Visitors age: "))
        if age < 5:
            print("Go and Enjoy Kid, its free")
            continue
        elif age >5 and age<=17:
            price = 5
        elif age >18 and age<=59:
            price = 10
        else:
            price = 7
        
              # checks cuopon
        cuopon = input("Do you have a cuopon YES/NO: ")
        if cuopon not in ('yes', 'no'):
            print("invalid cuopon input. please enter 'yes' of 'no'")
            continue
        if cuopon.lower() =="yes":
            discount = price * 0.20
            total = price - discount
            print("===========================")
            print(f"A 20% discount have been applied: ${discount:.2f}")
            
        else:
            total = price
        print("===========================")
        print(f"Visitors name: {name}")
        print(f"Entry fee: ${total}")
        print("===========================")
               
    except ValueError:
        print("Enter numbers only or Type 'done' to Exit") 


#  Amusement Park Entry Checker

# Scenario: Check multiple visitors' ticket prices.

# Instructions:

# - Use a loop to allow repeated entries.

# - For each visitor:

#      - Ask name and age (int).

#      - Based on age:

#      - < 5: Free

#      - 5-17: $5

#      - 18-59: $10

#      - 60+: $7

#      - Ask if they have a coupon (Yes/No). If yes, apply 20% discount.

#      - Show final price.

# - Exit loop when a special name like 'done' is entered.