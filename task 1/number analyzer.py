count_even = 0
count_odd = 0
count_zero = 0
count_neg = 0
count_pos = 0

for i in range(1,6):
    num = input(f"Enter number {i}: ")
    
    if num.isalpha():
        print("Enter only numbers")
        break
    
    try:
        num=float(num)
       
        if num % 2 ==0:
            print(f"{num} is even")
            count_even +=1
        elif num % 2 !=0:
            print(f"{num} is not odd")
            count_odd +=1
        elif num >0:
            print(f"{num} is positive")
            count_pos  +=1
        elif num <0:
            print(f"{num} is negative")
            count_neg+=1
        else:
            print(f"{num} is zero")
            count_zero+=1
    except ValueError:
        print("Insert only numbers")
print('==================')       
print(f"Even numbers: {count_even}")
print(f"Odd numbers: {count_odd}")
print(f"positive numbers: {count_pos}")
print(f"negative numbers: {count_neg}")
print(f"Zeros: {count_zero}")
print('==================')

# Task 4: Number Analyzer
# Scenario: Build a tool to analyze numbers entered by the user.
# Instructions:
# - Let the user enter up to 5 numbers (use a loop).
# - For each number:
#     - Check if it's even or odd.
#     - Check if it's positive, negative, or zero.
#     - Print the result for each.
# - After all entries, show how many:
#     - Were even
#     - Were odd
#     - Were negative
#     - Were zero