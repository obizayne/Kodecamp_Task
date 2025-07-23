from utility import Employee, save_employees_to_file, load_employees_from_file, search_employee_by_id

def add_employee():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    department = input("Enter department: ")

    while True:
        try:
            salary = float(input("Enter salary: "))
            break
        except ValueError:
            print("Invalid salary. Please enter a number.")
            
    print(f"Employee {name} added successfully.")

    return Employee(name, emp_id, department, salary)

def view_employees(employees):
    if not employees:
        print("No employee records available.")
        return
    for emp in employees:
        print(f"Name: {emp.name}, ID: {emp.emp_id}, Department: {emp.department}, Salary: {emp.salary}")

def search_by_id(employees):
    emp_id = input("Enter employee ID to search: ")
    emp = search_employee_by_id(employees, emp_id)
    if emp:
        print(f"Found - Name: {emp.name}, Department: {emp.department}, Salary: {emp.salary}")
    else:
        print("Employee not found.")

def main():
    employees = []
    while True:
        print("\nMenu:")
        print("1. Add employee")
        print("2. View all employees")
        print("3. Search by ID")
        print("4. Save to file")
        print("5. Load from file")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            employee = add_employee()
            employees.append(employee)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            search_by_id(employees)
        elif choice == '4':
            save_employees_to_file(employees)
            print("Employees saved successfully.")
        elif choice == '5':
            employees = load_employees_from_file()
            print("Employees loaded successfully.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == '__main__':
    main()
