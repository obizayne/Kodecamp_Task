# Task 1: Student Management System

# Goal: Build a program to store student names and their scores using lists/dictionaries.

# Core Features:

# - Add new students (with 3 subject scores)

# - Show all students with average and performance status

# - Search for a student by name

# - Use functions for actions

# - Use error handling for invalid inputs

students=[]

def add_student():
    try:
        name = input("Please input student name: ")
        scores = []
        for i in range(3):
            score = float(input(f"input your score for the {i} subject: "))
            if score <0 or score>100:
               print("invalid score")
            scores.append(score)
            
        student = {"name": name,"scores": scores}
        students.append(student)
        print(f"student by name {name} has be added successfully")
    except ValueError:
        print("invalid input please try again")

def cal_average(scores):
    return sum(scores)/len(scores)

def performance(average):
    if average < 50:
        return "fail" 
    elif average >50 and average <=79:
        return "pass" 
    else:
        return "Excellent!"

def show_details():
    if not students:
        print("no student found")
        return
    print("list of students and details")
    for student in students:
        avg = cal_average(student['scores'])
        perf =performance(avg)
        print(f"name: {student['name']}")
        print(f"Average: {avg}")
        print(f"Performance: {perf}")
    

def search_student():
    name = input("Please input student name to search: ")
    found = False
    for student in students:
        if student['name'].lower() ==name.lower():
             avg = cal_average(student["scores"])
             perf =performance(avg)
             print(f" student found: {student['name']}")
             print(f"Average: {avg}")
             print(f"Performance: {perf}")
             found = True
             break
    if not found:
        print("No student with such name was found")
            
    

def menu():
    while True:
        print("1. Add Students")
        print("2. show student")
        print("3. Search student")
        print("4. Exit")
        try:
            choice = int(input("please input choice:"))
            if choice == 1:
                add_student()
            elif choice ==2:
                show_details()
            elif choice ==3:
                search_student()
            elif choice ==4:
                print("GOODBYE")
                break
            else:
                print("invalid option")
        except ValueError:
            print("Invalid input")

# start program
menu()



