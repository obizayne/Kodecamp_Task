import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'student.json')

class Student:
    def __init__(self, name, subjects_scores):
        self.name = name
        self.subjects = subjects_scores
        self.average = self.calculate_average()
        self.grade = self.get_grade()

    def calculate_average(self):
        return sum(self.subjects.values()) / len(self.subjects)

    def get_grade(self):
        avg = self.average
        if avg >= 70:
            return 'A'
        elif avg >= 60:
            return 'B'
        elif avg >= 50:
            return 'C'
        elif avg >= 45:
            return 'D'
        else:
            return 'F'

    def to_dict(self):
        return {
            "name": self.name,
            "subjects": self.subjects,
            "average": self.average,
            "grade": self.grade
        }

def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_students(students):
    with open(DATA_FILE, 'w') as f:
        json.dump(students, f, indent=4)

def add_student():
    name = input("Enter student name: ")
    subjects = {}
    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            score = float(input(f"Enter score for {subject}: "))
            subjects[subject] = score
        except ValueError:
                print("Invalid input. Enter a number.")

    student = Student(name, subjects)
    students = load_students()
    students.append(student.to_dict())
    save_students(students)
    print("Student added successfully!")

def view_students():
    students = load_students()
    if not students:
        print("No students found.")
    else:
        for s in students:
            print(f"Name: {s['name']}, Average: {s['average']:.2f}, Grade: {s['grade']}")
            for subject, score in s['subjects'].items():
                print(f"  {subject}: {score}")
            print("---")

def menu():
    while True:
        print("\n--- Student Report Card App ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
