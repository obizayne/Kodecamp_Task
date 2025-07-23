burger_price = 5
fries_price = 2
drink_price = 1.5

count_customer = 0

while True:
     name = input("Enter customer name or Type Exit to leave: ")
     if name.lower() =="exit":
          break
     try:
          burgers = int(input("How many burgers do you want, $5 each: "))
          fries = int(input("How many fries do you want, $2 each: "))
          drink = int(input("How many drinks do you want, $1.5 each: "))
    
          # total 
          total = (burgers * burger_price) + (fries * fries_price) + (drink * drink_price)
          
          if total > 20:
               discount = total * 0.10
               total -=discount
          print(f"A 10% has been applied: ${discount:.2f}")
               
          print(f" Customer name: {name}")
          print(f"Number of burger: {burgers}")
          print(f"number of fries: {fries}")
          print(f"number of burger: {burgers}")
          print(f"Total: ${total:.2f}")
          print("========")
          count_customer +=1      
     except ValueError:
          print("input numbers only or type exit to leave: ")

print(f"Total number of customer(s) served:{count_customer}")


# <!-- Task 2: Fast Food Order System

# Scenario: A fast-food ordering system that supports multiple customers.

# Instructions:

# - Use a loop to serve multiple customers (stop when user types 'exit').

# - For each customer:

#      - Ask for name and quantity of:

#      - Burger ($5), Fries ($2), Drink ($1.5)

#      - Calculate total.

#      - If total > $20, apply 10% discount.

#      - Display the bill.

# - After exit, show how many customers were served -->