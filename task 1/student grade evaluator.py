
#ask number of student
nos = int(input("Insert the number of student: "))

#counters
count_fail = 0
count_pass = 0
count_excel = 0

for i in range(1, nos +1):
    sname = input("please input your name: ")
    s1 = float(input("input first subject: "))
    s2 = float(input("input second subject:"))
    s3 = float(input("input third subject: "))


    total = s1+s2+s3

    average = round(total /3,1)
    
    if average < 50:
        remark = "fail"
        count_fail +=1
    elif average >50 and average <=79:
        remark= "pass"
        count_pass =+1
    else:
        remark="Excellent!"
        count_excel=+1
        
    # result for student 
    print("===================")
    print(f"{sname}, your score is {average}")
    print(f"Result: {remark}")
    print("===================")
    
#summary    
print("====SUMMARY====")
print(f"Number of student: {nos}")
print(f"Excellent: {count_excel}")
print(f"Passed: {count_pass}")
print(f"Fail: {count_fail}")
# Ask how many students to process.

# - Use a loop to:

#      - Ask for each student's name and 3 subject scores.

#      - Convert scores to float, calculate the average.

#      - Display result:

#      - Average < 50 -> Fail

#      - 50-79 -> Pass

#      - 80+ -> Excellent!

# - After all students are processed, display a summary:

#  how many passed, failed, and got excellent