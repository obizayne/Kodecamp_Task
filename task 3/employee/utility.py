import json
import os
print("Saving/Loading from:", os.getcwd())
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'employees.json')

class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            'name': self.name,
            'emp_id': self.emp_id,
            'department': self.department,
            'salary': self.salary
        }

    @staticmethod
    def from_dict(data):
        return Employee(
            name=data['name'],
            emp_id=data['emp_id'],
            department=data['department'],
            salary=data['salary']
        )

def save_employees_to_file(employees):
    with open(FILE_PATH, 'w') as file:
        json.dump([emp.to_dict() for emp in employees], file, indent=4)

def load_employees_from_file():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        data = json.load(file)
        return [Employee.from_dict(item) for item in data]

def search_employee_by_id(employees, emp_id):
    return next((emp for emp in employees if emp.emp_id == emp_id), None)